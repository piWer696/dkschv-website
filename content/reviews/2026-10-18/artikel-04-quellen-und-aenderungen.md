# Quellen- und Änderungsprüfung – Artikel 04

**Prüfdatum:** 18. Oktober 2026, ISO-Woche 42  
**Bewerteter Zeitraum:** Änderungen seit 4. Oktober 2026 bis 18. Oktober 2026, 09:00 Uhr (Europe/Zurich)  
**Tatsächlicher Abruf der Webquellen:** 18. Oktober 2026, ca. 09:04–09:05 Uhr (Europe/Zurich), somit nach 09:00 Uhr  
**Geprüfter Entwurf:** `blog-paket/articles/04-ransomware-resistente-backups.md`  
**Zugehöriges Arbeitsmittel:** `blog-paket/resources/04-backup-selbstcheck.md`  
**Titel / Slug:** *3-2-1-Backups für Schweizer KMU: So werden Sicherungen ransomware-resistent* / `/wissen/ransomware-resistente-backups`

## Ergebnis

Alle **14 eindeutigen externen Quellen-URLs**, die in Artikel und Arbeitsmittel zitiert sind, waren beim Abruf erreichbar und inhaltlich geprüft. Die doppelte CISA-Referenz im Artikel wurde einmal als Original-URL geprüft und deckt beide Verwendungsstellen ab. Zusätzlich wurden die BACS-Übersicht «Im Fokus» und die verpflichtend einbezogene, für dieses Thema nicht materielle BACS-Meldung «Oversharing» geöffnet.

Seit dem vorherigen Quellenstand vom 4. Oktober wurde als einschlägige BACS-Neuigkeit nur der Wochenrückblick **«Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion»**, veröffentlicht am 6. Oktober 2026, festgestellt. Er präzisiert die Grenze zwischen Symptomen und bestätigter Infektion sowie die Empfehlung, bei Verdacht Fachperson und bei Geschäftsgeräten die zuständige IT einzubeziehen. Artikel und Arbeitsmittel wurden dazu eng begrenzt ergänzt. Die manifestierten BACS-Kernaussagen zu nicht dauerhaft verbundenen Backups, 3-2-1, Verantwortlichkeiten, Wiederherstellungstests und dem Vorgehen bei Ransomware sind in den aktuell abgerufenen Originalfassungen weiterhin enthalten.

`all_references_verified=true`: Alle in beiden Dateien tatsächlich zitierten externen Quellen wurden auf Erreichbarkeit und für die verwendete Aussage geprüft. Das ist keine lückenlose historische Veränderungsprüfung: Mehrere BACS-Seiten haben weder einen ausgewiesenen Seitenstand noch ein öffentliches, seitenbezogenes Änderungsprotokoll. Interne relative Paketlinks wurden bewusst erhalten, aber nicht als künftige Live-URLs geprüft.

## Geprüfte Originalquellen und Quellenstand

