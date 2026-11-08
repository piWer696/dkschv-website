---
arbeitsmittel: "Lieferantenfragebogen und Priorisierungsmatrix für Cloud-, IT- und kritische Dienstleister"
passender_artikel: /wissen/lieferantenrisiken-cybersecurity
version: "1.2"
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/11-lieferantenfragebogen"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle neun eindeutigen externen Quellenreferenzen dieses Arbeitsmittels (fünf bestehende, vier neu aufgenommene) sowie die korrespondierenden Originalquellen des passenden Artikels gezielt geprüft; interne Paketlinks nur erhalten, nicht live geprüft."
quellenpruefung_status: "Alle externen Quellenreferenzen als Originalquellen geprüft; Fedlex-Korrespondenz zusätzlich über Chronologie, Änderungen und amtliche XML-Fassungen geprüft. Vier kontextbezogene Prüfpunkte ergänzt; keine automatische Freigabe, Rechts- oder Tenantentscheidung."
---

# Lieferantenfragebogen und Priorisierungsmatrix

**Version 1.2 · Quellenstand: 1. November 2026 · Arbeitsvorlage – nicht freigegeben**

> **[FACHPRÜFUNG ERFORDERLICH]** Auftragsbearbeitung, Auslandbekanntgaben, Geheimhaltung und Vertragsklauseln müssen im Einzelfall durch Datenschutz- und Rechtsfachpersonen geprüft werden.

## Zweck

Dieses Arbeitsmittel unterstützt Schweizer KMU dabei, Cloud-, IT- und geschäftskritische Dienstleister nach ihrem Cyberrisiko zu erfassen, zu priorisieren und gezielt zu prüfen. Es folgt dem BACS-Kreislauf: Lieferkette kennen, Lieferanten priorisieren, eigene Bestandesaufnahme durchführen, Lieferantengespräch führen, Prüfung auswerten, Verbesserungen festlegen und Verträge überprüfen.[1]

Der Fragebogen hilft, die richtigen Fragen zu stellen. Er bestätigt weder die Sicherheit eines Lieferanten noch die Rechtskonformität einer Auslagerung. Bei Personendaten bleibt das Unternehmen als Verantwortlicher grundsätzlich für die datenschutzkonforme Bearbeitung verantwortlich.[4] **[FACHPRÜFUNG ERFORDERLICH]** Datenschutzvereinbarungen, Unterauftragsbearbeitung, Auslandbekanntgaben und Vertragsklauseln sind im konkreten Fall durch Datenschutz- und Rechtsfachpersonen zu prüfen.

## Anwendung

1. Füllen Sie zuerst Teil A und B intern aus. Beziehen Sie Fachbereich, IT und die für Risikoentscheide zuständige Person ein.
2. Bestimmen Sie die Prüftiefe anhand der Priorisierung in Teil C. Hoch kritische Lieferanten werden vertieft geprüft; bei mittlerer und Basis-Kritikalität genügt ein angemessen reduzierter Umfang.
3. Senden Sie nur die passenden Fragen aus Teil D an den Lieferanten. Besprechen Sie offene Punkte wenn möglich direkt.
4. Dokumentieren Sie in Teil E Abweichungen, Massnahmen, Eigentümer und Termin. Entscheiden Sie Restrisiken nicht implizit.
5. Aktualisieren Sie das Blatt nach wesentlichen Änderungen an Provider, Vertrag, Datenfluss, Zugängen oder Geschäftsprozess sowie nach einem festgelegten risikobasierten Intervall.

Für die anschliessende Vertragsprüfung stellt das BACS eine Best-Practice-Unterlage mit möglichen Informationssicherheits- und Datenschutzthemen bereit.[2]

> **Ausfüllhinweis:** Verwenden Sie für zusätzliche Informationen oder Nachweise eine Beilage. «Nicht anwendbar» ist nur zulässig, wenn die Begründung eingetragen wird.

---

## Teil A – Lieferantenprofil und Landkarte

