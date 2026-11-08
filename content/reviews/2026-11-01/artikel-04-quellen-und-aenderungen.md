# Quellen- und Änderungsprüfung – Artikel 04

**Prüfdatum:** 1. November 2026, ISO-Woche 44  
**Bewertetes Newsfenster:** 25. Oktober 2026, 09:00 CET bis 1. November 2026, 09:00 CET (Europe/Zurich)  
**Zusätzlicher Änderungsabgleich:** 18. Oktober 2026 nach 09:00 CET bis 1. November 2026 nach 09:00 CET, weil dies der letzte vollständige Quellenpflegestand von Artikel und Arbeitsmittel war.  
**Tatsächlicher Abruf der Webquellen:** 1. November 2026, ca. 09:05:11–09:07:16 CET (Europe/Zurich), also nach dem Ende des Newsfensters. Die jeweils genannten Uhrzeiten sind tatsächliche Rückgabezeiten der stateless Abrufe, keine behaupteten Abschlusszeiten einer historischen Webfassung.  
**Geprüfter Entwurf:** `blog-paket/articles/04-ransomware-resistente-backups.md`  
**Zugehöriges Arbeitsmittel:** `blog-paket/resources/04-backup-selbstcheck.md`  
**Titel / Slug:** *3-2-1-Backups für Schweizer KMU: So werden Sicherungen ransomware-resistent* / `/wissen/ransomware-resistente-backups`

## Ergebnis

Alle 16 unterschiedlichen, in Artikel und Arbeitsmittel zitierten externen Original-URLs waren beim tatsächlichen Abruf über den stateless Quellenzugang erreichbar und auf ihre jeweilige Aussage geprüft. Im Artikel existieren 17 Quellendefinitionen, weil der CISA-StopRansomware-Leitfaden für zwei unterschiedliche Aussagen als [5] und [6] geführt wird; das Arbeitsmittel führt acht Quellendefinitionen. Die formale lokale Kontrolle bestätigt in beiden Dateien: keine fehlende Definition, keine ungenutzte Definition und keine unkodierte Klammer in einer Quellen-URL.

Für die Aktualität wurden zusätzlich die BACS-Übersicht «Im Fokus» sowie die seit dem letzten Quellenstand einschlägigen Originalmeldungen geöffnet. Materiell für den Evergreen-Text waren zwei neue Quellen: Die CISA-Warnung zu SafePay vom 20. Oktober dokumentiert, dass die dort untersuchte Gruppe in einzelnen Fällen alle netzwerkangebundenen Unternehmensbackups löschte. Die BACS-Meldung zur Studie «KMU Cybersicherheit 2026» vom 22. Oktober berichtet, dass neun von zehn KMU Backups erstellen, aber nur jedes vierte die Wiederherstellung testet. Beide Aussagen wurden eng eingegrenzt, mit einer numerischen Inlinezitation versehen und ausdrücklich nicht zu Befunden über ein bestimmtes Schweizer KMU überhöht. [15] [16]

Die BACS-Meldung vom 21. Oktober zu kritischen PHP-Schwachstellen ist für Inventarisierung eingebetteter Komponenten sowie den Nachweis von Herstellerfixständen relevant. Sie verändert die hier dargestellte Backup- und Restore-Architektur jedoch nicht und rechtfertigt keinen künstlichen CVE-Einschub in den Evergreen-Artikel. Die BACS-Wochenmeldungen vom 20. und 27. Oktober behandeln Hotelbuchungs-Phishing beziehungsweise die Übernahme von WhatsApp-Konten. Sie enthalten keine neue Backup-, Ransomware- oder Wiederherstellungsleitlinie. [18] [19] [20]

Die amtlichen Rechtsquellen wurden zusätzlich über die durch Fedlex verlinkten XML-Fassungen und die Änderungsübersichten kontrolliert. Die DSG-Fassung steht auf 7. Juli 2025, die DSV-Fassung auf 1. Dezember 2025. Die geprüften Änderungen betreffen beim DSG nicht Art. 8 und bei der DSV nicht Art. 1 bis 3. Deshalb bleibt der bestehende allgemeine Hinweis auf eine risikogerechte Datensicherheit und die rasche Wiederherstellbarkeit gedeckt. Ein Feld `rechtsstand` wird nicht ergänzt, da die Quellenpflege keine Einzelfall-Rechtsbeurteilung oder Freigabe ist. [7] [8]

