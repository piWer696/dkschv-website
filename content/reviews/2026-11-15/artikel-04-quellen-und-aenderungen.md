# Quellen- und Änderungsprüfung – Artikel 04

**Prüfdatum:** 15. November 2026, ISO-KW 46, Europe/Zurich CET.  
**Aktualitätsfenster:** Seit 1. November 2026 bis 15. November 2026, 09:00 CET.  
**Tatsächliche Fetch-Rückgaben:** 15. November 2026, 09:06:14–09:08:35 CET, also nach 09:00. Die unten genannten Uhrzeiten sind die tatsächlichen Tool-Rückgabezeiten, keine erfundenen historischen Abrufzeiten.  
**Artikel:** `blog-paket/articles/04-ransomware-resistente-backups.md`.  
**Arbeitsmittel:** `blog-paket/resources/04-backup-selbstcheck.md`.  
**Autor dieses Berichts:** Manus AI.

## Ergebnis und Veröffentlichungsstatus

Alle ursprünglich 16 unterschiedlichen zitierten externen Original-URLs wurden direkt mit `fetch` geöffnet. Die neue BACS-Heimnetzquelle ergibt jetzt 17 unterschiedliche zitierte Original-URLs: 18 Definitionen im Artikel wegen der doppelt verwendeten CISA-Leitfadenadresse und neun im Selbstcheck. Alle 17 lieferten den verwendeten Aussageumfang. Die Fedlex-HTML-Abrufe waren längenbedingt `partial`, aber die benötigten Artikel und Fassungslisten waren lesbar; zusätzlich wurden vorhandene amtliche XML und Chronologien gelesen. Die beiden gesonderten Fedlex-Änderungsseiten sind dagegen **inhaltlich nicht auslesbar**: Sie lieferten nur den JavaScript-Hinweis. Der technische Toolstatus `success` wird deshalb nicht als erfolgreiche Änderungskontrolle ausgegeben. [7] [8] [24] [25] [26] [27] [28] [29]

Materiell ergänzt wurden der begrenzte Homeoffice-/Heimnetzkontext im Wiederherstellungsabschnitt und der entsprechende Kontrollpunkt samt Nachweisgrenzen im Selbstcheck. Die BACS-Meldung vom 3. November betrifft private Heimnetzfälle, nicht ein bestimmtes KMU. Sie ersetzt keine Untersuchung einer Zielumgebung und keine abgeschlossene Forensik. [17] Die vorhandene NIST-Recover-Quelle bleibt verwendbar für die allgemeine Einordnung, wird nun aber im Artikel sichtbar als nicht mehr aktualisiert bezeichnet. [11]

Artikel und Arbeitsmittel bleiben **nicht freigegeben**. Es gab keine CMS- oder Browseroperation, keine Zugangsdatenverwendung, keine Tenant-/Produktprüfung und keine Veröffentlichung. Das geplante Veröffentlichungsdatum 22.10.2026 ist erhalten, begründet aber keine Erlaubnis. Die Wartungsbasis, Vorwochennews, Vormerkungen und der Einzelbericht vom 01.11. wurden lokal gelesen. Der dort dokumentierte alte CMS-/HTTP-Zustand wurde nicht als heutige Messung übernommen. Dieser Lauf prüft lokale Inhalte und externe Quellen, nicht den Live-Status.

## Quellenstand je zitierter externer Originalquelle

Alle folgenden Einträge beziehen sich auf den Abruf **15.11.2026, CET Europe/Zurich**. «Lesbar» bezeichnet Inhalt über den stateless Quellenzugang, nicht eine unabhängig gemessene HTTP-Statusprüfung oder Einzelfall-Fachprüfung. Original-URL und Titel stehen jeweils in der zugehörigen nummerierten Referenz.

### 1. BACS – Erste Schritte

**Original-URL:** https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden. **Rückgabe:** 09:06:14, lesbar, vollständiger Auszug. **Quellenstand:** Kein seitenbezogenes Veröffentlichungs-/Änderungsdatum im Text. **Aussage:** Regelmässig auf externes Medium oder sichere Cloud sichern; Backup nicht dauerhaft mit dem Computer verbunden halten. **Einschränkung:** Allgemeine Orientierung; kein Nachweis eines sicheren Cloud- oder Backup-Designs. Artikel [1]. [1]

### 2. BACS – Grundschutz

**Original-URL:** https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden. **Rückgabe:** 09:06:14, lesbar. **Quellenstand:** Kein seitenbezogenes Datum. **Aussage:** Datensicherung als technische Massnahme, Governance, Kontinuitätsmanagement und Zuständigkeiten als organisatorische Massnahmen. **Einschränkung:** Keine konkrete Architekturprüfung. Artikel [2]. [2]

### 3. BACS – Ransomware: Was nun?

**Original-URL:** https://www.bacs.admin.ch/de/ransomware-was-nun. **Rückgabe:** 09:06:14, lesbar. **Quellenstand:** Kein seitenbezogenes Datum. **Aussage:** Netztrennung, Infektionsweg, Neuinstallation und Restore; frühe forensische Entscheidung und fachkundige Sicherungen vor Reparatur oder Neustart. **Einschränkung:** Keine tatsächliche Triage, Beweissicherung oder Bereinigungsfreigabe. Artikel [3]. [3]

### 4. BACS – Zusammenarbeit mit IT-Dienstleistern

**Original-URL:** https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern. **Rückgabe:** 09:06:16, lesbar. **Quellenstand:** Kein seitenbezogenes Datum. **Aussage:** Zuständigkeiten, Backup-Konzept und letzter erfolgreicher Restore-Test, 3-2-1 mit externer idealerweise Offline-Kopie, periodische Leistungsprüfung. **Einschränkung:** Keine Vertrags-, Haftungs- oder Providerfreigabe. Artikel [4], Selbstcheck [1]. [4]

### 5. CISA – StopRansomware Guide

