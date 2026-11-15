---
arbeitsmittel: "Risikoregister-Vorlage für Cyberrisiken im KMU"
passender_artikel: /wissen/it-sicherheitscheck-kmu
version: "1.4"
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/08-risikoregister-vorlage"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
stand: "15. November 2026"
quellenpruefung_umfang: "Alle 17 Original-URLs dieser Vorlage direkt abgerufen und hinsichtlich der zitierten Aussagen gelesen; im Artikelpaar insgesamt 21 zitierte und 11 ergänzende Original-URLs einschliesslich Fedlex-History/XML und gezieltem BACS-/KEV-/Herstellerabgleich seit 1. November sowie NIST-Vormerkung vom 27. Oktober. Tatsächliche Rückgaben am 15. November nach 09:00 CET."
quellenpruefung_status: "17 Vorlagenquellen inhaltlich auslesbar; im ergänzenden Artikelpaar-Abgleich 1 BACS-KMU-DOCX nur als kodierter Binärtext, Inhalt nicht geprüft. Ausgabegrenzen bei langen Quellen dokumentiert. Keine Fach-, Rechts-, Forensik-, Produkt- oder Einzelfallfreigabe; interne Paketziele nicht live und kein CMS geprüft."
---

# Risikoregister-Vorlage für Cyberrisiken im KMU

> **[FACHPRÜFUNG ERFORDERLICH]** Datenschutz-, Vertrags- und sektorale Anforderungen sowie die Risikokriterien müssen vor Verwendung durch zuständige Fachpersonen geprüft werden.

**Arbeitsmittel zu:** [IT-Sicherheitscheck für Schweizer KMU: So wird aus Befunden ein priorisiertes Cyber-Risikoregister](/wissen/it-sicherheitscheck-kmu)  
**Version:** 1.4 | **Quellenstand:** 15. November 2026 (Quellenprüfung; keine Fach- oder Rechtsfreigabe)  
**Organisation:** ________________________________  
**Register-Verantwortung:** ________________________________  
**Letzte Überprüfung:** ________________________________
**Nächste Überprüfung:** ________________________________

## Zweck

Diese Vorlage hilft Geschäftsleitung, Fachbereichen und IT, technische Befunde in nachvollziehbare **Cyber-Risikoszenarien** zu übersetzen und deren Behandlung zu steuern. Ein Risikoszenario beschreibt, was aufgrund einer Schwachstelle oder Abhängigkeit passieren könnte und welche geschäftliche Folge daraus entstehen kann. Das Register macht Priorität, Verantwortlichkeit, Massnahme, Nachweis und Restrisiko sichtbar.

Die Vorlage ist für eine risikobasierte Arbeitsweise bestimmt. Der NIST-Leitfaden für kleine Unternehmen empfiehlt ebenfalls, Cyberrisiken, Massnahmen und Verantwortlichkeiten nachvollziehbar zu priorisieren.[3] Die Vorlage ersetzt weder technische Prüfungen, Schwachstellenscans, Datenschutz-Folgenabschätzungen noch eine individuelle rechtliche oder fachliche Beurteilung.

## Anwendung

