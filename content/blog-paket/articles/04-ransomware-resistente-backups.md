---
status: "Entwurf – nicht freigegeben"
slug: "/wissen/ransomware-resistente-backups"
meta_title: "Ransomware-resistente Backups für KMU | DKSchV"
meta_description: "Wie Schweizer KMU Sicherungen mit getrennten Zugängen, geschützten Kopien und dokumentierten Wiederherstellungstests robuster gegen Ransomware planen."
hauptkeyword: "ransomware-resistente Backups"
suchintention: "Informational – Backups gegen Ransomware planen und testen"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "22.10.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle 17 Quellendefinitionen des Artikels und alle acht des Arbeitsmittels, entsprechend 16 unterschiedlichen zitierten externen Original-URLs (der CISA-Leitfaden ist im Artikel zweimal referenziert), auf Erreichbarkeit und Aussagegehalt geprüft. Zusätzlich BACS «Im Fokus» sowie die BACS-Meldungen vom 20., 21. und 27. Oktober 2026 als Aktualitätskontext geprüft. Interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft."
quellenpruefung_status: "Vollständig für die 16 unterschiedlichen zitierten externen Original-URLs am 1. November 2026, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# 3-2-1-Backups für Schweizer KMU: So werden Sicherungen ransomware-resistent

**Kurzantwort:** Ein Backup schützt vor Ransomware nur, wenn Angreifer es nicht mit dem Produktivsystem löschen, verschlüsseln oder unbemerkt manipulieren können – und wenn Sie es rechtzeitig wiederherstellen können. Bauen Sie deshalb auf dem 3-2-1-Prinzip auf: mehrere Kopien, unterschiedliche Speicherarten und mindestens eine räumlich getrennte Kopie. Ergänzen Sie dies mit separaten Backup-Administrationswegen, einer Offline- oder für eine definierte Frist unveränderbaren Kopie sowie regelmässig geprüften Wiederherstellungen. Legen Sie für kritische Geschäftsprozesse einen maximal tolerierbaren Datenverlust (RPO) und eine maximal tolerierbare Ausfallzeit (RTO) fest. Nicht der grüne Status einer Backup-Software, sondern ein dokumentierter Restore-Test belegt die Wiederherstellungsfähigkeit.

## Ein vorhandenes Backup kann im Ernstfall trotzdem ausfallen

Ransomware verschlüsselt oder stiehlt nicht nur Daten. Angreifer suchen häufig nach erreichbaren Sicherungen, administrativen Konten und Wiederherstellungswegen. Ist ein Backup-Repository dauerhaft im selben Netzwerk erreichbar und können dieselben privilegierten Konten sowohl die Produktion als auch die Sicherung verwalten, kann ein erfolgreicher Angriff beide Bereiche treffen. Das BACS empfiehlt Unternehmen deshalb regelmässige Sicherungen auf einem externen Medium oder in einer sicheren Cloud; entscheidend ist, dass die Sicherung nicht dauerhaft mit dem Computer verbunden bleibt. [1]

Die am 20. Oktober veröffentlichte #StopRansomware-Warnung von CISA hält für die untersuchte SafePay-Gruppe fest, dass Akteure in einigen Fällen alle netzwerkangebundenen Sicherungen von Unternehmensdaten löschten. Das ist kein Befund zu einem Schweizer KMU. Es unterstreicht aber, dass eine Architektur den Daten- und Administrationspfad der letzten Rückfallebene getrennt planen und im Restore-Test prüfen muss. [16] [4] [6]

Die Geschäftsleitung sollte Backups deshalb nicht als reine Speicherfrage behandeln. Sie sind ein Instrument für die Betriebsfähigkeit: Rechnungen, Aufträge, Produktionsdaten, E-Mail, Fachanwendungen und Konfigurationen müssen in einer sinnvollen Reihenfolge wieder verfügbar werden. Das BACS ordnet Datensicherung folgerichtig als technische Massnahme ein, die mit klaren Verantwortlichkeiten, Governance und Kontinuitätsmanagement zusammenwirken muss. [2]

