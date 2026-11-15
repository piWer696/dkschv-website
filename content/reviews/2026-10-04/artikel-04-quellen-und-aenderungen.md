# Quellen- und Änderungsprüfung – Artikel 04

**Prüfdatum:** 4. Oktober 2026  
**Bewerteter Zeitraum:** 20. September 2026 bis einschliesslich 4. Oktober 2026, 09:00 Uhr (Europe/Zurich)  
**Tatsächlicher Abruf der Webquellen:** 4. Oktober 2026, ca. 09:06–09:08 Uhr (Europe/Zurich)  
**Geprüfter Entwurf:** `blog-paket/articles/04-ransomware-resistente-backups.md`  
**Zugehöriges Arbeitsmittel:** `blog-paket/resources/04-backup-selbstcheck.md`  
**Titel / Slug:** *3-2-1-Backups für Schweizer KMU: So werden Sicherungen ransomware-resistent* / `/wissen/ransomware-resistente-backups`  
**Umfang:** Ausschliesslich Artikel 04 und das zugehörige Arbeitsmittel. Das Wartungsmanifest, das CMS, andere Artikel und Freigabestati wurden nicht geändert.

## Ergebnis in Kürze

**Keine belegte materielle Änderung** der im Wartungsmanifest für Artikel 04 genannten BACS-Leitlinien wurde im bewerteten Zeitraum festgestellt. Die aktuell zugänglichen Originalseiten stützen die bestehenden Kernaussagen zu getrennten beziehungsweise nicht dauerhaft verbundenen Backups, 3-2-1, Wiederherstellungstests, Verantwortlichkeiten sowie zum Vorgehen nach einem Ransomware-Vorfall.

Daher wurden **keine inhaltlichen Aussagen, Quellenverweise, Struktur, Slug, Veröffentlichungsdatum, Status oder `[FACHPRÜFUNG ERFORDERLICH]`-Marker** verändert. Nach erfolgter Prüfung wurden nur die Metadatenstände aktualisiert:

- Artikel: `stand: "4. Oktober 2026"`
- Arbeitsmittel: `version: "Stand 4. Oktober 2026"`

Die Quellen konnten erst rund sechs bis acht Minuten **nach** dem verlangten Stichtag technisch abgerufen werden. Der Abruf belegt die zu diesem Zeitpunkt zugängliche Fassung, nicht lückenlos den Zustand exakt um 09:00 Uhr oder eine unveränderte Historie seit dem 20. September 2026.

## Geprüfte Primärquellen aus dem Wartungsmanifest