**Original-URL:** https://www.cisa.gov/stopransomware/ransomware-guide. **Rückgabe:** 09:06:18, relevante Abschnitte lesbar; vollständiger Abruf zusätzlich gespeichert. Der gespeicherte Versionshinweis wurde um 09:07:51 lokal gelesen, die Object-Lock-Passage zuvor gezielt lokal ausgewertet. **Quellenstand:** Linkbezeichnung «Guide September 2023», kein belastbares aktuelles Seitenänderungsdatum. **Aussage:** Offline und verschlüsselt sichern, Verfügbarkeit/Integrität testen, Admin-/Benutzerkonten trennen, Object Lock/Löschschutz und Versionierung sorgfältig einsetzen; kritische Dienste priorisieren und Reinfektion sauberer Systeme vermeiden. **Einschränkung:** US-Orientierung, kein Schweizer Rechtsstandard oder organisationsbezogener Test. Artikel [5] und [6], Selbstcheck [2]. [5]

### 6. AWS – S3 Object Lock

**Original-URL:** https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html. **Rückgabe:** 09:06:17, lesbar. **Quellenstand:** Kein Seitenänderungsdatum. **Aussage:** WORM auf Objektversionen, Aufbewahrungsmodi und Governance-Umgehung mit besonderer Berechtigung und Header; Schutz verhindert nicht neue Versionen oder Delete Marker. **Einschränkung:** Herstellerdokumentation, keine tatsächliche Object-Lock-/Schlüssel-/Kontoprüfung. Neue Details wie variable Retention wurden nicht als notwendige allgemeine Architekturvorgabe übernommen. Artikel [7]. [6]

### 7. Fedlex – DSG

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de. **Rückgabe:** 09:06:31, `partial` wegen Auszugslänge; Art. 8 und Fassungsliste lesbar. **Quellenstand:** In Kraft, Stand 07.07.2025. **Aussage:** Verantwortlicher und Auftragsbearbeiter gewährleisten risikogerechte Datensicherheit durch geeignete technische und organisatorische Massnahmen. **Einschränkung:** Allgemeine Norm; keine Bewertung der konkreten Retention, Datenbearbeitung oder Verträge. Der sichtbare Wartungshinweis 13.11.20:00–15.11.20:00 belegt nur eine mögliche temporäre Einschränkung, nicht die Ursache jedes Abrufproblems. Artikel [8], Selbstcheck [5]. [7]

### 8. Fedlex – DSV

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de. **Rückgabe:** 09:06:31, `partial` wegen Auszugslänge; Art. 1–3 und Fassungsliste lesbar. **Quellenstand:** In Kraft, Stand 01.12.2025. **Aussage:** Schutzbedarf und Risiken bestimmen; Art. 3 Abs. 2 Bst. d verlangt rasche Wiederherstellbarkeit von Verfügbarkeit und Zugang nach physischem oder technischem Zwischenfall. **Einschränkung:** Keine individuelle Rechts-, Retention- oder RPO/RTO-Freigabe. Artikel [9], Selbstcheck [6]. [8]

### 9. NIST – Recovery Point Objective

**Original-URL:** https://csrc.nist.gov/glossary/term/recovery_point_objective. **Rückgabe:** 09:06:31, lesbar. **Quellenstand:** Kein Seitenstanddatum; Definition aus SP 800-34 Rev. 1. **Aussage:** Zeitpunkt, auf den Daten nach einem Ausfall wiederhergestellt werden müssen. **Einschränkung:** Definition, nicht gemessener Datenverlust oder vereinbarter Zielwert. Artikel [10], Selbstcheck [3]. [9]

### 10. NIST – Recovery Time Objective

**Original-URL:** https://csrc.nist.gov/glossary/term/recovery_time_objective. **Rückgabe:** 09:06:31, lesbar. **Quellenstand:** Kein Seitenstanddatum; Definition aus SP 800-34 Rev. 1. **Aussage:** Gesamtdauer, während der Komponenten in der Wiederherstellungsphase sein können, bevor Geschäftsprozesse beeinträchtigt werden. **Einschränkung:** Definition, keine Restore-Kapazitätsmessung. Artikel [11], Selbstcheck [4]. [10]

### 11. NIST – Recover

**Original-URL:** https://www.nist.gov/cyberframework/recover. **Rückgabe:** 09:06:31, lesbar. **Quellenstand:** Erstellt 01.02.2018, aktualisiert 27.05.2026; ausdrücklich nicht mehr aktualisiert und möglicherweise veraltet. **Aussage:** Wiederherstellungsprozesse und Verfahren ausführen und pflegen für zeitgerechte Wiederherstellung nach Cybervorfällen. **Einschränkung:** Historische Zuordnungsseite, keine aktuelle Framework-Vollprüfung. Sichtbaren Hinweis und Quellentitel präzisiert, keine neue Quelle. Artikel [12]. [11]

### 12. NIST NCCoE – MSP-Backup-Leitfaden

**Original-URL:** https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final. **Rückgabe:** 09:06:31, lesbar. **Quellenstand:** April 2020, Final 24.04.2020. **Aussage:** Empfehlungen für MSPs und Kunden zum Durchführen, Pflegen und Testen von Backups, passend zu individuellen Bedürfnissen. **Einschränkung:** Verwendete Aussage im Abstract gedeckt; die verlinkte PDF wurde nicht als zusätzliche aktuelle technische Vollprüfung behauptet. Artikel [13]. [12]

### 13. BACS – Notfallkonzept

**Original-URL:** https://www.bacs.admin.ch/de/notfallkonzept. **Rückgabe:** 09:06:17, lesbar. **Quellenstand:** Kein eigenes Seitenänderungsdatum; nun sichtbare KMU-/Gemeindevorlagendaten 11.11.2026 statt des im Vorbericht dokumentierten KMU-Dateidatums 18.05.2026. **Aussage:** Vorbereitung, Vorfalleintritt, Bewältigung, Nachbearbeitung und zugeordnete Verantwortlichkeiten. **Einschränkung:** Nur die Seite gelesen; weder Inhalt noch Änderungsumfang der DOCX-Vorlagen geprüft. Das neue Dateidatum ist keine neue Freigabe und verlangt keine beleglose Inhaltsänderung des Artikels. Artikel [14], Selbstcheck [7]. [13]

### 14. BACS – Malwareverdacht vom 6. Oktober

