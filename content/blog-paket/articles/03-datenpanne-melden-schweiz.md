---
status: "Entwurf – nicht freigegeben"
slug: "/wissen/datenpanne-melden-schweiz"
meta_title: "Datenpanne melden: EDÖB oder BACS? | DKSchV"
meta_description: "Schweizer Entscheidungsweg zu Datenpannen: Art. 24 DSG, EDÖB und die getrennte BACS-Meldeprüfung bei kritischen Infrastrukturen."
hauptkeyword: "Datenpanne melden Schweiz"
suchintention: "Informational – Meldewege bei Datenpannen in der Schweiz einordnen"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "15.10.2026"
rechtsstand: "1. November 2026 (DSG, DSV, ISG und CSV amtlich verifiziert)"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle 12 zitierten externen Originalquellen dieses Artikels und des zugehörigen Arbeitsmittels; einschliesslich amtlicher Fedlex-Historien und ISG-XML bei stateless Leerabruf sowie einschlägiger EDÖB-/BACS-Originalmeldungen seit 18. Oktober 2026"
quellenpruefung_status: "Vollständig für die 12 zitierten externen Originalquellen geprüft am 1. November 2026; keine Fachfreigabe"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Datenpanne in der Schweiz: DSG-Entscheidungsbaum für EDÖB-Meldung und BACS-Pflicht

**Kurzantwort:** Eine Datenpanne ist nach Schweizer Datenschutzgesetz (DSG) dem Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) **so rasch als möglich** zu melden, wenn sie voraussichtlich ein hohes Risiko für Persönlichkeit oder Grundrechte natürlicher Personen schafft. Eine feste 72-Stunden-Frist steht nicht in Art. 24 DSG. Separat müssen die im Informationssicherheitsgesetz (ISG) erfassten Betreiber kritischer Infrastrukturen bestimmte Cyberangriffe dem Bundesamt für Cybersicherheit (BACS) innert **24 Stunden nach Entdeckung** melden; für fehlende Angaben gewährt das BACS eine Frist von 14 Tagen zur Ergänzung. Ein Vorfall kann beide Pflichten auslösen, nur eine oder keine. Klären Sie daher parallel Personendaten, Risiko, Branchenstatus und Angriffstatbestand. Im Zweifel über eine Meldepflicht ist **[FACHPRÜFUNG ERFORDERLICH]**: Veranlassen Sie umgehend eine datenschutz- und gegebenenfalls sektorrechtliche Fachprüfung.[1] [5] [6]

Eine Datenpanne verlangt zwei Entscheidungen, die nicht vermischt werden dürfen. Die erste betrifft den Schutz von Menschen und damit Art. 24 DSG. Die zweite betrifft die Cyberresilienz bestimmter Organisationen und damit die BACS-Meldepflicht nach ISG. Wer nur fragt «EDÖB oder BACS?», kann deshalb die falsche Frist oder den falschen Massstab anwenden.

Dieser Beitrag bietet eine allgemeine Orientierung für Schweizer KMU. Er ist **keine individuelle Rechtsberatung**. Ob eine konkrete Meldung geschuldet ist, ob weitere sektorspezifische Vorgaben gelten und wie Betroffene informiert werden müssen, braucht bei ernsthaften oder unklaren Fällen eine zeitnahe Fachprüfung anhand der Fakten, Verträge und anwendbaren Regeln.

## Zuerst stabilisieren, dann beurteilen

Eine **Verletzung der Datensicherheit** liegt nach Art. 5 Bst. h DSG vor, wenn Personendaten unbeabsichtigt oder widerrechtlich verlorengehen, gelöscht, vernichtet oder verändert werden oder Unbefugten offengelegt beziehungsweise zugänglich gemacht werden.[1] Personendaten sind Angaben über eine bestimmte oder bestimmbare **natürliche Person**. Damit kann ein fehlgeleitetes E-Mail ebenso relevant sein wie ein kompromittiertes Cloud-Konto, ein verlorener Laptop, ein Fehlrecht in einer Freigabe oder ein Ransomware-Angriff.