| Feld | Eintrag |
|---|---|
| Lieferant / rechtliche Einheit |  |
| Dienstleistung / Produkt |  |
| Interne fachliche Eigentümerschaft |  |
| Interne IT-Verantwortung |  |
| Vertragsverantwortung |  |
| Vertragsbeginn / nächster Review |  |
| Relevante Systeme und Schnittstellen |  |
| Unterstützte Geschäftsprozesse |  |
| Datenkategorien (keine / Personen- / besonders schützenswerte Personendaten / Geschäftsgeheimnisse / andere) |  |
| Datenbearbeitungs- und Speicherorte, soweit bekannt |  |
| Bekannte Unterauftragsbearbeiter |  |
| Rolle bei Datenbearbeitung (verantwortliche Stelle / Auftragsbearbeiter / andere; fachlich prüfen) |  |
| Ansprechpartner Lieferant: Fachlich / Sicherheit / Datenschutz-Datenbearbeitung / Notfall, je mit Stellvertretung |  |
| Interne Notfallkontakte und Stellvertretung |  |
| Kritische Produkte, Komponenten oder Appliances: Produkt/Paket, Einsatzort, zuständiger Betreiber, laufender Stand |  |
| SaaS-Integration, soweit anwendbar: Anwendung/Mandant, Anwendungs- oder Dienstprinzipal-ID, Rechte/Zustimmungen, Eigentümerschaft |  |
| KI-gestützter Dienst, soweit anwendbar: unterstützter Prozess, Anbieter/Modell oder Agent, Connectoren/Toolrechte, bekannte Quoten oder Limiten |  |

## Teil B – BACS-Lieferantentyp und Abhängigkeit

Kreuzen Sie alles Zutreffende an. Das BACS unterscheidet Partner mit privilegiertem Zugriff, Anbieter von Hardware oder Software und Anbieter wichtiger Dienstleistungen.[1]

| Kontrollpunkt | Ja | Nein | Unklar / Begründung |
|---|:---:|:---:|---|
| Der Lieferant oder seine Mitarbeitenden haben privilegierten Zugriff auf interne oder produktive Systeme. | ☐ | ☐ |  |
| Der Lieferant stellt Hardware, Software oder Komponenten bereit, deren Kompromittierung Schaden verursachen kann. | ☐ | ☐ |  |
| Der Lieferant erbringt eine wichtige Dienstleistung; ein Ausfall beeinträchtigt Vertraulichkeit, Verfügbarkeit oder Integrität von Daten oder Prozessen. | ☐ | ☐ |  |
| Eine SaaS-Integration, ein Dienstprinzipal oder ein vergleichbarer technischer Zugang hat weitreichende Rechte auf Daten, Systeme oder Identitäten. | ☐ | ☐ |  |
| Ein KI-gestützter Dienst unterstützt einen kritischen Prozess oder kann dessen Verfügbarkeit, Kosten oder Wiederanlauf beeinflussen. | ☐ | ☐ |  |
| Mehrere wichtige Dienste hängen vom gleichen Lieferanten oder dessen Plattform ab. | ☐ | ☐ |  |
| Ein Ausfall würde einen kritischen Geschäftsprozess blockieren. | ☐ | ☐ |  |
| Es gibt eine dokumentierte Ersatz-, Export- oder manuelle Übergangslösung. | ☐ | ☐ |  |
| Administrativer Zugriff kann bei Bedarf rasch gesperrt oder beschränkt werden. | ☐ | ☐ |  |

---

## Teil C – Priorisierungsmatrix

Bewerten Sie jeden Punkt mit **0 = gering**, **1 = mittel** oder **2 = hoch**. Die Summe ist eine Gesprächshilfe, keine automatische Risikofreigabe.

| Kriterium | 0 | 1 | 2 | Wert |
|---|---|---|---|:---:|
| Geschäftsfolgen bei Ausfall | Kaum spürbar | Beeinträchtigung einzelner Abläufe | Kritischer Prozess steht oder Kundenleistung stark beeinträchtigt |  |
| Umfang der Rechte und Zugänge | Kein oder stark begrenzter Zugriff | Begrenzter Betriebs- oder Supportzugriff | Privilegierter Zugriff auf produktive Systeme oder Identitäten |  |
| Daten und Schutzbedarf | Keine oder wenig schutzbedürftige Daten | Personendaten oder vertrauliche Geschäftsdaten | Besonders schützenswerte Personendaten, grosse Datenmenge oder Geschäftsgeheimnisse |  |
| Abhängigkeit und Austauschbarkeit | Ersatz kurzfristig verfügbar | Ersatz möglich, aber aufwendig | Kein realistischer kurzfristiger Ersatz oder deutliche Konzentration |  |
| Wiederanlauf und Datenzugriff | Dokumentiert und erprobt | Teilweise dokumentiert | Unklar, nicht getestet oder vom Lieferanten abhängig |  |
| Transparenz zu Unterlieferanten / Datenorten | Vollständig und aktuell | Teilweise verfügbar | Unklar oder nicht verfügbar |  |
| **Total** |  |  |  | **/12** |