**Original-URL:** https://www.bacs.admin.ch/de/26w40-de. **Rückgabe:** 09:06:31, lesbar. **Quellenstand:** Veröffentlicht 06.10.2026. **Aussage:** Einzelindikator ist kein Infektionsbeweis; mehrere Auffälligkeiten untersuchen; Fachperson und bei Geschäftsgeräten zuständige IT einbeziehen. **Einschränkung:** Keine forensische Einzelfallprüfung. Artikel [15], Selbstcheck [8]. [14]

### 15. CISA – SafePay

**Original-URL:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a. **Rückgabe:** 09:06:32, relevante Abschnitte lesbar; gespeicherter Volltext lokal auf Versionshinweise ausgewertet. **Quellenstand:** Release und Initial Version 20.10.2026, keine weitere Version im gelesenen Verlauf. **Aussage:** SafePay-Akteure löschten in einigen Fällen alle netzwerkangehängten Unternehmensbackups. **Einschränkung:** Gruppenspezifische Beobachtung, kein Befund zu einem Schweizer KMU; keine IOC-/Forensikprüfung. Bestehende begrenzte Passage erhalten. Artikel [16]. [15]

### 16. BACS – KMU Cybersicherheit 2026

**Original-URL:** https://www.bacs.admin.ch/de/26-kmustudie-de. **Rückgabe:** 09:06:33, lesbar. **Quellenstand:** Veröffentlicht 22.10.2026. **Aussage:** Neun von zehn KMU erstellen Backups, nur jedes vierte testet Wiederherstellung. **Einschränkung:** BACS-Mitteilung zur Studie; keine neu geprüfte Studienmethodik oder Individualaussage. Bestehende Attribution erhalten. Artikel [17]. [16]

### 17. BACS – Heimnetzwerke, neue zitierte Quelle

**Original-URL:** https://www.bacs.admin.ch/de/26w44-de. **Rückgabe:** 09:06:33, lesbar. **Quellenstand:** Veröffentlicht 03.11.2026, Rückblick Woche 44. **Aussage:** Gemeldete private Heimnetzinfektionen, Risiken aus Internetexposition und ungepatchten Diensten; gegebenenfalls Neuinstallation und Untersuchung anderer Geräte im Netz durch Fachpersonen. **Einschränkung:** Kein KMU-Vorfall, keine fertige Forensik, kein sauberer Backup-Nachweis. Keine Plex-CVE oder bereinigte Version in der Meldung. Neue Artikelquelle [18], neue Selbstcheckquelle [9], beide im Text verwendet. [17]

## Zusatzquellen und Aktualitätsabgleich seit 1. November

Die Websuche lieferte am 15.11.2026 Antworten um 09:06:16, 09:07:52 und 09:08:13 CET. Gesucht wurde nach BACS-November-/Heimnetz-/Cyberresilienzmeldungen und auf Englisch nach CISA-Ransomware-/Backup-/Recovery-Meldungen. Suchsnippets wurden nicht als Inhaltsbelege übernommen. Die ausgewählten amtlichen Treffer wurden mit `fetch` geöffnet. Die Auswahl ist ein gezielter Aktualitätsabgleich, kein vollständiger Nachweis aller weltweiten oder seitenbezogenen Änderungen. Nicht einschlägige Sekundärtreffer wurden nicht zitiert oder in Wiederholungsschleifen weitergesucht.

### 18. BACS – Im Fokus

**Original-URL:** https://www.bacs.admin.ch/de/im-fokus. **Rückgabe:** 15.11.2026, 09:06:34 CET, selektierter Novemberbereich lesbar. **Quellenstand:** Kein eigener Seitenstand; sichtbare Meldungen vom 02., 03., 06., 09. und 10.11.2026. **Aussage:** Identifiziert die unten direkt geprüften Novembermeldungen. **Einschränkung:** Übersicht, keine vollständige historische News-/Änderungsgarantie. Nicht in Artikel/Selbstcheck aufgenommen. [18]

### 19. BACS – Brown-Bag-Lunches zur Cyberresilienz

**Original-URL:** https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de. **Rückgabe:** 15.11.2026, 09:07:27 CET, lesbar. **Quellenstand:** Veröffentlicht 02.11.2026. **Aussage:** Kritische Prozesse, IT-/OT-/Dienstleisterabhängigkeiten und eingeübte Notfall-/Wiederherstellungspläne. **Entscheid:** Bestätigt bestehende prozessorientierte Abschnitte; Veranstaltungstermine nicht künstlich in Evergreen-Text eingebaut. **Einschränkung:** Keine Zielarchitektur- oder RPO/RTO-Freigabe. [19]

### 20. BACS – Kühl- und Kältesteuerungen

**Original-URL:** https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de. **Rückgabe:** 15.11.2026, 09:07:27 CET, lesbar. **Quellenstand:** Veröffentlicht 10.11.2026. **Aussage:** Systeme und externe Wartung identifizieren, Internetexposition prüfen, Herstellerupdates und EOL-Schutz berücksichtigen; Manipulationen können Betriebsunterbrüche verursachen. **Entscheid:** Relevant für bereits vorhandenes Inventar und Abhängigkeiten, aber keine neue generische Backup-Leitlinie. **Einschränkung:** Kein Organisations-/OT-Befund oder Gerätefix geprüft; keine Produktfreigabe und keine ungeprüfte Firmwarematrix im Artikel. [20]

### 21. BACS – KI-Fakeshops und Paket-Phishing

**Original-URL:** https://www.bacs.admin.ch/de/26w45-de. **Rückgabe:** 15.11.2026, 09:07:27 CET, lesbar. **Quellenstand:** Veröffentlicht 10.11.2026. **Aussage:** Einkaufs-/Paketphishing, Karten- und Identitätsmissbrauch. **Entscheid:** Keine Backup-, Retention- oder Restore-Änderung aus der Meldung abgeleitet. **Einschränkung:** Nur diese Meldung, kein allgemeiner Nichtfund. [21]

### 22. BACS – EHRA-Phishing