Die am 1. November zugänglichen unversionierten BACS- und Herstellerseiten belegen ihren beim Abruf sichtbaren Inhalt. Ohne öffentliches, seitenbezogenes Änderungsprotokoll belegen sie weder einen minutengenauen Wortlaut um 09:00 Uhr noch eine lückenlose historische Unverändertheit. Das gilt nicht für die amtlich ausgewiesenen Fedlex-Fassungen, deren Fassungsliste, XML-Zugang und Änderungen separat gelesen wurden.

## Geprüfte Originalquellen und Quellenstand

| Nr. | Originalquelle und URL | Tatsächlicher Abruf / Erreichbarkeit | Version oder datierter Quellenstand | Aussagegehalt für Artikel / Arbeitsmittel |
|---|---|---|---|---|
| 1 | BACS – Erste Schritte: https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden | 01.11.2026, 09:05:11 CET; erreichbar, kein Abruffehler. | Kein Publikations-, Aktualisierungs- oder Versionsdatum im abgerufenen Seitentext. | Deckt regelmässige Sicherungen auf externem Medium oder in sicherer Cloud und die Vorgabe, das Backup nicht dauerhaft mit dem Computer verbunden zu halten. |
| 2 | BACS – Grundschutz: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden | 01.11.2026, 09:05:11 CET; erreichbar, kein Abruffehler. | Kein Publikations-, Aktualisierungs- oder Versionsdatum im abgerufenen Seitentext. | Nennt Datensicherung als technische Massnahme sowie Governance, Kontinuitätsmanagement und geregelte Verantwortlichkeiten als organisatorische Massnahmen. |
| 3 | BACS – Ransomware: Was nun?: https://www.bacs.admin.ch/de/ransomware-was-nun | 01.11.2026, 09:05:12 CET; erreichbar, kein Abruffehler. | Kein Publikations-, Aktualisierungs- oder Versionsdatum im abgerufenen Seitentext. | Stützt Isolation infizierter Systeme, Log-Sicherung, frühzeitige forensische Entscheidung, fachkundige Sicherungen vor Reparaturversuchen oder Neustarts, Neuinstallation und Wiederherstellung aus Backups. |
| 4 | BACS – Zusammenarbeit mit IT-Dienstleistern: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern | 01.11.2026, 09:05:15 CET; erreichbar, kein Abruffehler. | Kein Publikations-, Aktualisierungs- oder Versionsdatum im abgerufenen Seitentext. | Bestätigt klare Zuständigkeiten, Nachfrage nach Backup-Konzept und letztem erfolgreichen Restore-Test sowie das 3-2-1-Prinzip mit externer, idealerweise Offline-Kopie. |
| 5 | CISA – StopRansomware Guide: https://www.cisa.gov/stopransomware/ransomware-guide | 01.11.2026, 09:05:19 CET; erreichbar, Abrufauszug aus umfangreicher Seite, kein Inhaltsfehler. | Im selektierten Abruf kein belastbares Seitenstanddatum. | Deckt getrennte Administrations- und Benutzerkonten, offline und verschlüsselt gehaltene Backups, Verfügbarkeits- und Integritätstests, Wiederherstellung nach kritischen Diensten sowie Schutz sauberer Systeme vor Reinfektion. Die Quelle erscheint im Artikel aus Aussagegründen zweimal als [5] und [6]. |
| 6 | Amazon Web Services – S3 Object Lock: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html | 01.11.2026, 09:05:22 CET; erreichbar, kein Abruffehler. | Kein Publikations- oder Versionsdatum im abgerufenen Seitentext. | Bestätigt WORM-Ansatz, versionsbezogene Aufbewahrung, Governance- und Compliance-Modus; im Governance-Modus erlaubt `s3:BypassGovernanceRetention` unter den dokumentierten Bedingungen eine Umgehung. Stützt keine Anbieter- oder Konfigurationsfreigabe. |
| 7 | Fedlex – DSG: https://www.fedlex.admin.ch/eli/cc/2022/491/de | 01.11.2026, 09:05:43 CET; erreichbar. HTML, Fassungsliste, Änderungen und amtliches XML waren zugänglich; kein Leerabruf. | In Kraft, Stand am 07.07.2025. Die Änderungsliste zeigt keine Änderung von Art. 8 seit dieser Fassung. | Art. 8 verlangt vom Verantwortlichen und Auftragsbearbeiter geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit. Dies ist keine organisationsbezogene Rechtsfreigabe. |
| 8 | Fedlex – DSV: https://www.fedlex.admin.ch/eli/cc/2022/568/de | 01.11.2026, 09:05:43 CET; erreichbar. HTML, Fassungsliste, Änderungen und amtliches XML waren zugänglich; kein Leerabruf. | In Kraft, Stand am 01.12.2025. Die Änderungsliste weist für die aktuelle Fassung Änderungen unter anderem bei Art. 4, nicht bei Art. 1 bis 3, aus. | Art. 1 bis 3 enthalten risikobasierte Massnahmen und Art. 3 Abs. 2 Bst. d verlangt, Verfügbarkeit und Zugang zu Personendaten nach physischem oder technischem Zwischenfall rasch wiederherstellen zu können. Dies ist keine organisationsbezogene Rechtsfreigabe. |
| 9 | NIST CSRC Glossary – RPO: https://csrc.nist.gov/glossary/term/recovery_point_objective | 01.11.2026, 09:05:41 CET; erreichbar, kein Abruffehler. | Kein Seitenstanddatum; das Glossar weist NIST SP 800-34 Rev. 1 als Quelle aus. | Definiert RPO als den Zeitpunkt, bis zu dem Daten nach einem Ausfall wiederhergestellt sein müssen. Die erläuternde RPO-Passage bleibt gedeckt. |
| 10 | NIST CSRC Glossary – RTO: https://csrc.nist.gov/glossary/term/recovery_time_objective | 01.11.2026, 09:05:41 CET; erreichbar, kein Abruffehler. | Kein Seitenstanddatum; das Glossar weist NIST SP 800-34 Rev. 1 als Quelle aus. | Definiert RTO als die gesamte Zeit, während der sich Komponenten in der Wiederherstellungsphase befinden können, bevor Geschäftsprozesse beeinträchtigt werden. Die erläuternde RTO-Passage bleibt gedeckt. |
| 11 | NIST Cybersecurity Framework – Recover: https://www.nist.gov/cyberframework/recover | 01.11.2026, 09:05:22 CET; erreichbar, kein Abruffehler. | Erstellt am 01.02.2018, aktualisiert am 27.05.2026; die Seite weist selbst darauf hin, dass sie nicht mehr aktualisiert wird. | Deckt die Aussage, dass Wiederherstellungsprozesse und -verfahren ausgeführt und gepflegt werden, um Systeme oder Assets nach Cybervorfällen zeitgerecht wiederherzustellen. Die Selbstkennzeichnung als nicht mehr aktualisiert bleibt für die Leserschaft im Quellenbefund relevant. |
| 12 | NIST NCCoE – Protecting Data from Ransomware and Other Data Loss Events: https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final | 01.11.2026, 09:05:46 CET; erreichbar, kein Abruffehler. | Final, veröffentlicht April 2020; Dokumenthistorie: 24.04.2020. | Die Publikation richtet sich an Managed Service Providers und deren Kunden und behandelt das Durchführen, Pflegen und Testen von Backups. Sie stützt den Anspruch an einen dokumentierten Testnachweis. |
| 13 | BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz: https://www.bacs.admin.ch/de/notfallkonzept | 01.11.2026, 09:05:15 CET; erreichbar, kein Abruffehler. | Kein Seitenstanddatum; die Seite weist das KMU-Template für IT-Notfall- und Krisenplan mit Datum 18.05.2026 aus. | Deckt Vorbereitung, Vorfalleintritt, Vorfallsbewältigung und Nachbearbeitung sowie die Bedeutung klar zugeteilter Verantwortlichkeiten. |
| 14 | BACS – Woche 40: Mythen zu Schadsoftware: https://www.bacs.admin.ch/de/26w40-de | 01.11.2026, 09:05:16 CET; erreichbar, kein Abruffehler. | Veröffentlicht am 06.10.2026. | Deckt die bereits vorhandene und weiterhin begrenzte Aussage: Ein Einzelindikator beweist keine Infektion, mehrere Auffälligkeiten sollen untersucht werden; bei Verdacht Fachperson und bei Geschäftsgeräten zuständige IT beiziehen. Keine forensische Einzelfalltriage. |
| 15 | CISA – #StopRansomware: SafePay Ransomware: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a | 01.11.2026, 09:05:52 CET; erreichbar, Abrufauszug aus umfangreicher Seite, kein Inhaltsfehler. | Release Date 20.10.2026, Initial version. | Neue, verwendete Originalquelle. Sie beschreibt für SafePay unter «Inhibit System Recovery», dass in einzelnen Fällen alle netzwerkangebundenen Backups von Unternehmensdaten gelöscht wurden. Sie empfiehlt unter anderem Offline-Backups, regelmässiges Testen und Pflegen von Backup-/Restore-Prozessen, Verschlüsselung und Unveränderbarkeit. Kein Befund über ein Schweizer KMU und keine Freigabe einer konkreten Architektur. |
| 16 | BACS – KMU Cybersicherheit 2026: https://www.bacs.admin.ch/de/26-kmustudie-de | 01.11.2026, 09:07:16 CET; erreichbar, kein Abruffehler. | Veröffentlicht am 22.10.2026. | Neue, verwendete Originalquelle. Die Meldung berichtet, neun von zehn KMU erstellten Backups, aber nur jedes vierte prüfe die Wiederherstellbarkeit. Die neue Artikelpassage nutzt die Zahl ausschliesslich als Schweizer Vergleichspunkt und nicht als Individualbefund. |