1. Erfassen Sie zunächst wichtige Geschäftsprozesse und die dafür notwendigen Systeme, Daten, Konten und Dienstleister. Das BACS empfiehlt diese Reihenfolge auch in seiner Cybersicherheits- und Resilienzmethode.[1]
2. Übernehmen Sie geprüfte Befunde aus Sicherheitschecks, Betriebsereignissen, Lieferantenprüfungen oder Wiederherstellungstests. Notieren Sie für jeden Befund eine Evidenz, etwa eine Befund-ID oder einen Konfigurationsnachweis. Bei Verdacht auf Schadsoftware dokumentieren Sie den Befundstatus, etwa «Verdacht», «untersucht» oder «bestätigt»: Ein einzelnes Anzeichen ist noch kein Infektionsbeweis, mehrere ungewöhnliche Beobachtungen sollten genauer untersucht werden. Das BACS empfiehlt bei Verdacht die Untersuchung durch eine Fachperson sowie bei geschäftlich genutzten Geräten die Information der zuständigen IT-Stelle.[4]
3. Formulieren Sie das Risiko als Satz: **Wenn** eine Bedrohung eine Schwachstelle oder Abhängigkeit ausnutzt, **dann** tritt ein Ereignis ein, **wodurch** eine geschäftliche Folge entsteht.
4. Bewerten Sie Auswirkung und Eintrittswahrscheinlichkeit unter Berücksichtigung der nachweislich bestehenden Kontrollen. Legen Sie die Skala vor der ersten Bewertung fest und verwenden Sie sie einheitlich.
5. Benennen Sie Risiko- und Massnahmen-Eigentümer. Schliessen Sie eine Zeile erst, wenn das Abnahmekriterium erfüllt und die Restbewertung geprüft ist.
6. Legen Sie Top-Risiken dem zuständigen Führungsgremium zur Entscheidung vor und überführen Sie relevante Ausfallszenarien in die Notfallplanung.

**Methodengrenze:** Die CSRM nutzt einen erweiterten Grundschutz und eine qualitative Schutzbedarfsbewertung; das amtliche Dokument vom 24. November 2025 verzichtet ausdrücklich auf eine vollständige Risikoanalyse und Quantifizierung.[9] Dieses Register ergänzt die Prozesssicht um Geschäftsentscheide. Seine Skala ist kein offizieller CSRM-Prüfkatalog, keine Zertifizierung und keine Bestätigung erfüllter Anforderungen. Dokumentieren Sie auch Abhängigkeiten zu vorläufig zurückgestellten Schutzobjekten.[1]

**Nachweise zuordnen:** Notieren Sie Beobachtungsdatum, Schutzobjekt, tatsächlichen Lauf- oder Paketstand, Zugangspfad, Prüfumfang und zuständige Person. Trennen Sie öffentliche Warnung, mögliche Produktbetroffenheit und bestätigten lokalen Befund. Ein Warnungs- oder KEV-Eintrag ersetzt weder die Prüfung der konkreten Instanz noch einen Nachweis ihrer Kompromittierung.[5] [12] Fehlende Nachweise erhalten einen Klärungsauftrag mit Eigentümer und Termin; «nicht geprüft» bedeutet nicht «nicht betroffen».

**Homeoffice und OT einbeziehen:** Erfassen Sie geschäftliche Zugangspfade und bekannte Grenzen der Netztrennung, wenn private Heimnetze für die Arbeit genutzt werden. Das BACS nennt bei exponierten Heimdiensten Segmentierung, beschränkte Zugriffe, VPN und möglichst einen zweiten Faktor als Schutzpunkte; es liefert keine konkrete Plex-Fixversion.[10] Prüfen Sie ausserdem betriebliche Steuerungen samt direkten, indirekten und dienstleisterbetriebenen Fernwartungswegen. Die Warnung zu Kühlanlagen vom 10. November 2026 ist ein Beispiel für mögliche Waren- und Betriebsfolgen, keine Bestätigung der eigenen Gerätebetroffenheit.[11] Private Geräte dürfen daraus nicht pauschal als geprüft oder für uneingeschränkte Prüfungen freigegeben gelten.

### Zusätzliche Kontrollpunkte bei Komponenten und KI

Ergibt ein Befund eine möglicherweise betroffene eingebettete oder extern betriebene Komponente, erfassen Sie zusätzlich Produkt, Komponente, tatsächlichen Lauf- oder Paketstand, Erreichbarkeit und Betreiber. Verlangen Sie vom Hersteller, Hoster oder Dienstleister eine Fixbestätigung für die konkrete Instanz und prüfen Sie den Nachweis des tatsächlich laufenden, behobenen Stands. Eine reine Hauptversionsangabe genügt bei zurückportierten Sicherheitskorrekturen nicht zwingend.[5]

