# Quellennotizen – Aktiv ausgenutzte Schwachstellen

**Berichtsfenster:** nach 04.10.2026 09:00 bis 11.10.2026 09:00 Europe/Zurich. Die Quellen wurden am 11.10.2026 nach dem Fenster abgerufen; dies ist kein historischer Snapshot um 09:00.

## Aufgenommene Meldungen

### FortiMail – CVE-2026-104286
- CISA meldete die Aufnahme am 01.10.2026; die Meldung liegt damit innerhalb des neuen Berichtsfensters nicht als neue KEV-Aufnahme nach dem 04.10., wurde aber wegen einer belegten materiellen Herstelleränderung aufgenommen.
- Fortinet FG-IR-26-175: unauthentifizierter Path-Traversal/NULL-Byte-Fehler, der das Schreiben beliebiger Dateien ermöglichen kann; Exploitation in the wild bestätigt.
- Betroffene Versionen/Fixes: 8.0.0–8.0.1 -> 8.0.2+; 7.6.0–7.6.6 -> 7.6.7+; 7.4.0–7.4.8 -> 7.4.9+; 7.2.0–7.2.9 -> 7.4+.
- Workarounds: IBE deaktivieren; alternativ Webmail nicht aus dem Internet erreichbar machen bzw. nur vertrauenswürdige Netze zulassen; bei WAF POST auf `/ibe` mit `../` blockieren. Fortinet nennt IoCs und empfiehlt Logs zu prüfen.
- Neue Fixverfügbarkeit gegenüber der Vorwochenausgabe: Fortinet aktualisierte am 05.10.2026 die Solution; FortiMail Cloud wurde am 05.10. auf 7.6.7 GA bzw. 8.0.2 GA gebracht. Cloud-Kunden müssen laut Hersteller nichts tun. Advisory am 07.10.2026 nochmals mit Cloud-Fixpräzisierung aktualisiert.
- Quelle: https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- Gegenquelle: https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog

### Citrix NetScaler ADC/Gateway – CVE-2026-88779
- CISA-KEV-Katalog: Eintrag am 04.10.2026, Due Date 07.10.2026; CISA führt die Lücke als aktiv ausgenutzt. Die CISA-Frist ist eine US-FCEB-Frist und entfaltet keine Schweizer Rechtswirkung.
- Produktumfang: kundenseitig betriebene NetScaler ADC und NetScaler Gateway; Cloud-managed Services werden laut Citrix durch Cloud Software Group aktualisiert. Voraussetzung laut Hersteller: Konfiguration als SAML SP oder SAML IdP. Auswirkung: Memory overflow bis Denial of Service.
- Fixe laut Citrix CTX697174: 14.1-73.41+, 13.1-64.28+, 14.1-FIPS-73.41 FIPS+ sowie 13.1-FIPS/NDcPP-37.282+. Keine belastbare separate Hersteller-Workaround-Angabe gefunden; Voraussetzung und Konfiguration prüfen, dann auf den passenden Build aktualisieren.
- Das ist eine neue KEV-Aufnahme gegenüber der Vorwochenausgabe; die Vorwoche behandelte andere NetScaler-CVEs 88771/88772.
- Quellen: https://www.cisa.gov/known-exploited-vulnerabilities-catalog ; https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174

## Geprüfte, aber nicht aufgenommene Quellen und Ausschlüsse