## Zusätzlich geprüfte Originalmeldungen und Aktualitätskontext

| Originalquelle und URL | Tatsächlicher Abruf / Erreichbarkeit | Version oder Datum | Befund und Bearbeitungsentscheidung |
|---|---|---|---|
| BACS – Im Fokus: https://www.bacs.admin.ch/de/im-fokus | 01.11.2026, 09:05:59 CET; erreichbar. Vollständiger Abruf liegt als Abrufartefakt vor, kein Inhaltsfehler. | Die Übersicht hat keinen eigenen ausgewiesenen Seitenstand. Sichtbar waren für den Zeitraum seit 18.10. Einträge am 20., 21., 22., 23. und 27.10.2026. | Diente der Quellensuche und der Vollständigkeitsbegrenzung. Die Übersicht selbst wird nicht im Artikel zitiert. Sie identifizierte die neuen BACS-Meldungen für die gezielte Primärprüfung. |
| BACS – Woche 42, Hotelbuchungs-Phishing: https://www.bacs.admin.ch/de/26w42-de | 01.11.2026, 09:05:47 CET; erreichbar, kein Abruffehler. | Veröffentlicht am 20.10.2026. | Inhalt zu Phishing in Verbindung mit Hotelbuchungen, TWINT- und E-Banking-Zugängen. Keine Aussage zu Backup, Ransomware, Aufbewahrung oder Wiederherstellung. Keine Änderung. |
| BACS – Kritische Schwachstellen in PHP: https://www.bacs.admin.ch/de/warnung-php-de | 01.11.2026, 09:07:15 CET; erreichbar, kein Abruffehler. | Veröffentlicht am 21.10.2026. | BACS nennt Fixstände für PHP 8.5.12, 8.4.27, 8.3.36 und 8.2.35 und verlangt die Prüfung eingebetteter Komponenten, Betreiber und nachweisbarer Fixstände. Sachlich relevant für Komponenteninventar und Wiederanlaufvorbereitung, aber keine neue Backup- oder Restore-Leitlinie. Kein CVE-Abschnitt und keine Quellenaufnahme in Artikel 04. |
| BACS – Woche 43, WhatsApp-Konten: https://www.bacs.admin.ch/de/26w43-de | 01.11.2026, 09:07:15 CET; erreichbar, kein Abruffehler. | Veröffentlicht am 27.10.2026. | Inhalt zu Social Engineering bei WhatsApp-Kontoübernahmen mittels SMS- oder QR-Code. Keine Backup-, Ransomware- oder Wiederherstellungsaussage. Keine Änderung. |

