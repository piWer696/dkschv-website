---
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/03-datenpanne-entscheidungsbaum"
titel: "EDÖB-/BACS-Entscheidungsbaum und Vorfallsprotokoll"
meta_title: "EDÖB-/BACS-Entscheidungsbaum für Datenpannen | DKSchV"
meta_description: "Arbeitsvorlage zur getrennten Strukturierung der EDÖB- und BACS-Meldeprüfung nach einem Cyber- oder Datenschutzvorfall."
suchintention: "Arbeitsmittel – Meldeprüfung bei Datenpannen strukturieren"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer Organisationen"
version: "Rechtsstand 1. November 2026 (DSG, DSV, ISG und CSV amtlich verifiziert)"
bezug: "/wissen/datenpanne-melden-schweiz"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle 12 zitierten externen Originalquellen dieses Arbeitsmittels und des zugehörigen Artikels; einschliesslich amtlicher Fedlex-Historien und ISG-XML bei stateless Leerabruf sowie einschlägiger EDÖB-/BACS-Originalmeldungen seit 18. Oktober 2026"
quellenpruefung_status: "Vollständig für die 12 zitierten externen Originalquellen geprüft am 1. November 2026; keine Fachfreigabe"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# EDÖB-/BACS-Entscheidungsbaum und Vorfallsprotokoll

**Arbeitsmittel zu:** [Datenpanne in der Schweiz: DSG-Entscheidungsbaum für EDÖB-Meldung und BACS-Pflicht](/wissen/datenpanne-melden-schweiz)  
**Quellenprüfung:** 1. November 2026; Abrufe der Originalquellen am 1. November 2026 nach 09:00 CET, zwischen 09:05 und 09:07 CET; keine Fachfreigabe  
**Rechtsstand:** 1. November 2026 (DSG, DSV, ISG und CSV amtlich verifiziert)  
**Status:** Arbeitsvorlage – allgemeine Orientierung, keine Rechtsberatung

---

## Zweck

Dieses Arbeitsmittel hilft Schweizer Organisationen, einen Cyber- oder Datenschutzvorfall in den ersten Stunden geordnet zu erfassen und zwei **separate** Meldeprüfungen vorzunehmen:

1. **EDÖB / Art. 24 DSG:** Liegt eine Verletzung der Datensicherheit mit voraussichtlich hohem Risiko für Persönlichkeit oder Grundrechte natürlicher Personen vor? Dann meldet der Verantwortliche dem EDÖB **so rasch als möglich**.[1]
2. **BACS / Art. 74a–74f ISG:** Ist die Organisation meldepflichtig und liegt ein meldepflichtiger Cyberangriff vor? Dann ist die Erstmeldung an das BACS innert **24 Stunden nach Entdeckung** erforderlich; bei fehlenden Angaben gewährt das BACS eine Frist von 14 Tagen zur Ergänzung.[4] [5] [6]

> **Wichtig:** Dieses Blatt entscheidet keine Meldepflicht. Es dokumentiert den Faktenstand für die zuständigen Entscheidpersonen. **[FACHPRÜFUNG ERFORDERLICH]** Bei hohem, unklarem oder sektorspezifischem Risiko ist umgehend eine datenschutz-, aufsichts- und gegebenenfalls strafrechtliche Fachprüfung einzuholen.

---

## Anwendung

1. Drucken Sie das Arbeitsmittel aus oder führen Sie es in einem zugriffsgeschützten Vorfallsordner.
2. Füllen Sie die Faktenfelder bei Entdeckung aus. Kennzeichnen Sie jede Angabe als **bestätigt**, **vermutet** oder **offen**.
3. Bearbeiten Sie die DSG- und die BACS-Spur parallel. Ein «Nein» in einer Spur beendet die andere nicht.
4. Erfassen Sie Entscheide, Uhrzeit, Begründung und Nachweise. Aktualisieren Sie den Stand, wenn neue Fakten eintreffen.
5. Bewahren Sie Meldungen, Empfangsbestätigungen und Nachreichungen bei der Ereignisakte auf.

---

## A. Vorfallkopf: Fakten, Verantwortung und Eindämmung

| Feld | Eintrag |
|---|---|
| Interne Vorfallsnummer | ________________________________________________ |
| Entdeckt am / um | ____________________ Datum / Uhrzeit / Zeitzone |
| Entdeckt durch | ________________________________________________ |
| Vorfallleitung | ________________________________________________ |
| Stellvertretung | ________________________________________________ |
| Entscheidzuständige Person / Geschäftsleitung | ________________________________________________ |
| Datenschutz-Ansprechperson | ________________________________________________ |
| IT-/Forensik-Ansprechperson | ________________________________________________ |
| Auftragsbearbeiter oder Provider betroffen? | ☐ Nein ☐ Ja: _________________________________ |
| Status der Fakten | ☐ bestätigt ☐ teilweise bestätigt ☐ vorläufig |
| Nächste Lagebeurteilung am / um | ________________________________________________ |