| Nr. | Originalquelle | Abruf / Quellenstand | Geprüfter Befund und Bezug zum Entwurf |
|---:|---|---|---|
| 1 | BACS, [Erste Schritte](https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden) | Abruf erfolgreich; HTTP 200; Serverdatum 4. Oktober 2026, 09:06 Uhr Europe/Zurich. Im abgerufenen Seitentext kein Redaktions- oder Versionsdatum. | Empfiehlt regelmässige Backups auf externem Medium oder in sicherer Cloud und hält fest, dass das Backup nicht dauerhaft mit dem Computer verbunden bleiben soll. Dies stützt Artikel Abs. 21 und die Trennungsfragen im Arbeitsmittel. Keine neue, im Zeitraum datierte Änderung ersichtlich. |
| 2 | BACS, [Grundschutz: Schützen Sie Ihr Unternehmen und Ihre Behörde](https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden) | Abruf erfolgreich; HTTP 200; Serverdatum 4. Oktober 2026, 09:06 Uhr Europe/Zurich. Im abgerufenen Seitentext kein Redaktions- oder Versionsdatum. | Ordnet Datensicherung als technische Massnahme ein und nennt Governance, Kontinuitätsmanagement sowie klare Verantwortlichkeiten als organisatorische Massnahmen. Dies stützt Artikel Abs. 23 sowie die Rollen- und Verantwortlichkeitsfragen. Keine neue, im Zeitraum datierte Änderung ersichtlich. |
| 3 | BACS, [Ransomware – Was nun?](https://www.bacs.admin.ch/de/ransomware-was-nun) | Abruf erfolgreich; HTTP 200; Serverdatum 4. Oktober 2026, 09:06 Uhr Europe/Zurich. Im abgerufenen Seitentext kein Redaktions- oder Versionsdatum. | Nennt das umgehende Trennen infizierter Systeme vom Netz, die Sicherung von Logs, die frühzeitige Abklärung einer Forensik, forensische Sicherungen vor Reparaturversuchen oder Neustarts, Neuinstallation betroffener Systeme und Wiederherstellung aus vorhandenen Backups. Dies stützt Artikel Abs. 27. Keine neue, im Zeitraum datierte Änderung ersichtlich. |
| 4 | BACS, [Zusammenarbeit mit IT-Dienstleistern](https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern) | Abruf erfolgreich; HTTP 200; Serverdatum 4. Oktober 2026, 09:06 Uhr Europe/Zurich. Im abgerufenen Seitentext kein Redaktions- oder Versionsdatum. | Verlangt klar geregelte Zuständigkeiten und spricht das Backup-Konzept sowie den letzten erfolgreichen Wiederherstellungstest an. Die Seite beschreibt 3-2-1 als drei Kopien, zwei verschiedene Medien sowie eine Kopie ausser Haus, idealerweise offline. Dies stützt Artikel Abs. 31 und 52 sowie Arbeitsmittel Abs. 22. Keine neue, im Zeitraum datierte Änderung ersichtlich. |

> **Wichtig zur Einordnung des Quellenstands:** Die vier abgerufenen BACS-Seiten stellten im verfügbaren Text kein Änderungsprotokoll oder ein belastbares Publikations-/Aktualisierungsdatum bereit. Deshalb ist die Aussage «keine materielle Änderung festgestellt» ein Ergebnis der zugänglichen aktuellen Originalfassungen und der Suche nach zeitnahen BACS-Informationen; sie ist **kein** Nachweis einer lückenlosen, bytegleichen Unverändertheit seit dem 20. September 2026.

## Zusätzliche Originalquellen zur Plausibilisierung bereits vorhandener Aussagen

Diese Quellen sind nicht die vier im Wartungsmanifest festgelegten Primärquellen für Artikel 04, wurden aber herangezogen, um bereits im Entwurf enthaltene, konkrete Aussagen nicht ungeprüft fortzuschreiben.

| Quelle | Abruf / Quellenstand | Befund |
|---|---|---|
| CISA, [#StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) | Erfolgreich abgerufen. Der Leitfaden bezeichnet sich als Fassung September 2023. | Bestätigt Offline- und verschlüsselte Backups, regelmässige Verfügbarkeits- und Integritätstests, getrennte Administrator- und Benutzerkonten sowie priorisierten Wiederaufbau sauberer Systeme. Die bestehenden Aussagen zu getrennter Administration, Offline-Kopien und Restore-Tests bleiben sachlich gedeckt. |
| Amazon Web Services, [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) | Erfolgreich abgerufen; kein im extrahierten Text ausgewiesenes Standdatum. | Bestätigt WORM, versionsbezogenen Schutz, Aufbewahrungsmodi und die Umgehungsmöglichkeit im Governance-Modus mittels spezieller Berechtigung. Die erklärende Passage im Artikel bleibt sachlich gedeckt. |
| Fedlex, [Datenschutzgesetz (DSG)](https://www.fedlex.admin.ch/eli/cc/2022/491/de) | Original-URL erreichbar, aber die Textausgabe lieferte nur den JavaScript-Hinweis. | Der direkte Artikelwortlaut von Art. 8 konnte in diesem Abruf nicht unabhängig extrahiert werden. Die rechtliche Einordnung bleibt daher ausdrücklich durch den vorhandenen Fachprüfungsmarker begrenzt. |
| Fedlex, [Datenschutzverordnung (DSV)](https://www.fedlex.admin.ch/eli/cc/2022/568/de) | Erfolgreich abgerufen. | Art. 2 verlangt Verfügbarkeit, Integrität und Nachvollziehbarkeit; Art. 3 Abs. 2 Bst. d verlangt eine rasche Wiederherstellbarkeit von Verfügbarkeit und Zugang zu Personendaten bei physischem oder technischem Zwischenfall. Die bestehende, mit Fachprüfungsmarker versehene Passage bleibt sachlich gedeckt. |
| NIST, [Recovery Point Objective](https://csrc.nist.gov/glossary/term/recovery_point_objective) und [Recovery Time Objective](https://csrc.nist.gov/glossary/term/recovery_time_objective) | Erfolgreich abgerufen; die Glossarseiten nennen NIST SP 800-34 Rev. 1 als Quelle. | Die verwendeten RPO- und RTO-Erklärungen entsprechen den dargestellten NIST-Definitionen. |
| NIST, [Recover](https://www.nist.gov/cyberframework/recover) | Erfolgreich abgerufen; Seite als nicht mehr fortlaufend aktualisiert gekennzeichnet, «Updated May 27, 2026». | Die Seite beschreibt zeitgerechte Wiederherstellung betroffener Systeme oder Assets als Ziel der Wiederherstellungsplanung. Der Entwurf referenziert dies zutreffend; kein Update im Prüfzeitraum angezeigt. |
| NIST NCCoE, [Protecting Data from Ransomware and Other Data Loss Events](https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final) | Erfolgreich abgerufen; Final vom April 2020. | Die Publikation behandelt das Durchführen, Pflegen und Testen von Backups gegen Ransomware und andere Datenverlustereignisse. Die Aussage zum Testnachweis bleibt gedeckt. |
| BACS, [Das Notfallkonzept als Schlüssel zur Cyberresilienz](https://www.bacs.admin.ch/de/notfallkonzept) | Erfolgreich abgerufen. Die Seite enthält eine Veranstaltung vom September 2026; für die vier Phasen selbst kein versionsbezogener Änderungsnachweis. | Bestätigt die Phasen Vorbereitung, Vorfall tritt ein, Vorfallsbewältigung und Nachbearbeitung sowie Rollen und Notfall-/Krisenplanung. Die Verweise in Artikel und Arbeitsmittel bleiben sachlich gedeckt. |

## Prüfung der Aktualisierungsauslöser

| Auslöser gemäss Wartungsmanifest | Prüfergebnis | Änderungsentscheid |
|---|---|---|
| Änderungen der Backup-Leitlinien | Keine datierte neue oder abweichende Backup-Leitlinie in den vier BACS-Originalseiten oder in der gezielten Suche identifiziert. Die aktuellen Aussagen bestätigen 3-2-1, externe beziehungsweise nicht dauerhaft verbundene Backups und Wiederherstellungstests. | **Keine materielle Änderung.** |
| Änderungen der Ransomware-Leitlinien | Die abgerufene BACS-Anleitung bestätigt weiterhin Isolation, forensische Vorsicht, Neuinstallation und Wiederherstellung aus Backups. | **Keine materielle Änderung.** |
| Änderungen der Aufbewahrungs-/Löschvorgaben | Die vier vorgeschriebenen BACS-Quellen enthalten keinen neuen, belastbar datierten Rechts- oder Löschstandard. Der Artikel behauptet keine allgemeingültige fixe Aufbewahrungsfrist; die konkrete DSG-/DSV-Konformität ist bereits mit `[FACHPRÜFUNG ERFORDERLICH]` gekennzeichnet. | **Keine Änderung ohne fachliche/rechtliche Verifikation.** |
| Änderungen der Zielarchitektur | Kein neuer verbindlicher Architekturstandard festgestellt. Die BACS- und CISA-Quellen stützen weiter die vorhandene risikobasierte Kombination aus 3-2-1, getrennten Zugängen, geschützten Kopien und Restore-Tests. | **Keine materielle Änderung.** |
| Organisationsspezifische Nutzung | Nicht Gegenstand dieser Quellenprüfung. Für konkrete technische, vertragliche oder rechtliche Umsetzung liegen keine Organisationsdaten vor. | **Nicht in Inhalt umsetzen; Fachprüfung erforderlich.** |

## Änderungen an den Dateien

### Artikel

**Datei:** `blog-paket/articles/04-ransomware-resistente-backups.md`

- Metadatenfeld `stand` von **20. September 2026** auf **4. Oktober 2026** aktualisiert.
- **Keine** fachliche Textänderung, weil keine relevante, belegte Korrektur identifiziert wurde.
- Vollständige Langfassung, Struktur, Slug `/wissen/ransomware-resistente-backups`, Veröffentlichungsdatum **22.10.2026**, Status **Entwurf – nicht freigegeben** und alle vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker unverändert belassen.

### Arbeitsmittel

**Datei:** `blog-paket/resources/04-backup-selbstcheck.md`

- Metadatenfeld `version` von **Stand 20. September 2026** auf **Stand 4. Oktober 2026** aktualisiert.
- **Keine** inhaltliche Änderung, weil keine relevante, belegte Korrektur identifiziert wurde.
- Status, Slug, Bezug, Struktur und alle vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker unverändert belassen.

## Nicht verifizierte Punkte und Grenzen

1. **Zeitstichtag:** Die Webabrufe erfolgten nach dem vorgegebenen Stichtag (ca. 09:06–09:08 statt exakt 09:00 Uhr). Für die Minuten zwischen 09:00 und Abruf liegt kein separater Snapshot vor.
2. **Historischer Vergleich:** Die BACS-Primärseiten zeigten im verfügbaren Abruf weder Änderungsprotokolle noch verlässliche Seitenstände. Es kann deshalb nicht belegt werden, dass jede Formulierung seit dem 20. September 2026 unverändert war; festgestellt wurde lediglich keine aktuell sichtbare, relevante Abweichung oder neu datierte Änderung.
3. **DSG Art. 8:** Die offizielle Fedlex-URL war erreichbar, ihr Artikeltext war über die verwendete Textabfrage aber wegen JavaScript nicht auslesbar. Der rechtliche Teil wurde nicht als rechtlich freigegeben bewertet.
4. **Konkrete Architektur und Verträge:** Die Quellen ersetzen keine Prüfung der gewählten Backup-Plattform, Rollen, Berechtigungen, Object-Lock-Konfiguration, Aufbewahrungsfristen, Auftragsbearbeitung oder Wiederherstellungsziele einer einzelnen Organisation.
5. **Erreichbarkeit:** Die genannten URLs waren nur zum dokumentierten Abrufzeitpunkt technisch erreichbar. Es wird keine zukünftige oder dauerhafte URL-Erreichbarkeit behauptet.

## Blocker vor Veröffentlichung

1. Der Artikel hat unverändert den Status **«Entwurf – nicht freigegeben»**. Eine Quellenprüfung ist keine Veröffentlichungsfreigabe.
2. Alle bestehenden `[FACHPRÜFUNG ERFORDERLICH]`-Marker müssen vor einer Veröffentlichung weiterhin fachlich behandelt werden, insbesondere zu DSG/DSV, Aufbewahrung, Löschung, Verträgen und organisationsspezifischer Backup-Architektur.
3. Wegen fehlender BACS-Änderungshistorien und des Abrufs nach dem Stichtag ist vor Veröffentlichung eine erneute Quellenprüfung auf dann aktuelle Leitlinien und Original-Links nötig.
4. Es liegt keine fachliche Freigabe vor; eine solche wird nicht behauptet.
5. Artikel 01 war seit 1. Oktober 2026 terminlich fällig, ist aber gemäss Aufgabenstellung nicht freigegeben. Er wurde weder verändert noch veröffentlicht; daraus folgt keine Freigabe oder Veröffentlichung für Artikel 04.

## CMS- und Veröffentlichungsstatus

**Keine CMS-Änderung und keine Veröffentlichung vorgenommen.**
