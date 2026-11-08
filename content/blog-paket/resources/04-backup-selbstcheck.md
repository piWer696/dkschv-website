---
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/04-backup-selbstcheck"
titel: "Backup-Selbstcheck für ransomware-resistente Sicherungen"
meta_title: "Backup-Selbstcheck für Schweizer KMU | DKSchV"
meta_description: "Arbeitsvorlage für 3-2-1-Backups, getrennte Administration, geschützte Kopien und dokumentierte Restore-Tests."
suchintention: "Arbeitsmittel – Backup- und Wiederherstellungsfähigkeit prüfen"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
version: "Stand 1. November 2026"
quellenpruefung_umfang: "Alle acht zitierten externen Original-URLs des Arbeitsmittels auf Erreichbarkeit und Aussagegehalt geprüft; interne relative Paketlinks wurden erhalten, nicht als künftige Live-URLs geprüft."
quellenpruefung_status: "Vollständig für die acht zitierten externen Original-URLs am 1. November 2026, tatsächlicher Abruf ca. 09:05–09:07 CET Europe/Zurich; keine Freigabe und keine lückenlose historische Änderungsverifikation."
bezug: "/wissen/ransomware-resistente-backups"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Backup-Selbstcheck: Wiederherstellung nach Ransomware vorbereiten

## Zweck

Dieser Selbstcheck hilft Geschäftsleitungen und IT-Verantwortlichen von Schweizer KMU, die **Wiederherstellungsfähigkeit** ihrer Backup-Architektur strukturiert zu besprechen. Er fokussiert auf das 3-2-1-Prinzip, getrennte Administration, Offline- oder unveränderbare Kopien, Wiederherstellungsziele und Restore-Tests.

Das Arbeitsmittel ist eine Orientierung für die Priorisierung von Verbesserungen. Ein ausgefüllter Selbstcheck, ein erfolgreiches Backup-Protokoll oder ein einzelner Test sind **keine Garantie** gegen Ransomware, Datenverlust oder Betriebsunterbruch.

Das BACS empfiehlt getrennte Sicherungskopien und regelmässige Wiederherstellungstests. Der internationale StopRansomware-Leitfaden empfiehlt zusätzlich offline gehaltene, geschützte Sicherungen und Integritätsprüfungen.[1] [2]

Bei einem aktuellen Verdacht auf Schadsoftware ist dieser Selbstcheck keine Vorfallsanweisung: Das BACS empfiehlt die Untersuchung durch eine Fachperson und bei Geschäftsgeräten die Information der zuständigen IT. [8]

## Anwendung

Füllen Sie den Selbstcheck gemeinsam mit der internen IT, Prozessverantwortlichen und – falls vorhanden – dem IT-Dienstleister aus. Verwenden Sie pro kritischem Dienst oder Dienstgruppe ein separates Blatt. Belegen Sie Antworten soweit möglich mit einem Datum, einer Konfiguration, einem Testprotokoll oder einem vertraglichen Nachweis.

**Bewertung je Kontrollpunkt:** ☐ Ja  ☐ Teilweise  ☐ Nein  ☐ Nicht bekannt  
**Nachweis / Fundstelle:** ________________________________________________  
**Massnahme, Verantwortliche Person, Termin:** ______________________________

> **Arbeitsregel:** «Nicht bekannt» ist ein Befund. Behandeln Sie ihn wie eine offene Klärung, nicht wie ein «Ja».

---

## 1. Geltungsbereich und Verantwortlichkeit

**Unternehmen / Bereich:** ________________________________________________  
**Kritischer Dienst / Prozess:** ____________________________________________  
**Fachverantwortliche Person:** ____________________________________________  
**IT-Verantwortliche Person:** ______________________________________________  
**IT-Dienstleister / Notfallkontakt:** _______________________________________  
**Datum der Erhebung:** __________________  
**Letzter dokumentierter Restore-Test:** ____________________________________

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Der geschäftskritische Dienst, seine Daten und der zuständige Fachbereich sind benannt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Abhängigkeiten für den Wiederanlauf sind erfasst, etwa Identitäten, Netzwerk, DNS, Lizenzen, Schlüssel und externe Dienste. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Es ist festgelegt, wer einen Restore auslöst, wer ihn technisch durchführt und wer ihn fachlich abnimmt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Kontakt- und Eskalationswege sind auch verfügbar, wenn E-Mail oder Kollaborationsplattformen ausfallen. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

