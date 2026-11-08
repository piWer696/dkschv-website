---
status: Entwurf
slug: /wissen/backup-wiederherstellung-testen
meta_title: "Backup-Wiederherstellung testen: KMU-Leitfaden"
meta_description: "So testen Schweizer KMU Backups, Wiederanlauf, Rollen und Kommunikation in einem realistischen Ransomware-Szenario."
suchintention: "Informational – Backup-Wiederherstellung und Restore-Tests planen"
hauptkeyword: "Wiederherstellungstest Backup"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "12.11.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "9 zitierte externe Originalquellen, darunter Fedlex zusätzlich über amtliche Chronologie, Änderungen und XML; ergänzend BACS Im Fokus, BACS-KMU-Studie, CISA SafePay und CISA-Ressourceneintrag geprüft. Abrufe am 01.11.2026, 09:05–09:09 CET Europe/Zurich. Interne bzw. geplante DKSchV-URLs wurden nicht live geprüft."
quellenpruefung_status: "vollständig für die 9 zitierten externen Originalquellen; kein Nachweis eines minutengenauen historischen Website-Wortlauts und keine Fach-, Rechts- oder Veröffentlichungsfreigabe"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Ransomware-Wiederherstellung testen: Leitfaden für Schweizer KMU mit IT-Notfallplan

*Quellenstand: 1. November 2026. Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Veröffentlichungsfreigabe.*

> **[FACHPRÜFUNG ERFORDERLICH]** Die technischen Wiederanlaufannahmen sowie die rechtlichen Hinweise zu einem tatsächlichen Vorfall müssen vor Veröffentlichung durch zuständige Fachpersonen geprüft werden.

**Kurzantwort:** Ein Wiederherstellungstest zeigt nicht bloss, ob sich einzelne Dateien zurückspielen lassen. Er zeigt, ob Ihr Unternehmen nach einem Ransomware-Vorfall einen kritischen Geschäftsprozess mit sauberen Systemen, nutzbaren Daten, klaren Rollen und innerhalb der vereinbarten Zeit wieder aufnehmen kann. Beginnen Sie deshalb bei den Geschäftsprozessen und deren Abhängigkeiten. Legen Sie für jeden kritischen Prozess ein **RTO** (zulässige Wiederanlaufzeit) und ein **RPO** (vertretbarer Datenverlust in Zeit) fest. Üben Sie anschliessend ein abgegrenztes, realitätsnahes Szenario in einer isolierten Umgebung, messen Sie Soll gegen Ist und behandeln Sie Abweichungen als konkrete Verbesserungsaufträge. Ein Debriefing und ein Nachtest schliessen den Kreislauf.

Ein Backup ist erst dann ein belastbarer Teil der Cyberresilienz, wenn seine Wiederherstellung unter realistischen Bedingungen funktioniert. Das Bundesamt für Cybersicherheit (BACS) ordnet das Notfallkonzept in die vier Phasen Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung ein. Für Schweizer KMU steht seit dem 18. Mai 2026 zudem eine angepasste Vorlage für einen IT-Notfall- und Krisenplan bereit.[1] Ein Restore-Test macht diese Phasen für den Wiederanlauf überprüfbar.

Der Test ist kein Nachweis dafür, dass jeder künftige Angriff folgenlos bleibt. Er beantwortet eine engere, aber geschäftskritische Frage: **Können Sie einen fest definierten Prozess nach einem angenommenen Ransomware-Ereignis mit der vorgesehenen Qualität und in der vereinbarten Zeit wieder betreiben?**

## Der Startpunkt sind Geschäftsprozesse, nicht Sicherungsjobs

Viele Unternehmen wissen, dass ihre Sicherung über Nacht gelaufen ist. Weniger klar ist oft, welche Kombination aus Anwendung, Identität, Netzwerk, Schnittstelle, Lieferant und Daten ein Prozess tatsächlich braucht. Genau dort beginnt die Vorbereitung.