Bei einem KI-gestützten Prozess dokumentieren Sie, welche Funktion von dem Dienst abhängt, welche Kapazitäts-, Budget- oder Quotenannahme gilt, ab welchen Schwellen gewarnt wird und wer bei eingeschränkter Verfügbarkeit entscheidet. Ergänzen Sie einen manuellen oder anderen Ausweichablauf, soweit der Prozess kritisch ist. Die Orientierung zu KI-Tokenverbrauch nennt risikobasierte Priorisierung, Monitoring, Warnschwellen sowie Kapazitäts- und Ausweichplanung als mögliche organisatorische Massnahmen.[6] [7]

Bei KI-Agenten erfassen Sie zudem die eigene Identität, den konkreten Auftrag, angebundene Daten und Werkzeuge, zulässige Netzwerkverbindungen und mögliche externe Wirkungen. Für Handlungen mit hohem Schadenspotenzial oder geringer Rückgängigkeitsmöglichkeit sind menschliche Freigabe, Protokollierung und ein auf die Aufgabe begrenzter Berechtigungsumfang als mögliche Kontrollen zu beurteilen.[8] Diese Punkte sind keine Freigabe eines Agenten und begründen keine Aussage über eine konkrete Schwachstelle oder einen Patchstand.

Prüfen Sie zusätzlich, welche vom Modell getrennte Stelle Berechtigungsregeln durchsetzt, wie Zugriffe deterministisch entschieden und Rechte widerrufen werden sowie ob der Agent seine eigenen Nachweise verändern kann. Diese Punkte greifen die vorgeschlagenen NIST-Gestaltungsgrundsätze vom 27. Oktober 2026 auf, keinen finalen verbindlichen Standard.[17] Die kanadische Orientierung empfiehlt eine vorsichtige Einführung für nicht sensible Aufgaben mit niedrigem Risiko. Eine menschliche Freigabe allein ist keine Legitimation eines Hochrisikoeinsatzes.[8]

**Datierter Prüfkontext, 15. November 2026:** KEV führt SonicWall CVE-2026-19868 seit 6. November, Apple CVE-2024-27834 seit 4. November und WordPress CVE-2026-119977 seit 3. November 2026.[12] Erfassen Sie dies bei passenden Produkten als Prüfauftrag, nicht als bestätigten Befund. Bei SonicWall sind Modellgeneration, Build, SAML und alternative Authentisierung zu prüfen; die Revision vom 9. November ergänzt einen Workaround, dessen Eignung separat fachlich zu beurteilen ist.[13] Bei WordPress zählen Versionslinie, Backport und tatsächlich ausgelieferter Hosterstand.[14] Bei Apple sind historische CVE-Fixes von aktuellen, gerätespezifischen Sicherheitsreleases zu trennen.[15] [16] KEV-Fristen sind hier keine Schweizer gesetzlichen Fristen. Keine Produkt-, Patch-, Konfigurations- oder Vorfallfreigabe folgt aus diesem Kontext.

## Registerrahmen und Bewertungsskala

**Zuständiges Entscheidgremium:** ____________________________________________  
**Berichtsintervall:** ☐ monatlich ☐ quartalsweise ☐ nach Ereignis ☐ anderes: __________  
**Risikotoleranz / Eskalationsregel:** ________________________________________________

| Stufe | Auswirkung auf Geschäft, Daten oder Verpflichtungen | Eintrittswahrscheinlichkeit im eigenen Umfeld |
|---|---|---|
| 1 – niedrig | Geringe, kurzfristig beherrschbare Beeinträchtigung; kein kritischer Prozess betroffen. | Ausnutzung im aktuellen Umfeld wenig plausibel; wirksame Kontrollen sind nachgewiesen. |
| 2 – mittel | Spürbare Beeinträchtigung eines Bereichs, zusätzliche Arbeit oder begrenzter Unterbruch. | Ausnutzung ist möglich; Kontrollen sind teilweise vorhanden oder nicht vollständig überprüft. |
| 3 – hoch | Kritischer Prozess, vertrauliche oder wichtige Daten, Vertrags- oder Meldeabklärungen könnten betroffen sein. | Ausnutzung ist plausibel; Exponierung, fehlende Kontrolle oder bekannte Abhängigkeit erhöhen das Risiko. |
| 4 – sehr hoch | Schwerer oder länger dauernder Geschäftsausfall, erhebliche Beeinträchtigung von Daten oder wesentlichen Verpflichtungen möglich. | Ausnutzung ist unmittelbar oder wiederholt plausibel; wirksame Kontrolle fehlt. |

