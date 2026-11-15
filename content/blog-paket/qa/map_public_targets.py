#!/usr/bin/env python3
"""Ermittelt öffentliche Ressourcenlinks, ohne Inhalte zu ändern oder sich anzumelden."""
from __future__ import annotations
import argparse
import csv
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = 'https://www.dkschv.ch'


def meta(path: Path) -> dict[str, str]:
    front = path.read_text(encoding='utf-8').split('---', 2)[1]
    return {k.strip(): v.strip().strip('"').strip("'") for line in front.splitlines()
            if ':' in line for k, v in [line.split(':', 1)]}


def get(url: str) -> tuple[str, str, str]:
    try:
        req = Request(url, headers={'User-Agent': 'DKSchV-Content-QA/1.0 (+manual review)'})
        with urlopen(req, timeout=15) as response:
            return str(response.status), response.url, response.read().decode('utf-8', 'replace')
    except HTTPError as exc:
        return str(exc.code), exc.url, ''
    except (URLError, OSError, TimeoutError) as exc:
        return 'ERROR: ' + str(exc)[:120], url, ''


def resource_row(article: Path) -> dict[str, str]:
    number = article.name[:2]
    resource = next((ROOT / 'resources').glob(number + '-*.md'))
    source_url = ORIGIN + meta(article)['slug']
    status, final, html = get(source_url)
    candidates = set()
    for anchor in BeautifulSoup(html, 'html.parser').select('a[href]'):
        target = urljoin(final, anchor['href'])
        parsed = urlparse(target)
        if parsed.hostname == 'www.dkschv.ch' and '/resources/' in parsed.path and resource.stem in parsed.path:
            candidates.add(target.split('#')[0])
    target = next(iter(candidates)) if len(candidates) == 1 else ''
    check, resolved, _ = get(target) if target else ('nicht eindeutig gefunden', '', '')
    return {'type': 'resource', 'number': number, 'local_slug': meta(resource)['slug'],
            'source_url': source_url, 'source_status': status, 'target_url': target,
            'target_status': check, 'resolved_url': resolved,
            'qualification': 'HTTP-Prüfung, keine Schutz-, Inhalts- oder Fachfreigabe'}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(resource_row, sorted((ROOT / 'articles').glob('*.md'))))
    for name in ('sicherheitsanalyse', 'risikomanagement', 'notfallplanung'):
        url = ORIGIN + '/' + name + '.html'
        status, resolved, _ = get(url)
        rows.append({'type': 'service', 'number': '', 'local_slug': '/unsere-dienstleistungen/' + name,
                     'source_url': ORIGIN + '/kontakt', 'source_status': 'Link im Kontaktseiten-Inhaltsabruf',
                     'target_url': url, 'target_status': status, 'resolved_url': resolved,
                     'qualification': 'HTTP-Prüfung, keine Schutz-, Inhalts- oder Fachfreigabe'})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'{len(rows)} öffentliche Zielzuordnungen dokumentiert: {args.output}')
    for row in rows:
        print(row['local_slug'], '=>', row['target_url'], row['target_status'])


if __name__ == '__main__':
    main()