Weitere neue BACS-Einträge aus der Übersicht vom 19. und 23. Oktober betreffen Authentifizierungsorientierung beziehungsweise einen Cyber-Security-Month-Workshop und wurden nicht als Backup- oder Restore-Leitlinien verarbeitet. Das Newsfenster vom 25.10.09:00 bis 01.11.09:00 enthält über die BACS-Übersicht nur die Wochenmeldung vom 27.10.; sie ist für Artikel 04 nicht materiell. Die CISA-SafePay-Warnung und die BACS-KMU-Studie liegen vor dem Newsfenster, aber nach dem vollständigen Quellenstand vom 18.10. und wurden deshalb bei der zweiwöchentlichen Quellenpflege sorgfältig abgeglichen.

## Fedlex: amtliche Fassungen, XML und Änderungskontrolle

Die Fedlex-HTML-Seiten lieferten beim stateless Abruf Text und die Links zu Chronologie, Änderungen sowie allen Fassungen. Die amtlichen XML-Dateien waren ebenfalls zugänglich und enthielten den für die verwendeten Aussagen massgeblichen Wortlaut:

- **DSG, XML-Fassung 07.07.2025:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml. Abruf am 01.11.2026 um 09:06:23 CET, erreichbar. Art. 8 enthält weiterhin die risikogerechte Datensicherheit durch geeignete technische und organisatorische Massnahmen.
- **DSV, XML-Fassung 01.12.2025:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml. Abruf am 01.11.2026 um 09:06:24 CET, erreichbar. Art. 3 Abs. 2 Bst. d enthält weiterhin die rasche Wiederherstellbarkeit von Verfügbarkeit und Zugang nach physischem oder technischem Zwischenfall.
- **DSG, Änderungen:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes. Abruf am 01.11.2026 um 09:06:20 CET, erreichbar. Die aktuelle Änderungenübersicht listet Art. 24 sowie weitere, nicht Art. 8 betreffende Bestimmungen.
- **DSV, Änderungen:** https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes. Abruf am 01.11.2026 um 09:06:26 CET, erreichbar. Die aktuelle Änderungenübersicht listet unter anderem Art. 4, 8, 37a und 46; Art. 1 bis 3 sind nicht als aktuell geänderte Bestimmungen aufgeführt.