| Originalquelle | URL | Datierten Quellenstand soweit belegt | Abruf / Erreichbarkeit | Befund für Artikel und Arbeitsmittel |
|---|---|---|---|---|
| BACS – Erste Schritte | https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden | Kein Publikations- oder Aktualisierungsdatum im abgerufenen Seitentext. | 18.10.2026, ca. 09:04, erreichbar. | Sichert die Aussage, dass Backups regelmässig auf externem Medium oder in sicherer Cloud erfolgen und nicht dauerhaft mit dem Computer verbunden bleiben sollen. |
| BACS – Grundschutz | https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden | Kein Publikations- oder Aktualisierungsdatum im abgerufenen Seitentext. | 18.10.2026, ca. 09:04, erreichbar. | Nennt Datensicherung als technische Massnahme sowie Governance, Kontinuitätsmanagement und geregelte Verantwortlichkeiten als organisatorische Massnahmen. |
| BACS – Ransomware: Was nun? | https://www.bacs.admin.ch/de/ransomware-was-nun | Kein Publikations- oder Aktualisierungsdatum im abgerufenen Seitentext. | 18.10.2026, ca. 09:04, erreichbar. | Stützt Isolation infizierter Systeme, Sicherung von Logs, frühzeitige forensische Entscheidung, fachkundige Sicherungen vor Reparaturversuchen oder Neustarts, Neuinstallation und Wiederherstellung aus Backups. |
| BACS – Zusammenarbeit mit IT-Dienstleistern | https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern | Kein Publikations- oder Aktualisierungsdatum im abgerufenen Seitentext. | 18.10.2026, ca. 09:04, erreichbar. | Bestätigt klare Zuständigkeiten, Nachfrage nach Backup-Konzept und letztem erfolgreichen Restore-Test sowie 3-2-1 mit drei Kopien, zwei Medien und einer externen, idealerweise Offline-Kopie. |
| CISA – #StopRansomware Guide | https://www.cisa.gov/stopransomware/ransomware-guide | Kein belastbares Seitenstanddatum im abgerufenen Auszug. | 18.10.2026, ca. 09:04, erreichbar. | Bestätigt Offline- und verschlüsselte Backups, regelmässige Verfügbarkeits- und Integritätstests, getrennte Administrations- und Benutzerkonten, Wiederherstellung nach Priorität kritischer Dienste und Vermeidung einer Reinfektion sauberer Systeme. |
| AWS – S3 Object Lock | https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html | Kein Publikations- oder Versionsdatum im abgerufenen Seitentext. | 18.10.2026, ca. 09:04, erreichbar. | Bestätigt versionsbezogenen Schutz, Aufbewahrungszeiträume sowie Compliance- und Governance-Modus; im Governance-Modus kann `s3:BypassGovernanceRetention` unter den dokumentierten Voraussetzungen den Schutz umgehen. |
| Fedlex – DSG | https://www.fedlex.admin.ch/eli/cc/2022/491/de | Text in Kraft; aktuelle sichtbare Fassung **07.07.2025**. | 18.10.2026, ca. 09:05, erreichbar; amtliche HTML-Ausgabe und Fassungsliste lesbar. | Art. 8 verlangt vom Verantwortlichen und Auftragsbearbeiter geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit. Kein Rechtsstand oder Fachfreigabe geändert. |
| Fedlex – DSV | https://www.fedlex.admin.ch/eli/cc/2022/568/de | Text in Kraft; Stand der sichtbaren Fassung **01.12.2025**. | 18.10.2026, ca. 09:05, erreichbar; amtliche HTML-Ausgabe und Fassungsliste lesbar. | Art. 1–3 enthalten risikobasierte Massnahmen und verlangen in Art. 3 Abs. 2 Bst. d die rasche Wiederherstellbarkeit von Verfügbarkeit und Zugang bei physischem oder technischem Zwischenfall. Kein Rechtsstand oder Fachfreigabe geändert. |
| NIST CSRC – Recovery Point Objective | https://csrc.nist.gov/glossary/term/recovery_point_objective | Kein Seitenstanddatum; Glossar nennt NIST SP 800-34 Rev. 1 als Quelle. | 18.10.2026, ca. 09:05, erreichbar. | Definiert RPO als den Zeitpunkt, bis zu dem Daten nach einem Ausfall wiederhergestellt werden müssen; die Erläuterung im Artikel und Selbstcheck bleibt gedeckt. |
| NIST CSRC – Recovery Time Objective | https://csrc.nist.gov/glossary/term/recovery_time_objective | Kein Seitenstanddatum; Glossar nennt NIST SP 800-34 Rev. 1 als Quelle. | 18.10.2026, ca. 09:05, erreichbar. | Definiert RTO als die gesamte Zeit, während der sich Komponenten in der Wiederherstellungsphase befinden können, bevor Geschäftsprozesse negativ betroffen sind; die Erläuterung bleibt gedeckt. |
| NIST – Recover | https://www.nist.gov/cyberframework/recover | Seite mit Hinweis «no longer being updated»; **Updated May 27, 2026**. | 18.10.2026, ca. 09:05, erreichbar. | Beschreibt Recovery Planning als ausgeführte und gepflegte Prozesse für die zeitgerechte Wiederherstellung betroffener Systeme oder Assets. Die Quelle bleibt für den verwendeten allgemeinen Satz tragfähig, ist aber laut NIST selbst nicht fortlaufend aktualisiert. |
| NIST NCCoE – Protecting Data from Ransomware and Other Data Loss Events | https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final | Final, **April 2020**; Dokumenthistorie: **24.04.2020**. | 18.10.2026, ca. 09:05, erreichbar. | Die Publikation behandelt das Durchführen, Pflegen und Testen von Backups für Managed Service Providers und deren Kunden. Sie deckt die Aussage zum dokumentierten Testnachweis. |
| BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz | https://www.bacs.admin.ch/de/notfallkonzept | Kein Seitenstanddatum. Die Seite weist unter anderem ein KMU-Template vom **18.05.2026** aus. | 18.10.2026, ca. 09:04, erreichbar. | Bestätigt die Phasen Vorbereitung, Vorfall, Vorfallsbewältigung und Nachbearbeitung sowie die Rolle klarer Verantwortlichkeiten und eines Notfall-/Krisenplans. |
| BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion | https://www.bacs.admin.ch/de/26w40-de | **Veröffentlicht am 06.10.2026.** | 18.10.2026, ca. 09:04, erreichbar. | Neue einschlägige Meldung seit 04.10.: Ein Einzelindikator beweise keine Infektion; mehrere ungewöhnliche Beobachtungen sollen untersucht werden. Bei Verdacht empfiehlt das BACS eine Fachperson; bei Geschäftsgeräten die Information der zuständigen IT. Als neue Primärquelle [15] beziehungsweise [8] verwendet. |
| BACS – Im Fokus | https://www.bacs.admin.ch/de/im-fokus | Relevante Listeinträge nach 04.10.: Woche 40 vom 06.10. und Woche 41 vom 13.10.; Stand der Übersichtsseite im Abruf nicht separat versioniert. | 18.10.2026, ca. 09:04, erreichbar. | Auf neuere einschlägige BACS-Meldungen geprüft. Woche 40 war die einzige für Backup-/Ransomware-Wiederherstellung inhaltlich relevante Neuigkeit. Woche 41 betrifft Online-Shop-Betrug, die weiteren neuen Einträge keine Backup-Leitlinie. |
| BACS – Cyber Security Month 2026: Oversharing | https://www.bacs.admin.ch/de/csm26-s2-de | **Veröffentlicht am 05.10.2026.** | 18.10.2026, ca. 09:04, erreichbar. | Pflichtgemäss einbezogen. Die Meldung warnt unter anderem vor einem in ein KI-Tool eingegebenen internen Dokument; sie betrifft Oversharing und ist keine neue Backup-, Ransomware-, Aufbewahrungs- oder Wiederherstellungsanforderung. Für Artikel 04 nicht zitiert und keine Änderung ausgelöst. |