Erstellen Sie mit den Prozessverantwortlichen eine kurze Liste der geschäftskritischen Abläufe. Das können beispielsweise Auftragsannahme, Produktion, Leistungserbringung, Versand, Fakturierung oder Lohnlauf sein. Beschreiben Sie bei jedem Ablauf nicht nur die führende Anwendung. Halten Sie auch fest, welche Vorbedingungen erforderlich sind: Benutzerkonten und Mehrfaktor-Authentisierung, Namensauflösung, Netzwerkzugang, Datenbank, Dateifreigaben, Druck, externe Schnittstellen, Cloud-Mandanten, Lizenzserver und die erreichbaren Ansprechpartner von Dienstleistern.

Diese Sicht verhindert einen typischen Irrtum: Ein Server kann technisch wieder laufen, während der Geschäftsprozess wegen einer fehlenden Identität, einer nicht erreichbaren Schnittstelle oder einer nicht geprüften Datenbasis trotzdem stillsteht. CISA empfiehlt ebenfalls, kritische Systeme nach ihrer Bedeutung für Sicherheit, Umsatz oder andere kritische Leistungen sowie nach ihren Abhängigkeiten zu erfassen; diese Übersicht dient der Wiederherstellungspriorisierung.[3]

Verankern Sie die Arbeit in Ihrem [Risikomanagement](/unsere-dienstleistungen/risikomanagement). Die Geschäftsleitung entscheidet, welche Unterbrüche und Datenverluste tragbar sind. Die IT übersetzt diesen Entscheid in Wiederherstellungsreihenfolge, Sicherungsarchitektur, Kapazität und Testumfang. Eine [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) kann dabei Schwachstellen sichtbar machen, etwa gemeinsam genutzte Administrationskonten oder eine ungetrennte Backup-Verwaltung.

### RTO und RPO so festlegen, dass sie testbar sind

Das **Recovery Time Objective (RTO)** bezeichnet die für einen Prozess maximal akzeptierte Zeit bis zur Wiederaufnahme der vorher festgelegten Betriebsfähigkeit. Das **Recovery Point Objective (RPO)** beschreibt, wie viel Datenverlust, als Zeitspanne gemessen, akzeptiert wird. Diese Ziele gehören in eine Business-Impact-Analyse und in den Wiederanlaufplan; NIST behandelt sie als Planungswerte für Wiederherstellungsanforderungen und -prioritäten.[4]

Formulieren Sie Ziele präzise. «Das ERP rasch wiederherstellen» ist kein Ziel. Besser ist: «Auftragsannahme kann innerhalb von acht Stunden auf einer sauberen Umgebung verarbeitet werden; die verwendeten Auftragsdaten dürfen höchstens vier Stunden älter sein als der dokumentierte Ereigniszeitpunkt.» Die acht und vier Stunden sind hier **nur ein Beispiel**. Ihre Werte müssen aus Verträgen, gesetzlichen Aufbewahrungspflichten, Lieferfähigkeit, Liquidität, Sicherheit und der tatsächlichen Wiederanlauffähigkeit abgeleitet werden.

| Prüfgegenstand | Für den Test verbindlich festlegen |
|---|---|
| Geschäftsprozess | Prozessverantwortliche Person, Mindestfunktion und zulässige Behelfsabläufe |
| RTO | Start- und Endzeitpunkt der Messung sowie die zulässige Dauer |
| RPO | Referenzzeitpunkt des Datenstands und maximal zulässige Datenlücke |
| Abhängigkeiten | Systeme, Konten, Daten, Schnittstellen, Lieferanten und Freigaben |
| Abnahmekriterium | Fachliche Transaktion, Datenprüfung und verantwortliche Abnahme |

RTO und RPO sind Managemententscheide, keine technischen Wunschwerte. Ist ein Ziel mit der heutigen Architektur nicht erreichbar, dokumentieren Sie die Differenz als Risiko und entscheiden Sie über Massnahme, Behelfsprozess oder akzeptiertes Restrisiko.

## Ein sicheres Testszenario für Ransomware definieren

Ein guter Test muss nicht mit echter Schadsoftware arbeiten. Verwenden Sie **niemals** Ransomware oder produktive Verschlüsselung, um einen Restore-Test zu «realistisch» zu machen. Simulieren Sie stattdessen die Lage: Eine kritische Anwendung und die zugehörige Dateifreigabe gelten als kompromittiert und sind nicht verfügbar. Der Testauftrag lautet, den priorisierten Prozess aus einem definierten Sicherungsstand auf einer getrennten, kontrollierten Umgebung wiederherzustellen.

