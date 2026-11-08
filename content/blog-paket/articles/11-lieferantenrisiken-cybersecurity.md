---
status: Entwurf
slug: /wissen/lieferantenrisiken-cybersecurity
meta_title: "Cyberrisiken bei IT-Lieferanten prüfen | DKSchV"
meta_description: "So priorisieren und prüfen Schweizer KMU Cloud-, IT- und andere kritische Lieferanten mit einem pragmatischen Risikokreislauf."
suchintention: "Informational – Cyberrisiken bei Lieferanten erfassen und priorisieren"
hauptkeyword: "Lieferantenrisiken Cybersecurity KMU"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "10.12.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle zwölf eindeutigen externen Quellenreferenzen in Artikel und Arbeitsmittel (acht bestehende, vier neu aufgenommene) sowie einschlägige BACS-Originalmeldungen seit 18. Oktober 2026 gezielt geprüft; interne Paketlinks nur erhalten, nicht live geprüft."
quellenpruefung_status: "Alle externen Quellenreferenzen als Originalquellen geprüft; Fedlex zusätzlich über Chronologie, Änderungen und amtliche XML-Fassungen. Vier kontextbezogene Prüfpunkte ergänzt; keine neue pauschale Rechts-, Vertrags- oder technische Pflicht abgeleitet."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Lieferantenrisiken im Griff: BACS-Kreislauf für Cloud-, IT- und kritische Dienstleister in Schweizer KMU

**Quellenstand: 1. November 2026.**

> **[FACHPRÜFUNG ERFORDERLICH]** Die Aussagen zu Auftragsbearbeitung, Auslandbekanntgaben, Geheimhaltung und Vertragsklauseln müssen vor Veröffentlichung durch Datenschutz- und Rechtsfachpersonen geprüft werden.

**Kurzantwort:** Lieferantenrisiken lassen sich nicht mit einem Fragebogen allein beherrschen. Erstellen Sie zuerst eine Landkarte Ihrer Cloud-, IT- und kritischen Dienstleister: Welche Daten, Zugänge und Geschäftsprozesse hängen an wem? Priorisieren Sie danach nach Auswirkung, Abhängigkeit und Wiederanlauf. Das Bundesamt für Cybersicherheit (BACS) empfiehlt dafür einen Kreislauf aus Transparenz, Priorisierung, Bestandesaufnahme, Lieferantengespräch, Prüfung, Verbesserungsmassnahmen und Vertragsabsicherung.[1] Wer im konkreten Fall datenschutzrechtlich Verantwortlicher ist, bleibt für die Rechtmässigkeit der Bearbeitung verantwortlich, auch wenn ein Auftragsbearbeiter Daten verarbeitet.[6] Prüfen Sie daher die wenigen kritischen Partner vertieft, halten Sie Abweichungen mit Verantwortlichen nach und verbinden Sie Verträge mit realistischen Notfallwegen.

Ein Cybervorfall bei einem Dienstleister kann den eigenen Betrieb ebenso treffen wie ein Angriff auf die eigene Infrastruktur. Das Risiko besteht nicht nur beim Hosting- oder Cloud-Provider: Es entsteht auch durch Fernwartungszugänge, eine kompromittierte Softwarekomponente oder den Ausfall eines externen Service Desks. Für die Geschäftsleitung ist dies ein Führungs- und Kontinuitätsthema. Für die IT ist es eine Frage von Zugängen, Datenflüssen, Wiederherstellung und Zusammenarbeit.

Das BACS nennt diesen Ansatz **Cyber-Supply-Chain-Risk-Management (C-SCRM)**. Gemeint ist das fortlaufende Erkennen, Bewerten und Behandeln von Cyberrisiken, die aus Produkten, Dienstleistungen, Lieferanten und deren Abhängigkeiten entstehen.[1] Auch NIST ordnet die Identifikation, Bewertung und Minderung solcher Risiken in das unternehmensweite Risikomanagement ein.[8] Dieser Artikel überträgt den BACS-Kreislauf auf die Realität eines Schweizer KMU: fokussiert, nachvollziehbar und ohne Scheinsicherheit durch umfangreiche Standardfragebogen.

