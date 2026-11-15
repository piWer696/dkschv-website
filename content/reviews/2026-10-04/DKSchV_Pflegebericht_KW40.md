# DKSchV – Sonntagsnews und Blogpflege, ISO-Woche 40

**Datum:** 4. Oktober 2026 · **Berichtsfenster:** 27. September bis 4. Oktober 2026, 09:00 Europe/Zurich · **Status:** lokale Redaktion; **nichts live geändert**.

## Ergebnis auf einen Blick

- Die [Sonntagsnews](../../news/2026-10-04_DKSchV_Branchennews.md) enthalten sechs priorisierte Meldungen zu aktiv ausgenutzten Sicherheitslücken, Microsoft Entra Connect Sync, BACS-Malware und dem sicheren Umgang mit KI-Eingaben; jede Meldung verlinkt auf die Primärquelle.
- **Alle zwölf Artikel und zwölf Arbeitsmittel** wurden gegen die je Themenfeld massgeblichen Primärquellen gezielt geprüft. Die in den Einzelberichten dokumentierten Abrufe erfolgten **nach 09:00 Uhr**. Nicht versionierte Webseiten können für exakt 09:00 Uhr nicht rückwirkend zugesichert werden.
- Materiell bzw. redaktionell geändert: Artikel **02** (archivierte CISA-Referenz ersetzt, unabhängige Rückbestätigung präzisiert), **05** (Microsoft-Telefonieprovider erst ab 30.10.2026 konfigurierbar; Text und Checkliste korrigiert), Arbeitsmittel **08** (sichtbare Version von 1.0 auf die bereits hinterlegte Version 1.1 vereinheitlicht). In den anderen Beiträgen wurde keine belegte fachliche Änderung im abgegrenzten Zeitraum festgestellt; deren geprüfte Quellenstandsangaben wurden aktualisiert. **Dies ist keine Vollprüfung sämtlicher zusätzlicher Quellen.**
- Das [Wartungsmanifest](../../blog-paket/maintenance-manifest.md) und das [CMS-Importmanifest](../../blog-paket/cms-import-manifest.csv) weisen die neue gezielte Prüfung und die weiterhin offenen Sperren aus. Die acht ursprünglichen CMS-Importfelder stehen unverändert am Anfang der CSV; ergänzende Statusspalten sind hinzugekommen.
- Der [öffentliche Linktest](public-link-check.csv) prüfte 28 eindeutige Pfade: **24 vorgesehene Artikel-/Arbeitsmittel-Pfade mit HTTP 404**, vier bestehende Kontakt-/Dienstleistungspfade mit HTTP 200. Paketinterne Verweise sind lokal konsistent, aber für die geplanten Beiträge noch **nicht öffentlich nutzbar**.
- `qa/validate_package.py` meldet **12 Artikel, 12 Arbeitsmittel, 0 Fehler, 0 Warnungen**. Diese formale Prüfung ersetzt keine Fachfreigabe und keine Live-Linkprüfung vor Veröffentlichung.

## Artikelweise Änderungs- und Quellenprotokolle