Das Szenario sollte einen konkreten Auslöser, einen Zeitpunkt und klare Annahmen enthalten. Beispiel: «Um 08.30 Uhr wird eine Verschlüsselung auf der Auftragsdatenablage festgestellt. Der betreffende Anwendungsserver gilt als nicht vertrauenswürdig. Die Produktivumgebung wird nicht für die Wiederherstellung verwendet. Das Team muss die Auftragsannahme auf einer sauberen Wiederanlaufumgebung wieder ermöglichen.» Ergänzen Sie, ob der externe IT-Partner nur über seinen normalen Kontaktweg erreichbar ist oder ob ein Ausfall des Fernzugriffs angenommen wird. So testen Sie auch die praktische Handlungsfähigkeit.

CISA empfiehlt, verfügbare und integre Backups regelmässig in einem Disaster-Recovery-Szenario zu testen, kritische Dienste zu priorisieren und Offline-Kopien zu schützen. Die Behörde weist auch darauf hin, dass Ransomware zugängliche Backups löschen oder verschlüsseln kann.[3] Beziehen Sie deshalb in den Test ein, ob der Zugriff auf Sicherungen und auf vertrauenswürdige Systemvorlagen funktioniert, ohne die angenommene kompromittierte Umgebung zu verwenden.

Ein vereinfachtes **hypothetisches Praxisbeispiel**: Ein Handelsunternehmen priorisiert die Auftragsannahme vor der späteren Auswertung von Berichten. Im Test werden die Netzwerkbasis, die für den Prozess erforderlichen Identitäten, die Auftragsanwendung und ein geprüfter Datenstand in einer separaten Umgebung bereitgestellt. Die Prozessverantwortliche erfasst einen Testauftrag, prüft den Bestand und löst eine Auftragsbestätigung aus. Erst nach dieser fachlichen Prüfung gilt der Prozess als wiederhergestellt. Der erfolgreiche Start einer virtuellen Maschine genügt nicht.

## Rollen, Stellvertretungen und Offline-Unterlagen vor dem Test festlegen

Ein Test scheitert häufig nicht am Backup, sondern an unklarer Entscheidungskompetenz. Das BACS nennt klar zugeordnete Verantwortlichkeiten, die Koordination durch Notfallorganisation oder Krisenstab sowie interne und externe Kommunikation als zentrale Elemente der Vorfallsbewältigung.[1]

| Rolle | Aufgabe im Restore-Test | Stellvertretung und Nachweis |
|---|---|---|
| Testleitung | aktiviert das Szenario, führt Lagebild und stoppt bei Sicherheitsrisiko | Name, Mobilnummer, Entscheidungsprotokoll |
| Wiederanlaufleitung | steuert technische Reihenfolge, Zeiten und Übergaben | Name, Zugriff auf Runbooks und Systemvorlagen |
| Systemverantwortung | stellt das zugewiesene System sauber wieder her | Wiederherstellungsprotokoll, Konfigurationsnachweis |
| Prozessverantwortung | definiert Mindestfunktion und nimmt fachlich ab | dokumentierter Testfall und Abnahme |
| Sicherheits- bzw. Forensikkoordination | beurteilt die Trennung, Beweissicherung und Freigabe zur Rückkehr | Freigabeentscheidung, offene Befunde |
| Lieferantenkoordination | aktiviert Provider nach vereinbartem Weg und dokumentiert Reaktionsschritte | Kontaktliste, Ticket- oder Gesprächsnotiz |
| Protokollführung | erfasst Zeiten, Entscheidungen, Abweichungen und Aufgaben | vollständiges Testprotokoll |

Bewahren Sie Kontaktlisten, Rollenübersicht, Wiederanlaufreihenfolge und die nötigen Freigabewege auch offline oder über einen vom Test betroffenen Mandanten unabhängigen Zugang auf. CISA empfiehlt eine Hardcopy und eine Offline-Version des Incident-Response- und Kommunikationsplans.[3] Ergänzen Sie für jedes externe Produkt oder jeden Provider die Informationen, die im Ernstfall tatsächlich gebraucht werden: Vertrags- oder Kundennummer, Eskalationsweg, technische Zuständigkeit sowie Zugang zu Lizenzen und Installationsmedien.