## Warum Lieferantenrisiken bei der Geschäftsleitung beginnen

Ein Lieferant kann technisch gut aufgestellt sein und dennoch für Ihr Unternehmen kritisch bleiben: etwa weil ein einzelner Zugang zu weit reicht, ein notwendiger Datenauszug im Notfall fehlt oder keine Alternative für den Ausfall der Dienstleistung vorgesehen ist. Entscheidend ist deshalb nicht allein die allgemeine Sicherheitsreife des Lieferanten, sondern die konkrete Abhängigkeit Ihres Unternehmens.

Die Geschäftsleitung sollte festlegen, welche Ausfälle, Datenverluste oder Manipulationen nicht akzeptiert werden können und wer Restrisiken akzeptieren darf. **Restrisiko** bezeichnet das Risiko, das nach den geplanten und bestehenden Massnahmen verbleibt. Die IT liefert die technische Sicht; Fachbereiche bewerten die Geschäftsfolgen. Erst diese Verbindung verhindert, dass der gleiche Prüfumfang auf den Druckerlieferanten und den Betreiber einer geschäftskritischen Fachanwendung angewandt wird.

Bei Personendaten ist die Verantwortlichkeit zusätzlich klar geregelt: Verantwortliche und Auftragsbearbeiter müssen eine dem Risiko angemessene Datensicherheit gewährleisten; der Verantwortliche muss sich insbesondere vergewissern, dass ein Auftragsbearbeiter dazu in der Lage ist.[4] [5] Der EDÖB hält zudem fest, dass Verantwortliche Auftragsbearbeiter sorgfältig auswählen, instruieren und soweit nötig überwachen müssen.[7] Die nachfolgenden Hinweise sind allgemeine Orientierung und keine individuelle Rechtsberatung. **[FACHPRÜFUNG ERFORDERLICH]** Ob eine konkrete Auslagerung, ein Vertrag oder eine Auslandbekanntgabe datenschutzrechtlich zulässig ausgestaltet ist, muss im Einzelfall durch Datenschutz- und Rechtsfachpersonen geprüft werden.

## Die Lieferantenlandkarte: Daten, Zugänge und Abhängigkeiten sichtbar machen

Beginnen Sie nicht mit dem Vertrag, sondern mit einer einfachen, gemeinsamen Landkarte. Eine Tabellenzeile pro Lieferant reicht für den Anfang. Ziel ist nicht ein vollständiger Einkaufsstamm, sondern Transparenz über die Lieferanten, deren Ausfall oder Kompromittierung Ihren Betrieb spürbar beeinträchtigen würde.

Erfassen Sie mindestens die Dienstleistung, den verantwortlichen Fachbereich, den technischen Eigentümer im Unternehmen, die verwendeten Systeme, die Datenkategorien, allfällige Datenbearbeitungsorte, Zugänge und Unterlieferanten. Ergänzen Sie, was bei einem Ausfall, einer unbefugten Veränderung oder einem Datenabfluss passiert. Fragen Sie konkret: Kann der Lieferant auf produktive Systeme administrativ zugreifen? Speichert oder verarbeitet er Personendaten? Würde ein Ausfall Aufträge, Produktion, Buchhaltung oder Kundenkommunikation blockieren? Gibt es einen dokumentierten Export, eine Ersatzlösung oder einen manuellen Übergangsprozess?

Diese Landkarte sollte auch **Abhängigkeiten zweiter Ebene** sichtbar machen. Bei einer Cloud-Anwendung können dies etwa Identitätsdienst, Hosting, Backup, Zahlungsanbieter oder Unterauftragsbearbeiter sein. Vollständige Transparenz über jede globale Lieferkette ist selten erreichbar. Der EDÖB erwartet bei Cloud-Diensten aber ausdrücklich, dass Verantwortliche Auftrags- und Unterauftragsbearbeiter, die Sicherheit der Bearbeitung sowie Übermittlungen in Drittländer beachten.[6] Der BACS-Kreislauf verlangt ebenfalls eine bestmögliche Transparenz, damit Risiken für die eigene Organisation und Endkunden verstanden werden können.[1]