> **Unklarheit zur Veränderungshistorie:** Bei den unversionierten BACS-Informationsseiten belegt der Abruf die am 18. Oktober zugängliche Fassung. Mangels offenem, seitenbezogenem Änderungsprotokoll belegt er keine bytegleiche Unverändertheit seit dem 4. Oktober. Für Fedlex wurde die amtliche Fassungsliste und der aktuelle Gesetzestext gelesen; es wurde keine nicht belegbare Fassung oder Freigabe behauptet.

## Änderungen seit dem Quellenstand vom 4. Oktober 2026

### Artikel

**Datei:** `blog-paket/articles/04-ransomware-resistente-backups.md`

| Betroffener Teil | Vorher | Nachher / Grund |
|---|---|---|
| Frontmatter `stand` | `4. Oktober 2026` | `18. Oktober 2026`; dies bezeichnet ausschliesslich diese Quellenprüfung. |
| Frontmatter `quellenpruefung_umfang` | Feld fehlte. | Ergänzt: Umfang der 14 bisherigen Referenzen, der neuen BACS-Meldung und des BACS-Aktualitätskontexts; interne relative Links nicht als künftige Live-URLs geprüft. |
| Frontmatter `quellenpruefung_status` | Feld fehlte. | Ergänzt: Vollständige Prüfung der zitierten externen Quellen am 18. Oktober nach 09:00; keine Freigabe und keine lückenlose historische Änderungsverifikation. |
| Abschnitt «Ein vorhandenes Backup kann im Ernstfall trotzdem ausfallen», nach dem Absatz zur BACS-Ransomware-Anleitung | Kein Hinweis auf die aktuelle BACS-Meldung vom 06.10.2026. | Eng begrenzter Absatz ergänzt: Einzelanzeichen beweisen keine Infektion, mehrere Auffälligkeiten erfordern Untersuchung; bei Verdacht Fachperson und bei Geschäftsgeräten zuständige IT. Explizite Grenze: keine forensische oder organisationsspezifische Triage. |
| Quellen | Quellen [1]–[14]. | Neue, verwendete Primärquelle [15] zur BACS-Meldung vom 06.10.2026 ergänzt. |

Die Langfassung wurde nicht pauschal umgeschrieben und bleibt deutlich über 1’400 Wörtern. Original-H1, Kurzantwort, Struktur, Slug, Veröffentlichungsdatum **22.10.2026**, Status **«Entwurf – nicht freigegeben»**, alle bestehenden `[FACHPRÜFUNG ERFORDERLICH]`-Marker, interne relative Links und Schweizer Schreibweise wurden erhalten. `meta_title` und `meta_description` sind **unverändert**, weil die eng begrenzte Ergänzung keine Metadatenänderung erfordert. `rechtsstand` und `fachlich_geprueft_am` wurden nicht ergänzt oder geändert.

### Arbeitsmittel

**Datei:** `blog-paket/resources/04-backup-selbstcheck.md`