## Der saubere Wiederanlauf: erst vertrauen schaffen, dann Daten freigeben

Bei einem echten Ransomware-Fall sind Wiederherstellung und Bereinigung nicht dasselbe. Das BACS empfiehlt, den Infektionsweg zu suchen, Neuinfektionen zu verhindern, betroffene Systeme neu aufzusetzen und erst danach Daten aus vorhandenen Backups wiederherzustellen. Vor Reparaturversuchen oder Neustarts können forensische Sicherungen von Zwischenspeicher und Festplatten wichtig sein; dies ist frühzeitig mit Fachpersonen und gegebenenfalls Strafverfolgungsbehörden abzustimmen.[2]

Die BACS-Meldung vom 6. Oktober 2026 präzisiert den Umgang mit Malware-Verdacht: Ein einzelnes Anzeichen beweist keine Infektion; mehrere ungewöhnliche Beobachtungen begründen aber eine genauere Untersuchung. Bei einer bestätigten Infektion empfiehlt das BACS, das System neu aufzusetzen und anschliessend die Passwörter zu ändern.[8] Ein Restore-Test ersetzt diese Untersuchung in einem echten Vorfall nicht.

Für den Test leiten Sie daraus eine kontrollierte Reihenfolge ab:

1. **Testlage bestätigen und Grenze ziehen.** Halten Sie Startzeit, angenommenen Schadensumfang, zulässige Testsysteme und Abbruchkriterien fest. Der Test darf keine Produktion gefährden.
2. **Wiederanlaufumgebung vorbereiten.** Prüfen Sie Segmentierung, Administrationszugänge, vertrauenswürdige Installationsquellen und aktuelle Konfigurationen. Die Testumgebung muss vom angenommen kompromittierten Bereich getrennt bleiben.
3. **Grundlagen in Abhängigkeitsreihenfolge herstellen.** Stellen Sie nur die Identitäts-, Netzwerk- und Plattformkomponenten bereit, die der priorisierte Prozess braucht. Jede Komponente erhält eine Sicherheits- und Funktionsprüfung.
4. **Anwendung und Daten wiederherstellen.** Wählen Sie den Sicherungsstand anhand des vereinbarten RPO. Notieren Sie den tatsächlichen Datenstand und jede Lücke gegenüber dem Sollwert.
5. **Fachlich validieren.** Die Prozessverantwortung führt vorab definierte Testfälle aus: anmelden, eine zulässige Transaktion erfassen, Daten wiederfinden, eine Schnittstelle oder Ausgabe prüfen und den Behelfsprozess beenden. Dokumentieren Sie Resultat und Einschränkungen.
6. **Kontrolliert in den Betrieb überführen.** Definieren Sie eine ausdrückliche Freigabe, Überwachung nach dem Start und einen Rückfallweg. In einem realen Vorfall darf nur eine bereinigte Umgebung wieder verbunden werden; CISA warnt vor einer erneuten Infektion sauberer Systeme während der Wiederherstellung.[3]

### Komponenten- und Patchnachweise vom Vorfallsbefund trennen

Dokumentieren Sie für die Komponenten, die in der Wiederanlaufumgebung tatsächlich verwendet werden, getrennt vom fachlichen Test die vertrauenswürdige Systemvorlage, Produkt- oder Paketversion, Konfigurationsstand, zuständige Betreiberin oder zuständigen Betreiber und den vorliegenden Fixnachweis. Die BACS-Warnung vom 21. Oktober 2026 empfiehlt dies für PHP ausdrücklich auch bei integrierten Komponenten, Anwendungen, Containern, Appliances und extern betriebenen Angeboten: Massgebend sind die tatsächlich laufende korrigierte Version oder das vom Anbieter als behoben bestätigte Paket, nicht bloss eine Hauptversionsnummer.[9] Für einen Restore-Test ist dieser Nachweis ein prüfbarer Bestandteil der sauberen Wiederanlaufumgebung; er ist kein künstlicher wöchentlicher CVE-Check und kein Nachweis, dass die Produktionsumgebung zuvor nicht kompromittiert war.