> **Ransomware-resistent** bedeutet nicht «unverletzlich». Gemeint ist eine Architektur, welche die Chance erhöht, nach einem Angriff auf einen sauberen, ausreichenden Datenstand zurückzukehren, ohne sich auf eine Lösegeldzahlung verlassen zu müssen.

Im Ernstfall empfiehlt das BACS, infizierte Systeme vom Netz zu trennen, den Infektionsweg zu klären, Systeme neu aufzusetzen und Daten aus vorhandenen Backups wiederherzustellen. Vor Reparaturversuchen oder Neustarts sind bei Bedarf forensische Sicherungen durch Fachpersonen wichtig. [3] Der Backup-Plan muss daher mit dem [IT-Notfallplan](/unsere-dienstleistungen/notfallplanung) und der Vorfallsbehandlung zusammenpassen – nicht erst nach einem Befall entstehen.

Der BACS-Wochenrückblick vom 6. Oktober 2026 ergänzt: Einzelne Anzeichen beweisen keine Infektion; bei mehreren ungewöhnlichen Beobachtungen soll eine genauere Untersuchung erfolgen. Bei Verdacht empfiehlt das BACS die Untersuchung durch eine Fachperson; bei Geschäftsgeräten ist die zuständige IT zu informieren. Dieser Hinweis ersetzt keine forensische oder organisationsspezifische Triage. [15]

## 3-2-1 richtig anwenden: Redundanz ist nur der Anfang

Die **3-2-1-Regel** ist eine einfache Mindeststruktur: Halten Sie mindestens drei Kopien der wichtigen Daten vor, nutzen Sie zwei unterschiedliche Speicherarten und bewahren Sie mindestens eine Kopie ausserhalb des primären Standorts auf. Das BACS nennt diese drei Elemente und empfiehlt die externe Kopie idealerweise offline. [4]

Die Regel beantwortet jedoch noch nicht, *welche* Daten gesichert werden, *wer* eine Kopie löschen kann und *ob* eine Wiederherstellung den Betrieb tatsächlich wieder aufnimmt. Für ein KMU wird sie erst wirksam, wenn sie pro kritischem Dienst konkret ausgestaltet wird.

| Baustein | Praktische Frage | Prüfkriterium |
|---|---|---|
| Drei Kopien | Gibt es neben der produktiven Fassung mindestens zwei Sicherungskopien? | Datenbestand und System-/Konfigurationsdaten sind im Backup-Inventar aufgeführt. |
| Zwei Speicherarten | Hängt nicht jede Kopie an derselben Technik oder demselben Fehlerbild? | Die Schutzmechanismen und Fehlerdomänen der Kopien sind dokumentiert. |
| Eine externe Kopie | Überlebt mindestens eine Kopie einen Standort-, Konto- oder Netzwerkausfall? | Die Kopie liegt ausserhalb des primären Standorts und ist nicht dauerhaft aus der Produktion erreichbar. |
| Wiederherstellbarkeit | Kann das Team einen priorisierten Dienst auf einen sauberen Stand zurückbringen? | Ein Test weist Datenstand, Dauer, Abweichungen und Folgemassnahmen aus. |

Unterscheiden Sie dabei die Begriffe. Ein **Backup** ist eine Kopie, die für die Wiederherstellung angelegt und aufbewahrt wird. **Synchronisation** verteilt Änderungen zwischen Orten; eine versehentlich gelöschte oder verschlüsselte Datei kann deshalb mitverteilt werden. Ein **Snapshot** ist ein zeitbezogener Zustand eines Systems oder Speichers, der je nach Plattform im selben Verwaltungs- und Vertrauensbereich liegen kann. Ein **Archiv** dient vor allem der langfristigen Aufbewahrung. Snapshot, Synchronisation und Archiv können nützlich sein, ersetzen aber nicht automatisch eine unabhängige, getestete Sicherung.

## Backup-Administration vom Produktivbetrieb trennen

Die wichtigste Frage lautet: Kann eine kompromittierte Identität auch das Backup zerstören? Wenn die Antwort «ja» oder «unbekannt» ist, fehlt eine wesentliche Schutzschicht.