**Original-URL:** https://www.bacs.admin.ch/de/warnung-ehra-de. **Rückgabe:** 15.11.2026, 09:07:27 CET, lesbar. **Quellenstand:** Veröffentlicht 06.11.2026. **Aussage:** Angebliche Handelsregister-Datenaktualisierung, unabhängige Verifikation. **Entscheid:** Vormerkung gelesen; keine neue Backup-Leitlinie. **Einschränkung:** Keine Einzelfall- oder Meldefreigabe. [22]

### 23. BACS – ESTV-Phishing

**Original-URL:** https://www.bacs.admin.ch/de/warnung-estv-de. **Rückgabe:** 15.11.2026, 09:07:27 CET, lesbar. **Quellenstand:** Veröffentlicht 09.11.2026. **Aussage:** Phishing sammelt persönliche Angaben für weitere Betrugsversuche. **Entscheid:** Keine Änderung am Backup-Artikel. **Einschränkung:** Kein konkreter Vorfall; der fehlerhaft extrahierte weiterführende Melde-Link wurde nicht als neue Artikelreferenz verwendet. [23]

### 24. Fedlex – vorhandene amtliche DSG-XML

**Original-URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml. **Rückgabe:** 15.11.2026, 09:07:26 CET, relevanter Wortlaut lesbar. **Quellenstand:** Fassung 07.07.2025, in aktueller Fassungsübersicht und History verlinkt. **Aussage:** Art. 8 bestätigt. **Einschränkung:** Keine gesamte Einzelfall-Rechtsanalyse. Es wurde die vorhandene URL genutzt, keine XML-Adresse erfunden. [24]

### 25. Fedlex – vorhandene alternative amtliche DSV-XML

**Original-URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml. **Rückgabe:** 15.11.2026, 09:07:26 CET, Art. 1–3 lesbar. **Quellenstand:** Fassung 01.12.2025. **Aussage:** Rasche Wiederherstellbarkeit nach Art. 3 Abs. 2 Bst. d bestätigt. **Einschränkung:** Keine Retention- oder Rechtsfreigabe; vorhandene alternative URL mit `xml-2`, keine abgeleitete `xml-1`-Adresse. [25]

### 26. Fedlex – DSG-History

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/history. **Rückgabe:** 15.11.2026, 09:07:25 CET, Chronologie lesbar. **Quellenstand:** Jüngste ausgewiesene Fassung 07.07.2025. **Aussage:** Kein neuerer Konsolidierungsstand in der gelesenen amtlichen Chronologie. **Einschränkung:** Ersetzt nicht die gesperrte artikelweise Änderungsübersicht; keine lückenlose Rechtsänderungsanalyse. [26]

### 27. Fedlex – DSV-History

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de/history. **Rückgabe:** 15.11.2026, 09:07:25 CET, Chronologie lesbar. **Quellenstand:** Jüngste ausgewiesene Fassung 01.12.2025. **Aussage:** Kein neuerer Konsolidierungsstand in der gelesenen Chronologie. **Einschränkung:** Keine vollständige artikelweise Änderungskontrolle. [27]

### 28. Fedlex – DSG-Änderungen: Inhaltsblocker

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes. **Rückgabe:** 15.11.2026, 09:07:27 CET. **Status:** Tool `success`, aber nur 1’205 Zeichen JavaScript-/Browserhinweis, keine Änderungstabelle. **Quellenstand/Aussage:** Aktueller Inhalt der Änderungsübersicht nicht feststellbar. **Entscheid und Einschränkung:** **Nicht erfolgreich geprüft**; kein heutiger Satz «Art. 8 nicht in Änderungsliste» behauptet. Lesbare History/XML sichern nur den dokumentierten Fassungs-/Wortlautbefund. Kein Browser und keine Wiederholungsschleife. [28]

### 29. Fedlex – DSV-Änderungen: Inhaltsblocker

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes. **Rückgabe:** 15.11.2026, 09:07:27 CET. **Status:** Tool `success`, aber nur 1’205 Zeichen JavaScript-/Browserhinweis, keine Änderungstabelle. **Quellenstand/Aussage:** Aktueller Inhalt der Änderungsübersicht nicht feststellbar. **Entscheid und Einschränkung:** **Nicht erfolgreich geprüft**; keine heute vollständig kontrollierte artikelweise Änderungsliste. History/XML lesbar, Teilblocker bleibt. Kein Browser und keine Wiederholungsschleife. [29]

### 30. CISA – Advisory-Übersicht

**Original-URL:** https://www.cisa.gov/news-events/cybersecurity-advisories. **Rückgabe:** 15.11.2026, 09:08:30 CET, lesbar. **Quellenstand:** Sichtbare erste Ergebnisseite bis 13.11.2026, kein eigener Stand. **Aussage:** Novembereinträge umfassen KEV-Meldungen und Kühlsteuerungsorientierung; die sichtbare Liste enthält keine neue benannte Ransomwarewarnung. **Entscheid:** Kein pauschaler Nichtfund und keine unkontrollierte CVE-Aufnahme. **Einschränkung:** Nur erste Ergebnisseite und gezielte Suchtreffer, keine Vollprüfung jeder KEV-/Produktmeldung oder aller Revisionen. [30]

### 31. CISA – Resilienzmonat 2026

**Original-URL:** https://www.cisa.gov/news-events/news/cisa-kicks-critical-infrastructure-security-and-resilience-month-2026. **Rückgabe:** 15.11.2026, 09:08:30 CET, lesbar. **Quellenstand:** Released 02.11.2026. **Aussage:** Wichtigste Systeme/externe Abhängigkeiten kennen, Risiken priorisieren, Reaktions-/Recoverypläne und Lernprozess. **Entscheid:** Bestätigt bestehende Kontrollpunkte, keine materielle Backupregeländerung. **Einschränkung:** US-Kampagne, keine Schweizer Pflicht oder geprüfte Zielarchitektur. [31]

### 32. Microsoft – Azure Backup Sicherheitsorientierung