### Sofortkontrollpunkte

- ☐ Betroffene Systeme oder Konten wurden, soweit fachlich vertretbar, kontrolliert isoliert.
- ☐ Zugänge, Logdaten, Zeitstempel, Alarmmeldungen und relevante Konfigurationen wurden gesichert.
- ☐ Keine unnötigen Neustarts, Reparaturen oder Löschungen vorgenommen, bevor der forensische Bedarf beurteilt wurde.
- ☐ Der Vorfallszeitraum und der mögliche Zugriffsweg werden untersucht.
- ☐ Backups und Wiederherstellungszugänge sind gegen weitere Beeinträchtigung geschützt.
- ☐ Die Kontaktwege zu Dienstleistern, Versicherer und gegebenenfalls Behörden sind geprüft.

**Notizen zu Sofortmassnahmen, Zeit und Verantwortlichkeit:**

________________________________________________________________________________

________________________________________________________________________________

________________________________________________________________________________

Das BACS empfiehlt bei Ransomware, infizierte Systeme vom Netz zu trennen und Logdateien zu sichern. Sollen forensische Untersuchungen möglich bleiben, sollten fachkundige Personen Speicher- und Festplattensicherungen vor weiteren Reparaturversuchen oder Neustarts vornehmen.[8]

> **Verdacht ist kein Beweis:** Ein einzelnes Anzeichen, etwa ein langsames Gerät, beweist keine Schadsoftware-Infektion. Mehrere ungewöhnliche Beobachtungen rechtfertigen aber eine Untersuchung; bei geschäftlich verwendeten Geräten empfiehlt das BACS, die zuständige IT oder den Arbeitgeber zu informieren.[9]

---

## B. Entscheidungsschema: Beide Spuren prüfen

```text
[Vorfall entdeckt]
          |
          v
[Systeme schützen, Fakten sichern, Vorfallsleitung einsetzen]
          |
          +-----------------------------+-----------------------------+
          |                                                           |
          v                                                           v
[DSG-SPUR]                                                   [BACS-SPUR]
Sind Personendaten natürlicher Personen                    Gehört die Organisation zu Art. 74b ISG
betroffen und unbefugt/verloren/verändert?                 (unter Berücksichtigung CSV-Ausnahmen)?
          |                                                           |
   Nein --+--> Art. 24 DSG nicht ausgelöst;                      Nein --+--> Keine BACS-Pflicht
          |     andere Pflichten prüfen.                                  aus diesem Grund;
          Ja                                                                  andere Pflichten prüfen.
          |                                                           |
          v                                                           Ja / unklar
Besteht voraussichtlich ein hohes Risiko                          |
für Persönlichkeit oder Grundrechte?                              v
          |                                              Liegt ein Cyberangriff nach Art. 74d ISG vor?
   Nein --+--> Begründung dokumentieren;                          |-- gefährdete Funktionsfähigkeit?
          |     weitere Pflichten prüfen.                          |-- Manipulation oder Informationsabfluss?
          Ja                                                      |-- längere Zeit unentdeckt?
          |                                                      |-- Erpressung, Drohung oder Nötigung?
          v                                                           |
[EDÖB: Verantwortlicher meldet so rasch als möglich]              Nein --+--> Begründung dokumentieren;
[DSV-Angaben ergänzen, falls nötig]                               |         andere Pflichten prüfen.
[Betroffeneninformation getrennt prüfen]                          Ja / unklar
                                                                      |
                                                                      v
                                                         [BACS: Erstmeldung innert 24 Stunden
                                                          nach Entdeckung; BACS gewährt bei fehlenden
                                                          Angaben 14 Tage zur Ergänzung]
```

**Entscheidregeln:**

- Eine **Datensicherheitsverletzung** bedeutet, dass Personendaten unbeabsichtigt oder widerrechtlich verlorengehen, gelöscht, vernichtet oder verändert werden oder Unbefugten offengelegt beziehungsweise zugänglich gemacht werden.[1]
- Für die EDÖB-Meldung ist nicht jede Datenpanne massgeblich, sondern ein **voraussichtlich hohes Risiko**. Beurteilen Sie Schwere und Wahrscheinlichkeit für die am stärksten betroffenen Personen. Bei Zweifel, der ein hohes Risiko nicht innert kurzer Zeit ausschliesst, soll nicht auf lange Abklärungen gewartet werden.[3]
- Die BACS-Pflicht trifft nicht pauschal alle KMU. Sie folgt dem Katalog in Art. 74b ISG und den Ausnahmen der CSV. Das BACS kann auf Anfrage zur Unterstellung Auskunft geben und auf Antrag verfügen.[4] [5]
- Eine EDÖB-Meldung und eine BACS-Meldung können nebeneinander nötig sein. Prüfen Sie sie getrennt.