**Getrennte Administration** bedeutet, dass die Verwaltung von Backup-Speicher, Aufbewahrungsregeln und Wiederherstellung nicht ausschliesslich über dieselben Konten, Endgeräte, Verzeichnisse und Fernzugänge erfolgt wie der Tagesbetrieb. CISA empfiehlt, Administrationskonten von Benutzerkonten zu trennen und nur benannte Administrationskonten für administrative Aufgaben einzusetzen. [5] Für Backups sollte dieses Prinzip bis zum Repository, Cloud-Mandanten, Schlüsselsystem und Dienstleisterzugang durchdacht werden.

In der Praxis heisst das nicht zwingend, dass jedes KMU eine komplexe Parallelumgebung braucht. Entscheidend ist ein nachvollziehbarer, dem Risiko angemessener Trennungsgrad. Definieren Sie beispielsweise eigene Backup-Admin-Konten mit Mehrfaktor-Authentisierung, vergeben Sie Berechtigungen nach dem Prinzip der minimalen Rechte und verhindern Sie, dass alltägliche Benutzer- oder Serverkonten Sicherungsfristen verkürzen oder Daten endgültig löschen können. Bewahren Sie Notfallzugänge kontrolliert, dokumentiert und getrennt von der Produktionsumgebung auf. Prüfen Sie auch, welche Rechte ein IT-Provider und dessen Fernwartungswerkzeuge besitzen.

Bei ausgelagerter IT bleibt die Verantwortung für die Klärung der Rollen beim Unternehmen. Das BACS empfiehlt, Zuständigkeiten für technische und organisatorische Massnahmen klar zu regeln, nach dem Backup-Konzept und dem letzten erfolgreichen Wiederherstellungstest zu fragen sowie die vereinbarten Leistungen periodisch zu kontrollieren. [4] Verankern Sie daher mindestens Datenumfang, Aufbewahrung, Verantwortliche, Eskalationswege, Testnachweise und Rückgabe- beziehungsweise Wiederherstellungsprozess im Leistungsbeschrieb. Diese Punkte gehören auch in das [Cyber-Risikomanagement](/unsere-dienstleistungen/risikomanagement), weil sie Geschäftsrisiken und nicht nur IT-Parameter betreffen.

## Offline und unveränderbar: zwei unterschiedliche Schutzmechanismen

Eine **Offline-Kopie** ist physisch oder logisch vom produktiven Umfeld getrennt und während der Trennung nicht über das Netzwerk erreichbar. Sie reduziert das Risiko, dass Schadsoftware auf eine zugängliche Sicherung zugreift. CISA empfiehlt verschlüsselte Offline-Backups kritischer Daten und regelmässige Tests auf Verfügbarkeit und Integrität, gerade weil Ransomware erreichbare Sicherungen löschen oder verschlüsseln kann. [6]

Eine **unveränderbare Kopie** ist für eine vordefinierte Aufbewahrungsdauer gegen Überschreiben und Löschen geschützt. Solche Funktionen werden oft als WORM (*Write Once, Read Many*) oder Object Lock bezeichnet. Der Schutz entsteht aber nicht durch das Etikett: Entscheidend sind aktivierte Aufbewahrungsregeln, die gewählte Schutzstufe, Rechte zum Ändern der Regeln, Schlüsselverwaltung, Protokollierung und der tatsächliche Ablauf beim Restore. Herstellerdokumentationen zeigen diese Unterschiede deutlich: Bei Amazon S3 Object Lock hängt der Schutz beispielsweise an Objektversionen, Aufbewahrungsmodus und Berechtigungen; der Governance-Modus kann mit einer speziellen Berechtigung umgangen werden. [7]

Eine unveränderbare Kopie ist auch nicht automatisch offline. Sie kann online verfügbar sein, aber Löschen oder Überschreiben während der Frist verhindern. Umgekehrt ist ein vom Netz getrenntes Medium nicht zwingend unveränderbar. Für kritische Daten ist deshalb die Kombination sinnvoll: eine vom Produktionsweg getrennte Kopie und ein Schutz gegen vorzeitige Veränderung, abgestimmt auf das Risikoszenario und die Wiederherstellungsziele. CISA weist darauf hin, dass Cloud-Objektsperren und Versionsverwaltung helfen können, Löschen oder Überschreiben zu begrenzen, zugleich aber sorgfältig konfiguriert werden müssen. [6]

