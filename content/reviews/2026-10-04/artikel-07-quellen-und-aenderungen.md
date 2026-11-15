# Quellen- und Änderungsprüfung – Artikel 07

**Prüfdatum:** 4. Oktober 2026  
**Prüfzeitraum:** 20. September 2026 bis einschliesslich 4. Oktober 2026, 09:00 Uhr (Europe/Zurich)  
**Gegenstand:** `07-backup-wiederherstellung-testen.md` und das zugehörige Arbeitsmittel `07-restore-testprotokoll.md`  
**Artikel-Slug:** `/wissen/backup-wiederherstellung-testen`  
**Paketstatus vor und nach Prüfung:** Entwurf; keine Veröffentlichungsfreigabe

## Prüfauftrag und Methode

Geprüft wurden die im Wartungsmanifest für Artikel 07 genannten **offiziellen Primärquellen**. Die Recherche erfolgte über Suchtreffer zu den Originalseiten und anschliessenden Abruf dieser Originalseiten. Zusätzlich wurden die aktuellen BACS-Veröffentlichungen im relevanten Zeitraum sowie die im Entwurf zitierten amtlichen Rechts- und Fachquellen auf konkrete, für Wiederanlauf, Restore-Tests und Meldepflichten relevante Änderungen geprüft.

> Der technische Abruf der Webseiten wurde zwischen 09:06 und 09:08 Uhr Europe/Zurich ausgeführt. Bewertet wurden nur Veröffentlichungen mit einem auf der Originalseite ausgewiesenen Datum spätestens 4. Oktober 2026, 09:00 Uhr. Die unversionierten BACS-Seiten weisen keinen Seitenänderungszeitpunkt aus; ein exakter historischer Snapshot um 09:00 Uhr ist damit nicht nachweisbar. Dies ist unter «Nicht verifizierte Punkte» festgehalten.

## Geprüfte Primärquellen

| Quelle gemäss Manifest | Original-URL | Festgestellter Quellenstand / relevante Aussage | Ergebnis für Artikel und Arbeitsmittel |
|---|---|---|---|
| BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz | https://www.bacs.admin.ch/de/notfallkonzept | Aktuelle Seite: vier Phasen Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung; klar zugeordnete Verantwortlichkeiten und Debriefing. Das Template für den IT-Notfall- und Krisenplan für KMU ist weiterhin mit **18. Mai 2026** datiert. | Die Aussagen in Artikel Ziff. 21, 63 und 102 sowie im Arbeitsmittel Ziff. 19 und 185 sind weiterhin gedeckt. Keine Korrektur. |
| BACS – Ransomware: Was nun? | https://www.bacs.admin.ch/de/ransomware-was-nun | Aktuelle Seite: Infektionsweg ermitteln, Neuinfektion verhindern, betroffene Systeme neu aufsetzen und Daten aus Backups wiederherstellen. Forensische Sicherungen sollen vor Reparaturversuchen oder Neustarts fachkundig beurteilt werden. | Die Aussagen in Artikel Ziff. 79–88 und Arbeitsmittel Ziff. 220 sind weiterhin gedeckt. Keine Korrektur. |
| CISA – StopRansomware Guide | https://www.cisa.gov/stopransomware/ransomware-guide | Der aktuelle Leitfaden fordert offline verschlüsselte Backups, regelmässige Tests von Verfügbarkeit und Integrität in einem Disaster-Recovery-Szenario, Offline-/Hardcopy-Pläne, Priorisierung kritischer Systeme auf sauberem Netzwerk und Schutz vor Reinfektion. Die offizielle Ressourcenseite führt als Revision **19. Oktober 2023**: https://www.cisa.gov/resources-tools/resources/stopransomware-guide | Die Aussagen in Artikel Ziff. 31, 57, 75 und 88 sowie Arbeitsmittel Ziff. 19 sind weiterhin gedeckt. Keine neue Leitlinienrevision im Prüfzeitraum festgestellt. |
| BACS – Meldepflicht für Cyberangriffe auf kritische Infrastrukturen | https://www.bacs.admin.ch/de/meldepflicht | Aktuelle Seite: Meldung durch betroffene Betreiberinnen und Betreiber kritischer Infrastrukturen innert 24 Stunden nach Entdeckung; Vervollständigung fehlender Angaben innert 14 Tagen. Sie verweist auf ISG Art. 74b, meldepflichtige Angriffe und den Cyber Security Hub. | Die Aussage in Artikel Ziff. 122 ist weiterhin gedeckt. Keine Korrektur. |