Der technische Zugriff auf HTML und XML war damit erfolgreich. Ein fehlender oder verkürzter Webabruf wurde ausdrücklich nicht als fehlende Rechtsfassung interpretiert. Dennoch wird weder ein Rechtsstandfeld ergänzt noch eine Rechtsfreigabe behauptet: Die Aussage bleibt abstrakt und eine Aufbewahrungs-, Lösch-, Datenbearbeitungs- oder Vertragsbeurteilung braucht den konkreten Sachverhalt.

## Änderungen gegenüber dem Stand vom 18. Oktober 2026

### Artikel

**Datei:** `blog-paket/articles/04-ransomware-resistente-backups.md`

| Betroffener Teil | Vorher | Nachher / belegter Grund |
|---|---|---|
| Frontmatter `stand` | `18. Oktober 2026` | `1. November 2026`. Die sichtbare Standangabe bezeichnet ausschliesslich die Quellenpflege. |
| Frontmatter `quellenpruefung_umfang` | «Alle 14 bestehenden Quellenreferenzen sowie die neue BACS-Meldung vom 6. Oktober 2026; BACS «Im Fokus» und die BACS-Meldung vom 5. Oktober 2026 als Aktualitätskontext geprüft. Interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft.» | Auf den tatsächlich geprüften Umfang präzisiert: 17 Artikel- und acht Arbeitsmitteldefinitionen entsprechen 16 unterschiedlichen zitierten Original-URLs; BACS «Im Fokus» sowie die BACS-Meldungen vom 20., 21. und 27.10. als Aktualitätskontext. Interne relative Links bleiben ausdrücklich ungeprüfte Planungswerte. |
| Frontmatter `quellenpruefung_status` | «Vollständig für die zitierten externen Quellen am 18. Oktober 2026 nach 09:00 Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation.» | «Vollständig für die 16 unterschiedlichen zitierten externen Original-URLs am 1. November 2026, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation.» |
| Abschnitt «Ein vorhandenes Backup kann im Ernstfall trotzdem ausfallen», nach dem Absatz zur BACS-Basisempfehlung | Kein Bezug auf die seit 18.10. veröffentlichte CISA-SafePay-Warnung. | Ergänzt: CISA dokumentiert für SafePay das Löschen aller netzwerkangebundenen Unternehmensbackups in einzelnen Fällen. Explizite Begrenzung: kein Befund über ein Schweizer KMU. Daraus wird nur die bestehende Architekturfrage nach Trennung des Daten- und Administrationspfads sowie Test der letzten Rückfallebene abgeleitet. [15] |
| Abschnitt «Wiederherstellungsfähigkeit beweisen, nicht vermuten», nach dem ersten Testabsatz | Kein aktueller Schweizer Vergleichspunkt zur Differenz zwischen Backups und getesteter Wiederherstellung. | Ergänzt: Die BACS-Meldung zur Studie «KMU Cybersicherheit 2026» mit neun von zehn KMU mit Backups und nur jedem vierten mit Wiederherstellungstest; ausdrücklich kein Individualbefund. [16] |
| Quellen | Quellen [1]–[15]. | Zwei verwendete, numerisch zitierte Primärquellen ergänzt: [16] CISA SafePay und [17] BACS «KMU Cybersicherheit 2026». |