Legen Sie die Aufbewahrungsdauer nicht willkürlich fest. Sie muss mindestens lange genug sein, um eine unbemerkte Manipulation zu entdecken, einen sauberen Wiederherstellungspunkt zu wählen und die Wiederherstellung umzusetzen. Zu lange Fristen können Kosten, Datenschutz- und Löschkonzepte berühren. **[FACHPRÜFUNG ERFORDERLICH]** Ob Ihre konkrete Aufbewahrung und Sicherungsarchitektur den Anforderungen des DSG und weiterer anwendbarer Vorgaben genügt, braucht eine fachliche und bei rechtlichen Fragen eine fachjuristische Prüfung; dieser Beitrag ist keine individuelle Rechtsberatung. Das DSG verlangt risikogerechte technische und organisatorische Massnahmen; die Datenschutzverordnung verlangt unter anderem, dass Personendaten bei einem physischen oder technischen Zwischenfall rasch wiederhergestellt werden können. [8] [9]

## RPO, RTO und Wiederanlauf: vom Backup-Journal zur Geschäftsentscheidung

Ein Backup-Job kann technisch erfolgreich sein und dennoch die falschen Ziele verfolgen. Definieren Sie deshalb mit den Prozessverantwortlichen zwei Kennzahlen:

- Das **Recovery Point Objective (RPO)** ist der Zeitpunkt, bis zu dem Daten nach einem Ausfall wiederhergestellt sein müssen. Praktisch beschreibt es den maximal hinnehmbaren Datenverlust zwischen zwei Wiederherstellungspunkten. [10]
- Das **Recovery Time Objective (RTO)** ist die maximal vertretbare Dauer der Wiederherstellungsphase, bevor Geschäftsprozesse unvertretbar beeinträchtigt werden. [11]

Ein RPO von vier Stunden ist keine Zusage, dass ein Dienst nach vier Stunden läuft. Es legt fest, wie alt der Datenstand höchstens sein darf. Ein RTO von acht Stunden ist keine Eigenschaft einer Backup-Lizenz, sondern ein Ziel für die gesamte Kette: Angriff erkennen, Systeme bereinigen, Infrastruktur bereitstellen, Daten zurückspielen, Zugänge prüfen und den Prozess freigeben. NIST ordnet Wiederherstellungsprozesse dem Ziel zu, Systeme oder Vermögenswerte nach Cybervorfällen zeitgerecht wiederherzustellen. [12]

Priorisieren Sie daher nicht nach Datenmenge, sondern nach Geschäftswirkung. Die Buchhaltung braucht vielleicht zuerst die Zahlungsfreigabe und Lieferantendaten; die Produktion braucht zuerst die Steuerungs- oder Auftragsdaten; der Vertrieb benötigt möglicherweise Kunden- und Kontaktinformationen. Dokumentieren Sie je Dienst den Eigentümer, Abhängigkeiten wie Identitätsdienst, Netzwerk, Lizenzen und DNS, den RPO, den RTO, den vorgesehenen Wiederherstellungsort und die Abnahme durch den Fachbereich. So verbinden Sie die Backup-Architektur mit einer realistischen [Wiederherstellungsübung](/wissen/backup-wiederherstellung-testen).

### Hypothetisches Praxisbeispiel: Was der Restore-Test sichtbar macht

Ein hypothetisches Handels-KMU sichert seine Dateidaten jede Nacht und sieht täglich erfolgreiche Jobs. Im Test stellt das Team jedoch fest, dass die Fachanwendung ohne separaten Lizenzserver und ohne die Dokumentation der Firewall-Regeln nicht startet. Zudem kann der externe IT-Provider die Backup-Konsole nur mit einem Konto öffnen, das auch die produktive Domäne verwaltet. Der Test zeigt damit zwei Risiken: Das geplante RTO ist mit dem aktuellen Ablauf nicht erreichbar, und ein kompromittiertes Domänenkonto könnte den Wiederherstellungsweg gefährden.