| Nr. | Inhalt | Geänderte Passagen / Quellenstand | Nachweis |
|---:|---|---|---|
| 01 | Ransomware: erste 60 Minuten | Artikelstand, Standhinweis im Abschnitt «Grenzen» und Checklistenstand aktualisiert; BACS-/EDÖB-/Fedlex-Grundaussagen laut gezielter Prüfung unverändert. Der geplante Termin 01.10. ist verstrichen, **keine Freigabe**. | [Einzelbericht 01](artikel-01-quellen-und-aenderungen.md) |
| 02 | CEO-Betrug/BEC | Stand aktualisiert; im Warnzeichen-Abschnitt unabhängigen Kontaktweg präzisiert; CISA-Archivquelle durch aktuelle [CISA-KMU-Anleitung](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/teach-employees-avoid-phishing) ersetzt. Vorlagenstand erneuert. | [Einzelbericht 02](artikel-02-quellen-und-aenderungen.md) |
| 03 | Datenpanne melden | `rechtsstand`, `stand` und Arbeitsmittel-Rechtsstand aktualisiert; keine belegte Änderung der geprüften DSG-/DSV-/EDÖB-/BACS-Meldegrundlagen. | [Einzelbericht 03](artikel-03-quellen-und-aenderungen.md) |
| 04 | Ransomware-resistente Backups | Artikel- und Vorlagenstand aktualisiert; keine belegte Änderung der geprüften BACS-Empfehlungen. | [Einzelbericht 04](artikel-04-quellen-und-aenderungen.md) |
| 05 | MFA/Passkeys | Stand, Providerabschnitt, Umstiegsplan, Checklistenabschnitt und Quellenapparat ergänzt: [Microsoft](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers) nennt Providerkonfiguration **ab 30.10.2026**. Lizenz-/Tenant-Fachprüfung offen. | [Einzelbericht 05](artikel-05-quellen-und-aenderungen.md) |
| 06 | Microsoft 365 absichern | Artikel- und Checklistenstand aktualisiert; keine belegte Änderung der gezielt geprüften Microsoft-/EDÖB-/Fedlex-Aussagen; Tenantprüfung offen. | [Einzelbericht 06](artikel-06-quellen-und-aenderungen.md) |
| 07 | Wiederherstellung testen | Artikel- und Vorlagenstand aktualisiert; keine belegte Änderung der geprüften BACS-/CISA-Leitlinien. | [Einzelbericht 07](artikel-07-quellen-und-aenderungen.md) |
| 08 | IT-Sicherheitscheck | Artikel- und Arbeitsmittelstand aktualisiert; sichtbare Vorlagenversion an die bestehende Metadatenversion **1.1** angeglichen. Keine fachliche Änderung. | [Einzelbericht 08](artikel-08-quellen-und-aenderungen.md) |
| 09 | Schatten-KI | Artikel- und Vorlagenstand aktualisiert; keine belegte Änderung von DSG/DSV/EDÖB-Grundaussagen. Konkrete Anbieter-/Datenflussprüfung offen. | [Einzelbericht 09](artikel-09-quellen-und-aenderungen.md) |
| 10 | Kommunikation nach Cyberangriff | Artikel- und Vorlagenstand aktualisiert; keine belegte Änderung der geprüften BACS-/EDÖB-Grundaussagen. | [Einzelbericht 10](artikel-10-quellen-und-aenderungen.md) |
| 11 | Lieferantenrisiken | Artikel- und Vorlagenstand aktualisiert; keine belegte Änderung der geprüften BACS-/EDÖB-Grundaussagen. Verträge/Datenflüsse offen. | [Einzelbericht 11](artikel-11-quellen-und-aenderungen.md) |
| 12 | NIS2/DORA | Artikel- und Vorlagenstand aktualisiert; keine belegte materielle Änderung in den geprüften EU-/Schweizer Originalquellen. Nationales Recht und Einzelfall-Unterstellung offen. | [Einzelbericht 12](artikel-12-quellen-und-aenderungen.md) |

## Konkrete Blocker für Live-Publikation

1. **Fehlende Freigabe:** Alle zwölf Artikel und zwölf Arbeitsmittel enthalten `[FACHPRÜFUNG ERFORDERLICH]`; keine zuständige Fachperson hat hier eine tatsächliche Freigabe erteilt. Rechts-, Datenschutz-, Forensik-, Microsoft-Tenant- und NIS2/DORA-Einzelfragen bleiben offen. Artikel 01 darf trotz erreichtem Datum **nicht** nachträglich live geschaltet werden.
2. **CMS-Zugang für diesen Lauf fehlt:** In der aktuellen Connector-Konfiguration ist kein Webador-Connector aktiv; My Browser ist deaktiviert. Der am 20. September zuvor verifizierte interaktive Webador-Zugang ist **keine** in diesem Lauf authentifizierte CMS-Sitzung. Es wurde daher weder im Webador-Projekt **DKSchV Pro** navigiert noch ein öffentlicher Inhalt verändert. Bei Webador können normale Editoränderungen unmittelbar live gehen.
3. **Öffentliche Ziele fehlen:** Alle zwölf vorgesehenen `/wissen/`- und zwölf `/resources/`-URLs liefern HTTP 404. Ohne geprüfte Zielseiten wären interne Links live fehlerhaft. Vor einer Publikation alle Primärquellen und sämtliche öffentlichen Verweisziele **am Publikationstag** erneut prüfen, widersprüchliche Aussagen klären, Fachmarker bearbeiten und erst danach einen authentifizierten CMS-Import ausführen.
4. **Keine fiktive Freigabe aus technischer QA ableiten:** Der Validator prüft Aufbau, Metadaten, referenzierte Quellen und lokale Slugs; ein 404-Ziel oder eine fehlende Fachprüfung kann dadurch nicht aufgehoben werden.

## Fortsetzung

Der geplante Task **«DKSchV News und Blogpflege»** wurde am 04.10.2026 als **aktiv** verifiziert und läuft sonntags um **09:00 Europe/Zurich**. Nächste News: **11.10.2026 (ISO-Woche 41)**; nächste zweiwöchentliche Artikelprüfung: **18.10.2026 (ISO-Woche 42)**. Die weitere lokale Quellenpflege läuft; eine autonome Webador-Live-Publikation bleibt bis zur Klärung der genannten Blocker gesperrt. **Live-Änderungsprotokoll:** keine Einträge, da keine Live-Änderung stattgefunden hat.