Der Artikel umfasst nach der Änderung 2’408 Wörter und damit weiterhin deutlich mehr als 1’400 Wörter. Unverändert erhalten wurden `status: "Entwurf – nicht freigegeben"`, der Slug, das ursprüngliche Veröffentlichungsdatum `22.10.2026`, `fachprüfung_status` und der bestehende sichtbare `[FACHPRÜFUNG ERFORDERLICH]`-Marker. `meta_title` und `meta_description` wurden nicht verändert; die punktuellen, quellengestützten Ergänzungen machen keine konkrete Metadatenkorrektur erforderlich. Auch `rechtsstand` und `fachlich_geprueft_am` wurden nicht erstellt.

### Arbeitsmittel

**Datei:** `blog-paket/resources/04-backup-selbstcheck.md`

| Betroffener Teil | Vorher | Nachher / belegter Grund |
|---|---|---|
| Frontmatter `version` | `Stand 18. Oktober 2026` | `Stand 1. November 2026`; konsistent zum sichtbaren Quellenstand des Artikels. |
| Frontmatter `quellenpruefung_umfang` | «Alle sieben bestehenden Quellenreferenzen sowie die ergänzte BACS-Meldung vom 6. Oktober 2026; interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft.» | Präzisiert auf alle acht zitierten externen Original-URLs des Arbeitsmittels, die auf Erreichbarkeit und Aussagegehalt geprüft wurden; interne relative Links bleiben ungeprüfte Planungswerte. |
| Frontmatter `quellenpruefung_status` | «Vollständig für die zitierten externen Quellen am 18. Oktober 2026 nach 09:00 Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation.» | Aktualisiert auf die vollständige Prüfung der acht zitierten URLs am 1. November, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich, mit unveränderter Freigabe- und Historiengrenze. |

Inhaltliche Kontrollpunkte und Quellenliste des Arbeitsmittels blieben bewusst unverändert. Die neue SafePay-Warnung bestätigt die bereits vorhandenen Punkte zu Offline-/unveränderbaren Kopien und Wiederherstellungstests, macht aber keine neue generische Produkt-, Object-Lock-, Rechte- oder Aufbewahrungsvorgabe. Die BACS-Studie ist ein allgemeiner Vergleichswert und erweitert keinen Kontrollpunkt. Dadurch wird keine punktuelle Wochennews in eine dauerhafte Arbeitsvorlage eingetragen.