**Original-URL:** https://learn.microsoft.com/de-de/azure/backup/security-overview. **Rückgabe:** 15.11.2026, 09:08:35 CET, lesbar. **Quellenstand:** Zuletzt aktualisiert 06.11.2026. **Aussage:** Logische Isolation ist keine physische/Netzwerk-Air-Gap und ersetzt keine Identitätskontrollen; Soft Delete, Unveränderlichkeit und Mehrbenutzerautorisierung haben unterschiedliche Funktionen, Unterstützung variiert; Threat Detection und Cross-Tenant-Restore sind als Vorschau beschrieben. **Entscheid:** Aktuelle Herstellerorientierung bestätigt die vorhandene Unterscheidung von Offline-/Unveränderbarkeitsschutz. Keine Azure-Funktions-, Regions-, Tenant- oder Retentiondetails in die produktneutrale Vorlage übernommen. **Einschränkung:** Kein tatsächlicher Tenant, keine Konfiguration, keine Wiederherstellung und keine Schweizer Eignung geprüft. [32]

Damit umfassen die Zusatzabrufe **15 unterschiedliche Adressen**, davon **13 inhaltlich lesbar und zwei Inhaltsblocker**. Keine neue materielle DSG-/DSV-Änderung ist anhand der lesbaren Chronologien und des relevanten XML-Wortlauts belegt; wegen der nicht auslesbaren Änderungsseiten wird keine vollständige artikelweise Änderungskontrolle behauptet. Neue Quellenstände stehen hier im Journal, nicht als Fachfreigabedatum in den Inhaltsdateien.

## Genau betroffene Abschnitte: vorher und nachher

### Artikel – Frontmatter

`stand` vorher: `1. November 2026`. Nachher: exakt `15. November 2026`.

`quellenpruefung_umfang` vorher:

> Alle 17 Quellendefinitionen des Artikels und alle acht des Arbeitsmittels, entsprechend 16 unterschiedlichen zitierten externen Original-URLs (der CISA-Leitfaden ist im Artikel zweimal referenziert), auf Erreichbarkeit und Aussagegehalt geprüft. Zusätzlich BACS «Im Fokus» sowie die BACS-Meldungen vom 20., 21. und 27. Oktober 2026 als Aktualitätskontext geprüft. Interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft.

Nachher:

> Alle 18 Quellendefinitionen des Artikels und alle neun des Arbeitsmittels: 17 unterschiedliche zitierte externe Original-URLs direkt abgerufen und im verwendeten Aussageumfang gelesen. Zusätzlich sechs BACS-Aktualitätsquellen seit 1. November, CISA-Übersicht und Resilienzmeldung, Microsoft-Backup-Orientierung sowie sechs amtliche Fedlex-Zusatzadressen geprüft. Interne Paketziele nur lokal abgeglichen, nicht live geprüft.

`quellenpruefung_status` vorher:

> Vollständig für die 16 unterschiedlichen zitierten externen Original-URLs am 1. November 2026, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation.

Nachher:

> 15. November 2026, tatsächliche Fetch-Rückgaben 09:06:14–09:08:35 CET Europe/Zurich: 17 zitierte Original-URLs inhaltlich lesbar, Fedlex-HTML teilweise gekürzt und durch lesbare History/XML ergänzt. Von 15 Zusatzadressen zwei Blocker: DSG-/DSV-Änderungsseiten liefern nur JavaScript-Hinweis. Keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe; keine RPO/RTO-, Retention- oder Architekturfreigabe und keine lückenlose historische Änderungsverifikation.

### Artikel – «RPO, RTO und Wiederanlauf: vom Backup-Journal zur Geschäftsentscheidung»

**Vorher:** Nach dem Absatz mit den hypothetischen Vier-/Achtstundenwerten und der NIST-Recover-Zitation stand direkt «Priorisieren Sie daher nicht nach Datenmenge, sondern nach Geschäftswirkung.» Der bestehende Absatz und die Definitionen bleiben unverändert.

**Nachher:** Dazwischen ergänzt:

> Die verwendete NIST-Zuordnungsseite «Recover» wird ausdrücklich nicht mehr aktualisiert. Sie dient hier nur der allgemeinen Begriffseinordnung, nicht als Nachweis einer aktuellen organisationsspezifischen Wiederherstellungsfreigabe. [12]

Die Zitation bezeichnet Artikelquelle [12], hier dokumentiert als [11]. Keine Änderung eines RPO-/RTO-Zielwerts oder der Architektur.

### Artikel – «Wiederherstellungsfähigkeit beweisen, nicht vermuten»

**Vorher:** Zwischen dem ersten Absatz zum isolierten Restore-Test und dem Absatz zur BACS-KMU-Studie gab es keinen Homeoffice-/Heimnetzbezug.

**Nachher:** Genau dort ergänzt:

> Berücksichtigen Sie auch Homeoffice- und externe Zugangswege, soweit diese für den Dienst relevant sind. Das BACS berichtete am 3. November 2026 über Schadsoftware in privaten Heimnetzen mit aus dem Internet erreichbaren, verwundbaren Diensten. Bei einer Infektion kann eine Neuinstallation nötig sein; auch weitere Geräte im selben Netz sollen untersucht oder von Fachpersonen untersucht werden. Für die Wiederherstellungsplanung ist dies ein Anlass, Heimnetzabhängigkeiten und die Beurteilung der Zielumgebung mit der zuständigen IT zu klären. Die Meldung belegt weder einen Vorfall in Ihrem KMU noch einen sauberen Sicherungsstand oder eine fertige forensische Untersuchung. Sie gibt keine konkrete PHP-/Plex-Version oder Backup-Architektur frei. [18] [6]

Die Zitationen bezeichnen Artikelquellen [18] und [6], hier dokumentiert als [17] und [5].

### Artikel – «Quellen»

**Vorher:** 17 Definitionen, keine Heimnetzquelle; Titel [12] «NIST Cybersecurity Framework – Recover».

**Nachher:** 18 Definitionen. Neue Definition [18] ist die geöffnete BACS-Original-URL `https://www.bacs.admin.ch/de/26w44-de` mit Titel «BACS – Woche 44: Wenn das Heimnetzwerk zum Einfallstor für Cyberkriminelle wird, 3. November 2026». Titel [12] nun «NIST Cybersecurity Framework – Recover, nicht mehr aktualisierte Zuordnungsseite». Alle bestehenden URLs erhalten; keine ungenutzte neue Referenz.

### Selbstcheck – Frontmatter und sichtbare Version

