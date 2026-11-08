---
status: Entwurf
slug: /wissen/it-sicherheitscheck-kmu
meta_title: "IT-Sicherheitscheck und Risikoregister für KMU | DKSchV"
meta_description: "So werden technische Befunde zu nachvollziehbaren Cyberrisiken, Prioritäten, Verantwortlichkeiten und Massnahmen für die Geschäftsleitung."
suchintention: "Informational – technische Befunde in ein Cyber-Risikoregister überführen"
hauptkeyword: "IT-Sicherheitscheck KMU"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "19.11.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle 13 Quellenreferenzen dieses Artikels (12 eindeutige Original-URLs) und alle 8 Quellenreferenzen des zugehörigen Arbeitsmittels direkt geprüft; zusätzlich Fedlex-Chronologien und amtliche XML-Fassungen sowie einschlägige BACS- und CISA-Originalmeldungen bis 27. Oktober 2026 abgeglichen."
quellenpruefung_status: "Vollständig für alle externen Quellenreferenzen und die dokumentierten einschlägigen Originalmeldungen; interne relative Paketlinks erhalten, nicht als künftige Live-URLs geprüft."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# IT-Sicherheitscheck für Schweizer KMU: So wird aus Befunden ein priorisiertes Cyber-Risikoregister

**Stand:** 1. November 2026 (Quellenprüfung; keine Fach- oder Rechtsfreigabe)

> **[FACHPRÜFUNG ERFORDERLICH]** Die datenschutzrechtliche Einordnung, sektorale Vorgaben und die organisationsspezifische Risikotoleranz müssen vor Veröffentlichung durch zuständige Fachpersonen geprüft werden.

**Kurzantwort:** Ein IT-Sicherheitscheck wird erst für die Geschäftsleitung steuerbar, wenn jeder technische Befund in ein konkretes Geschäftsszenario übersetzt wird: Was könnte passieren, welcher Prozess oder welche Daten wären betroffen, wie gross wäre die Auswirkung und welche bereits vorhandenen Kontrollen begrenzen das Risiko? Halten Sie das Ergebnis in einem Risikoregister fest. Priorisieren Sie nicht nach der Länge einer Befundliste, sondern nach dem verbleibenden Risiko für Geschäft, Kunden und Verpflichtungen. Jeder Eintrag braucht eine verantwortliche Person, eine überprüfbare Massnahme, einen Termin und eine bewusste Entscheidung zum Restrisiko. So wird aus einem einmaligen Check ein Führungsinstrument für Sicherheitsmassnahmen und Notfallplanung.

Ein Scan kann fehlende Updates, offene Dienste oder zu weit gehende Berechtigungen aufzeigen. Er beantwortet jedoch nicht, ob deshalb die Auftragsabwicklung stillsteht, Personendaten betroffen sind oder ein wichtiger Lieferant ausfällt. Diese Entscheidung verlangt den Blick auf den Geschäftsprozess. Das Bundesamt für Cybersicherheit (BACS) beginnt seine Cybersicherheits- und Resilienzmethode folgerichtig bei wichtigen Tätigkeiten und Geschäftsprozessen, bevor es Informatikmittel und deren Schutzbedarf bestimmt.[1]

## Warum ein automatischer Scan nicht genügt

Ein **technischer Befund** ist eine festgestellte Abweichung oder Schwachstelle. Beispiele sind ein nicht unterstütztes Betriebssystem, ein Administratorkonto ohne Mehrfaktor-Authentisierung oder eine Sicherung, deren Wiederherstellung nicht nachgewiesen ist. Der Befund ist wichtig, aber er ist noch kein Risikoentscheid.

Ein **Cyber-Risikoszenario** beschreibt dagegen Ursache, mögliches Ereignis und geschäftliche Folge in einem Satz. Statt «MFA fehlt» lautet es beispielsweise: «Wenn ein Angreifer die Zugangsdaten eines Mitarbeiters erlangt und das E-Mail-Konto ohne Mehrfaktor-Authentisierung übernehmen kann, könnten betrügerische Zahlungsanweisungen oder vertrauliche Kommunikation versendet werden; betroffen wären Zahlungsfreigaben, Kundenvertrauen und allenfalls Personendaten.»