## 2. 3-2-1-Architektur und Datenumfang

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Neben der produktiven Fassung bestehen mindestens zwei Sicherungskopien der für den Dienst notwendigen Daten. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Die Kopien nutzen unterschiedliche Speicherarten oder ausreichend getrennte Fehlerdomänen. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Mindestens eine Kopie befindet sich ausserhalb des primären Standorts. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Der Backup-Umfang umfasst nicht nur Fach- und Dateidaten, sondern auch notwendige Konfigurationen und Wiederanlaufunterlagen. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Es ist dokumentiert, was bewusst **nicht** gesichert wird und welches Risiko damit akzeptiert wird. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

**Kopienübersicht**

| Kopie | Daten / Systeme | Speicherort und Speicherart | Eigentümer / Zugriff | Aufbewahrung | Offline / unveränderbar? |
|---|---|---|---|---|---|
| Produktion | __________________ | __________________ | __________________ | __________________ | __________________ |
| Backup 1 | __________________ | __________________ | __________________ | __________________ | __________________ |
| Backup 2 | __________________ | __________________ | __________________ | __________________ | __________________ |
| Weitere | __________________ | __________________ | __________________ | __________________ | __________________ |

## 3. Schutz der Backup-Administration

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Backup-Administrationskonten sind von normalen Benutzerkonten getrennt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Privilegierte Backup-Zugänge sind von der Produktivadministration sinnvoll getrennt und mit Mehrfaktor-Authentisierung geschützt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Nur berechtigte Personen können Aufbewahrung, Löschungen oder Schutzregeln verändern. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Berechtigungen von IT-Dienstleistern, Fernwartung und Notfallzugängen sind dokumentiert und periodisch überprüft. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Administrative Änderungen und fehlgeschlagene Zugriffe sind nachvollziehbar protokolliert und werden ausgewertet. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

## 4. Isolierte und unveränderbare Kopien

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Mindestens eine relevante Sicherungskopie ist nicht dauerhaft aus dem Produktivnetz erreichbar. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Für eine kritische Kopie ist eine unveränderbare Aufbewahrung mit klarer Frist und überprüften Änderungsrechten konfiguriert. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Die Schutzdauer ist aus Erkennungs-, Wiederherstellungs- und Geschäftsanforderungen abgeleitet. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Für die unveränderbare Kopie sind Modus, Aufbewahrungsregel, Rechte zum Umgehen oder Ändern und Protokollierung dokumentiert. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Wiederherstellung aus der geschützten Kopie ist praktisch möglich, ohne sie unnötig dem kompromittierten Produktivumfeld auszusetzen. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

**Konfiguration der letzten Rückfallebene**  
Kopietyp / Plattform: _______________________________________________________  
Offline- oder Trennungsmechanismus: ________________________________________  
Unveränderbarkeitsmodus / Aufbewahrungsfrist: _______________________________  
Wer darf die Regeln ändern oder umgehen? ___________________________________  
Letzte Prüfung der Konfiguration: ___________________________________________

## 5. Wiederherstellungsziele und Reihenfolge

Der **Recovery Point Objective (RPO)** beschreibt den angestrebten Wiederherstellungspunkt und damit den tolerierten Datenverlust in Zeit. Der **Recovery Time Objective (RTO)** beschreibt die angestrebte Zeit bis zur Wiederherstellung.[3] [4]

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Für den Dienst ist ein RPO definiert: der maximal hinnehmbare Datenverlust bis zum Wiederherstellungspunkt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Für den Dienst ist ein RTO definiert: die maximal vertretbare Wiederherstellungsdauer bis zur fachlichen Nutzbarkeit. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| RPO und RTO sind vom Fachbereich bestätigt und mit der tatsächlichen Backup-Frequenz sowie Restore-Kapazität abgeglichen. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Die Wiederanlaufreihenfolge berücksichtigt technische und fachliche Abhängigkeiten. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Für den Fall, dass RPO oder RTO nicht erreicht werden, ist eine Eskalation oder Behelfslösung definiert. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