Akute Eindämmung und rechtliche Einordnung laufen parallel. Trennen Sie eindeutig infizierte Systeme kontrolliert vom Netz, ohne Beweise unnötig zu verändern. Sichern Sie verfügbare Protokolle, Zeitstempel, Konfigurationsstände und die betroffenen Objekte. Das BACS empfiehlt bei Ransomware unter anderem das rasche Trennen infizierter Systeme sowie das Sichern von Logdateien. Forensische Sicherungen von Zwischenspeicher und Festplatten sollten vor weiteren Reparaturversuchen oder Neustarts durch Fachpersonen erfolgen, wenn eine forensische Untersuchung in Betracht kommt.[9]

Ein Verdacht auf Schadsoftware ist nicht mit einem bestätigten Angriff gleichzusetzen. Ein einzelnes Anzeichen, etwa ein langsames Gerät, beweist keine Infektion. Mehrere ungewöhnliche Beobachtungen rechtfertigen aber eine genauere Untersuchung; bei geschäftlich verwendeten Geräten empfiehlt das BACS, die zuständige IT oder den Arbeitgeber zu informieren.[11]

Bestimmen Sie unmittelbar eine verantwortliche Person für den Vorfall, eine Stellvertretung und einen Entscheidkanal zur Geschäftsleitung. Halten Sie fest, **was** bekannt ist, **was** nur vermutet wird und **wann** eine Annahme überprüft wird. Diese sachliche Ereignisakte hilft der technischen Untersuchung ebenso wie der späteren Meldung. Ein Muster für Rollen, Erfassung und Entscheidpunkte gehört in Ihre [IT-Notfallplanung](/unsere-dienstleistungen/notfallplanung); für die ersten Eindämmungsschritte kann auch der Beitrag [Ransomware im KMU: die ersten 60 Minuten](/wissen/ransomware-erste-60-minuten) herangezogen werden.

## Entscheidungsbaum: Drei Fragen, zwei Meldewege

Der folgende Ablauf ist bewusst kein Ersatz für die Prüfung des Einzelfalls. Er zeigt, welche Abklärungen parallel erfolgen sollten.

### 1. Sind Personendaten betroffen und liegt eine Datensicherheitsverletzung vor?

Erfassen Sie Datenarten, Systeme, Personengruppen und möglichen Zugriff. Entscheidend ist nicht, ob ein Datensatz bereits nachweislich veröffentlicht wurde. Auch ein unbefugter Zugang oder eine unbeabsichtigte Offenlegung kann eine Datensicherheitsverletzung sein.[1]

Wenn keine Personendaten natürlicher Personen betroffen sind, greift Art. 24 DSG für diesen Vorfall nicht. Das bedeutet **nicht**, dass keine anderen Pflichten bestehen. Ein Ausfall, eine Erpressung oder ein Abfluss von Betriebsinformationen kann bei einer erfassten kritischen Infrastruktur dennoch BACS-relevant sein.[5]

Klären Sie zudem Ihre Rolle. Der **Verantwortliche** entscheidet über Zweck und Mittel der Datenbearbeitung. Ein **Auftragsbearbeiter** verarbeitet Personendaten im Auftrag. Nach Art. 24 Abs. 3 DSG muss der Auftragsbearbeiter dem Verantwortlichen eine Verletzung so rasch als möglich melden. Die Meldung an den EDÖB obliegt dagegen dem Verantwortlichen.[1] Der EDÖB hält ausdrücklich fest, dass der Auftragsbearbeiter den Verantwortlichen über jede Datensicherheitsverletzung informieren muss, unabhängig von der späteren Risikoeinschätzung.[4]

