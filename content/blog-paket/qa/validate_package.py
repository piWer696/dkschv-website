#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import sys
from datetime import datetime

ROOT = Path('/home/ubuntu/dkschv-audit/blog-paket')
ARTICLES = sorted((ROOT / 'articles').glob('*.md'))
RESOURCES = sorted((ROOT / 'resources').glob('*.md'))
errors = []
warnings = []

required_article_keys = {
    'status', 'slug', 'meta_title', 'meta_description', 'hauptkeyword',
    'zielgruppe', 'autor', 'veröffentlichungsdatum', 'fachprüfung_status'
}
required_resource_keys = {'status', 'slug'}

slug_to_file = {}
resource_slug_to_file = {}


def parse_frontmatter(text, path):
    if not text.startswith('---\n'):
        errors.append(f'{path}: YAML-Frontmatter fehlt')
        return {}
    end = text.find('\n---\n', 4)
    if end < 0:
        errors.append(f'{path}: YAML-Frontmatter nicht geschlossen')
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def defined_refs(text):
    return {int(x) for x in re.findall(r'^\[(\d+)\]:\s+https?://', text, flags=re.M)}


def cited_refs(text):
    body = re.sub(r'^\[(\d+)\]:.*$', '', text, flags=re.M)
    return {int(x) for x in re.findall(r'\[(\d+)\]', body)}


def check_controls(text, path):
    for char in text:
        code = ord(char)
        if code in list(range(0, 9)) + [11, 12] + list(range(14, 32)) + [127]:
            errors.append(f'{path}: unzulässiges Steuerzeichen U+{code:04X}')
            return

for path in ARTICLES:
    text = path.read_text(encoding='utf-8')
    meta = parse_frontmatter(text, path)
    missing = sorted(required_article_keys - set(meta))
    if missing:
        errors.append(f'{path.name}: Metadaten fehlen: {", ".join(missing)}')
    if 'entwurf' not in meta.get('status', '').lower():
        errors.append(f'{path.name}: Status ist nicht Entwurf')
    if '[FACHPRÜFUNG ERFORDERLICH]' not in text:
        errors.append(f'{path.name}: Fachprüfungsmarker fehlt')
    if not re.search(r'^#\s+\S', text, flags=re.M):
        errors.append(f'{path.name}: H1 fehlt')
    if '**Kurzantwort:**' not in text:
        errors.append(f'{path.name}: Kurzantwort fehlt')
    if '## Quellen' not in text:
        errors.append(f'{path.name}: Quellenabschnitt fehlt')
    refs_defined = defined_refs(text)
    refs_cited = cited_refs(text)
    if refs_defined != refs_cited:
        errors.append(f'{path.name}: Quellenabweichung, definiert={sorted(refs_defined)}, zitiert={sorted(refs_cited)}')
    words = len(re.findall(r"\b[\wÀ-ž’'-]+\b", re.sub(r'^---.*?---\n', '', text, flags=re.S)))
    if words < 1400:
        errors.append(f'{path.name}: nur {words} Wörter')
    if 'ß' in text:
        errors.append(f'{path.name}: enthält ß')
    check_controls(text, path)
    slug = meta.get('slug')
    if slug:
        if slug in slug_to_file:
            errors.append(f'{path.name}: doppelter Slug {slug}')
        slug_to_file[slug] = path

for path in RESOURCES:
    text = path.read_text(encoding='utf-8')
    meta = parse_frontmatter(text, path)
    missing = sorted(required_resource_keys - set(meta))
    if missing:
        errors.append(f'{path.name}: Metadaten fehlen: {", ".join(missing)}')
    status = meta.get('status', '').lower()
    if not any(marker in status for marker in ('entwurf', 'nicht freigegeben', 'prüfen')):
        errors.append(f'{path.name}: Status kennzeichnet keine ungeprüfte Arbeitsvorlage')
    if '[FACHPRÜFUNG ERFORDERLICH]' not in text:
        errors.append(f'{path.name}: Fachprüfungsmarker fehlt')
    if '## Quellen' not in text:
        errors.append(f'{path.name}: Quellenabschnitt fehlt')
    refs_defined = defined_refs(text)
    refs_cited = cited_refs(text)
    if refs_defined != refs_cited:
        errors.append(f'{path.name}: Quellenabweichung, definiert={sorted(refs_defined)}, zitiert={sorted(refs_cited)}')
    if 'ß' in text:
        errors.append(f'{path.name}: enthält ß')
    check_controls(text, path)
    slug = meta.get('slug')
    if slug:
        resource_slug_to_file[slug] = path