- CISA-Meldung vom 02.10.2026: CVE-2026-102489 und CVE-2026-102490 (Zammad) bestätigt als KEV-Aufnahmen. Nicht aufgenommen, weil im verfügbaren Herstellerquellencheck kein belastbarer direkter Hersteller-Fix-/Workaround-Nachweis für die konkrete neue Meldung verifiziert werden konnte; keine Schweizer KMU-Relevanz aus den Quellen belegt. Quelle: https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA-Katalogeinträge vom 08.10.2026: ProFTPD CVE-2015-3306, ONLYOFFICE Docs CVE-2021-3199 und Strapi CVE-2023-22894. CISA-Aufnahme und Due Date 11.10.2026 wurden geprüft. Direkte Herstellerseiten wurden ebenfalls geöffnet: ProFTPD nennt aktuelle Releases 1.3.9d/1.3.10rc4, aber keinen CVE-spezifischen Fixnachweis auf der Startseite; Strapi nennt den Fix für CVE-2023-22894 in 4.8.0, die Offenlegung ist jedoch alt (2023, Seite aktualisiert 17.07.2026) und keine neue Herstelleränderung im Berichtsfenster; ONLYOFFICE-Changelog wurde geöffnet, aber der konkrete CVE-Fix konnte dort nicht eindeutig einer aktuellen Version zugeordnet werden. Deshalb nicht als neue Meldungen aufgenommen.
- Microsoft, Cisco, BACS, EDÖB, Fedlex, EU-Kommission und EUR-Lex: keine zusätzliche neue, im Fenster belegte aktiv ausgenutzte Schwachstellenmeldung mit für Schweizer KMU hinreichend verifiziertem Produkt-/Fixumfang gefunden.
- FortiMail wurde nicht wegen der alten 01.10.-KEV-Aufnahme erneut als unveränderte Meldung aufgenommen, sondern ausschliesslich wegen der belegten Solution-/Cloud-Fixänderung vom 05./07.10.

## Wartungsmanifest-Abgrenzung

Das Manifest enthält keinen dedizierten Schwachstellenartikel und keine konkrete Artikelnummer für FortiMail oder NetScaler. Daher wurden keine `affected_articles` zugeordnet. Es wurden keine Artikel, Arbeitsmittel, Manifeste oder CMS-Inhalte verändert. Die Zuordnung zu einem kommenden Review bleibt offen.

## Unbestätigt

- Eine tatsächliche Betroffenheit eines Schweizer KMU, Internet-Exponierung, Tenant-/Cloud-Konfiguration oder erfolgreiche Kompromittierung ist aus den Quellen nicht ableitbar.
- CISA-Due-Dates gelten im Kontext des US-FCEB-Regimes; sie sind keine Schweizer Fristen.

## Gezielte Endkorrektur am 11.10.2026

Das CTX697174-Bulletin verlinkt inzwischen auf ein weiteres [NetScaler-Bulletin CTX697191](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697191) zu **CVE-2026-107406**, initial veröffentlicht am **08.10.2026**, zuletzt geändert am 09.10. Dieses wurde im Rahmen der konkreten Fixstand-Klärung geöffnet. Es beschreibt einen kritischen Speicherfehler mit möglicher Remote Code Execution oder Denial of Service. Bei 14.1-73.37 bis 14.1-73.41 und 13.1-64.23 bis 13.1-64.28 (einschliesslich, mit den zugehörigen FIPS/NDcPP-Spannen) gilt die Voraussetzung **SAML IdP**; bei älteren Versionen **SAML SP oder IdP**. Neue Fixstände: 14.1-73.46+, 13.1-64.29+, 14.1-73.46 FIPS+ und 13.1-FIPS/NDcPP 13.1.37.283+ laut Hersteller. Die bisherige nur auf CVE-2026-88779 gerichtete News-Update-Empfehlung wurde deshalb erweitert: vor dem Upgrade beide aktuellen Bulletins und Versionszweig prüfen, nicht einen inzwischen unzureichenden älteren Fixstand pauschal empfehlen.

Der offizielle CISA-JSON-Katalog wurde zusätzlich unter `cisa-kev-snapshot.json` gesichert, Datensatzstand **2026-10-08T20:09:18.9833Z**. Er enthält CVE-2026-88779 (Date Added 04.10., Due Date 07.10.) und **keinen Eintrag** für CVE-2026-107406. Im finalen Text wird für die neue CVE deshalb keine aktive Ausnutzung behauptet. Das Fehlen im Katalog beweist nicht Nichtausnutzung.

Die Datumsdarstellung `10-04-2026` im CTX697174-Header ist im Kontext des Changelogs **Oktober**, nicht April: das Changelog nennt 2026-10-03 (PST). Die KEV-Aufnahme ist datumsscharf auf 04.10.2026 belegt; eine Uhrzeit der Aufnahme im Verhältnis zum 09:00-Fensteranfang ist nicht ausgewiesen.