## Die drei BACS-Typen: Nicht jeder Lieferant verursacht dasselbe Risiko

Das BACS unterscheidet für die Priorisierung drei nützliche Lieferantentypen.[1]

### 1. Partner mit privilegiertem Zugriff

**Privilegierter Zugriff** ist ein Zugang mit weitreichenden administrativen Rechten, etwa für Fernwartung, Mandantenadministration oder den Betrieb einer Serverumgebung. Dieser Typ ist oft zuerst zu prüfen, weil ein kompromittiertes Konto oder eine Fehlkonfiguration unmittelbare Folgen in Ihrer IT- oder OT-Umgebung haben kann. **OT** steht für Operational Technology, also steuernde oder überwachende Systeme in physischen Betriebsumgebungen.

Klären Sie für diese Partner den konkreten Zugangsweg, die berechtigten Personen, die verwendete Mehrfaktor-Authentisierung, die Protokollierung und die Möglichkeit, den Zugang im Ereignisfall rasch zu sperren. Prüfen Sie ebenso, ob ein Zugriff dauerhaft benötigt wird oder nur zeitlich und auftragsbezogen freigegeben werden sollte.

Bei hochberechtigten SaaS-Integrationen genügen Produktname und Vertragskontakt nicht. Erfassen Sie, soweit anwendbar, auch Mandanten- oder Anwendungskennung, zugehörigen Dienstprinzipal, erteilte Berechtigungen und Zustimmungen, Eigentümerschaft, benötigte Protokolle sowie den letzten Review. Ein von Microsoft am 21. Oktober beschriebener Vorfall bei bestimmten ConnectWise-Cloudanwendungen ist kein Befund gegen andere SaaS-Produkte. Er zeigt jedoch, weshalb Integrationen mit weitreichenden Berechtigungen als eigener Lieferantenzugang erkennbar bleiben müssen. Die dort genannten Sofortmassnahmen gelten nur für die konkret betroffenen Anwendungen; vor irreversiblen Änderungen sollen Konfiguration und Belege gesichert werden.[11]

### 2. Anbieter von Hardware oder Software

Dieser Typ umfasst Produkte, deren Kompromittierung oder Sicherheitsmängel Schaden verursachen können. Dazu zählen neben Geräten auch Fachanwendungen, Bibliotheken und Betriebskomponenten. Entscheidend sind die technische Relevanz, Update- und Supportwege sowie die Fähigkeit, bekannte kritische Schwachstellen zu behandeln. Fragen Sie nicht pauschal nach «sicherer Software», sondern nach dem für Ihr Produkt vorgesehenen Weg für Sicherheitsmeldungen, Updates und Notfallinformationen.

Führen Sie bei kritischen Produkten zusätzlich einen nachprüfbaren Komponentennachweis: Produkt oder Komponente, Einsatzort, zuständiger Betreiber, genaue laufende Paket- oder Produktversion, zugesagter Fixstand, Datum der Bestätigung und Nachweis der Kontrolle nach dem Update. Das BACS hat am 21. Oktober bei PHP ausdrücklich auch integrierte Komponenten und extern betriebene Anwendungen genannt. Bei zurückportierten Korrekturen genügt die sichtbare Hauptversion nicht; massgebend sind die konkrete Paketversion und die Sicherheitsinformation des jeweiligen Anbieters. Ein Update beseitigt keine Spuren oder Folgen einer bereits erfolgten Kompromittierung.[9]

### 3. Anbieter kritischer Dienstleistungen

Hierzu gehören beispielsweise SaaS-Anbieter, Outsourcing-Partner, Service Desks, Logistikpartner oder Lieferanten von Produkten, deren Wegfall Vertraulichkeit, Verfügbarkeit oder Integrität Ihrer Daten und Prozesse beeinträchtigt.[1] **SaaS** bedeutet Software as a Service: eine über das Netz bereitgestellte Anwendung. Bei diesen Partnern stehen neben Schutzmassnahmen insbesondere Verfügbarkeit, Datenzugriff, Kündigungs- und Übergangswege im Vordergrund.