---

## C. DSG-Spur: EDÖB-Prüfung nach Art. 24 DSG

### C1. Liegt eine Datensicherheitsverletzung mit Personendaten vor?

| Kontrollpunkt | Ergebnis / Notiz |
|---|---|
| Betroffene Systeme, Anwendungen, Dateien oder Papierakten | ________________________________________________ |
| Welche Personendaten? | ________________________________________________ |
| Besonders schützenswerte Daten, Identitätsdokumente, Zahlungsdaten oder andere sensible Kontexte? | ________________________________________________ |
| Welche Personen sind betroffen? (z. B. Kundschaft, Mitarbeitende, Patientinnen/Patienten) | ________________________________________________ |
| Geschätzte Anzahl Personen / Datenobjekte | ________________________________________________ |
| Was geschah? ☐ Verlust ☐ Löschung ☐ Veränderung ☐ Offenlegung ☐ unbefugter Zugang ☐ anderes | ________________________________________________ |
| Zeitpunkt, Dauer und möglicher Umfang | ________________________________________________ |
| Beleg für tatsächlichen oder möglichen Zugriff durch Unbefugte | ________________________________________________ |
| Verantwortlicher nach DSG | ________________________________________________ |
| Auftragsbearbeiter meldete dem Verantwortlichen am / um | ________________________________________________ |

**Rollen und Datenfluss vor dem Entscheid festhalten:** Notieren Sie pro betroffenem Dienstleister mindestens die bearbeiteten Datenkategorien, die festgestellten oder möglichen Übermittlungen, den Verantwortlichen, den Auftragsbearbeiter, die vertraglich vereinbarten Vorfallkontakte und den tatsächlichen Erreichbarkeitsweg. Die EDÖB-Mitteilung zur hängigen Untersuchung gegen die PK Softech AG zeigt, dass bei einem Lieferantenvorfall gerade übermittelte Personendaten, Rechtsgrundlagen, tatsächliche Datenübertragungen und der Umfang abgeflossener Informationen abgeklärt werden können. Sie stellt weder einen abschliessenden Verstossbefund noch eine neue allgemeine Meldefrist dar.[10]

### C2. Risiko für Betroffene begründen

Kreuzen Sie nur an, was faktenbasiert ist, und begründen Sie die Einschätzung.

- ☐ Besonders schützenswerte Personendaten können betroffen sein.
- ☐ Die Daten erleichtern Identitätsdiebstahl, Zahlungsbetrug, Diskriminierung, Rufschädigung oder Vermögensschäden.
- ☐ Minderjährige, Personen mit Behinderungen oder andere besonders verletzliche Personen können betroffen sein.
- ☐ Die Daten erlauben eine einfache Bestimmung einzelner Personen.
- ☐ Unberechtigte Dritte, Erpressung, Veröffentlichung oder ein breiter Empfängerkreis sind möglich oder bestätigt.
- ☐ Die Daten waren wirksam verschlüsselt; eine Zugriffsmöglichkeit auf den Schlüssel durch Unbefugte ist nachweislich ausgeschlossen.
- ☐ Die Daten waren nur pseudonymisiert; eine Re-Identifikation ist möglich.
- ☐ Sofortmassnahmen haben das Risiko nachweislich ausgeschlossen oder gemindert. Nachweis: ____________________________

| Beurteilung | Eintrag |
|---|---|
| Schwere der möglichen Folgen für die am stärksten betroffenen Personen | ☐ tief ☐ mittel ☐ hoch – Begründung: __________________________ |
| Wahrscheinlichkeit der möglichen Folgen | ☐ tief ☐ mittel ☐ hoch – Begründung: __________________________ |
| Voraussichtlich hohes Risiko? | ☐ Ja ☐ Nein ☐ unklar – bei unklar: **[FACHPRÜFUNG ERFORDERLICH]** veranlasst am: __________ |
| EDÖB-Meldung erforderlich? | ☐ Ja ☐ Nein ☐ noch zu entscheiden – Entscheid durch: __________ |
| Entscheiduhrzeit und Faktenstand | ________________________________________________ |

