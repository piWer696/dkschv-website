#!/usr/bin/env python3
"""Korrigiert nur Markdown-Linkziele lokal; keine Slug-/Status- oder CMS-Änderung."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--target-map', type=Path, required=True)
    parser.add_argument('--review-dir', type=Path, required=True)
    args = parser.parse_args()
    with args.target_map.open(encoding='utf-8', newline='') as file:
        rows = list(csv.DictReader(file))
    mapping = {row['local_slug']: row['target_url'] for row in rows
               if row['target_status'] == '200' and row['target_url'].startswith('https://www.dkschv.ch/')}
    timestamp = datetime.now(ZoneInfo('Europe/Zurich')).isoformat(timespec='seconds')
    changes = []
    for path in sorted((ROOT / 'articles').glob('*.md')) + sorted((ROOT / 'resources').glob('*.md')):
        text = path.read_text(encoding='utf-8')
        updated = text
        file_changes = []
        for old, new in mapping.items():
            count = updated.count('](' + old + ')')
            if count:
                updated = updated.replace('](' + old + ')', '](' + new + ')')
                file_changes.append({'before': old, 'after': new, 'count': count})
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            changes.append({'file': str(path.relative_to(ROOT)), 'links': file_changes})
    args.review_dir.mkdir(parents=True, exist_ok=True)
    (args.review_dir / 'lokaler-live-linkabgleich.json').write_text(
        json.dumps({'timestamp': timestamp, 'scope': 'Nur lokale Markdown-Linkziele; logische Slugs, SEO, Status, Quellenstand und Fachmarker erhalten; keine Live-Änderung', 'changes': changes},
                   ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for number in range(1, 13):
        report = args.review_dir / f'artikel-{number:02d}-quellen-und-aenderungen.md'
        if not report.is_file():
            raise ValueError(f'Einzelbericht fehlt: {report}')
        relevant = [change for change in changes if Path(change['file']).name.startswith(f'{number:02d}-')]
        heading = '\n## Nachtrag des lokalen Linkabgleichs\n\n'
        if heading.strip() in report.read_text(encoding='utf-8'):
            raise ValueError(f'Nachtrag schon vorhanden: {report}')
        note = heading + f'Bearbeitungszeit: {timestamp}. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. '
        note += 'Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.\n\n'
        if relevant:
            for change in relevant:
                note += f"**{change['file']}:** "
                note += '; '.join(f"`{x['before']}` → `{x['after']}`: {x['count']} Linkvorkommen" for x in change['links']) + '.\n\n'
        else:
            note += 'Bei diesem Paar war kein altes verifiziert ersetzbares Markdown-Linkziel vorhanden.\n\n'
        note += 'Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.\n'
        with report.open('a', encoding='utf-8') as file:
            file.write(note)
    print(f'{len(changes)} lokale Inhaltsdateien mit gezielt korrigierten Markdown-Linkzielen; zwölf Berichte ergänzt. CMS unverändert.')


if __name__ == '__main__':
    main()