Ein Partner kann mehreren Typen angehören. Ein Managed-Service-Provider kann beispielsweise privilegierten Zugriff besitzen und gleichzeitig eine kritische Dienstleistung erbringen. Vermerken Sie beide Eigenschaften in der Landkarte, statt ihn künstlich einer einzigen Kategorie zuzuordnen.

## Kritikalität bewerten und die Prüfung passend zuschneiden

Priorisieren Sie die Landkarte in einem kurzen Workshop mit Fachbereich, IT und einer Person mit Entscheidungsbefugnis. Verwenden Sie keine mathematische Präzision, die nicht belastbar ist. Eine dreistufige Einordnung – hoch, mittel, basis – genügt, wenn die Kriterien dokumentiert sind.

Ein Lieferant ist in der Regel **hoch kritisch**, wenn mindestens eine der folgenden Bedingungen erfüllt ist: Er hat privilegierten Zugriff auf produktive Systeme; ohne ihn steht ein kritischer Geschäftsprozess still; er verarbeitet besonders schützenswerte oder umfangreiche Personendaten; oder die Ablösung beziehungsweise Wiederherstellung ist unklar. Berücksichtigen Sie auch Konzentrationsrisiken: Mehrere Anwendungen beim gleichen Provider können gemeinsam ausfallen, obwohl jede für sich als mittel kritisch erscheint.

Für hoch kritische Lieferanten folgt eine vertiefte Prüfung. Bei mittlerer Kritikalität reichen fokussierte Nachweise und eine periodische Aktualisierung. Für Basislieferanten genügen dokumentierte Mindestanforderungen und eine Neubewertung bei wesentlichen Änderungen. Dieser risikobasierte Zuschnitt entspricht dem Grundgedanken des BACS, Lieferanten nach Business Impact, Abhängigkeit und den geteilten Informationen zu priorisieren.[1] Auch die Schweizer Datenschutzverordnung verlangt, Schutzbedarf, Risiko und technische sowie organisatorische Massnahmen über die gesamte Bearbeitungsdauer zu überprüfen und nötigenfalls anzupassen.[5]

> **Hypothetisches Praxisbeispiel:** Ein Handelsunternehmen nutzt einen externen IT-Partner für Endgeräte und eine Cloud-Fachanwendung für Bestellungen. Der IT-Partner erhält administrative Fernzugänge und wird deshalb als hoch kritisch eingestuft. Die Fachanwendung ist ebenfalls hoch kritisch, weil sie Aufträge und Kundendaten verarbeitet; der Ausfall würde den Verkauf beeinträchtigen. Für den Büroartikel-Lieferanten genügt die Basisstufe. Das Unternehmen prüft damit zwei relevante Abhängigkeiten vertieft, statt alle Lieferanten gleich intensiv zu befragen.

## Risikobasiert prüfen: erst eigene Antworten, dann das Lieferantengespräch

Das BACS sieht nach Auswahl und Priorisierung zunächst eine **Bestandesaufnahme der eigenen Organisation** vor. Danach werden Leitfragen je Lieferant angepasst, im Vorgespräch besprochen und in einer Lieferantenprüfung ausgewertet.[1] Das ist wirksamer als ein unkommentierter Standardfragebogen, weil Sie zuerst wissen, welche Leistung und welches Risiko Sie tatsächlich prüfen.

Bereiten Sie für jeden hoch kritischen Partner ein kurzes Prüfdossier vor. Es sollte die Landkarten-Informationen, die vorhandenen Verträge, die offenen Annahmen und die Fragen enthalten. Die folgenden Leitfragen sind für ein KMU meist aussagekräftiger als eine lange Kontrollliste:

- Welche Systeme, Daten und Geschäftsprozesse unterstützt der Partner konkret, und welche Rechte hat er darauf?
- Welche Personen oder Rollen erhalten administrativen Zugriff, wie wird dieser geschützt und wie ist er nachvollziehbar?
- Wo werden Daten bearbeitet und gespeichert, welche Unterauftragsbearbeiter sind beteiligt und wie werden Änderungen daran kommuniziert?
- Wie meldet der Partner Sicherheitsvorfälle, Datenschutzverletzungen oder relevante Schwachstellen an Ihre festgelegte Stelle, und wer ist ausserhalb der Geschäftszeiten erreichbar?
- Welche Wiederherstellungs-, Export- oder Übergangsmöglichkeiten bestehen, wenn die Dienstleistung ausfällt, der Vertrag endet oder ein Vorfall den Zugang beeinträchtigt?
- Welche Nachweise oder Gespräche passen zur Kritikalität: Selbstauskunft, technische Unterlagen, Auditbericht, Testbesprechung oder gegebenenfalls eine Vor-Ort-Überprüfung?

Der EDÖB nennt für Cloud-Nutzer insbesondere Weisungsbindung, Sicherheitsmassnahmen, Unterauftragsbearbeiter, Mitwirkung bei Betroffenenanfragen, Unterstützung bei einer möglichen Meldung und Audits als Prüfbereiche.[6] Eine Selbsteinschätzung ist nach BACS ein guter Ausgangspunkt für weitere Instrumente wie Audits oder Vor-Ort-Besuche; die Prüfung soll dabei nicht nur kontrollieren, sondern Verbesserungen und Kompetenzaufbau ermöglichen.[1]

Ordnen Sie bei datenbearbeitenden Lieferanten die Rollen nicht nur im Vertrag, sondern auch im Prüfdossier zu: verantwortliche Stelle, Auftragsbearbeiter, bekannte Unterauftragsbearbeiter sowie fachlicher, Sicherheits- und Vorfallkontakt mit Stellvertretung. Die EDÖB-Mitteilung vom 23. Oktober betrifft ein hängiges Verfahren nach einem Angriff auf einen Softwarelieferanten und stellt keinen Verstoss anderer Unternehmen fest. Sie macht aber deutlich, dass bei einem konkreten Vorfall übermittelte Personendaten, Rechtsgrundlagen, tatsächliche Datenübertragungen und Umfang abgeflossener Informationen geklärt werden müssen.[10]

Bewerten Sie Antworten nicht nach der Anzahl vorhandener Dokumente. Halten Sie je Abweichung fest, was fehlt, welche Auswirkung daraus folgt, welche Massnahme vereinbart wird, wer sie verantwortet und wann Sie den Nachweis erneut ansehen. Erweist sich eine Massnahme als nicht umsetzbar, entscheiden Sie bewusst: Risiko akzeptieren, Nutzung einschränken, zusätzlichen Schutz in Ihrer Umgebung einführen oder Anbieter wechseln. Dieses Vorgehen gehört in Ihr [Risikomanagement](/unsere-dienstleistungen/risikomanagement), nicht in eine isolierte Beschaffungsablage.

## Verträge: Nachweisbare Pflichten statt pauschaler Sicherheitsversprechen

Ein Vertrag ersetzt keine technische Prüfung. Er macht jedoch Erwartungen, Mitwirkung und Folgen verbindlich. Das BACS empfiehlt, nach der Lieferantenprüfung Verträge zu erstellen, zu überprüfen oder anzupassen, damit informationssicherheits- und datenschutzrechtliche Vorgaben verankert sind.[1] Seine Best-Practice-Unterlage nennt unter anderem risikogerechten Schutz nach Stand der Technik, Verschlüsselung, Zugriffstransparenz, Meldewege für Angriffe, Datenschutzverletzungen und Schwachstellen, Regeln für Unterlieferanten sowie Überwachung und Incident Response als mögliche Vertragselemente.[2]

Für kritische Cloud- und IT-Verträge sind inhaltlich besonders wichtig: eine klare Leistungs- und Datenbeschreibung; dokumentierte Weisungen; Anforderungen an Zugriffe, Protokollierung und Schutzmassnahmen; Melde- und Eskalationswege; Mitwirkung bei Untersuchung, Wiederherstellung und Auskunftsbegehren; Regeln für Unterauftragsbearbeiter und deren Änderungen; Datenrückgabe oder -löschung bei Vertragsende; sowie ein angemessenes Recht auf Informationen oder Nachweise. Vereinbaren Sie konkrete Fristen, Messgrössen oder Haftungsfolgen nur, wenn diese zur Dienstleistung, zum Risiko und zur Verhandlungsposition passen.