**Interne Einordnung und begründeter Entscheid**

| Ergebnis | Festlegung |
|---|---|
| Gesamteinstufung: ☐ Hoch kritisch ☐ Mittel ☐ Basis |  |
| Begründung, die wichtiger ist als die Punktzahl |  |
| Entscheiderin / Entscheider für Einstufung |  |
| Datum / nächster Review |  |

> **Empfohlene Anwendung:** Eine hohe Einzelbewertung bei privilegiertem Zugriff, kritischem Geschäftsprozess oder besonders schützenswerten Personendaten kann eine vertiefte Prüfung rechtfertigen, auch wenn die Summe niedrig ausfällt. Die Organisation legt die endgültige Prüftiefe risikobasiert fest.

---

## Teil D – Risikobasierte Lieferantenprüfung

### D1. Zugänge, Schutz und Betrieb

Für Software, Komponenten und externe Betriebsleistungen verlangen Sie nur bei risikorelevanten Produkten einen überprüfbaren Nachweis. Das BACS weist in seiner PHP-Warnung vom 21. Oktober darauf hin, auch integrierte Komponenten und extern betriebene Anwendungen zu erfassen. Bei zurückportierten Korrekturen sind die konkrete Paketversion und die Sicherheitsinformation des Anbieters aussagekräftiger als die sichtbare Hauptversion. Ein Update beseitigt keine Spuren oder Folgen einer bereits erfolgten Kompromittierung.[6]

Für hochberechtigte SaaS-Integrationen sind Anwendung, Mandant, Anwendungs- oder Dienstprinzipal, Berechtigungen und Zustimmungen getrennt vom üblichen Lieferantenkontakt zu dokumentieren. Ein Microsoft-Bericht vom 21. Oktober zu bestimmten ConnectWise-Cloudanwendungen begründet keine Vermutung gegen andere Produkte. Er stützt aber die kontextbezogene Prüfung weitreichender App-Berechtigungen, auffälliger anwendungsbasierter Aktivitäten und der Beweissicherung vor irreversiblen Änderungen.[8]

| Frage an den Lieferanten | Ja | Nein | N. a. | Nachweis / Erläuterung |
|---|:---:|:---:|:---:|---|
| Sind die für unsere Leistung eingesetzten Personen zur Vertraulichkeit verpflichtet? | ☐ | ☐ | ☐ |  |
| Werden administrative und Fernzugänge individuell zugeordnet und angemessen geschützt? | ☐ | ☐ | ☐ |  |
| Können Zugriffe auf unsere Daten oder Systeme nachvollzogen werden? | ☐ | ☐ | ☐ |  |
| Besteht ein Verfahren, Sicherheitsmassnahmen auf Wirksamkeit und Aktualität zu prüfen? | ☐ | ☐ | ☐ |  |
| Gibt es einen definierten Weg für Sicherheitsmeldungen, Updates und relevante Schwachstellen? | ☐ | ☐ | ☐ |  |
| Nennt der Lieferant für kritische Produkte oder integrierte Komponenten Produkt/Paket, tatsächlichen Fixstand, Datum und nachprüfbaren Sicherheitsnachweis? | ☐ | ☐ | ☐ |  |
| Kann der Lieferant nach einem Sicherheitsupdate den tatsächlich laufenden Stand oder eine gleichwertige Herstellerbestätigung nachweisen? | ☐ | ☐ | ☐ |  |
| Sind bei einer hochberechtigten SaaS-Integration die Anwendung oder der Dienstprinzipal, Rechte, Zustimmungen, Eigentümerschaft und erforderliche Prüfprotokolle dokumentiert? | ☐ | ☐ | ☐ |  |
| Können wir den Zugriff im Vorfall oder bei Vertragsende sperren oder beenden? | ☐ | ☐ | ☐ |  |