Die am 23. Oktober 2026 veröffentlichte Mitteilung des EDÖB zum Cyberangriff auf die PK Softech AG ist ein Anlass, Datenbearbeiterbeziehungen vor einem Vorfall greifbar zu machen. Der EDÖB untersucht dort unter anderem, welche Personendaten Vorsorgeeinrichtungen dem Softwareunternehmen zur Verfügung stellten, auf welchen rechtlichen Grundlagen Datenübertragungen beruhten, wie sie tatsächlich umgesetzt wurden und welche Informationen abgeflossen sind. Das Verfahren ist hängig. Die Mitteilung ist **weder** ein festgestellter Datenschutzverstoss **noch** eine neue allgemeine Meldefrist. Für die eigene Ereignisakte sollten Verantwortliche deshalb Datenflüsse, Rollen, Vertrags- und Meldewege sowie erreichbare Vorfallkontakte faktenbasiert festhalten; die rechtliche Rollenqualifikation bleibt im Einzelfall zu prüfen.[12]

### 2. Führt die Datenpanne voraussichtlich zu einem hohen Risiko?

Art. 24 Abs. 1 DSG knüpft die Meldung an den EDÖB nicht an jede Datenpanne, sondern an ein **voraussichtlich hohes Risiko** für Persönlichkeit oder Grundrechte betroffener Personen. Der EDÖB verlangt eine Beurteilung sowohl der Schwere möglicher Folgen als auch ihrer Wahrscheinlichkeit. Massgebend ist die Beeinträchtigung für die am schwersten betroffenen Personen, nicht ein Durchschnittswert über alle Fälle.[4]

Die folgenden Umstände sind keine starre Punkteliste. Sie strukturieren aber die Fachprüfung:

- **Daten und Kontext:** Besonders schützenswerte Personendaten wie Gesundheits-, biometrische oder Sozialhilfedaten sprechen häufig für ein hohes Risiko. Auch Kopien von Identitätsdokumenten oder Kreditkartendaten können je nach Kontext schwer wiegen.[1] [4]
- **Zugriff und Angreifer:** Ein möglicher Abfluss an unbekannte Dritte, eine Veröffentlichung im Darknet oder ein krimineller Zugriff kann das Risiko erhöhen. Ein blosses Vertrauen in unbekannte Empfänger genügt nicht, um ein objektiv hohes Risiko auszuschliessen.[4]
- **Folgen für Menschen:** Identitätsdiebstahl, Kreditkartenbetrug, Diskriminierung, Rufschädigung oder Vermögenseinbussen sind Beispiele möglicher schwerer Auswirkungen.[4]
- **Bestimmbarkeit und Schutz:** Wirksam verschlüsselte Daten, für die der unbefugte Dritte keinen Schlüssel besitzt, gelten für ihn als anonym; dies kann eine Meldepflicht ausschliessen. Pseudonymisierte Daten bleiben dagegen Personendaten. Auch der Umfang kann wichtig sein, doch viele Betroffene allein begründen nach dem EDÖB noch kein hohes Risiko.[4]

Geplante spätere Massnahmen dürfen die anfängliche Risikoeinstufung nicht kleinrechnen. Nachweisbare Sofortmassnahmen können in der Beurteilung berücksichtigt werden, wenn sie eine Zweckentfremdung rasch und belastbar ausschliessen oder mindern. Bei verbleibendem Zweifel, der ein hohes Risiko nicht mit hinreichender Wahrscheinlichkeit ausschliesst, soll nicht auf langwierige Abklärungen gewartet werden.[4] **[FACHPRÜFUNG ERFORDERLICH]** Diese Abwägung und insbesondere die Wirkung einer Verschlüsselung brauchen bei Grenzfällen eine datenschutzrechtliche Fachbeurteilung.

### 3. EDÖB melden: «so rasch als möglich», nicht schematisch nach 72 Stunden