Ein eingespieltes Update beseitigt laut BACS keine bereits erfolgte Kompromittierung.[9] Halten Sie deshalb die im Test verwendeten Komponenten- und Patchnachweise von der Untersuchung eines früheren Daten- oder Kontenkompromisses getrennt. Umfang, Zeitpunkt und Folgen eines Verdachts auf unbefugten Zugriff ergeben sich nicht aus einem erfolgreichen Restore-Test. Sie verlangen bei einem echten Vorfall eine gesonderte, fachlich gesteuerte Behandlung von Beweisen, Logs und betroffenen Systemen. Der Test ersetzt keine Forensik und trifft weder einen Befund noch eine Freigabe dazu.

Die Wiederanlaufreihenfolge gehört in den IT-Notfallplan, nicht nur in das Wissen einzelner Administratoren. Für die technische Vorsorge und die Trennung von Sicherungszugängen ist auch der Beitrag [Ransomware-resistente Backups](/wissen/ransomware-resistente-backups) eine sinnvolle Ergänzung. Was in der Akutphase vor dem Wiederanlauf zu tun ist, behandelt [Ransomware im KMU: Die ersten 60 Minuten](/wissen/ransomware-erste-60-minuten).

## Zeit, Datenstand und Qualität messen

Starten und stoppen Sie die Messung nicht erst bei der technischen Wiederherstellung. Messen Sie ab dem im Szenario definierten Alarmzeitpunkt bis zur fachlichen Abnahme der Mindestfunktion. Erfassen Sie zusätzlich Teilzeiten: Entscheid zur Aktivierung, Bereitstellung der sauberen Umgebung, Wiederherstellung von Anwendung und Daten, Fachtest und Freigabe.

Vergleichen Sie beim RPO den Zeitstempel des wiederhergestellten Datenstands mit dem im Szenario vereinbarten Referenzzeitpunkt. Prüfen Sie die Daten nicht nur auf Lesbarkeit. Stimmen Kernobjekte, Berechtigungen, Transaktionen, Anhänge, Schnittstellen und das Ergebnis des Fachtests? Eine Prüfsumme kann Datenintegrität unterstützen, ersetzt aber keine fachliche Prüfung des Prozesses.

Das beigefügte [Restore-Testprotokoll](/resources/07-restore-testprotokoll) hält Zielsysteme, Soll- und Istzeiten, Datenstand, Befunde, Verantwortlichkeiten und den Nachtesttermin strukturiert fest. Nutzen Sie es auch dann, wenn ein Test früh abgebrochen wird: Gerade der Abbruch ist eine wichtige Erkenntnis.

## Debriefing und Nachtest machen aus dem Test eine Verbesserung

Beenden Sie den Test mit einem zeitnahen Debriefing. Das BACS sieht in der Nachbearbeitung die Analyse von Vorfall und Bewältigung vor; ein strukturiertes Debriefing soll die Planung laufend verbessern.[1] Trennen Sie dabei Beobachtung und Schuldzuweisung. Fragen Sie: Was hat den Wiederanlauf verzögert? Welche Annahme war falsch? Welche Information, Berechtigung, Abhängigkeit oder Entscheidung fehlte? Was hat besonders gut funktioniert?

Ordnen Sie jeden Befund einer verantwortlichen Person, einer Priorität und einem Termin zu. Beispiele sind eine fehlende Offline-Kontaktliste, ein unklarer Freigabepunkt, eine nicht erreichbare Sicherung, fehlende Kapazität oder ein Datenvalidierungsschritt ohne fachliche Abnahme. Aktualisieren Sie danach den Notfallplan, die Systemdokumentation, die Rollenvertretungen und die Wiederanlauf-Runbooks. Planen Sie einen **Nachtest**, der genau die kritische Abweichung erneut prüft. Ein behobener Befund ist erst nach diesem Nachweis geschlossen.