Die Lösung ist nicht zwingend ein neues Produkt. Das Unternehmen trennt die Backup-Administration, sichert Konfigurationen und Wiederanlaufdokumente mit, definiert eine saubere Wiederherstellungsumgebung und wiederholt den Test nach der Anpassung. Das Ergebnis wird als Soll-Ist-Vergleich festgehalten. Erst dann ist klarer, ob RPO und RTO plausibel sind.

## Wiederherstellungsfähigkeit beweisen, nicht vermuten

Ein vollständiger Test muss nicht jeden Monat die ganze Umgebung lahmlegen. Beginnen Sie mit einem priorisierten, abgegrenzten Szenario: Stellen Sie einen repräsentativen Datensatz oder einen kritischen Dienst in einer isolierten Umgebung wieder her. Prüfen Sie Datenintegrität, Benutzerzugriff, Abhängigkeiten und fachliche Nutzbarkeit. Messen Sie vom Start des Wiederanlaufs bis zur Abnahme durch den Fachbereich. CISA empfiehlt, Wiederherstellung aus Offline-Backups nach der Priorität kritischer Dienste vorzunehmen und saubere Systeme nicht erneut zu infizieren. [6]

Als aktueller Schweizer Vergleichspunkt berichtete das BACS am 22. Oktober zur Studie «KMU Cybersicherheit 2026»: Neun von zehn KMU erstellen Backups, aber nur jedes vierte testet die Wiederherstellung. Die Studienangabe ist kein Nachweis für die Situation eines einzelnen Unternehmens, bestärkt jedoch den Fokus auf nachweisbare Tests. [17]

Der Testnachweis sollte mindestens den gewählten Sicherungsstand, den Start- und Endzeitpunkt, die tatsächlich erreichte Datenaktualität, verwendete Konten, Abweichungen, getroffene Entscheide und offene Massnahmen enthalten. NIST betont, dass Backups durchgeführt, gepflegt und getestet werden müssen; dessen Leitfaden richtet sich ausdrücklich an Dienstleister und ihre Kunden im Kontext von Ransomware und anderen Datenverlustereignissen. [13]

Das BACS strukturiert die Notfallvorsorge in Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung. Für KMU stellt es eine Vorlage für einen IT-Notfall- und Krisenplan bereit. [14] Verankern Sie darin, wer den Restore autorisiert, wer die Sauberkeit der Zielumgebung beurteilt, wer den Fachtest abnimmt und wie bei einem fehlgeschlagenen Wiederherstellungspunkt entschieden wird. Halten Sie Kontaktwege auch ausserhalb der potenziell betroffenen Systeme bereit; ein zentral gepflegter [Kontakt](/kontakt) kann dabei als zusätzliche Anlaufstelle dokumentiert werden.

## Typische Fehler, die den Backup-Schutz entwerten

**«Wir haben eine Cloud, also ein Backup.»** Cloud-Verfügbarkeit, Papierkorb und Versionierung können helfen, sind aber nicht automatisch eine unabhängige Sicherung. Klären Sie Datenumfang, Aufbewahrung, Löschrechte und Restore-Verfahren ausdrücklich.

**«Der Backup-Job war grün.»** Ein Jobprotokoll belegt vor allem, dass ein Prozess Daten übertragen hat. Es belegt weder einen sauberen Wiederherstellungspunkt noch einen funktionierenden Geschäftsdienst.

**«Ein Domänen-Admin darf alles.»** Dieses Muster bündelt Risiko. Trennen Sie alltägliche, produktive und Backup-Administration, und überprüfen Sie privilegierte Rechte regelmässig.

**«Snapshots genügen.»** Ein Snapshot im selben kompromittierten Speicher-, Hypervisor- oder Administrationsbereich ist keine gleichwertige letzte Rückfallebene.

**«Wir testen später.»** Ungetestete Sicherungen machen RPO und RTO zu Annahmen. Testen Sie nach wesentlichen Architektur-, Anwendungs- oder Provideränderungen und verbessern Sie den Ablauf anhand der Ergebnisse.

## Ein umsetzbarer 30-Tage-Plan