### D2. Daten, Unterauftragsbearbeiter und Datenschutz

Diese Fragen sind besonders relevant, wenn der Lieferant Personendaten bearbeitet. Der EDÖB nennt für Cloud-Dienste unter anderem Weisungsbindung, Sicherheit, Unterauftragsbearbeiter, Mitwirkung und Audits als relevante Prüffelder.[3]

Die Rollen- und Kontaktangaben sollen im Vorfall nachvollziehbar sein. Die EDÖB-Mitteilung vom 23. Oktober betrifft eine hängige Untersuchung nach einem Angriff auf einen Softwarelieferanten und ist kein Verstossbefund gegen andere Lieferanten. Sie verdeutlicht aber, dass bei einem konkreten Ereignis übermittelte Personendaten, Rechtsgrundlagen, tatsächliche Übertragungen und der Umfang abgeflossener Informationen geklärt werden müssen.[7]

| Frage an den Lieferanten | Ja | Nein | N. a. | Nachweis / Erläuterung |
|---|:---:|:---:|:---:|---|
| Bearbeitet der Lieferant Personendaten nur auf dokumentierte Weisungen und nicht für eigene Zwecke, soweit nicht rechtlich anders zulässig? | ☐ | ☐ | ☐ |  |
| Sind die Rollen der verantwortlichen Stelle, des Auftragsbearbeiters und der bekannten Unterauftragsbearbeiter für diese Leistung nachvollziehbar dokumentiert? | ☐ | ☐ | ☐ |  |
| Sind Datenkategorien, Bearbeitungszweck sowie Datenbearbeitungs- und Speicherorte dokumentiert? | ☐ | ☐ | ☐ |  |
| Liegt eine aktuelle Liste der Unterauftragsbearbeiter vor? | ☐ | ☐ | ☐ |  |
| Werden Änderungen bei Unterauftragsbearbeitern rechtzeitig mitgeteilt, damit wir sie prüfen können? | ☐ | ☐ | ☐ |  |
| Unterstützt der Lieferant uns bei Auskunftsbegehren, Löschung/Korrektur sowie nötigenfalls bei der Behandlung einer Verletzung der Datensicherheit? | ☐ | ☐ | ☐ |  |
| Sind Datenrückgabe oder Löschung bei Vertragsende geregelt und praktisch möglich? | ☐ | ☐ | ☐ |  |
| Sind mögliche Auslandbekanntgaben identifiziert und vor Einsatz fachlich sowie rechtlich geprüft? | ☐ | ☐ | ☐ |  |

### D3. Vorfall, Kontinuität und Notfallweg

| Frage an den Lieferanten | Ja | Nein | N. a. | Nachweis / Erläuterung |
|---|:---:|:---:|:---:|---|
| Gibt es einen benannten Sicherheits- und Notfallkontakt mit Eskalationsweg? | ☐ | ☐ | ☐ |  |
| Ist im Vertrag oder Anhang geregelt, wie und an wen Cybervorfälle, Datenschutzverletzungen und relevante Schwachstellen gemeldet werden? | ☐ | ☐ | ☐ |  |
| Ist die erforderliche Mitwirkung bei Eindämmung, Untersuchung und Wiederherstellung beschrieben? | ☐ | ☐ | ☐ |  |
| Ist bekannt, wie wir Daten oder wesentliche Konfigurationen bei Ausfall oder Vertragsende erhalten? | ☐ | ☐ | ☐ |  |
| Besteht ein dokumentierter Übergangs- oder manueller Ersatzprozess für einen längeren Ausfall? | ☐ | ☐ | ☐ |  |
| Wurde der interne Eskalations- und Kontaktweg geprüft oder geübt? | ☐ | ☐ | ☐ |  |

---

### D4. KI-gestützte Dienste, Quoten und Notbetrieb