> **Arbeitsdefinition:** Ein Cyberrisiko ist die Möglichkeit, dass eine Bedrohung eine Schwachstelle oder Abhängigkeit ausnutzt und dadurch ein geschäftlich relevanter Schaden entsteht. Das Risikoregister hält diese Szenarien, ihre Bewertung und ihren Umgang nachvollziehbar fest.

Diese Übersetzung verhindert zwei gegensätzliche Fehler. Erstens wird eine lange Liste technischer Hinweise nicht automatisch zur Prioritätenliste. Zweitens bleibt ein kritisch wirkendes Einzelsignal nicht unbemerkt, nur weil es technisch schwer verständlich ist. NIST beschreibt Risikobewertung als systematische Grundlage, damit Entscheidungsträger Risiken laufend beurteilen, priorisieren und eine angemessene Behandlung wählen können.[2]

Ein Risikoregister ersetzt keinen Schwachstellenscan, keine Penetrationstests und kein Inventar. Es verbindet deren Ergebnisse mit Entscheidungen. Im NIST Cybersecurity Framework (CSF) 2.0 sind Geschäftskontext, Rollen, Risiko-Management-Strategie und Aufsicht deshalb Teil der Funktion «Govern»; die übrigen Sicherheitsaktivitäten werden daran ausgerichtet.[3]

## Zuerst den Geschäftskontext erfassen

Beginnen Sie nicht mit der vollständigen Liste aller Geräte. Erfassen Sie zuerst die wenigen Prozesse, deren Ausfall oder Manipulation die Organisation spürbar treffen würde. Das können Auftragsannahme, Produktion, Lohnlauf, Zahlungsfreigabe, Kundenportal, Serviceeinsatz oder die Kommunikation mit Kunden sein. Fragen Sie für jeden Prozess: Welche Anwendungen, Daten, Konten, Schnittstellen, Personen und Dienstleister werden dafür zwingend benötigt?

Ordnen Sie jedem wichtigen Objekt einen **fachlichen Eigentümer** zu. Das ist die Person, welche die geschäftliche Bedeutung, tolerierbare Unterbrüche und Folgen eines Ausfalls beurteilen kann. Der technische Betrieb bleibt bei IT oder einem Provider, doch die Fachseite entscheidet nicht allein über technische Lösungen. Sie beschreibt, welche Folge akzeptabel ist und welche nicht.

Das BACS empfiehlt in seiner Methode, Prozesse zu analysieren, zugehörige Informatikmittel zu Schutzobjekten zusammenzufassen und deren Schutzbedarf zu bestimmen. Es lässt ausdrücklich ein prioritätsgesteuertes, iteratives Vorgehen zu, wenn zunächst die wichtigsten Prozesse und Schutzobjekte behandelt werden.[1] Für ein KMU ist das ein praktikabler Einstieg: Kritische Abhängigkeiten werden sichtbar, ohne dass die Arbeit auf ein perfektes Inventar warten muss.

Berücksichtigen Sie dabei auch externe Abhängigkeiten. Ein Cloud-Dienst, eine Fernwartung, eine Zahlungsplattform oder ein Softwarepartner kann für den Geschäftsprozess genauso kritisch sein wie ein eigener Server. Halten Sie fest, wer administrativen Zugriff hat, welche Daten betroffen sind, ob es Alternativen gibt und wie ein Ausfall gemeldet wird.

Berücksichtigen Sie bei Sicherheitswarnungen auch Komponenten, die in Produkten oder Diensten eingebettet sind. Eine Laufzeitumgebung wie PHP kann beispielsweise Teil einer Verwaltungsoberfläche, Fachanwendung, Hosting-Plattform, eines Containers oder einer Appliance sein, ohne dass sie im üblichen Inventar sichtbar ist. Erfassen Sie deshalb Produkt, Komponente, tatsächlich laufenden Stand, Erreichbarkeit und zuständigen Betreiber. Bei extern betriebenen Lösungen braucht es eine auf die konkrete Instanz bezogene Fixbestätigung des Herstellers, Hosters oder Dienstleisters sowie einen überprüfbaren Nachweis des tatsächlich behobenen Stands. Eine angezeigte Hauptversion allein kann bei zurückportierten Sicherheitskorrekturen unzureichend sein.[10]

