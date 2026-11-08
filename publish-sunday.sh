#!/usr/bin/env bash
# ==============================================================================
# DKSchV Schweiz · 1-Klick Sonntags-Blog Publikation
#
# Liest das neueste Manus-Paket aus ~/Downloads, importiert die Artikel,
# generiert die HTML-Seiten für https://dkschv.ch und aktualisiert die Navigation.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================================="
echo "  DKSchV Schweiz · Sonntags-Blog Publikation"
echo "=========================================================="

# Führe Node Importer & Generator aus
node scripts/import-sunday-package.mjs "$@"

echo "=========================================================="
echo "  Publikation erfolgreich abgeschlossen!"
echo "  Die statischen Seiten sind bereit zum Upload auf Infomaniak."
echo "=========================================================="