Besteht voraussichtlich ein hohes Risiko, meldet der Verantwortliche die Verletzung dem EDÖB **so rasch als möglich**. Art. 24 DSG nennt dafür keine pauschale Stundenfrist. Eine aus der EU-Datenschutz-Grundverordnung bekannte 72-Stunden-Regel darf daher weder als Schweizer Frist behauptet noch als Grund für ein Abwarten verstanden werden.[1] [10] Der EDÖB erläutert: Ist das hohe Risiko nach einer raschen Analyse erkennbar oder nicht innert kurzer Zeit abschliessend auszuschliessen, muss gemeldet werden; bei Ransomware kann dies je nach Umständen bereits in der ersten Analyse der Fall sein.[4]

Die Datenschutzverordnung (DSV) verlangt für die Meldung unter anderem Art der Verletzung, soweit möglich Zeitpunkt und Dauer, Kategorien und ungefähre Anzahl der betroffenen Daten und Personen, Folgen und Risiken, getroffene oder vorgesehene Massnahmen sowie eine Ansprechperson. Nicht verfügbare Angaben dürfen so rasch als möglich nachgereicht werden.[2] Das EDÖB-Portal **DataBreach** dient Verantwortlichen zur sicheren digitalen Übermittlung und ermöglicht den Download einer Bestätigung.[3]

Die Information betroffener Personen ist ein eigener Entscheid. Der Verantwortliche informiert sie, wenn dies zu ihrem Schutz erforderlich ist oder der EDÖB dies verlangt. Das Gesetz enthält Möglichkeiten, eine Information unter bestimmten Voraussetzungen einzuschränken, aufzuschieben oder darauf zu verzichten. **[FACHPRÜFUNG ERFORDERLICH]** Ob eine solche Ausnahme vorliegt und wie konkret informiert wird, braucht eine fachjuristische Beurteilung.[1]

## Die BACS-Pflicht: anderer Geltungsbereich, kürzere Frist

Seit 1. April 2025 gilt die Meldepflicht für Cyberangriffe auf kritische Infrastrukturen. Sie betrifft die im Art. 74b ISG aufgeführten Behörden und Organisationen, nicht pauschal jedes Schweizer KMU.[5] Der Katalog umfasst unter anderem bestimmte Energie-, Finanz-, Gesundheits-, Verkehrs-, Telekommunikations- und Cloud-Anbieter sowie weitere öffentliche und private Betreiber. Beispielsweise erfasst das Gesetz Cloudcomputing-Anbieter mit Sitz in der Schweiz, wenn sie entsprechende Leistungen erbringen; es erfasst nicht automatisch jedes IT-Unternehmen. Für einzelne Gruppen bestehen Ausnahmen in der Cybersicherheitsverordnung (CSV). Das BACS kann auf Anfrage Auskunft über die Unterstellung geben und auf Antrag eine Verfügung erlassen.[5] [6]

Für eine erfasste Organisation ist zusätzlich zu klären, ob ein **Cyberangriff** nach Art. 74d ISG vorliegt. Meldbar ist ein Angriff, wenn er die Funktionsfähigkeit der betroffenen kritischen Infrastruktur gefährdet, Informationen manipuliert oder abfliessen lässt, länger unentdeckt blieb oder mit Erpressung, Drohung oder Nötigung verbunden ist.[5] Das ist ein anderer Test als das hohe Risiko nach DSG: Hier können auch nicht personenbezogene Informationen oder ein Verfügbarkeitsangriff relevant sein.

Die Erstmeldung an das BACS ist innert **24 Stunden nach Entdeckung** des Angriffs fällig. Sind dabei nicht alle erforderlichen Informationen bekannt, gewährt das BACS für deren Ergänzung eine Frist von **14 Tagen**.[5] [6] Das BACS stellt dafür im Cyber Security Hub ein Meldeformular bereit; alternativ beschreibt der Meldebutton eine Meldemöglichkeit ohne Plattformzugang.[8] Das Formular kann auf Wunsch an weitere zuständige Behörden, beispielsweise den EDÖB, weiterleiten. **Verlassen Sie sich im konkreten Fall nicht ungeprüft auf eine Weiterleitung:** Ordnen Sie die EDÖB-Prüfung und die BACS-Prüfung getrennt zu, klären Sie den Umfang der Weiterleitung und sichern Sie die Eingangsbestätigung.[8]

