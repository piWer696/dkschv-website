#!/usr/bin/env python3
"""Prüft Originalmetadaten/Fachmarker gegen eine Sicherung und lokale Berichtslinks."""
from __future__ import annotations
import argparse
import csv
import difflib
import re
import tarfile
from pathlib import Path

FIELDS = (
    'slug', 'status', 'meta_title', 'meta_description', 'veröffentlichungsdatum',
    'fachprüfung_status', 'rechtsstand', 'fachlich_geprueft_am', 'fachlich_geprüft_am',
)
MARKER = '[FACHPRÜFUNG ERFORDERLICH]'


def metadata(text: str) -> dict[str, str]:
    front = text.split('---', 2)[1]
    result = {}
    for line in front.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--review-dir', type=Path, required=True)
    parser.add_argument('--news', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    rows = []
    changes = []
    with tarfile.open(args.baseline) as baseline:
        for directory in ('articles', 'resources'):
            for path in sorted((args.root / directory).glob('*.md')):
                relative = path.relative_to(args.root)
                source = baseline.extractfile(f'{args.root.name}/{relative}')
                if source is None:
                    raise ValueError(f'Sicherung fehlt: {relative}')
                before = source.read().decode('utf-8')
                after = path.read_text(encoding='utf-8')
                original, current = metadata(before), metadata(after)
                for field in FIELDS:
                    if original.get(field) != current.get(field):
                        raise ValueError(f'Originalfeld verändert: {relative}: {field}')
                if after.count(MARKER) < before.count(MARKER):
                    raise ValueError(f'Ursprüngliche Fachmarker fehlen: {relative}')
                rows.append({
                    'Datei': str(relative),
                    'Originalfelder unverändert': 'ja',
                    'Fachmarker vorher': before.count(MARKER),
                    'Fachmarker nachher': after.count(MARKER),
                    'Geändert': before != after,
                })
                changes.extend(difflib.unified_diff(
                    before.splitlines(True), after.splitlines(True),
                    fromfile=f'vorher/{relative}', tofile=f'nachher/{relative}',
                ))
    if len(rows) != 24:
        raise ValueError(f'24 Inhaltsdateien erwartet, gefunden: {len(rows)}')
    with (args.review_dir / 'integritaetsvergleich.csv').open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (args.review_dir / 'inhaltliche-aenderungen.diff').write_text(''.join(changes), encoding='utf-8')
    files = [args.root / name for name in ('maintenance-manifest.md', 'README.md', 'AUTOMATION_STATUS.md')]
    files += [args.news, args.report]
    for path in files:
        text = path.read_text(encoding='utf-8')
        if len(text) <= 100 or not text.endswith('\n'):
            raise ValueError(f'Unvollständiges Dokument: {path}')
        if any(ord(char) < 32 and char not in '\n\t\r' for char in text):
            raise ValueError(f'Steuerzeichen in Dokument: {path}')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
            if not target.startswith(('http://', 'https://', '#')):
                if not (path.parent / target.split('#')[0]).exists():
                    raise ValueError(f'Lokaler Berichtslink fehlt: {path}: {target}')
    news = args.news.read_text(encoding='utf-8')
    definitions = set(re.findall(r'^\[(\d+)\]:', news, re.M))
    used = set(re.findall(r'\[(\d+)\](?!:)', news))
    if used != definitions:
        raise ValueError(f'News-Quellenreferenzen inkonsistent: {used ^ definitions}')
    print('24 Inhaltsdateien: Originalfelder und alle ursprünglichen Fachmarker erhalten.')
    print('Lokale Berichtslinks, Dateivollständigkeit und News-Referenzen: OK.')
    print('Diff und Integritätsvergleich gespeichert. Keine Fach- oder Live-Freigabe erteilt.')


if __name__ == '__main__':
    main()