| Betroffener Teil | Vorher | Nachher / Grund |
|---|---|---|
| Frontmatter `version` | `Stand 4. Oktober 2026` | `Stand 18. Oktober 2026`; konsistent zum Artikelstand. |
| Frontmatter `quellenpruefung_umfang` | Feld fehlte. | Ergänzt: sieben bisherige Referenzen plus die ergänzte BACS-Meldung; interne relative Links nicht als künftige Live-URLs geprüft. |
| Frontmatter `quellenpruefung_status` | Feld fehlte. | Ergänzt: Vollständige Prüfung der zitierten externen Quellen am 18. Oktober nach 09:00; keine Freigabe und keine lückenlose historische Änderungsverifikation. |
| Abschnitt «Zweck», nach dem Satz zu BACS/CISA | Kein Hinweis für einen aktuellen Malwareverdacht. | Ergänzt: Der Selbstcheck ist keine Vorfallsanweisung; bei aktuellem Verdacht verweist er auf BACS-Empfehlung zu Fachperson und zuständiger IT. |
| Quellen | Quellen [1]–[7]. | Neue, verwendete Primärquelle [8] zur BACS-Meldung vom 06.10.2026 ergänzt. |

Status **«Arbeitsvorlage – nicht freigegeben»**, Slug, Bezug, Struktur, alle bestehenden `[FACHPRÜFUNG ERFORDERLICH]`-Marker und der interne Bezug zum Artikel blieben unverändert. `meta_title` und `meta_description` sind **unverändert**, weil die Ergänzung keine Metadatenänderung erfordert. Kein `rechtsstand` oder `fachlich_geprueft_am` wurde ergänzt oder geändert.

## Referenz- und Linkprüfung

- Artikel: Quellen [1]–[15] sind im Text verwendet; keine undefinierte oder ungenutzte Quellenreferenz.
- Arbeitsmittel: Quellen [1]–[8] sind im Text verwendet; keine undefinierte oder ungenutzte Quellenreferenz.
- Alle Quellen des Arbeitsmittels sind auch im geprüften Quellenbestand des Artikels enthalten; die doppelte Verwendung derselben CISA-URL im Artikel wurde inhaltlich einmal geprüft.
- Die bestehenden relativen Paketlinks wurden nicht verändert. Sie wurden nicht als zukünftige öffentliche URLs geprüft und es wird keine Live-Erreichbarkeit behauptet.
- Es wurden weder CMS noch Manifest, QA-Skripte oder andere Paketdateien verändert.

## Offene Fachfragen und Publikationsblocker

1. **Entwurfsstatus:** Der Artikel bleibt **«Entwurf – nicht freigegeben»**, das Arbeitsmittel **«Arbeitsvorlage – nicht freigegeben»**. Die Quellenprüfung ist keine Publikations-, Rechts-, Forensik-, Tenant-, NIS2- oder DORA-Freigabe.
2. **Bestehende Fachprüfungsmarker:** Alle vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker bleiben offen. Vor Verwendung sind insbesondere konkrete Aufbewahrungs- und Löschfristen, DSG-/DSV-Konformität, Rollen und Berechtigungen, Auftragsbearbeitung, Vertragsregelungen sowie die gewählte Backup-, Object-Lock- und Schlüsselarchitektur für die einzelne Organisation fachlich und bei Rechtsfragen fachjuristisch zu prüfen.
3. **Konkreter Verdachts- oder Ransomwarefall:** Die BACS-Meldung vom 06.10.2026 liefert keine organisationsspezifische forensische Triage. Offene Frage: *Welche Systeme, Konten, Beweise, Meldepflichten, Fachpersonen und Wiederherstellungspunkte sind im konkreten Vorfall betroffen und wer darf welche Massnahme freigeben?* Das kann erst nach organisationsspezifischer Incident- und Rechtsbeurteilung beantwortet werden.
4. **Wiederherstellungsfähigkeit:** Keine Quelle beweist, dass eine konkrete Organisation RPO/RTO erreicht oder eine bestimmte Backup-Konfiguration sicher ist. Offene Frage: *Ist der priorisierte Dienst einschliesslich Identitäten, Lizenzen, Schlüsseln, Konfigurationen, Abhängigkeiten und fachlicher Abnahme tatsächlich innerhalb der gewählten Ziele aus einem sauberen Sicherungsstand wiederherstellbar?* Dies erfordert einen dokumentierten, kontrollierten Restore-Test.
5. **Rechtsquellen:** Die amtlichen Fedlex-Texte wurden aktuell verifiziert, aber dies ist keine organisationsspezifische Rechtsberatung oder juristische Freigabe. Ein `rechtsstand` wurde daher nicht gesetzt.
6. **Erneute Prüfung vor Go-live:** Unversionierte BACS-Seiten und öffentliche Zielseiten sind vor einer allfälligen Veröffentlichung erneut abzurufen. Der heutige Abruf belegt keine zukünftige Erreichbarkeit.

## CMS- und Veröffentlichungsstatus

**Keine CMS-Änderung und keine Veröffentlichung vorgenommen.**