### Hypothetisches Praxisbeispiel: Ein Angriff, zwei Prüfungen

Ein **hypothetisches** Spital, das auf einer kantonalen Spitalliste steht, entdeckt Ransomware. Patientendaten sind vorübergehend nicht verfügbar; die Angreifer behaupten zudem, Daten kopiert zu haben. Das Spital trennt betroffene Systeme, sichert Beweise und bewertet die Behandlungsauswirkung. Wegen des Spitalstatus ist die BACS-Unterstellung nach Art. 74b ISG zu prüfen; die Gefährdung der Funktionsfähigkeit und der behauptete Abfluss sind mögliche BACS-Tatbestände. Die Erstmeldung muss daher gegebenenfalls innerhalb von 24 Stunden erfolgen.[5] [7]

Unabhängig davon sind Gesundheitsdaten besonders schützenswerte Personendaten. Der behauptete Abfluss kann für einzelne Patientinnen und Patienten ein voraussichtlich hohes Risiko darstellen. Der Verantwortliche muss deshalb parallel die EDÖB-Meldung «so rasch als möglich» beurteilen und die Schutzbedürftigkeit einer Betroffeneninformation prüfen.[1] [4] Das Beispiel entscheidet keine Rechtsfrage vorweg: Tatsächlicher Datenzugriff, Rollen, Unterstellung und Sofortmassnahmen sind konkret festzustellen und fachlich zu würdigen.

## In sieben Schritten vom Alarm zur nachvollziehbaren Entscheidung

1. **Vorfall eröffnen und eindämmen.** Erfassen Sie Entdeckungszeit, Meldende, Systeme, Datenquellen und erste Schutzmassnahmen. Verhindern Sie weitere Ausbreitung, ohne Untersuchungsdaten unnötig zu zerstören.
2. **Fakten in zwei Spuren ordnen.** Führen Sie eine Datenschutzspur für Personendaten, Betroffene und Risiken sowie eine Cyber-/Betriebsspur für Auswirkung, Angriff und BACS-Status. Ergänzen Sie den Stand laufend.
3. **Rollen und Verträge prüfen.** Bestimmen Sie Verantwortlichen, Auftragsbearbeiter, Versicherer, Dienstleister und allfällige regulatorische Ansprechpartner. Der Auftragsbearbeiter informiert den Verantwortlichen unverzüglich; die Zuständigkeit für die EDÖB-Meldung bleibt klar zuzuweisen.[1]
4. **EDÖB-Risiko früh beurteilen.** Beurteilen Sie Schwere und Wahrscheinlichkeit für die am stärksten betroffenen Personen. Kann ein hohes Risiko nicht innert kurzer Zeit belastbar ausgeschlossen werden, bereiten Sie eine zeitnahe Meldung vor.[4]
5. **BACS-Geltung und Angriffstatbestand separat prüfen.** Gleichen Sie die Organisation mit Art. 74b ISG und allfälligen CSV-Ausnahmen ab. Prüfen Sie danach die Kriterien des Art. 74d ISG. Bei Unsicherheit nutzen Sie die Auskunftsmöglichkeit des BACS und holen Sie rechtzeitig Fachhilfe bei.[5] [6]
6. **Melden, ergänzen, kommunizieren.** Übermitteln Sie jede erforderliche Meldung über den vorgesehenen Kanal. Reichen Sie fehlende Fakten nach, wenn dies vorgesehen ist. Bereiten Sie eine Betroffeneninformation nur auf einer geprüften Faktenbasis vor. Für die Kommunikation nach einem Angriff hilft der Beitrag [Notfallkommunikation für Schweizer KMU](/wissen/cyberangriff-kommunikation).
7. **Entscheid und Verbesserung festhalten.** Archivieren Sie Faktenstand, Risikobegründung, Meldungen, Bestätigungen, Kommunikationsfreigaben und Folgemassnahmen. Überführen Sie technische und organisatorische Lücken in Ihr [Risikomanagement](/unsere-dienstleistungen/risikomanagement) und testen Sie den Prozess im Notfallplan.