Wenn ein Geschäftsprozess einen KI-Dienst nutzt, kann auch dessen Verbrauch ein Risikoszenario sein. Halten Sie den Anbieter, die für den Prozess verfügbare Kapazität oder Quote, Budget- und Warnschwellen, verantwortliche Personen sowie einen manuellen oder anderen Ausweichablauf fest. Unkontrollierter Verbrauch kann Kosten, Leistung und Verfügbarkeit beeinträchtigen; die CISA verweist hierzu auf Orientierung für die Priorisierung kritischer Funktionen, Monitoring und Planung bei eingeschränkter Dienstverfügbarkeit.[11] [12] Ob und in welcher Form solche Schwellen angemessen sind, hängt vom konkreten Dienst, Vertrag, Prozess und Risiko der Organisation ab.

Für einen eingesetzten KI-Agenten genügt es nicht, nur das Modell zu erfassen. Dokumentieren Sie den vorgesehenen Auftrag, die zugehörige Identität, angebundene Daten und Werkzeuge, erlaubte Netzwerkverbindungen sowie mögliche externe Wirkungen. Legen Sie für folgenschwere oder schwer rückgängig zu machende Handlungen menschliche Freigabepunkte, Protokollierung und einen eng begrenzten Berechtigungsumfang fest. Die kanadische Behördenorientierung empfiehlt eigenständige Agentenidentitäten, auf die genehmigte Aufgabe beschränkte Rechte und menschliche Kontrolle bei Handlungen mit hohem Schadenspotenzial.[13] Das sind mögliche risikobasierte Prüfpunkte, keine Aussage über einen konkreten Agenten, eine Schwachstelle oder einen Patchstand.

## Den Befund in ein belastbares Szenario übersetzen

Verwenden Sie pro Risiko einen klaren Satz nach diesem Muster:

**Wenn** eine bestimmte Bedrohung eine konkrete Schwachstelle oder Abhängigkeit ausnutzt, **dann** passiert ein nachvollziehbares Ereignis, **wodurch** ein benannter Geschäftsprozess, Datenbestand oder Verpflichtung beeinträchtigt wird.

Ein Szenario darf mehrere zusammenhängende Befunde zusammenführen, wenn sie dieselbe Ursache oder Folge haben. Mehrere fehlende Sicherheitsupdates auf vergleichbaren öffentlich erreichbaren Systemen können etwa ein Patch-Management-Risiko bilden. Verschiedene Befunde mit unterschiedlichen Geschäftsfolgen gehören dagegen getrennt: Ein nicht gesicherter Lager-PC und ein ungeschütztes Finanzkonto sind nicht dasselbe Risiko.

Dokumentieren Sie neben dem Szenario die **Evidenz**. Das kann die Befund-ID des Checks, ein Konfigurationsauszug, eine Testbeobachtung oder die Rückmeldung eines Systemeigentümers sein. Evidenz macht später überprüfbar, ob die Massnahme die Ursache wirklich adressiert hat. Vermeiden Sie Formulierungen wie «System unsicher» oder «Sicherheit verbessern». Sie benennen weder den Auslöser noch die Entscheidung.

Bei Verdacht auf Schadsoftware trennen Sie ein Anzeichen von einem bestätigten Befund: Ein einzelnes Anzeichen ist noch kein Infektionsbeweis. Mehrere ungewöhnliche Beobachtungen sollten dagegen genauer untersucht werden. Das BACS empfiehlt bei Verdacht die Untersuchung durch eine Fachperson sowie bei geschäftlich genutzten Geräten die Information der zuständigen IT-Stelle.[9] Halten Sie im Register deshalb fest, ob ein Befund nur vermutet, untersucht oder bestätigt ist.

### Hypothetisches Praxisbeispiel: Vom Patch-Befund zur Geschäftsentscheidung

Das folgende Beispiel ist hypothetisch und beschreibt keinen DKSchV-Kunden. Ein Sicherheitscheck stellt fest, dass eine internetzugängliche Anwendung nicht innerhalb des festgelegten Prozesses aktualisiert wird. Die IT nennt als Ursache eine unklare Zuständigkeit zwischen internem Team und Provider.

Der Registereintrag lautet nicht lediglich «Update fehlt». Er beschreibt: «Wenn eine bekannte Schwachstelle in der extern erreichbaren Kundenanwendung ausgenutzt wird, könnten Angreifer die Anwendung beeinträchtigen oder auf verarbeitete Kundendaten zugreifen. Die Auftragsannahme wäre gestört; abhängig von den betroffenen Daten könnte eine Datensicherheitsverletzung zu beurteilen sein.» Als bestehende Kontrollen sind etwa Überwachung, eingeschränkte Administrationszugriffe und Sicherungen festzuhalten, aber nur soweit sie tatsächlich nachweisbar vorhanden sind.