`version` vorher: `Stand 1. November 2026`. Nachher: `Stand 15. November 2026`. Die Version wird **wegen materiell ergänzter Kontroll- und Nachweisfragen** geändert, nicht allein wegen des Quellenabrufs. Ein `stand`-Feld war vorher nicht vorhanden; nachher enthält es exakt `15. November 2026`.

`quellenpruefung_umfang` vorher:

> Alle acht zitierten externen Original-URLs des Arbeitsmittels auf Erreichbarkeit und Aussagegehalt geprüft; interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft.

Nachher:

> Alle neun zitierten externen Original-URLs direkt abgerufen und im verwendeten Aussageumfang gelesen; gemeinsamer Abgleich mit Artikel 04 umfasst 17 zitierte Original-URLs und 15 Zusatzadressen. DSG/DSV zusätzlich mit vorhandener amtlicher History/XML geprüft. Interne Paketziele nur lokal abgeglichen, nicht live geprüft.

`quellenpruefung_status` vorher:

> Vollständig für die acht zitierten externen Original-URLs am 1. November 2026, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation.

Nachher:

> 15. November 2026, tatsächliche Fetch-Rückgaben 09:06:14–09:08:35 CET Europe/Zurich: neun zitierte Original-URLs inhaltlich lesbar. Zwei Zusatzblocker: DSG-/DSV-Änderungsseiten liefern nur JavaScript-Hinweis; History/XML lesbar. Keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe; keine RPO/RTO-, Retention- oder Architekturfreigabe und keine lückenlose historische Änderungsverifikation.

**Vorher nach H1:** Direkt «Zweck», keine sichtbare Version. **Nachher vor «Zweck»:**

> **Arbeitsmittelversion: Stand 15. November 2026.** Die Version bezeichnet die ergänzten Kontroll- und Nachweisfragen, keine fachliche Abnahme.

### Selbstcheck – «Zweck»

**Vorher:** Der Malwareverdacht-Absatz mit Quelle [8] war der letzte Absatz vor «Anwendung».

**Nachher:** Bestehende Absätze vollständig erhalten; danach ergänzt:

> Der BACS-Bericht vom 3. November 2026 betrifft private Heimnetze mit aus dem Internet erreichbaren, verwundbaren Diensten. Bei einer Infektion kann eine Neuinstallation erforderlich sein; weitere Geräte im selben Netz sollen untersucht oder durch eine Fachperson untersucht werden. Der Bericht ist hier nur ein begrenzter Anlass, Homeoffice-Abhängigkeiten im Wiederherstellungsweg zu erfassen. Er belegt keinen Vorfall im eigenen Unternehmen, keine sauberen Backups und keine abgeschlossene Forensik. Konkrete PHP-/Plex-Fixversionen oder eine zulässige Backup-Architektur werden daraus nicht abgeleitet. [9]

Zudem rein typografisch `Integritätsprüfungen.[1] [2]` zu `Integritätsprüfungen. [1] [2]` korrigiert.

### Selbstcheck – «Anwendung»

**Vorher:** Auf den Absatz «Füllen Sie den Selbstcheck gemeinsam …» folgte direkt die Bewertung je Kontrollpunkt.

**Nachher:** Bestehender Absatz erhalten; davor zwei Nachweisabsätze ergänzt:

> Halten Sie bei einem «Ja» fest, was genau nachgewiesen ist. Die Zusage eines Dienstleisters, ein Jobprotokoll und ein praktisch beobachteter Restore beantworten unterschiedliche Fragen. Ein Jobprotokoll kann den gewählten Sicherungslauf dokumentieren; daraus folgt noch nicht, dass die Daten für den Fachbereich nutzbar oder die Zielsysteme sauber sind. Notieren Sie deshalb den tatsächlich getesteten Dienst, die Umgebung, den Sicherungsstand und die Grenzen der Beobachtung. BACS und CISA verlangen den Blick auf die Wiederherstellung und regelmässige Tests, nicht nur auf vorhandene Kopien. [1] [2]
>
> Erheben Sie für Heimnetz- und Homeoffice-Bezüge nur die für den Wiederherstellungsweg benötigten Angaben. Vermerken Sie, ob ein geschäftlich genutztes Gerät oder ein notwendiger Fernzugang betroffen sein könnte und wer die weitere Abklärung verantwortet. Eine Unsicherheit ist kein Infektionsnachweis. Nehmen Sie über diesen Selbstcheck keine eigenmächtigen Reparaturen, Löschungen oder Änderungen an privaten Geräten vor. Der Prüfpunkt dient der Abstimmung mit der zuständigen IT; bei Verdacht bleibt eine fachkundige Untersuchung erforderlich. [8] [9]

Die Selbstcheckzitate [1], [2], [8], [9] sind hier [4], [5], [14], [17] dokumentiert. Die materiellen Ergänzungen halten auch den Volltext des vorher kürzeren Arbeitsmittels über 1’400 Wörter, ohne Originalinhalte zu streichen.

### Selbstcheck – «6. Restore-Test und Verbesserungen»

**Vorher:** Fünf bestehende Kontrollpunkte, danach direkt das Restore-Protokoll.

**Nachher:** Die fünf Originalpunkte bleiben; sechster Kontrollpunkt ergänzt:

> Relevante Homeoffice-/Heimnetz- und Fernzugangsabhängigkeiten sind benannt; offene Fragen zur Zielumgebung sind der zuständigen IT zur Abklärung zugewiesen.

Danach vor dem unveränderten Protokoll ergänzt:

> **Abgrenzung beim neuen Kontrollpunkt:** «Benannt» bedeutet nicht «forensisch untersucht» oder «freigegeben». Erfassen Sie nur, welche Abhängigkeit für den Dienst besteht, welche Erkenntnisse vorliegen und welche konkrete Frage noch offen ist. Das BACS beschreibt Heimnetzinfektionen und die mögliche Untersuchung weiterer Geräte; CISA warnt vor der erneuten Infektion sauberer Systeme während der Wiederherstellung. Diese Orientierungen ersetzen keine Beurteilung der tatsächlichen Umgebung. [9] [2]
>
> Besprechen Sie vor einem Test, wer die Eignung des Wiederherstellungsorts beurteilt und welche Systeme in das Szenario einbezogen werden. Das Testblatt darf dabei nicht als Erlaubnis verstanden werden, eine verdächtige Umgebung mit der letzten Sicherungskopie zu verbinden. Dokumentieren Sie eine offene Beurteilung als Einschränkung und vereinbaren Sie die zuständige Fachstelle. Ein erfolgreicher Dateirestore beweist nur das beobachtete Szenario. Er beweist weder, dass alle Geräte im selben Netz untersucht wurden, noch dass alle für den Geschäftsdienst erforderlichen Abhängigkeiten wieder funktionieren. Die Prüfung sauberer Systeme und die Priorität kritischer Dienste gehören laut CISA in den Wiederanlauf. [2]

### Selbstcheck – rein typografische Passagen und «Quellen»

In «5. Wiederherstellungsziele und Reihenfolge» wurde nur `Wiederherstellung.[3] [4]` zu `Wiederherstellung. [3] [4]` geändert. In «Grenzen und fachliche Prüfung» wurden nur `genügt.[5] [6]` und `ein.[7]` zu `genügt. [5] [6]` beziehungsweise `ein. [7]` geändert. Der gesamte Fachprüfungsmarker und die Aussage bleiben wortgleich.

«Quellen» vorher acht Definitionen; nachher neun. Neue Definition [9] ist dieselbe BACS-Heimnetz-Original-URL wie Artikelquelle [18], mit demselben Titel. Alle acht Originaldefinitionen bleiben erhalten und zitiert.

## Unveränderte Abschnitte und historische Felder

Im Artikel vollständig unverändert: H1 und Kurzantwort; «Ein vorhandenes Backup kann im Ernstfall trotzdem ausfallen» einschliesslich SafePay und Malwareverdacht; «3-2-1 richtig anwenden»; «Backup-Administration vom Produktivbetrieb trennen»; «Offline und unveränderbar» einschliesslich Retention-/Rechtshinweis und Fachmarker; hypothetisches Praxisbeispiel; typische Fehler; gesamter 30-Tage-Plan; nächster Schritt. Im RPO/RTO- und Wiederherstellungsabschnitt blieben alle bisherigen Absätze erhalten; nur die oben bezeichneten Absätze kamen hinzu.

Im Selbstcheck vollständig unverändert: H1; Originalaussagen und Bewertungsfelder ausser den dokumentierten Leerzeichen; alle Kontrollpunkte und Felder in Abschnitten 1–4; alle Kontrollpunkte und Zielwertfelder in Abschnitt 5; die fünf Originalkontrollpunkte und das vollständige Restore-Protokoll in Abschnitt 6; Kurzfazit/Priorisierung; Grenzen/Fachfragen ausser Zitationsleerzeichen. Es wurde kein Originalvolltext gelöscht.

`status`, Slugs, `meta_title`, `meta_description`, Zielgruppen-/Suchintentionfelder, Artikelautor und Veröffentlichungsdatum sowie Bezug des Selbstchecks sind unverändert. Alle vier ursprünglichen Vorkommen des Markers `[FACHPRÜFUNG ERFORDERLICH]` bleiben exakt erhalten, je zwei pro Datei. Die Dateien enthielten vor diesem Lauf weder `rechtsstand` noch `fachlich_geprüft_am`/`fachlich_geprueft_am`; solche Felder wurden nicht angelegt. Der Fachstatus ist unverändert. Neue Rechtsquellenstände stehen ausschliesslich in diesem Journal.

## Lokale Struktur- und Linkgrenzen

Die gezielte lokale Kontrolle am 15.11. um 09:10:22 CET ergab für den Artikel **18 definierte und 18 verwendete Quellenkennungen**, für den Selbstcheck **neun definierte und neun verwendete Kennungen**; keine fehlende oder ungenutzte Definition. Der CISA-Leitfaden bleibt aus Aussagegründen im Artikel doppelt definiert. Es gibt keine unkodierten Klammern in Quellen-URLs und kein Eszett in den Inhaltsdateien. Vier bereits vorhandene fehlende Leerzeichen vor Quellenzitationen im Selbstcheck wurden danach gezielt korrigiert.

Die Wortzählung ohne Frontmatter und Quellenliste mit demselben Unicode-Wortmuster ergab **2’318 Wörter im Artikel** und **1’501 Wörter im Selbstcheck**; vorher 2’192 und 1’076. Beide Volltexte liegen damit über 1’400 Wörtern. Die sichtbare Arbeitsmittelversion und Frontmatter `version` lauten identisch «Stand 15. November 2026»; beide Frontmatter-Standfelder exakt «15. November 2026».

Keine neuen internen Ziele wurden eingeführt. Erhalten wurden `/resources/04-backup-selbstcheck`, `/wissen/backup-wiederherstellung-testen`, `/unsere-dienstleistungen/notfallplanung`, `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/sicherheitsanalyse` und `/kontakt`. Artikel-/Ressourcen-Slugs sind lokal vorhanden; die Service-/Kontaktziele sind bereits Paketziele der Wartungs-/Importbasis, keine hier neu erzeugten Seiten. Wiederholte Nennung eines Serviceziels wird nicht als Existenz- oder Live-Nachweis ausgegeben. Öffentliche Erreichbarkeit, CMS-Synchronität und Publikationsstatus dieser Ziele wurden ausdrücklich nicht getestet.

Es wurden nur die beiden freigegebenen Inhaltsdateien und dieser Bericht bearbeitet. Keine anderen Artikel, Arbeitsmittel, Manifeste, globalen QA-Skripte oder Dokumente wurden geändert. Es wurde kein globaler Paketvalidator gestartet und kein fiktives CMS-Prüfergebnis ausgegeben.

## Konkrete offene Fachfragen und Blocker

**Fedlex-Teilblocker:** Die heutigen DSG-/DSV-Änderungsseiten sind nicht auslesbar. Vor einer behaupteten vollständigen artikelweisen Änderungskontrolle müssen die amtlichen Änderungstabellen tatsächlich gelesen werden. Die lesbaren aktuellen History/XML-Fassungen sind dokumentiert, beseitigen aber nicht diesen eigenständigen Teilblocker. [28] [29]