Der [EDÖB-/BACS-Entscheidungsbaum und das Vorfallsprotokoll](/resources/03-datenpanne-entscheidungsbaum) übersetzen diese Schritte in ausfüllbare Kontrollpunkte. Sie unterstützen die erste Strukturierung, nicht die fachliche Entscheidung.

## Typische Fehler, die Fristen und Schutz gefährden

| Fehler | Warum er problematisch ist | Bessere Praxis |
|---|---|---|
| Auf eine pauschale 72-Stunden-Frist warten | Das DSG verlangt eine Meldung so rasch als möglich, wenn voraussichtlich ein hohes Risiko besteht. | Nach einer kurzen, belastbaren Erstbeurteilung entscheiden und fehlende DSV-Angaben nachreichen.[1] [2] |
| EDÖB- und BACS-Prüfung zusammenziehen | Auslöser, Adressat und Frist sind verschieden. | Zwei getrennte Entscheidspuren mit einer gemeinsamen Ereignisakte führen.[1] [5] |
| Erst vollständige Forensik abwarten | Bei unklarem hohem Risiko kann dies die zeitnahe DSG-Meldung verzögern. | Früh melden, falls nötig ergänzen, und die Untersuchung fortführen.[2] [4] |
| «Kein Datenabfluss bewiesen» mit «kein Risiko» verwechseln | Ein unbefugter Zugang oder Verlust kann bereits relevant sein; Ransomware schafft oft Unsicherheit. | Zugriff, Datenarten und Ausschlussgründe nachvollziehbar bewerten.[1] [4] |
| Die Information Betroffener als automatische Folge jeder EDÖB-Meldung behandeln | Der Massstab ist der erforderliche Schutz der Betroffenen oder eine Anordnung des EDÖB. | Betroffeneninformation separat, verständlich und fachlich geprüft entscheiden.[1] |

## Meldefähigkeit ist Führungsaufgabe

Eine belastbare Entscheidung entsteht nicht erst im Incident. Geschäftsleitung und IT sollten vorab festlegen, wer den Vorfall führt, wer den Verantwortlichen vertritt, wer die BACS-Unterstellung prüft und wer Meldungen freigibt. Ebenso wichtig sind aktuelle Kontaktlisten, Zugänge zu Meldeportalen, abgestimmte Auftragsbearbeitungsverträge und ein erprobter Weg für Betroffenenkommunikation. Eine [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) kann die technischen und organisatorischen Grundlagen sichtbar machen; ein Meldeprozess muss anschliessend in der Notfallplanung tatsächlich geübt werden.

> **Nächster Schritt:** Halten Sie Fakten, Fristen und Entscheide im [Entscheidungsbaum](/resources/03-datenpanne-entscheidungsbaum) fest. Für eine Anfrage zur [DKSchV-Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) steht [Kontakt](/kontakt) zur Verfügung. Das ersetzt keine rechtliche Einzelfallbeurteilung.

## Quellen

[1]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 5 und Art. 24"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), Art. 15 zur Meldung von Datensicherheitsverletzungen"
[3]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach: Meldung von Datensicherheitsverletzungen durch Verantwortliche"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information der Betroffenen nach Art. 24 DSG, Version 1.2"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Bundesgesetz über die Informationssicherheit beim Bund (ISG), Art. 74a–74f"
[6]: https://www.fedlex.admin.ch/eli/cc/2025/169/de "Fedlex – Verordnung über die Cybersicherheit (CSV), Art. 12 sowie Art. 14–16"
[7]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[8]: https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden "BACS – Wie muss ein Cyberangriff gemeldet werden?"
[9]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[10]: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679 "EUR-Lex – Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung), Art. 33"
[11]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[12]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant, 23. Oktober 2026"