Die Massnahme könnte lauten: «Providervertrag und Betriebsprozess so ergänzen, dass Verantwortlichkeit, Frist, Nachweis und Eskalation für sicherheitsrelevante Updates festgelegt sind; anschliessend den Nachweis an einer Anwendung prüfen.» Eigentümer der Massnahme ist beispielsweise der IT-Verantwortliche. Der Prozesseigentümer bestätigt, ob ein Wartungsfenster möglich ist. Nach Umsetzung bewertet das zuständige Gremium das **Restrisiko** neu: also das Risiko, das trotz umgesetzter Kontrollen verbleibt. Der Eintrag bleibt offen, bis Evidenz und Bewertung aktualisiert sind.

## Wirkung, Eintrittswahrscheinlichkeit und bestehende Kontrollen bewerten

Bewerten Sie Risiko nicht mit Scheingenauigkeit. Eine einheitliche, beschriebene Skala ist für viele KMU nützlicher als eine angeblich exakte Geldzahl. Legen Sie vor der ersten Bewertung fest, was die Stufen für **Auswirkung** und **Eintrittswahrscheinlichkeit** bedeuten. Die Auswirkung kann sich auf Unterbruch kritischer Prozesse, Integrität von Daten, Vertraulichkeit, vertragliche Folgen, Wiederherstellungsaufwand und Vertrauensverlust beziehen. Die Wahrscheinlichkeit beurteilt die plausible Ausnutzbarkeit im eigenen Umfeld, nicht bloss die Existenz einer Schwachstelle.

Bewerten Sie immer mit Blick auf die bestehenden Kontrollen. Eine Kontrolle ist nur dann anzurechnen, wenn sie konkret beschrieben, zugewiesen und soweit sinnvoll überprüft ist. «Wir haben ein Backup» ist keine ausreichende Aussage. Relevant ist beispielsweise, ob der Zugriff getrennt ist, ob die Wiederherstellung getestet wurde und ob die Sicherung die tatsächlich benötigten Daten und Systeme abdeckt. Für kleine und mittlere Organisationen empfiehlt NIST ausdrücklich, Risiken, Bedrohungen, Schwachstellen und Anforderungen festzuhalten und interne sowie externe Bedrohungen mit zugehörigen Reaktionen in einem Risikoregister zu dokumentieren.[4]

Bei Personendaten kommt eine zusätzliche Perspektive hinzu. Das Schweizer Datenschutzgesetz verlangt vom Verantwortlichen und vom Auftragsbearbeiter eine dem Risiko angemessene Datensicherheit durch geeignete technische und organisatorische Massnahmen.[5] Die Datenschutzverordnung verlangt unter anderem, Schutzbedarf, Risiken, Ursachen, Gefahren, Massnahmen sowie Wahrscheinlichkeit und Schwere einer Verletzung zu beurteilen; diese Beurteilung ist während der Bearbeitungsdauer zu überprüfen.[6]

**[FACHPRÜFUNG ERFORDERLICH]** Ob eine konkrete Bearbeitung dem DSG untersteht, welche Massnahmen angemessen sind oder ob zusätzliche sektorale, vertragliche oder ausländische Vorgaben gelten, ist im Einzelfall durch Datenschutz- oder Rechtsfachpersonen zu beurteilen. Dieser Artikel ist keine individuelle Rechtsberatung. Bei einer Datensicherheitsverletzung, die voraussichtlich zu einem hohen Risiko für Persönlichkeit oder Grundrechte führt, ist der EDÖB nach Art. 24 DSG so rasch wie möglich zu informieren.[7] Diese mögliche Folge gehört deshalb in das Szenario, nicht als pauschale Meldeannahme in jede Zeile.

## Prioritäten festlegen: Nicht alles muss sofort geschehen

Eine einfache Matrix aus Auswirkung und Wahrscheinlichkeit kann die Reihenfolge sichtbar machen. Sie ist jedoch nur der Startpunkt. Prüfen Sie zusätzlich vier Fragen:

1. **Geschäftskritikalität:** Unterbricht das Szenario einen Prozess, der nicht kurzfristig manuell oder mit einer Alternative weitergeführt werden kann?
2. **Exponierung:** Ist der Angriffspfad von ausserhalb erreichbar, betrifft er privilegierte Konten oder erleichtert er eine rasche Ausbreitung?
3. **Abhängigkeit:** Würde eine Massnahme mehrere Risiken gleichzeitig senken, etwa getrennte Administrationskonten oder ein belastbarer Wiederherstellungstest?
4. **Frist und Verpflichtung:** Gibt es eine realistische zeitliche Dringlichkeit durch bekannte Schwachstellen, Vertragsvorgaben oder gesetzliche Pflichten?

Leiten Sie daraus eine kleine, erklärbare Prioritätenfolge ab: sofort zu entscheiden, in der nächsten Umsetzungsphase zu behandeln oder bewusst zu beobachten. Das ist keine Norm, sondern eine Führungsentscheidung auf Basis der eigenen Risikotoleranz. Der CSF 2.0 betont, dass Prioritäten aus Organisationszielen, Bedrohungslage und Geschäftsanforderungen abgeleitet werden sollen; seine Ergebnisse sind keine starre Checkliste.[3]

## Eigentümer, Massnahmen und Restrisiko verbindlich machen

Jede Zeile braucht mindestens zwei klar getrennte Rollen. Der **Risiko-Eigentümer** trägt die Verantwortung, dass das Szenario bewertet, behandelt und bei Bedarf eskaliert wird. Das ist meist eine Führungskraft mit Verantwortung für den betroffenen Prozess oder Bereich. Der **Massnahmen-Eigentümer** setzt die konkrete technische oder organisatorische Massnahme um und liefert den Nachweis. Eine Person kann beide Rollen übernehmen, doch die Unterscheidung muss sichtbar bleiben.

Beschreiben Sie eine Massnahme als überprüfbares Ergebnis, nicht als Absicht. «MFA verbessern» ist zu offen. «Für alle administrativen Konten eine phishing-resistentere Anmeldung gemäss beschlossener Zielkonfiguration aktivieren; Ausnahmen begründen und halbjährlich prüfen» ist überprüfbar. Erfassen Sie Abhängigkeiten, Budget- oder Entscheidbedarf sowie einen Zieltermin. Schliessen Sie den Eintrag erst nach einer Abnahme anhand vorher definierter Evidenz.

Das **Restrisiko** ist nicht «kein Risiko». Es ist die verbleibende Möglichkeit eines Schadens, nachdem Massnahmen umgesetzt wurden. Die Geschäftsleitung oder ein dafür eingesetztes Gremium muss entscheiden, ob dieses Restrisiko innerhalb der festgelegten Risikotoleranz liegt, weiter reduziert, übertragen oder befristet akzeptiert wird. Akzeptanz braucht Datum, Entscheider, Begründung und einen nächsten Prüftermin. So wird eine Ausnahme nicht stillschweigend dauerhaft.

## Top-Risiken in Notfallplanung und Steuerung überführen

Die wichtigsten offenen Szenarien gehören in die [IT-Notfallplanung](/unsere-dienstleistungen/notfallplanung). Für jedes Top-Risiko sollte klar sein, wer einen Vorfall führt, welche Systeme zuerst wiederhergestellt werden, welche Kontakte offline verfügbar sind und welche Kommunikation oder Meldung geprüft werden muss. Das BACS ordnet Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung als vier Phasen eines Notfallkonzepts ein und hebt klar zugeordnete Verantwortlichkeiten hervor.[8]

Nutzen Sie das Register zudem als Verbindung zwischen [Risikomanagement](/unsere-dienstleistungen/risikomanagement), Budgetplanung und Betrieb. Berichten Sie der Geschäftsleitung regelmässig knapp: die wichtigsten Risiken, Veränderungen seit dem letzten Bericht, überfällige Massnahmen, Entscheidungen zum Restrisiko und neue Abhängigkeiten. Ein Register ist lebendig. Aktualisieren Sie es nach Sicherheitsvorfällen, grösseren System- oder Lieferantenänderungen, neuen Geschäftsprozessen sowie nach einem erneuten Sicherheitscheck.

Passende Vertiefungen finden Sie in den Beiträgen zu [ransomware-resistenten Backups](/wissen/ransomware-resistente-backups), [Wiederherstellungstests](/wissen/backup-wiederherstellung-testen) und [Microsoft-365-Sicherheit](/wissen/microsoft-365-sicherheit-kmu). Redaktionelle Rückmeldungen können über den [Kontakt](/kontakt) eingereicht werden.