Legen Sie einen risikobasierten Testtakt fest und planen Sie nach wesentlichen Änderungen an Prozess, Anwendung, Backup, Identitätsplattform oder Lieferant einen gezielten zusätzlichen Test. Der Takt ist eine organisationsspezifische Entscheidung und keine Zusage zur Wiederherstellbarkeit. NIST beschreibt Tests und Übungen als Teil der Pflege eines Notfallplans und der Validierung von Wiederherstellungsanforderungen.[4]

## Typische Fehler, die der Test aufdecken soll

**«Der Backup-Job war erfolgreich, also sind wir vorbereitet.»** Ein erfolgreicher Job belegt weder die Verfügbarkeit von Zugangsdaten und Kapazität noch die fachliche Nutzbarkeit der Daten. Testen Sie daher die ganze Kette.

**«Wir testen nur die IT.»** Ohne Prozessverantwortung bleibt offen, ob der Betrieb tatsächlich weiterarbeiten kann. Die Abnahme gehört dem Fachbereich, nicht nur der IT.

**«Wir stellen direkt in die Produktion zurück.»** Ein kontrollierter Test braucht eine klare Abgrenzung. In einem echten Vorfall erhöht ein voreiliger Anschluss zudem das Risiko, bereinigte Systeme erneut zu kompromittieren.[2] [3]

**«Unser Dienstleister kennt den Plan.»** Dienstleisterwissen ersetzt keine dokumentierten Rollen, Zugriffswege, Prioritäten und Stellvertretungen. Testen Sie die vorgesehenen Kontakt- und Eskalationswege.

**«Der Test ist bestanden, sobald alles wieder hochgefahren ist.»** Ein Dienst ist erst für den Geschäftsprozess verfügbar, wenn die vereinbarte Mindestfunktion fachlich geprüft und freigegeben ist.

## Melde- und Datenschutzfragen vom technischen Test trennen

Ein geplanter Test ersetzt weder die Behandlung eines echten Vorfalls noch die rechtliche Beurteilung seiner Meldepflichten. Betreiberinnen und Betreiber kritischer Infrastrukturen müssen Cyberangriffe seit dem 1. April 2025 innerhalb von 24 Stunden nach Entdeckung dem BACS melden; fehlende Angaben der Erstmeldung sind innerhalb von 14 Tagen zu ergänzen.[5] Für andere Unternehmen kann eine Meldung freiwillig sinnvoll sein, die gesetzliche Pflicht ist jedoch anhand des konkreten Geltungsbereichs zu prüfen.

Bei einer Verletzung der Datensicherheit meldet der Verantwortliche dem EDÖB nach Art. 24 DSG so rasch als möglich, wenn voraussichtlich ein hohes Risiko für Persönlichkeit oder Grundrechte betroffener Personen besteht. Die Meldung muss mindestens Art der Verletzung, Folgen sowie ergriffene oder vorgesehene Massnahmen enthalten.[6] Der EDÖB erläutert die Begriffe Datensicherheitsverletzung und «voraussichtlich hohes Risiko» in seinem Leitfaden.[7]

**[FACHPRÜFUNG ERFORDERLICH]** Diese Hinweise sind keine individuelle Rechtsberatung. Wenn ein Test Hinweise auf einen tatsächlichen Datenabfluss, eine unbefugte Offenlegung oder eine reale Kompromittierung ergibt, müssen Melde- und Informationspflichten anhand der konkreten Tatsachen durch Datenschutz- und Rechtsfachpersonen geprüft werden. Die Dokumentation kann die Sachverhaltsklärung unterstützen, ersetzt diese Prüfung aber nicht.

> Für eine organisationsspezifische Einordnung Ihres Wiederherstellungstests können Sie [DKSchV kontaktieren](/kontakt). Eine Kontaktaufnahme ersetzt keine technische, rechtliche oder forensische Fachprüfung.

## Quellen

[1]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[2]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[3]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide"
[4]: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final "NIST SP 800-34 Rev. 1 – Contingency Planning Guide for Federal Information Systems"
[5]: https://www.bacs.admin.ch/de/meldepflicht "BACS – Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[6]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Art. 24"
[7]: https://www.edoeb.admin.ch/de/leitfaden-data-breach "EDÖB – Leitfaden DataBreach"
[8]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[9]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