### Tage 1 bis 7: Bestand und Prioritäten klären

Erstellen Sie ein kompaktes Inventar der kritischen Prozesse, Daten, Anwendungen, Konfigurationen und Identitäten. Benennen Sie je Dienst einen Fachverantwortlichen. Halten Sie vorhandene Kopien, Speicherorte, Aufbewahrungsfristen, Zugriffsrechte und den letzten dokumentierten Restore-Test fest. Nutzen Sie dafür den [Backup-Selbstcheck](/resources/04-backup-selbstcheck).

### Tage 8 bis 14: Schutzlücken im Wiederherstellungsweg schliessen

Prüfen Sie, ob mindestens eine Kopie vom produktiven Zugriff getrennt und eine Kopie gegen vorzeitige Veränderung geschützt ist. Reduzieren und trennen Sie Backup-Administrationsrechte. Sichern Sie zusätzlich die für den Wiederanlauf notwendigen Konfigurationen, Installationsmedien, Lizenzen, Schlüssel, Dokumentationen und Kontaktlisten.

### Tage 15 bis 21: Ziele und Reihenfolge verbindlich festlegen

Vereinbaren Sie RPO und RTO mit den Prozessverantwortlichen. Legen Sie die Wiederanlaufreihenfolge sowie Akzeptanzkriterien fest. Ergänzen Sie Rollen, Stellvertretungen und Eskalation im Notfallplan. Bei Unsicherheiten über Risiken und Prioritäten hilft eine methodische [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse), die technische Befunde mit den betroffenen Geschäftsprozessen verbindet.

### Tage 22 bis 30: Wiederherstellung üben und nachsteuern

Führen Sie einen abgegrenzten Restore-Test in einer geeigneten Umgebung durch. Vergleichen Sie Ist-Datenstand und Ist-Dauer mit RPO und RTO. Dokumentieren Sie Abweichungen, weisen Sie Massnahmen mit Verantwortlichen und Termin zu und legen Sie den Folgetest fest. Eine periodische Überprüfung ist auch deshalb wichtig, weil sich Anwendungen, Datenmengen, Berechtigungen und Dienstleisterbeziehungen verändern.

## Nächster Schritt

Dokumentieren Sie den Ist-Stand mit dem [Backup-Selbstcheck](/resources/04-backup-selbstcheck) und planen Sie einen abgegrenzten Restore-Test. Wenn Sie Unterstützung bei einer [DKSchV-Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) wünschen, klären Sie Umfang, Annahmen und gewünschte Ergebnisse vorab; eine Analyse garantiert keine Wiederherstellbarkeit.

## Quellen

[1]: https://www.bacs.admin.ch/de/erste-schritte-unternehmen-behoerden "BACS – Erste Schritte für Unternehmen und Behörden: Backup nicht dauerhaft verbunden"
[2]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz für Unternehmen und Behörden"
[3]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[4]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern: 3-2-1 und Wiederherstellungstest"
[5]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide: getrennte Administrationskonten"
[6]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide: Offline-Backups, Integritätstests und priorisierte Wiederherstellung"
[7]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html "Amazon S3 – Object Lock: WORM, Aufbewahrungsmodi und Berechtigungen"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz (DSG), Art. 8 Datensicherheit"
[9]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung (DSV), Art. 1 bis 3 Datensicherheit und Wiederherstellung"
[10]: https://csrc.nist.gov/glossary/term/recovery_point_objective "NIST CSRC Glossary – Recovery Point Objective"
[11]: https://csrc.nist.gov/glossary/term/recovery_time_objective "NIST CSRC Glossary – Recovery Time Objective"
[12]: https://www.nist.gov/cyberframework/recover "NIST Cybersecurity Framework – Recover"
[13]: https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final "NIST NCCoE – Protecting Data from Ransomware and Other Data Loss Events"
[14]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[15]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, veröffentlicht am 6. Oktober 2026"
[16]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a "CISA – StopRansomware: SafePay Ransomware, 20. Oktober 2026"
[17]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026: Cyberkriminalität wird zum Geschäftsrisiko für Schweizer KMU, 22. Oktober 2026"
