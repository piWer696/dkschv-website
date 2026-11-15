# DKSchV-Blogpaket – Stand 15. November 2026

**12 Artikel und 12 Arbeitsmittel lokal gepflegt; sämtliche Inhalte bleiben nicht freigegeben.** Der Quellenprüfstand lautet 15. November 2026. Ein recherchierter Quellenstand, der erreichte Veröffentlichungstermin und ein erfolgreicher Validator sind keine Einzelfall-Fachfreigabe.

## Inhalt und Nachweise

Die Artikel liegen unter `articles/`, die gleich nummerierten Checklisten und Vorlagen unter `resources/`. Das [Wartungsmanifest](maintenance-manifest.md) führt Themen, Termine, Quellen und Aktualisierungsauslöser. Das [CMS-Importmanifest](cms-import-manifest.csv) enthält zwölf lokale Datensätze mit unveränderten ersten acht Importfeldern sowie Prüfbericht, Quellenumfang, Fach-/CMS-Blockern und getrennten tatsächlichen Live-Zielen. Die CSV ist kein bestätigter Import.

Der [Pflegebericht KW46 mit zwölf Einzelprotokollen](../reviews/2026-11-15/DKSchV_Pflegebericht_KW46.md) dokumentiert Quellenstände, betroffene Passagen, Fachfragen und Quellenzugriffsgrenzen. Alle ursprünglichen Fachmarker, SEO-Importfelder, Slugs, Termine und historischen Fach-/Rechtsfelder bleiben erhalten. Arbeitsmittelversionen wurden bei materiellen Änderungen mit den sichtbaren Versionshinweisen abgeglichen.

Die [Paketvalidierung](../reviews/2026-11-15/validator-ergebnis.txt) bestätigt **0 Fehler und 0 Warnungen**. Der [gezielte lokale Linkabgleich](../reviews/2026-11-15/lokaler-live-linkabgleich.json) korrigierte alte Markdown-Linkziele in 14 Inhaltsdateien auf separat mit HTTP 200 geprüfte Adressen. Logische Ressourcen-Slugs bleiben zur Paketzuordnung erhalten.

## Aktueller öffentlicher Stand – keine eigene Veröffentlichung

Alle zwölf Artikeladressen unter `/wissen/<Slug>` antworteten am 15.11. mit HTTP 200. Die zwölf alten Arbeitsmittelpfade unter `/resources/` und drei alten Servicepfade unter `/unsere-dienstleistungen/` antworteten mit 404. Die [tatsächlich auf der Website verlinkten Ziele](../reviews/2026-11-15/public-target-map.csv) antworten dagegen mit 200: Arbeitsmittel unter `/wissen/resources/<Dateiname>.html` und Serviceadressen im Root mit `.html`. Erreichbarkeit ist keine Schutz-, Inhalts- oder Fachfreigabe.

**Schutzblocker:** Der Wiederherstellungsartikel lieferte ohne Credentials umfangreichen Fachtext trotz «Kunden-Login erforderlich». Ein serverseitig wirksamer Zugriffsschutz für diesen als Mandanteninhalt bezeichneten Text ist nicht nachgewiesen. Der [strukturierte Befund](../reviews/2026-11-15/public-article-exposure.json) enthält nur Status und Inhaltsmerkmale, keine Zugangsdaten. Die öffentliche Darstellung enthält weiterhin einen Fachprüfungshinweis. Herkunft und Freigabe der öffentlichen Bereitstellung sind nicht bestätigt; dieser Lauf hat nichts davon veröffentlicht.

Artikel 01–07 sind am 15.11. terminlich fällig, bleiben aber nicht freigegeben. Artikel 08–12 sind noch nicht terminlich fällig, jedoch ebenfalls per HTTP200 erreichbar. Eine solche Erreichbarkeit ersetzt keine Freigabe und berechtigt nicht zur automatischen Live-Bearbeitung.

## CMS und Fachblocker

Der [aktuelle Webador-Test](../reviews/2026-11-15/cms-zugangsstatus.md) zeigt die Anmeldeseite statt einer authentifizierten DKSchV-Pro-Sitzung. Gespeicherte Anmeldereferenzen sind in dieser Umgebung nicht zugreifbar. My Browser ist als Einstellung aktiviert, aber nicht als verbundene Webador-Sitzung verwendet. Die aktuelle Hosting-/CMS-Zuordnung der geänderten öffentlichen Website ist nicht bestätigt.

Sämtliche `[FACHPRÜFUNG ERFORDERLICH]`-Marker bleiben offen. Rechts-, Datenschutz-, Forensik-, Architektur-, Tenant-, Vertrags- und NIS2/DORA-Einzelfragen sind nicht freigegeben. Nicht auslesbare Zusatzquellen sind im jeweiligen Bericht benannt, insbesondere Fedlex-/EDÖB-Übersichten, BACS-DOCX bei01/04/08, Microsoft-Roadmap, Kanada-HTTP403 und ein EUR-Lex-Verfahrenspfad. Ein erreichbarer Ersatzbeleg ist keine vorgetäuschte Prüfung der blockierten Ansicht.

**Live-Synchronisierung BLOCKIERT. Kein Editor geändert, kein geschützter Import gestartet und kein Beitrag veröffentlicht.** Normale Webador-Editoränderungen würden sofort live gehen. Vor Go-live müssen der richtige CMS-/Hostingzugang, aktuelle Quellen und Links, Widerspruchsfreiheit, alle zuständigen Fachfreigaben und der gewünschte serverseitige Kundenschutz nachgewiesen sein. Jede spätere erfolgreiche Änderung ist mit URL, Zeitpunkt, Abschnitten und Quellen zu protokollieren.

**Nächste News:** 22.11.2026, KW47. **Nächste Vollpflege:** 29.11.2026, KW48, Europe/Zurich. Der bestehende Sonntagszeitplan bleibt aktiv; es wurde keine neue Automation angelegt.