**Zielwerte und Abnahme**

| Dienst / Prozess | Priorität | RPO | RTO | Wiederanlaufreihenfolge | Fachliche Abnahme durch |
|---|---|---|---|---|---|
| __________________ | __________________ | __________________ | __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ | __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ | __________________ | __________________ | __________________ |

## 6. Restore-Test und Verbesserungen

| Kontrollpunkt | Bewertung | Nachweis / Massnahme |
|---|---|---|
| Ein Restore-Test ist geplant und umfasst ein realistisches Ransomware- oder Datenverlustszenario. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Der Test wird in einer geeigneten, kontrollierten Umgebung durchgeführt. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Der Test prüft Datenstand, Datenintegrität, technische Funktion, Benutzerzugriff und fachliche Nutzbarkeit. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Start, Ende, verwendete Sicherung, erreichte Datenaktualität und Abweichungen werden dokumentiert. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |
| Offene Punkte haben eine verantwortliche Person, einen Termin und einen Nachtest. | ☐ Ja ☐ Teilweise ☐ Nein ☐ Nicht bekannt | __________________________________ |

**Protokoll des letzten oder nächsten Restore-Tests**  
Testszenario: ______________________________________________________________  
Testdatum / Ort / Umgebung: __________________________________________________  
Verwendeter Sicherungsstand: _______________________________________________  
Teststart: __________________  Testende: __________________  
Erreichte Datenaktualität: __________________________________________________  
Technische Resultate: ______________________________________________________  
Fachliche Abnahme / Einschränkungen: ________________________________________  
Abweichung zu RPO / RTO: ___________________________________________________  
Offene Massnahmen / Eigentümer / Termin: ____________________________________

---

## Kurzfazit und Priorisierung

**Kritische Lücken, die vor dem nächsten Test oder vor einer Architekturänderung geklärt werden müssen:**

1. ________________________________________________________________________
2. ________________________________________________________________________
3. ________________________________________________________________________

**Nächste verbindliche Massnahme:** _________________________________________  
**Verantwortliche Person:** __________________  
**Termin:** __________________  
**Termin für Nachtest / Review:** ___________________________________________

## Grenzen und fachliche Prüfung

Dieses Arbeitsmittel bildet keine vollständige Sicherheits-, Datenschutz-, Vertrags- oder Risikoanalyse ab. Die passende Lösung hängt insbesondere von Schutzbedarf, Datenarten, Geschäftsprozessen, Infrastruktur, Dienstleistermodell, Wiederherstellungszielen und anwendbaren Aufbewahrungs- oder Löschpflichten ab.

**[FACHPRÜFUNG ERFORDERLICH]** Eine fachliche und bei rechtlichen Fragen fachjuristische Prüfung ist erforderlich, wenn Sie beurteilen müssen, ob Ihre konkrete Backup-Architektur, Aufbewahrungsfrist, Datenbearbeitung oder vertragliche Regelung den Anforderungen des DSG, der Datenschutzverordnung oder weiteren anwendbaren Vorgaben genügt.[5] [6] Der Selbstcheck ersetzt weder einen Restore-Test noch ein IT-Notfallkonzept. Das BACS ordnet Wiederanlauf, Verantwortlichkeiten und Nachbearbeitung in ein umfassendes Notfallkonzept ein.[7]

## Quellen

[1]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern: 3-2-1 und Wiederherstellungstest"
[2]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide: Offline-Backups, Integritätstests und Wiederherstellung"
[3]: https://csrc.nist.gov/glossary/term/recovery_point_objective "NIST CSRC Glossary – Recovery Point Objective"
[4]: https://csrc.nist.gov/glossary/term/recovery_time_objective "NIST CSRC Glossary – Recovery Time Objective"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz (DSG), Art. 8 Datensicherheit"
[6]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung (DSV), Art. 1 bis 3 Datensicherheit und Wiederherstellung"
[7]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[8]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, veröffentlicht am 6. Oktober 2026"