**Bewertungsregel:** Priorität = Auswirkung ___ × Wahrscheinlichkeit ___ = ___ .  
**Hinweis:** Die Multiplikation ist eine Orientierung, kein Ersatz für den Geschäftsentscheid. Bei sehr hoher Auswirkung, privilegierten Zugängen, externer Exponierung oder einer dringenden Verpflichtung ist eine Eskalation auch unabhängig vom Produktwert zu prüfen.

## Risikoregister

| ID | Befundstatus, Befund und Evidenz | Betroffener Prozess / Schutzobjekt | Risikoszenario: Wenn … dann … wodurch … | Bestehende Kontrollen und Nachweis | Auswirkung (1–4) | Wahrscheinlichkeit (1–4) | Priorität / Entscheid | Risiko-Eigentümer | Massnahme, Abnahmekriterium und Massnahmen-Eigentümer | Zieltermin / Status | Restrisiko, Entscheidung und Prüftermin |
|---|---|---|---|---|---:|---:|---|---|---|---|---|
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |
| CR-___ |  |  |  |  |  |  |  |  |  |  |  |

## Einzelblatt für ein priorisiertes Risiko

**Risiko-ID:** CR-__________  
**Datum der Erfassung:** ____________________  
**Letzte Überprüfung:** ____________________

### 1. Kontext und Evidenz

**Betroffener Geschäftsprozess:** ________________________________________________  
**Systeme, Daten, Konten oder Dienstleister:** _______________________________________  
**Befundstatus:** ☐ Verdacht ☐ untersucht ☐ bestätigt ☐ anderer: ____________________  
**Technischer oder organisatorischer Befund:** _________________________________________  
**Evidenz / Quelle / Befund-ID:** ___________________________________________________

**Beobachtungsdatum / Prüfumfang / prüfende Stelle / bekannte Nachweisgrenzen:**  
__________________________________________________________________________________

**Exposition:** ☐ direkt aus dem Internet ☐ indirekter Fernzugriff ☐ intern ☐ unbekannt  
**Zugangspfad / Netzsegment / Authentisierung / Nachweisdatum:**  
__________________________________________________________________________________

**Geschäftlicher Homeoffice- oder OT-Bezug / Betreiber / noch zu klärende Abhängigkeiten:**  
__________________________________________________________________________________

**Öffentliche Warnung / Herstellerrevision / CVE und getrenntes Ergebnis der lokalen Modell-, Versions- und Konfigurationsprüfung:**  
__________________________________________________________________________________

**Bei eingebetteter oder externer Komponente: Produkt / Komponente / Lauf- oder Paketstand / Betreiber:**  
__________________________________________________________________________________

**Betreiber-Fixbestätigung und überprüfter Nachweis (falls einschlägig):**  
__________________________________________________________________________________

### 2. Risikoszenario

**Bedrohung oder Auslöser:** ________________________________________________________  
**Schwachstelle oder Abhängigkeit:** __________________________________________________  
**Szenario:** Wenn __________________________________________________________________  
__________________________________________________________________________________  
**Mögliche geschäftliche Folgen:** ☐ Verfügbarkeit ☐ Vertraulichkeit ☐ Integrität ☐ Nachvollziehbarkeit ☐ Vertrag / Kunde ☐ Finanzen ☐ Andere: ____________________