## Häufige Fehler beim Aufbau eines Risikoregisters

**Technische Schwere mit Geschäftsrisiko verwechseln.** Eine hohe technische Bewertung kann ein dringendes Risiko bedeuten, aber ohne Kontext nicht zwingend. Umgekehrt kann eine scheinbar kleine Konfigurationsabweichung bei einem Zahlungsprozess gravierende Folgen haben.

**Kontrollen nur behaupten.** Nicht dokumentierte oder nie getestete Sicherungen, Alarmierungen und Prozesse dürfen die Bewertung nicht künstlich senken. Halten Sie Nachweise und Grenzen fest.

**Massnahmen ohne Ergebnis und Eigentümer notieren.** «IT kümmert sich» erzeugt keine nachverfolgbare Verantwortung. Benennen Sie Person, Ergebnis, Termin und Abnahmekriterium.

**Restrisiko stillschweigend akzeptieren.** Wenn eine Massnahme nicht möglich oder unverhältnismässig ist, braucht es eine dokumentierte Entscheidung samt Ablaufdatum und Neubewertung.

**Register und Notfallplan getrennt führen.** Ein hoch priorisiertes Ausfallszenario ohne Wiederanlauf- und Kommunikationsvorbereitung bleibt trotz sauberer Registerzeile schlecht beherrschbar.

## Ein pragmatischer Start

1. **Rahmen beschliessen:** Geschäftsleitung bestimmt Skala, Risikotoleranz, Berichtsweg und die Person, welche das Register pflegt.
2. **Kritische Prozesse auswählen:** Fachbereiche nennen die wichtigsten Prozesse, Daten, Systeme, Konten und Dienstleister samt Eigentümern.
3. **Befunde konsolidieren:** Führen Sie Ergebnisse aus Sicherheitscheck, Betrieb, Vorfällen, Lieferanten- und Wiederherstellungstests zusammen. Versehen Sie jeden Eintrag mit Evidenz.
4. **Szenarien formulieren:** Übersetzen Sie jeden priorisierten Befund in Ursache, Ereignis und geschäftliche Folge. Prüfen Sie Dopplungen und Abhängigkeiten.
5. **Bewertung kalibrieren:** Bewerten Sie Auswirkung und Wahrscheinlichkeit gemeinsam mit Fachseite und IT. Dokumentieren Sie bestehende Kontrollen und deren Nachweise.
6. **Massnahmen planen:** Legen Sie Massnahmen-Eigentümer, Termin, Ressourcen, Abnahmekriterium und erwartete Restbewertung fest.
7. **Entscheiden und berichten:** Lassen Sie Top-Risiken und Restrisikobehandlungen vom zuständigen Führungsgremium entscheiden. Überführen Sie relevante Szenarien in den Notfallplan.
8. **Überprüfen:** Kontrollieren Sie die Wirksamkeit nach Umsetzung und planen Sie den nächsten Review. Verwenden Sie dafür die druckbare [Risikoregister-Vorlage](/resources/08-risikoregister-vorlage).

## Sicherheitsstatus in einen priorisierten Massnahmenplan überführen

[Kontaktieren Sie DKSchV](/kontakt), wenn Sie Ihren Sicherheitsstatus und mögliche nächste Schritte besprechen möchten. Die Entscheidung über Prioritäten und Restrisiken bleibt bei der zuständigen Organisation.

## Quellen

[1]: https://www.bacs.admin.ch/de/cybersicherheits-und-resilienzmethode-csrm "BACS – Cybersicherheits- und Resilienzmethode (CSRM)"
[2]: https://csrc.nist.gov/glossary/term/risk_assessment "NIST Computer Security Resource Center – Definition Risk Assessment"
[3]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf "NIST – The Cybersecurity Framework (CSF) 2.0"
[4]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf "NIST – Cybersecurity Framework 2.0 Small Business Quick-Start Guide"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), Art. 8"
[6]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), Art. 1–3"
[7]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), Art. 24"
[8]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[9]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion"
[10]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen"
[11]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA – Managing AI Token Consumption for Operational Resilience"
[12]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI Token Consumption for Operational Resilience"
[13]: https://www.cyber.gc.ca/en/guidance/careful-adoption-agentic-ai "Canadian Centre for Cyber Security – Careful adoption of agentic AI"
