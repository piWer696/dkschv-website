#!/usr/bin/env python3
"""Gleicht Entwurfsmetadaten und lokalen Prüfstatus mit dem CMS-Importmanifest ab.

Dieses Skript schreibt ausschliesslich lokale CSV-Dateien. Es meldet sich nicht im CMS an
und vergibt niemals eine fachliche Freigabe oder einen Veröffentlichungsstatus.
"""
from __future__ import annotations
import argparse
import csv
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_FIELDS = ['Dateiname', 'Slug', 'Titel', 'Meta-Title', 'Meta-Description',
               'Veröffentlichungsdatum', 'Status', 'CTA-Ziel']
EXTRA_FIELDS = ['Letzte gezielte Quellenprüfung', 'Prüfbericht', 'Interne Paketlinks',
                'Öffentliche Artikel-URL', 'Öffentliche Arbeitsmittel-URL',
                'CMS-Synchronisierung', 'Fachprüfung', 'Quellenprüfungsumfang',
                'Quellenprüfungsstatus']


def metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError(f'Frontmatter fehlt: {path}')
    return dict((k.strip(), v.strip().strip('"').strip("'"))
                for line in match.group(1).splitlines() if ':' in line
                for k, v in [line.split(':', 1)])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--review-date', required=True)
    parser.add_argument('--link-check', type=Path, required=True)
    parser.add_argument('--review-dir', type=Path, required=True)
    parser.add_argument('--cms-status', default='BLOCKIERT – kein authentifizierter CMS-Zugang in diesem Lauf')
    args = parser.parse_args()
    path = ROOT / 'cms-import-manifest.csv'
    with path.open(encoding='utf-8', newline='') as handle:
        original = list(csv.DictReader(handle))
    if len(original) != 12 or len({r['Dateiname'] for r in original}) != 12:
        raise ValueError('Erwarte exakt zwölf unterschiedliche Artikelzeilen')
    with args.link_check.open(encoding='utf-8', newline='') as handle:
        public = {r['path']: r['public_status'] for r in csv.DictReader(handle)}
    date = datetime.strptime(args.review_date, '%Y-%m-%d')
    rows = []
    for record in original:
        article = ROOT / record['Dateiname']
        meta = metadata(article)
        text = article.read_text(encoding='utf-8')
        match = re.search(r'^#\s+(.+)$', text, re.M)
        if not match:
            raise ValueError(f'H1 fehlt: {article}')
        number = article.name[:2]
        matches = list((ROOT / 'resources').glob(number + '-*.md'))
        if len(matches) != 1:
            raise ValueError(f'Arbeitsmittel für {number} nicht eindeutig')
        resource_slug = metadata(matches[0])['slug']
        report = args.review_dir / f'artikel-{number}-quellen-und-aenderungen.md'
        if not report.is_file() or report.stat().st_size == 0:
            raise ValueError(f'Prüfbericht fehlt: {report}')
        if 'entwurf' not in meta['status'].lower() or '[FACHPRÜFUNG ERFORDERLICH]' not in text:
            raise ValueError(f'Sperre/Fachprüfungsmarker fehlt: {article}')
        record.update({
            'Slug': meta['slug'], 'Titel': match.group(1).strip(),
            'Meta-Title': meta['meta_title'],
            'Meta-Description': meta['meta_description'],
            'Veröffentlichungsdatum': datetime.strptime(meta['veröffentlichungsdatum'], '%d.%m.%Y').strftime('%Y-%m-%d'),
            'Status': 'Entwurf – nicht freigegeben',
            'Letzte gezielte Quellenprüfung': meta['stand'],
            'Prüfbericht': str(report.relative_to(ROOT.parent)),
            'Interne Paketlinks': 'Lokal konsistent; keine Live-Freigabe',
            'Öffentliche Artikel-URL': public.get(meta['slug'], 'nicht geprüft'),
            'Öffentliche Arbeitsmittel-URL': public.get(resource_slug, 'nicht geprüft'),
            'CMS-Synchronisierung': args.cms_status,
            'Fachprüfung': 'OFFEN – Fachprüfungsmarker vorhanden',
            'Quellenprüfungsumfang': meta.get('quellenpruefung_umfang', 'Siehe Einzelbericht'),
            'Quellenprüfungsstatus': meta.get('quellenpruefung_status', 'Siehe Einzelbericht'),
        })
        months = ('Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
                  'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember')
        expected_date = f'{date.day}. {months[date.month - 1]} {date.year}'
        if record['Letzte gezielte Quellenprüfung'] != expected_date:
            raise ValueError(f'Quellenstand fehlt/abweichend: {article}')
        rows.append(record)
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=BASE_FIELDS + EXTRA_FIELDS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(f'{path}: {len(rows)} nicht freigegebene Datensätze; 8 Import-Spalten unverändert an erster Stelle; CMS nicht verändert')


if __name__ == '__main__':
    main()