**Bei KI-gestütztem Prozess (falls einschlägig): Dienst / kritische Funktion / Kapazitäts-, Budget- oder Quotenannahme:**  
__________________________________________________________________________________

**Warnschwellen, Ausweichablauf und Entscheidkontakt:**  
__________________________________________________________________________________

**Bei KI-Agent (falls einschlägig): Identität / Auftrag / Daten und Werkzeuge / zulässige Netzwerkverbindungen / mögliche externe Wirkung:**  
__________________________________________________________________________________

**Unabhängige Berechtigungsdurchsetzung / Widerruf / Schutz der Nachweise vor Agentenänderung, soweit einschlägig:**  
__________________________________________________________________________________

### 3. Bewertung vor der Massnahme

**Auswirkung (1–4):** ______  **Begründung:** ________________________________________  
**Eintrittswahrscheinlichkeit (1–4):** ______  **Begründung:** __________________________  
**Priorität / Eskalation:** ____________________________________________________________

**Bestehende Kontrollen:** __________________________________________________________  
**Kontrollnachweis und bekannte Grenzen:** ____________________________________________

### 4. Behandlung und Verantwortlichkeit

**Behandlungsart:** ☐ reduzieren ☐ vermeiden ☐ übertragen ☐ befristet akzeptieren ☐ weiter analysieren  
**Risiko-Eigentümer (Name / Funktion):** ______________________________________________  
**Massnahmen-Eigentümer (Name / Funktion):** _________________________________________

**Massnahme als überprüfbares Ergebnis:**  
__________________________________________________________________________________  
__________________________________________________________________________________

**Abnahmekriterium / benötigter Nachweis:**  
__________________________________________________________________________________

**Abhängigkeiten, Ressourcen oder Entscheidbedarf:**  
__________________________________________________________________________________

**Zieltermin:** ____________________  **Status:** ☐ offen ☐ in Umsetzung ☐ abgenommen ☐ überfällig

### 5. Restrisiko und Führungentscheid

**Bewertung nach Massnahme:** Auswirkung ______ × Wahrscheinlichkeit ______ = ______  
**Begründung des Restrisikos:** ______________________________________________________  
**Entscheid:** ☐ akzeptiert ☐ weitere Massnahme ☐ eskalieren ☐ geschlossen nach Nachweis  
**Entscheider / Gremium:** ____________________  **Datum:** ____________________  
**Nächster Prüftermin:** ____________________

## Kontrollpunkte vor dem Schliessen eines Eintrags