## Zusätzlich geprüfte Originalquellen und Trigger

| Quelle / Trigger | Original-URL | Befund | Auswirkung |
|---|---|---|---|
| BACS, aktuelle Übersicht | https://www.bacs.admin.ch/de/im-fokus | Im Prüfzeitraum erschienen u. a. Beiträge vom 22., 24., 25., 28., 29. September und 1. Oktober 2026. Keine dort ausgewiesene neue Vorgabe zu Restore-Tests, Backup-Architektur oder dem bestehenden Notfallkonzept. | Keine materielle Änderung. |
| BACS, Schadsoftware-Wochenrückblick vom 29. September 2026 | https://www.bacs.admin.ch/de/26w39-de | Behandelt Infektionswege und Prävention. Keine neue Wiederanlauf-, Restore- oder Backup-Pflicht. | Keine materielle Änderung. |
| BACS, geplantes Cybersicherheitsgesetz vom 25. September 2026 | https://www.bacs.admin.ch/de/26-cybersicherheitsgesetz-de | Auftrag zur Erarbeitung einer Vernehmlassungsvorlage bis Juni 2027. Die bestehende, seit April 2025 geltende Meldepflicht soll künftig überführt werden; die Mitteilung enthält keine bereits in Kraft getretene Änderung der Fristen oder des Geltungsbereichs. | Kein Korrekturbedarf; keine vorweggenommene Rechtsänderung in den Entwurf aufgenommen. |
| NIST SP 800-34 Rev. 1 | https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final | Offizielle Publikation, Mai 2010, aktualisiert 11. November 2010; behandelt Wiederherstellungsanforderungen/-prioritäten sowie Tests und Übungen. | Die als allgemeine Planungsreferenz verwendeten Aussagen zu RTO/RPO und Tests bleiben verwendbar; keine neue Fassung im Prüfzeitraum festgestellt. |
| DSG Art. 24 (amtliche, statisch abrufbare Fassung) | https://www.fedlex.admin.ch/eli/oc/2022/491/de | Art. 24 Abs. 1–2: Meldung an den EDÖB «so rasch als möglich» bei voraussichtlich hohem Risiko; mindestens Art der Verletzung, Folgen sowie ergriffene oder vorgesehene Massnahmen. | Die Aussage in Artikel Ziff. 124 und Arbeitsmittel Ziff. 222 ist wörtlich sachlich gedeckt. |
| EDÖB – Leitfaden DataBreach | https://www.edoeb.admin.ch/de/leitfaden-data-breach | Seite veröffentlicht am 7. Februar 2025; verlinkter Leitfaden Version 1.2 vom 23. April 2025. Er behandelt Datensicherheitsverletzungen und den Begriff «voraussichtlich hohes Risiko». | Artikel Ziff. 124 bleibt gedeckt. Keine Änderung im Prüfzeitraum festgestellt. |

## Änderungsentscheidung

### Keine materielle fachliche Änderung festgestellt

Für die vier im Wartungsmanifest genannten Primärquellen wurde im definierten Zeitraum **keine belegte, relevante Änderung** festgestellt, die eine Anpassung der Aussagen zu Restore-Tests, Wiederanlaufreihenfolge, Backup-Verfügbarkeit/-Integrität, Rollen, Notfallplanung oder der BACS-Meldefrist erfordert.

Die am 25. September 2026 veröffentlichte BACS-Mitteilung zum geplanten Cybersicherheitsgesetz ist ein Rechtsetzungsvorhaben, keine bereits geltende Änderung. Sie darf daher weder als neue Pflicht noch als Änderung der bestehenden 24-Stunden-/14-Tage-Regel dargestellt werden.

### Ausgeführte, eng begrenzte Dateianpassungen