Unverändert erhalten wurden `status: "Arbeitsvorlage – nicht freigegeben"`, Slug, Bezug, Metadaten, `fachprüfung_status` und der bestehende sichtbare `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Die Arbeitsmittelversion lautet nach der Pflege konsistent **Stand 1. November 2026**. Kein `rechtsstand` und kein `fachlich_geprueft_am` wurden angelegt.

## Referenz- und Linkprüfung

- Der Artikel zitiert und definiert [1] bis [17]. Die zwei CISA-Definitionen [5] und [6] verweisen bewusst auf dieselbe Original-URL mit unterschiedlichen, im Text verwendeten Aussagebezeichnungen. Damit sind es 16 unterschiedliche externe Original-URLs.
- Das Arbeitsmittel zitiert und definiert [1] bis [8]; alle acht sind im geprüften Bestand des Artikels enthalten.
- Die zwei neuen Artikelquellen [16] und [17] sind jeweils im Text verwendet und in der Quellenliste definiert. Es gibt keine undefinierte oder ungenutzte Quellenreferenz.
- Die URLs in den Quellenlisten enthalten keine Klammern; eine URL-Klammer-Kodierung war daher nicht nötig.
- Die bestehenden internen relativen Slugs, darunter `/resources/04-backup-selbstcheck`, `/wissen/backup-wiederherstellung-testen`, `/unsere-dienstleistungen/notfallplanung`, `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/sicherheitsanalyse` und `/kontakt`, wurden unverändert erhalten. Sie wurden gemäss Auftrag nicht als künftige öffentliche URLs geprüft. Der Laufstatus vom 25.10. meldet hierfür weiterhin nicht aufgelöste öffentliche Ziele; daraus wird weder Erreichbarkeit noch eine Livekorrektur abgeleitet.

## Verbleibende genaue Blocker und Grenzen

1. **Entwurfs- und Fachstatus:** Artikel und Arbeitsmittel bleiben nicht freigegeben. Alle bestehenden Fachprüfungsmarker bleiben unverändert offen. Die Quellenprüfung ist keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Publikationsfreigabe.
2. **Konkrete Backup-, Object-Lock- und Schlüsselarchitektur:** Für die einzelne Organisation sind Schutzmodus, Rechte zur Änderung oder Umgehung, Schlüssel- und Identitätsverwaltung, Protokollierung, Mandantentrennung, Backup-Repository und Wiederherstellungsumgebung zu prüfen. Die AWS- und CISA-Quellen genehmigen keine konkrete Konfiguration und keinen Anbieter.
3. **Aufbewahrung, Löschung, Personendaten und Verträge:** Die erforderliche Frist sowie die Vereinbarkeit mit Löschkonzepten, Datenschutz, Auftragsbearbeitung, Datenstandorten und Leistungsvereinbarungen lassen sich nicht aus dem allgemeinen Artikel ableiten. DSG und DSV wurden amtlich geprüft, ersetzen aber keine fachjuristische Einzelfallprüfung.
4. **Vorfall und Forensik:** Bei einem konkreten Malware- oder Ransomwareverdacht sind betroffene Systeme, Konten, Beweismittel, Meldefragen, Befugnisse und zulässige Massnahmen organisations- und fallbezogen zu klären. Die vorhandene BACS-Woche-40-Passage bleibt ausdrücklich keine Triageanweisung.
5. **Praktische Wiederherstellungsfähigkeit:** Keine Quelle beweist, dass ein bestimmter Dienst inklusive Identitäten, Lizenzen, Schlüsseln, Konfigurationen, Abhängigkeiten und fachlicher Abnahme aus einem sauberen Stand innerhalb des gewählten RPO/RTO wiederhergestellt werden kann. Erforderlich ist ein dokumentierter, kontrollierter Restore-Test.
6. **Historischer Webwortlaut:** Unversionierte BACS-, AWS- und CISA-Webseiten haben für die verwendeten Inhalte keinen durchgehend ausgewiesenen Seitenstand oder eine lückenlose seitenbezogene Historie. Der Abruf belegt den am 1. November sichtbaren Stand, nicht den exakten Wortlaut zu einem historischen Stichtag.
7. **Öffentliche interne Verweise und Go-live:** Die relativen Slugs blieben aus Planungsgründen erhalten. Ihre öffentliche Erreichbarkeit ist vor einer Veröffentlichung erneut zu prüfen. Der bekannte CMS-/Linkstatus und die offenen Fachmarker sind weiterhin eigenständige Veröffentlichungsblocker.

## CMS- und Veröffentlichungsstatus

**Keine CMS-Änderung und keine Veröffentlichung vorgenommen.**

Es wurden ausschliesslich die zwei zugewiesenen lokalen Dateien und dieser zugewiesene Prüfbericht bearbeitet. Weder Manifest noch globale QA-Skripte, CMS-Importdateien, externe Systeme oder bereits öffentliche Inhalte wurden geändert.

## Referenzen

[1]: https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden "BACS – Erste Schritte für Unternehmen und Behörden"
[2]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz für Unternehmen und Behörden"
[3]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[4]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[5]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide"
[6]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html "Amazon S3 – Object Lock"
[7]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz DSG"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung DSV"
[9]: https://csrc.nist.gov/glossary/term/recovery_point_objective "NIST CSRC Glossary – Recovery Point Objective"
[10]: https://csrc.nist.gov/glossary/term/recovery_time_objective "NIST CSRC Glossary – Recovery Time Objective"
[11]: https://www.nist.gov/cyberframework/recover "NIST Cybersecurity Framework – Recover"
[12]: https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final "NIST NCCoE – Protecting Data from Ransomware and Other Data Loss Events"
[13]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[14]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware"
[15]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a "CISA – StopRansomware: SafePay Ransomware"
[16]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026"
[17]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[18]: https://www.bacs.admin.ch/de/26w42-de "BACS – Woche 42: Hotelbuchungs-Phishing"
[19]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP"
[20]: https://www.bacs.admin.ch/de/26w43-de "BACS – Woche 43: WhatsApp-Konten"