- ☐ Das Szenario nennt Ursache, Ereignis und geschäftliche Folge; es ist mehr als eine technische Befundbezeichnung.
- ☐ Der betroffene Prozess, die Schutzobjekte und die Evidenz sind dokumentiert.
- ☐ Befunddatum, Prüfumfang, Exposition und Nachweisgrenzen sind dokumentiert; offene Klärungsaufträge haben Eigentümer und Termin.
- ☐ Warnung oder KEV-Kontext sind von lokaler Modell-, Versions-, Konfigurations- und Vorfallprüfung getrennt.
- ☐ Geschäftliche Homeoffice- und OT-Abhängigkeiten samt Fernwartungswegen sind beurteilt, soweit einschlägig.
- ☐ Auswirkung und Wahrscheinlichkeit sind nach der festgelegten Skala begründet.
- ☐ Bestehende Kontrollen sind nachweisbar; ihre Grenzen sind bekannt.
- ☐ Risiko-Eigentümer und Massnahmen-Eigentümer sind benannt.
- ☐ Die Massnahme hat ein Abnahmekriterium und einen Termin.
- ☐ Das Restrisiko wurde nach Umsetzung neu bewertet und durch die zuständige Instanz entschieden.
- ☐ Bei einer eingebetteten oder extern betriebenen Komponente sind Betreiber, konkreter Fixnachweis und tatsächlich laufender Stand festgehalten, soweit einschlägig.
- ☐ Bei einem KI-gestützten kritischen Prozess sind Kapazitäts- oder Budgetannahmen, Warnschwellen und Ausweichablauf beurteilt, soweit einschlägig.
- ☐ Bei einem KI-Agenten sind Identität, Werkzeug- und Netzwerkzugriffe, mögliche externe Wirkungen sowie notwendige menschliche Freigaben beurteilt, soweit einschlägig.
- ☐ Bei einem KI-Agenten sind unabhängige Berechtigungsdurchsetzung, Widerruf und Nachweisschutz beurteilt, soweit einschlägig.
- ☐ Ein kritisches Ausfallszenario ist in der [IT-Notfallplanung](https://www.dkschv.ch/notfallplanung.html) berücksichtigt.
- ☐ Relevante Datenschutz-, Vertrags- oder sektorale Anforderungen wurden fachlich geprüft.

## Grenzen und fachliche Prüfung

Die Vorlage schafft Transparenz, garantiert aber weder die Vollständigkeit aller Risiken noch die Vermeidung von Cybervorfällen. Eine niedrige Bewertung oder eine akzeptierte Restrisikoentscheidung ist keine Sicherheitsgarantie. Bewerten Sie Annahmen neu, wenn sich Prozesse, Systeme, Bedrohungslage, Lieferanten oder gesetzliche und vertragliche Anforderungen ändern.

Bei Personendaten verlangt das DSG eine dem Risiko angemessene Datensicherheit. Die DSV nennt für die Beurteilung unter anderem Schutzbedarf, Ursache und Gefahr, vorhandene oder vorgesehene Massnahmen sowie Wahrscheinlichkeit und Schwere einer Datensicherheitsverletzung.[2] **[FACHPRÜFUNG ERFORDERLICH]** Ob eine konkrete Datenbearbeitung, ein Vertrag oder eine mögliche Meldung rechtliche Pflichten auslöst, ist durch qualifizierte Datenschutz- oder Rechtsfachpersonen zu beurteilen. Dieses Arbeitsmittel ist keine individuelle Rechtsberatung.

Für eine methodische Einordnung können Sie die [Sicherheitsanalyse](https://www.dkschv.ch/sicherheitsanalyse.html) und das [Risikomanagement](https://www.dkschv.ch/risikomanagement.html) von DKSchV konsultieren.

## Quellen

[1]: https://www.bacs.admin.ch/de/cybersicherheits-und-resilienzmethode-csrm "BACS – Cybersicherheits- und Resilienzmethode (CSRM)"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), Art. 1–3"
[3]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf "NIST – Cybersecurity Framework 2.0 Small Business Quick-Start Guide"
[4]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion"
[5]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen"
[6]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA – Managing AI Token Consumption for Operational Resilience"
[7]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI Token Consumption for Operational Resilience"
[8]: https://www.cyber.gc.ca/en/guidance/careful-adoption-agentic-ai "Canadian Centre for Cyber Security – Careful adoption of agentic AI"
[9]: https://www.bacs.admin.ch/dam/de/sd-web/KKDLbrGSAwdL/methode-csrm-2025-de.pdf "BACS – CSRM-Methodendokument vom 24. November 2025"
[10]: https://www.bacs.admin.ch/de/26w44-de "BACS – Woche 44: Heimnetzwerke, 3. November 2026"
[11]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen, 10. November 2026"
[12]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – KEV-Katalog, abgerufen am 15. November 2026"
[13]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall – SNWLID-2026-0014, Revision vom 9. November 2026"
[14]: https://wordpress.org/documentation/wordpress-version/version-7-1-4/ "WordPress – Version 7.1.4 und ältere Sicherheitsreleases"
[15]: https://support.apple.com/en-us/120896 "Apple – Sicherheitsinhalt von Safari 17.5, historischer CVE-Fix"
[16]: https://support.apple.com/en-us/100100 "Apple – Aktueller Sicherheitsrelease-Überblick, Abruf 15. November 2026"
[17]: https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems "NIST – Vorgeschlagene Grundsätze für Agentenidentität, 27. Oktober 2026"