Bei Personendaten darf ein Auftragsbearbeiter die Bearbeitung nur mit vorgängiger Genehmigung des Verantwortlichen einem Dritten übertragen. Bei einer allgemeinen Genehmigung muss der Auftragsbearbeiter über geplante Änderungen informieren, damit der Verantwortliche widersprechen kann.[4] Findet eine Bekanntgabe von Personendaten ins Ausland statt, sind die Voraussetzungen von Art. 16 DSG zu prüfen; ohne Angemessenheitsentscheid können unter anderem vertragliche Klauseln oder anerkannte Standarddatenschutzklauseln relevant sein.[4] **[FACHPRÜFUNG ERFORDERLICH]** Datenschutzvereinbarung, Unterauftragsbearbeitung und grenzüberschreitende Datenflüsse sind vor Vertragsabschluss oder wesentlichen Änderungen durch Datenschutz- und Rechtsfachpersonen zu prüfen.

## Notfallwege mit dem Lieferanten planen und üben

Ein kritischer Partner muss in der IT-Notfallplanung vorkommen. Erfassen Sie mindestens einen fachlichen, technischen und vertraglichen Kontakt sowie eine Stellvertretung. Halten Sie fest, wer bei einem Vorfall den Zugang sperrt, wer den Lieferanten aufbietet, wer die Kommunikation freigibt und wie Ihre Mitarbeitenden weiterarbeiten, wenn das Partnerportal, die Fachanwendung oder der Fernzugang nicht verfügbar ist.

Das BACS ordnet Notfallkonzepte in vier Phasen ein: Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung. Es betont dabei Grundschutz, Lieferkette, zentrale Notfallkontakte, klar zugeordnete Verantwortlichkeiten sowie das Debriefing zur laufenden Verbesserung.[3] Überführen Sie deshalb die hoch kritischen Zeilen Ihrer Lieferantenlandkarte in Ihre [Notfallplanung](/unsere-dienstleistungen/notfallplanung): Kontaktliste, Eskalationsschwelle, manuelle Umgehung, Datenexport, Wiederanlaufreihenfolge und Nachbearbeitung. Wie Sie die Wiederherstellbarkeit konkret nachweisen, erläutert der Beitrag [Backup-Wiederherstellung realistisch testen](/wissen/backup-wiederherstellung-testen).

Ein jährlicher Papier-Check genügt nicht. Prüfen Sie bei einem Tabletop – einer moderierten Szenarioübung ohne Echtbetrieb – ob Ihre Kontaktwege, Entscheidungsrechte und Beweissicherung funktionieren. Für besonders wichtige Partner kann eine abgestimmte Übung sinnvoll sein. Ziel ist nicht, eine Reaktionszeit zu versprechen, sondern Unklarheiten vor dem Ereignis zu finden.

Nutzen Sie ein KI-gestütztes Angebot eines Lieferanten in einem kritischen Prozess, prüfen Sie zusätzlich dessen Verbrauchs- oder Ratenlimiten, Kosten- und Warnschwellen, Connector- und Toolrechte sowie einen manuellen oder anders unterstützten Notbetrieb. Die kanadische Behördenorientierung vom 22. Oktober beschreibt Tokenerschöpfung als mögliches Verfügbarkeits- und Kostenrisiko und empfiehlt Monitoring, Schwellenwerte und Ausweichabläufe. Sie ist freiwillige ausländische Orientierung und keine Schweizer Rechtsvorgabe; der Prüfumfang bleibt vom konkreten KI-Einsatz und der Kritikalität abhängig.[12]

## Typische Fehler, die den Kreislauf aushebeln

Der erste Fehler ist der Glaube, eine Zertifizierung, ein Auditbericht oder ein unterschriebener Fragebogen mache eine konkrete Abhängigkeit automatisch beherrschbar. Diese Unterlagen können Hinweise liefern; sie ersetzen weder die eigene Risikoanalyse noch die Prüfung des tatsächlichen Zugriffs und Notfallwegs.