all_local = {**slug_to_file, **resource_slug_to_file}
for path in ARTICLES + RESOURCES:
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\((/wissen/[^)]+|/resources/[^)]+)\)', text):
        target = target.split('#', 1)[0]
        if target not in all_local:
            errors.append(f'{path.name}: lokales Linkziel fehlt: {target}')

csv_path = ROOT / 'cms-import-manifest.csv'
if not csv_path.exists():
    errors.append('cms-import-manifest.csv fehlt')
else:
    with csv_path.open(encoding='utf-8', newline='') as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 12:
        errors.append(f'CMS-Manifest enthält {len(rows)} statt 12 Datensätze')
    manifest_names = set()
    for row in rows:
        combined = ' '.join(row.values())
        if 'entwurf' not in combined.lower():
            errors.append(f'CMS-Manifestzeile ohne Entwurfsstatus: {row}')
        name = row.get('Dateiname', '')
        if name in manifest_names:
            errors.append(f'CMS-Manifest enthält doppelten Dateinamen {name}')
        manifest_names.add(name)
        if name not in {f'articles/{p.name}' for p in ARTICLES}:
            errors.append(f'CMS-Manifest enthält unbekannte Artikeldatei {name}')
            continue
        path = ROOT / name
        text = path.read_text(encoding='utf-8')
        meta = parse_frontmatter(text, path)
        h1 = re.search(r'^#\s+(.+)$', text, flags=re.M)
        try:
            date = datetime.strptime(meta['veröffentlichungsdatum'], '%d.%m.%Y').strftime('%Y-%m-%d')
        except (KeyError, ValueError):
            errors.append(f'{name}: unlesbares Veröffentlichungsdatum')
            date = None
        expected = {'Slug': meta.get('slug'), 'Titel': h1.group(1).strip() if h1 else None,
                    'Meta-Title': meta.get('meta_title'),
                    'Meta-Description': meta.get('meta_description'),
                    'Veröffentlichungsdatum': date,
                    'Letzte gezielte Quellenprüfung': meta.get('stand')}
        for key, value in expected.items():
            if row.get(key) != value:
                errors.append(f'{name}: CMS-Manifest {key} weicht von Artikel ab')
        if '[FACHPRÜFUNG ERFORDERLICH]' in text and 'OFFEN' not in row.get('Fachprüfung', ''):
            errors.append(f'{name}: offene Fachprüfung fehlt im CMS-Manifest')
        if not row.get('CMS-Synchronisierung'):
            errors.append(f'{name}: CMS-Synchronisierungsstatus fehlt')
        report = ROOT.parent / row.get('Prüfbericht', '')
        if not report.is_file():
            errors.append(f'{name}: Einzelbericht im CMS-Manifest nicht vorhanden')

if len(ARTICLES) != 12:
    errors.append(f'Artikelanzahl {len(ARTICLES)} statt 12')
if len(RESOURCES) != 12:
    errors.append(f'Arbeitsmittelanzahl {len(RESOURCES)} statt 12')

print(f'Artikel: {len(ARTICLES)}')
print(f'Arbeitsmittel: {len(RESOURCES)}')
print(f'Artikel-Slugs: {len(slug_to_file)}')
print(f'Arbeitsmittel-Slugs: {len(resource_slug_to_file)}')
print(f'Fehler: {len(errors)}')
print(f'Warnungen: {len(warnings)}')
for item in errors:
    print('ERROR:', item)
for item in warnings:
    print('WARNING:', item)
sys.exit(1 if errors else 0)