**Architektur und Object Lock:** Wer kann in der tatsächlichen Umgebung Kopien, Schutzregeln, Konto-/Mandantenressourcen oder Schlüssel verändern beziehungsweise vernichten? Welche Daten-/Administrationspfade sind getrennt, und funktioniert der Restore der letzten Rückfallebene? AWS, CISA und Microsoft erläutern Mechanismen, beantworten diese Fragen aber nicht für die Organisation. Keine Architektur-, Produkt- oder Tenantfreigabe. [5] [6] [32]

**Retention und Recht:** Wie lang muss ein sauberer Rückgriff möglich bleiben, und wie passt dies zu Löschung, Datenarten, Auftragsbearbeitung, Datenstandorten, Verträgen und weiteren Vorgaben? Keine Aufbewahrungsfrist festgelegt oder freigegeben. Art. 8 DSG und Art. 1–3 DSV stützen allgemeine Datensicherheit und Wiederherstellung, keine individuelle Rechtsbeurteilung. [7] [8] [24] [25]

**RPO/RTO:** Welche Zielwerte akzeptiert der Fachbereich, und erreicht die tatsächliche Kette einschliesslich Identitäten, Lizenzen, Netz, Schlüsseln, Konfigurationen und Abnahme diese Werte? Definitionsquellen und ein Selbstcheck messen dies nicht; dokumentierte Restore-Tests der tatsächlichen Umgebung fehlen hier. Keine RPO/RTO-Freigabe. [4] [5] [9] [10]

**Homeoffice, Vorfall und Forensik:** Welche Geschäftsgeräte, Heimnetzabhängigkeiten und Zugänge sind überhaupt relevant? Wer beurteilt Sicherungsstand und Zielumgebung, erhält Beweismittel und entscheidet über Untersuchung, Bereinigung und Wiederanlauf? Die neue BACS-Meldung ist begrenzter Kontext, weder Infektionsnachweis noch fertige Forensik. [3] [14] [17]

**BACS-Vorlageninhalt:** Die Notfallkonzeptseite zeigt neue DOCX-Dateidaten vom 11.11., deren Inhalt und Änderungsausmass wurden hier nicht gelesen. Eine organisationsspezifische Nutzung oder behauptete Vorlagenvollprüfung verlangt einen gesonderten Inhaltsabgleich; der Seitenbefund wird nicht zu einer Vollprüfung überhöht. [13]

**Historischer Wortlaut und Aktualitätsumfang:** Unversionierte BACS-/Herstellerseiten belegen den sichtbaren Abrufstand, nicht den exakten Text am 15.11.09:00 oder eine lückenlose Unverändertheit seit 01.11. CISA-Übersicht und gezielte Suche sind kein vollständiger Nichtfund aller neuen Advisories oder KEV-Revisionen. [18] [30]

**Veröffentlichung:** Offene Originalfachmarker und fehlende organisationsbezogene Freigaben bestehen fort. Kein CMS-/Live-Linktest durchgeführt, keine Veröffentlichung bestätigt oder vorgenommen. Erreichbarkeit und Inhalt von Quellen sowie allgemeine Orientierung sind keine tatsächliche Einzelfallprüfung.

## Referenzen

[1]: https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden "BACS – Erste Schritte"
[2]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz"
[3]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[4]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[5]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide"
[6]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html "AWS – S3 Object Lock"
[7]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – DSG, Stand 7. Juli 2025"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – DSV, Stand 1. Dezember 2025"
[9]: https://csrc.nist.gov/glossary/term/recovery_point_objective "NIST – Recovery Point Objective"
[10]: https://csrc.nist.gov/glossary/term/recovery_time_objective "NIST – Recovery Time Objective"
[11]: https://www.nist.gov/cyberframework/recover "NIST – Recover, nicht mehr aktualisierte Zuordnungsseite"
[12]: https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final "NIST NCCoE – MSP-Backup-Leitfaden, Final April 2020"
[13]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Notfallkonzept"
[14]: https://www.bacs.admin.ch/de/26w40-de "BACS – Malwareverdacht, 6. Oktober 2026"
[15]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a "CISA – SafePay, 20. Oktober 2026"
[16]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026, 22. Oktober 2026"
[17]: https://www.bacs.admin.ch/de/26w44-de "BACS – Heimnetzwerke, 3. November 2026"
[18]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[19]: https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de "BACS – Brown-Bag-Lunches zur Cyberresilienz, 2. November 2026"
[20]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen, 10. November 2026"
[21]: https://www.bacs.admin.ch/de/26w45-de "BACS – KI-Fakeshops und Paket-Phishing, 10. November 2026"
[22]: https://www.bacs.admin.ch/de/warnung-ehra-de "BACS – EHRA-Phishing, 6. November 2026"
[23]: https://www.bacs.admin.ch/de/warnung-estv-de "BACS – ESTV-Phishing, 9. November 2026"
[24]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – amtliche DSG-XML, Fassung 7. Juli 2025"
[25]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml "Fedlex – amtliche DSV-XML, Fassung 1. Dezember 2025"
[26]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG-Chronologie"
[27]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV-Chronologie"
[28]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex – DSG-Änderungen, heute nicht inhaltlich auslesbar"
[29]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes "Fedlex – DSV-Änderungen, heute nicht inhaltlich auslesbar"
[30]: https://www.cisa.gov/news-events/cybersecurity-advisories "CISA – Advisory-Übersicht"
[31]: https://www.cisa.gov/news-events/news/cisa-kicks-critical-infrastructure-security-and-resilience-month-2026 "CISA – Resilienzmonat 2026, 2. November 2026"
[32]: https://learn.microsoft.com/de-de/azure/backup/security-overview "Microsoft Learn – Azure Backup Sicherheit und Cyber-Wiederherstellung, Stand 6. November 2026"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/04-ransomware-resistente-backups.md:** `/resources/04-backup-selbstcheck` → `https://www.dkschv.ch/wissen/resources/04-backup-selbstcheck.html`: 2 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 2 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/notfallplanung` → `https://www.dkschv.ch/notfallplanung.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