Füllen Sie diesen Abschnitt nur aus, wenn der Lieferant einen KI-gestützten Dienst, Agenten oder Connector für einen relevanten Prozess bereitstellt. Die kanadische Behördenorientierung vom 22. Oktober beschreibt Quoten- und Tokenerschöpfung als mögliches Kosten- und Verfügbarkeitsrisiko. Sie empfiehlt unter anderem Monitoring, abgestufte Warnungen, die Prüfung von Drittanbieterlimiten und manuelle oder anders unterstützte Ausweichabläufe. Das ist freiwillige ausländische Orientierung, keine Schweizer Rechtsvorgabe.[9]

| Frage an den Lieferanten | Ja | Nein | N. a. | Nachweis / Erläuterung |
|---|:---:|:---:|:---:|---|
| Ist dokumentiert, welche Geschäftsprozesse, Datenquellen, Connectoren und Toolrechte der KI-gestützte Dienst unterstützt? | ☐ | ☐ | ☐ |  |
| Sind relevante Verbrauchs-, Raten-, Budget- oder Kapazitätslimiten sowie der Eskalationskontakt bekannt? | ☐ | ☐ | ☐ |  |
| Bestehen angemessene Monitoring- oder Warnmöglichkeiten für ungewöhnlichen Verbrauch oder sich nähernde Limiten? | ☐ | ☐ | ☐ |  |
| Ist für den Ausfall, eine Quotenausschöpfung oder unzuverlässige Ergebnisse ein manueller oder anders unterstützter Notbetrieb festgelegt und im Verhältnis zur Kritikalität geprüft? | ☐ | ☐ | ☐ |  |
| Sind weitreichende Tool- und Connectorrechte auf das für die Aufgabe notwendige Mass beschränkt und überprüfbar? | ☐ | ☐ | ☐ |  |

---

## Teil E – Auswertung, Massnahmen und Restrisiko

| Nr. | Feststellung / Abweichung | Auswirkung | Massnahme / Entscheid | Verantwortlich | Termin | Nachweis / Status |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |

| Abschlusskontrolle | Eintrag |
|---|---|
| Verbleibendes Restrisiko nach Massnahmen |  |
| Entscheid: ☐ akzeptieren ☐ reduzieren ☐ Nutzung beschränken ☐ Ersatz prüfen |  |
| Entscheiderin / Entscheider, Datum |  |
| Nächster Review / Auslöser für früheren Review |  |
| Ablageort von Vertrag, Nachweisen und Notfallkontaktliste |  |

## Grenzen des Arbeitsmittels

Dieses Arbeitsmittel ist eine strukturierte Entscheidungshilfe. Eine positive Selbstauskunft, ein Dokument oder eine Zertifizierung garantieren weder die tatsächliche Wirksamkeit von Schutzmassnahmen noch die Verfügbarkeit einer Dienstleistung. Die Prüftiefe muss dem Risiko, den Daten, den Zugängen und der Abhängigkeit entsprechen. Technische Tests, Audits oder eine unabhängige Fachbeurteilung können bei hoch kritischen Lieferanten erforderlich sein.

Das Blatt ersetzt keine rechtliche Beratung. Insbesondere ist eine **[FACHPRÜFUNG ERFORDERLICH]**, wenn Personendaten an Auftrags- oder Unterauftragsbearbeiter übertragen werden, wenn Daten ins Ausland bekanntgegeben werden, wenn Geheimhaltungspflichten gelten oder wenn Vertragsklauseln zur Haftung, Datenbearbeitung oder Meldepflicht festgelegt werden. Das DSG verlangt, dass sich Verantwortliche vergewissern, dass Auftragsbearbeiter die Datensicherheit gewährleisten können; die DSV verlangt eine laufende risikogerechte Überprüfung von Schutzbedarf, Risiko und Massnahmen.[4] [5]

## Quellen

[1]: https://www.bacs.admin.ch/de/supply-chain-de "BACS – Cybersicherheit in der Lieferkette"
[2]: https://www.bacs.admin.ch/dam/de/sd-web/iXNmDC-pccRC/best_practice_lieferantenvertrag_de.docx "BACS – Lieferantenverträge: Best Practice"
[3]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Artikel 8, 9 und 16"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), insbesondere Artikel 1 bis 3 und 7"
[6]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
[7]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant, 23. Oktober 2026"
[8]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise, 21. Oktober 2026"
[9]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience, 22. Oktober 2026"