| Datei | Änderung | Begründung |
|---|---|---|
| `/home/ubuntu/dkschv-audit/blog-paket/articles/07-backup-wiederherstellung-testen.md` | Frontmatter `stand` von `20. September 2026` auf `4. Oktober 2026` gesetzt. | Der Quellenstand wurde für die im Manifest bezeichneten Primärquellen geprüft. Keine Body-Standangabe war zu ersetzen. |
| `/home/ubuntu/dkschv-audit/blog-paket/resources/07-restore-testprotokoll.md` | Frontmatter `stand` von `20. September 2026` auf `4. Oktober 2026` gesetzt. | Das Arbeitsmittel wurde zusammen mit dem Artikel gegen dieselben Wiederanlaufquellen geprüft. Keine inhaltliche Korrektur belegt. |

Unverändert erhalten wurden: beide Slugs, das Veröffentlichungsdatum des Artikels (**12.11.2026**), der Status **Entwurf** beziehungsweise **Arbeitsvorlage – nicht freigegeben**, die vollständige Langfassung und Struktur sowie **alle** `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Das Wartungsmanifest, das CMS, andere Artikel und Freigabestati wurden nicht verändert.

## Nicht verifizierte Punkte

1. **Historischer Zeitpunkt 09:00 Uhr:** Die aktuellen, unversionierten BACS-Seiten veröffentlichen keinen Änderungszeitpunkt und keine öffentliche Versionshistorie. Der technische Abruf erfolgte sechs bis acht Minuten nach dem verlangten Stichtag. Daher lässt sich nicht beweisen, dass der Wortlaut um exakt 09:00 Uhr identisch war. Die Bewertung stützt sich nur auf die bis zum Stichtag datierten Veröffentlichungen und den beim Abruf sichtbaren Inhalt.
2. **Keine negative Vollständigkeitsbehauptung:** Aus der fehlenden Dokumentation einer Seitenrevision folgt nicht mit Sicherheit, dass seit 20. September keine redaktionelle Änderung an einer unversionierten Quelle erfolgt ist. Die aktuelle Quelle deckt jedoch die verwendeten Aussagen weiterhin.
3. **Organisationsspezifische Umsetzbarkeit:** RTO/RPO, Wiederanlaufreihenfolge, Isolierung, Forensik, Berechtigungen, Datenklassifikation, Providerabhängigkeiten und Testtakt bleiben organisations-, vertrag- und systemabhängig. Sie wurden nicht individualisiert verifiziert.
4. **Rechtsanwendung:** Der konkrete Status als kritische Infrastruktur sowie eine BACS-, EDÖB- oder sonstige Meldepflicht sind vorfalls- und organisationsabhängig. Die allgemeine Rechtsaussage wurde gegen Art. 24 DSG und die BACS-Seite geprüft; sie ersetzt keine Rechtsberatung.
5. **NIST:** SP 800-34 Rev. 1 stammt von 2010. Sie dient im Entwurf nur als allgemeine Fachreferenz, nicht als aktuelle schweizerische Rechtsquelle.

## Klare Blocker vor Veröffentlichung

1. **Keine Veröffentlichungsfreigabe:** Das Wartungsmanifest führt Artikel 07 als `Entwurf – nicht freigegeben`; der Paketstatus ist ausdrücklich keine Freigabe.
2. **Erforderliche Fachprüfung bleibt offen:** Alle vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker sind unverändert. Vor Veröffentlichung sind insbesondere technische Wiederanlaufannahmen, Forensik, organisationsspezifische RTO/RPO und Rechts-/Meldehinweise fachlich freizugeben.
3. **Offener Stichtagsnachweis:** Für eine Behauptung eines minutengenauen Quellenstands um 09:00 Uhr wäre ein versionierter bzw. archivierter Quellennachweis erforderlich; dieser liegt für die unversionierten Seiten nicht vor.
4. **Artikel 01:** Die terminliche Fälligkeit von Artikel 01 seit 1. Oktober begründet keine Freigabe. Für Artikel 01 wurde nichts geändert und nichts veröffentlicht.

**CMS-/Veröffentlichungsaktion:** Keine. Weder Artikel 07 noch Artikel 01 oder andere Inhalte wurden veröffentlicht oder im CMS bearbeitet.