Zweitens werden Verträge häufig ohne Datenfluss- und Unterlieferantensicht abgeschlossen. Gerade bei standardisierten Cloud-Diensten sind die Gestaltungsmöglichkeiten begrenzt. Der EDÖB weist darauf hin, dass ein Verantwortlicher gegebenenfalls einen alternativen Dienst wählen oder auf die Auslagerung verzichten muss, wenn sich die Datenschutzvorgaben nicht rechtmässig erfüllen lassen.[6]

Drittens bleiben festgestellte Abweichungen ohne Eigentümer und Termin liegen. Behandeln Sie sie als Risiken mit Massnahmenentscheid, nicht als E-Mail-Verkehr. Viertens endet die Prüfung beim Vertragsabschluss. Ändern sich Provider, Datenflüsse, Fernzugänge, Unterauftragsbearbeiter oder die geschäftliche Bedeutung einer Anwendung, muss auch die Einstufung aktualisiert werden.

## Umsetzung in sieben Schritten

1. Benennen Sie eine verantwortliche Person für den Kreislauf und legen Sie fest, wer Kritikalität und Restrisiken entscheidet.
2. Erstellen Sie eine erste Lieferantenlandkarte für Cloud-, IT- und geschäftskritische Dienstleister.
3. Ordnen Sie jeden relevanten Partner einem oder mehreren BACS-Typen zu und stufen Sie die Kritikalität ein.
4. Führen Sie für hoch kritische Partner die eigene Bestandesaufnahme durch: Zugänge, Daten, Abhängigkeiten, Verträge und Notfalloptionen.
5. Besprechen Sie die angepassten Leitfragen mit dem Partner und fordern Sie nur risikorelevante Nachweise an.
6. Führen Sie Abweichungen, Massnahmen, Eigentümer, Termin und Restrisiko in einem Register; verknüpfen Sie technische Befunde bei Bedarf mit einer [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse).
7. Prüfen Sie Vertrag, Eskalationskontakte und Notfallwege fachlich; aktualisieren Sie die Bewertung nach Provider-, Vertrags- oder Datenflussänderungen sowie nach einem festgelegten risikobasierten Intervall.

Als Arbeitsgrundlage steht der [**Lieferantenfragebogen mit Priorisierungsmatrix**](/resources/11-lieferantenfragebogen) aus diesem Beitragspaket zur Verfügung. Er strukturiert die Landkarte und das Gespräch, trifft aber keine automatische Freigabeentscheidung. Wenn EU-regulierte Kunden Anforderungen an digitale Dienstleister weitergeben, hilft Ihnen der weiterführende Beitrag [NIS2 und DORA für Schweizer Zulieferer](/wissen/nis2-dora-schweiz), die Relevanz getrennt von Schweizer Recht einzuordnen.

## Nächster Schritt

Für eine erste Einordnung Ihrer Ausgangslage erreichen Sie DKSchV über den [Kontakt](/kontakt). Die konkrete Lieferantenbewertung, Vertragsgestaltung und Rechtsprüfung bleiben organisations- und einzelfallbezogen.

## Quellen

[1]: https://www.bacs.admin.ch/de/supply-chain-de "BACS – Cybersicherheit in der Lieferkette"
[2]: https://www.bacs.admin.ch/dam/de/sd-web/iXNmDC-pccRC/best_practice_lieferantenvertrag_de.docx "BACS – Lieferantenverträge: Best Practice"
[3]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Artikel 8, 9 und 16"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), insbesondere Artikel 1 bis 3 und 7"
[6]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing"
[7]: https://www.edoeb.admin.ch/de/outsourcing-auftragsdatenbearbeitung "EDÖB – Outsourcing (Auftragsdatenbearbeitung)"
[8]: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final "NIST SP 800-161 Rev. 1, Update 1 – Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations"
[9]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
[10]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant, 23. Oktober 2026"
[11]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise, 21. Oktober 2026"
[12]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience, 22. Oktober 2026"