Der EDÖB nennt Datenart und Kontext, Art der Verletzung, Bestimmbarkeit, mögliche Auswirkungen und die Wahrscheinlichkeit als relevante Gesichtspunkte. Besonders schützenswerte Daten sprechen in vielen Fällen für ein hohes Risiko. Eine hohe Zahl Betroffener genügt für sich allein dagegen nicht.[3]

### C3. EDÖB-Meldung und Betroffeneninformation

**Falls EDÖB-Meldung bejaht oder fachlich empfohlen:**

- ☐ Meldung durch den Verantwortlichen **so rasch als möglich** veranlasst.
- ☐ Art der Verletzung beschrieben.
- ☐ Zeitpunkt und Dauer, soweit möglich, erfasst.
- ☐ Kategorien und ungefähre Anzahl betroffener Daten und Personen erfasst.
- ☐ Folgen und Risiken für Betroffene beschrieben.
- ☐ Getroffene und vorgesehene Abhilfe- und Minderungsmassnahmen dokumentiert.
- ☐ Kontaktperson für Rückfragen benannt.
- ☐ Fehlende Angaben, Frist und Verantwortlichkeit zur Nachreichung festgelegt.
- ☐ EDÖB-Meldung via DataBreach übermittelt; Bestätigung gesichert.

| Feld | Eintrag |
|---|---|
| EDÖB-Meldung übermittelt am / um | ________________________________________________ |
| Übermittelnde Person | ________________________________________________ |
| Referenz / Bestätigung abgelegt unter | ________________________________________________ |
| Fehlende Angaben und Termin zur Nachreichung | ________________________________________________ |
| Ist Betroffeneninformation zum Schutz erforderlich? | ☐ Ja ☐ Nein ☐ unklar – **[FACHPRÜFUNG ERFORDERLICH]**: _________________________ |
| Entscheid zur Betroffeneninformation, Begründung und Freigabe | ________________________________________________ |

Art. 15 DSV benennt die Angaben einer EDÖB-Meldung und erlaubt das rasche Nachreichen fehlender Informationen. Betroffene sind zu informieren, wenn dies zu ihrem Schutz erforderlich ist oder der EDÖB es verlangt. Ausnahmen und die konkrete Kommunikation brauchen im Einzelfall eine fachliche Prüfung.[1] [2]

---

## D. BACS-Spur: Unterstellung und Cyberangriff prüfen

### D1. Unterstellung der Organisation

| Kontrollpunkt | Ergebnis / Nachweis |
|---|---|
| Unternehmen / Behörde / Organisation | ________________________________________________ |
| Betroffene Tätigkeit oder Dienstleistung | ________________________________________________ |
| Möglicher Tatbestand nach Art. 74b ISG | ☐ Energie ☐ Finanzmarkt ☐ Gesundheit ☐ Verkehr ☐ Telekommunikation ☐ Cloud/Rechenzentrum ☐ andere: __________ |
| Wirkt sich der Angriff auf eine Tätigkeit nach Art. 74b ISG in der Schweiz aus? | ☐ Ja ☐ Nein ☐ unklar |
| Denkbare Ausnahme nach Art. 12 CSV? | ☐ Nein ☐ Ja ☐ unklar – Begründung: __________________________ |
| BACS-Unterstellung durch interne Prüfung, BACS-Auskunft oder Verfügung abgeklärt? | ________________________________________________ |
| **[FACHPRÜFUNG ERFORDERLICH]** / BACS-Anfrage ausgelöst am | ________________________________________________ |

### D2. Angriffstatbestand und Frist

| Kontrollpunkt | Ergebnis / Nachweis |
|---|---|
| Zeitpunkt der **Entdeckung** des Cyberangriffs | ____________________ Datum / Uhrzeit / Zeitzone |
| Funktionsfähigkeit der kritischen Infrastruktur gefährdet? | ☐ Ja ☐ Nein ☐ unklar – Details: _____________________________ |
| Manipulation von Informationen? | ☐ Ja ☐ Nein ☐ unklar – Details: _____________________________ |
| Abfluss von Informationen? | ☐ Ja ☐ Nein ☐ unklar – Details: _____________________________ |
| Längere Zeit unentdeckt / Hinweise auf Vorbereitung weiterer Angriffe? | ☐ Ja ☐ Nein ☐ unklar – Details: _____________________________ |
| Erpressung, Drohung oder Nötigung? | ☐ Ja ☐ Nein ☐ unklar – Details: _____________________________ |
| BACS-Meldung erforderlich oder vorsorglich fachlich empfohlen? | ☐ Ja ☐ Nein ☐ unklar |
| 24-Stunden-Zeitpunkt für Erstmeldung | ________________________________________________ |
| Verantwortliche Person für BACS-Meldung | ________________________________________________ |

### D3. BACS-Meldung durchführen und nachreichen

- ☐ Erstmeldung an BACS spätestens innerhalb von 24 Stunden nach Entdeckung vorbereitet.
- ☐ Meldeweg festgelegt: ☐ Cyber Security Hub ☐ alternative Meldemöglichkeit.
- ☐ Zeit, Umfang, Auswirkungen und bisherige Massnahmen sachlich beschrieben.
- ☐ Weitere zuständige Behörden und vertragliche Meldewege separat geprüft.
- ☐ Gewünschte Weiterleitung an andere Behörde kontrolliert und dokumentiert.
- ☐ Empfangsbestätigung abgelegt.
- ☐ Fehlende Angaben, verantwortliche Person und die vom BACS gewährte 14-Tage-Frist zur Ergänzung festgelegt.

Das BACS beschreibt die verfügbaren Meldewege und die erforderlichen Angaben für die Erstmeldung auf seiner Informationsseite zum Meldeprozess.[7]

| Feld | Eintrag |
|---|---|
| BACS-Erstmeldung übermittelt am / um | ________________________________________________ |
| Übermittelnde Person | ________________________________________________ |
| Referenz / Bestätigung abgelegt unter | ________________________________________________ |
| Ergänzung fällig am / um | ________________________________________________ |
| Ergänzung übermittelt am / um | ________________________________________________ |

Art. 74d ISG nennt Gefährdung der Funktionsfähigkeit, Manipulation oder Abfluss von Informationen, länger unentdeckte Angriffe sowie Erpressung, Drohung oder Nötigung als Meldekriterien. Art. 74e ISG verlangt die Erstmeldung innert 24 Stunden nach Entdeckung; bei fehlenden Angaben gewährt das BACS nach Art. 16 CSV eine Frist von 14 Tagen zur Ergänzung.[4] [5] [6]

---

## E. Abschluss, Freigabe und Nachbearbeitung

| Kontrollpunkt | Eintrag |
|---|---|
| Welche weiteren Stellen wurden geprüft? (z. B. Police, Versicherer, Vertragspartner, kantonale Vorgaben, FINMA) | ________________________________________________ |
| Entscheide, die eine Fachprüfung erforderten | ________________________________________________ |
| Offene Fragen und Eigentümer | ________________________________________________ |
| Ursachenanalyse und technische Verbesserungen | ________________________________________________ |
| Vertragliche / organisatorische Verbesserungen | ________________________________________________ |
| Datum der Nachbesprechung | ________________________________________________ |
| Verantwortliche Person für Massnahmenverfolgung | ________________________________________________ |
| Abschluss durch | ______________________________ Datum: __________ |

---

## Grenzen des Arbeitsmittels

Diese Vorlage erfasst weder alle sektoralen noch alle vertraglichen Melde-, Informations- oder Aufbewahrungspflichten. Insbesondere kann die Unterstellung unter Art. 74b ISG von der konkreten Tätigkeit, den CSV-Ausnahmen und der Auswirkung des Angriffs abhängen. Das BACS kann hierzu Auskunft erteilen und auf Antrag verfügen.[4] Eine EDÖB-Meldung, eine BACS-Meldung, eine Meldung an eine Aufsichtsbehörde, eine Strafanzeige oder eine Betroffeneninformation können parallel geprüft werden; keine ersetzt automatisch die andere.

Die Checkpunkte sind keine Zusicherung, dass eine Meldung rechtzeitig, vollständig oder rechtlich ausreichend ist. **[FACHPRÜFUNG ERFORDERLICH]** Eine konkrete Risikobewertung, die Auslegung von Ausnahmegründen und jede externe Kommunikation brauchen bei Unsicherheit eine angemessene Fachprüfung. Aktualisieren Sie die Vorlage bei Änderungen von DSG, DSV, ISG, CSV oder behördlichen Vorgaben.

## Quellen

[1]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 5 und Art. 24"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), Art. 15 zur Meldung von Datensicherheitsverletzungen"
[3]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information der Betroffenen nach Art. 24 DSG, Version 1.2"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Bundesgesetz über die Informationssicherheit beim Bund (ISG), Art. 74a–74f"
[5]: https://www.fedlex.admin.ch/eli/cc/2025/169/de "Fedlex – Verordnung über die Cybersicherheit (CSV), Art. 12 sowie Art. 14–16"
[6]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[7]: https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden "BACS – Wie muss ein Cyberangriff gemeldet werden?"
[8]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[9]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[10]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant, 23. Oktober 2026"
