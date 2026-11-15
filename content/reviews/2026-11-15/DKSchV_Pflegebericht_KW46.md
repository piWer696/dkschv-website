---
datum: "15.11.2026"
stand: "15. November 2026"
kalenderwoche: "KW 46"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
zeitzone: "Europe/Zurich"
newsfenster: "08.11.2026 09:00 bis 15.11.2026 09:00 CET"
grundlage: "Zwölf fertige Artikelpflegebefunde und fünf News-Einzelberichte; keine neue Recherche für diese Zusammenfassung"
---

# DKSchV Pflegebericht · KW 46

 ## Abschluss des Gesamtlaufs am 15. November

 **Die lokale Pflege ist abgeschlossen.** Alle zwölf Artikel und zwölf Arbeitsmittel tragen den Quellenprüfstand 15. November 2026; die Reichweite und offenen Quellenfragen stehen in den Einzelberichten. Die [Paketvalidierung](validator-ergebnis.txt) meldet **0 Fehler und 0 Warnungen**. Das lokale CMS-Importmanifest ist synchronisiert; echte Live-Zieladressen sind getrennt von logischen Paket-Slugs erfasst. Der [lokale Linkabgleich](lokaler-live-linkabgleich.json) korrigierte Markdown-Linkziele in 14 Inhaltsdateien. Dies ist keine Fach-, Schutz- oder Publikationsfreigabe.

 **Wichtiger Schutzbefund:** Alle zwölf Artikeladressen liefern HTTP200, auch die noch nicht terminlich fälligen Beiträge 08–12. Der Wiederherstellungsartikel lieferte ohne Credentials rund 22.200 Zeichen Fachtext, obwohl die Seite «Kunden-Login erforderlich» und «Mandanten-Bereich» ausweist. Der [strukturierte Abrufbefund](public-article-exposure.json) bestätigt, dass detaillierte Wiederanlauf- und Forensikabschnitte bereits in der Antwort enthalten waren. Ein serverseitig wirksamer Schutz dieses Inhalts ist nicht nachgewiesen. Eine reine Login-Darstellung schützt bereits ausgelieferten Text nicht. Die Herkunft und Fachfreigabe der gefundenen öffentlichen Bereitstellung sind nicht bestätigt; dieser Agent hat sie in diesem Lauf nicht veröffentlicht.

 Der [ursprüngliche HTTP-Test](public-link-check.csv) ergab 13×200 und 15×404: zwölf Arbeitsmittelpfade und drei frühere Servicepfade fehlen an den alten Adressen. Die [auf der Website verlinkten neuen Ziele](public-target-map.csv) antworten dagegen alle mit 200: zwölf Arbeitsmittel unter `/wissen/resources/<Dateiname>.html` und drei Serviceadressen im Root mit `.html`. Lokale Markdown-Verweise wurden gezielt auf diese geprüften Adressen korrigiert; Slugs, SEO-Importfelder, Termine und Fachmarker bleiben erhalten.200 ist keine Schutz- oder Fachfreigabe.

 **Live-Synchronisierung BLOCKIERT:** Der [Webador-Test](cms-zugangsstatus.md) zeigte die Anmeldeseite, keinen authentifizierten Projektzugang. Aktuelles Hosting/CMS und die Zuordnung der öffentlichen `.html`-Darstellung zum historischen Webador-Projekt sind nicht bestätigt. Kein Editor wurde geändert, kein geschützter Import gestartet und kein Beitrag veröffentlicht. Vor einer späteren Synchronisierung sind der passende Hosting-/CMS-Zugang, die tatsächlichen Fachfreigaben und der gewünschte serverseitige Kundenschutz zu klären. Die historischen Fach-/Rechtsfelder sind keine heutige Einzelfallprüfung.

 **Live-Änderungsprotokoll:** Keine Einträge. Artikel 01–07 sind am 15.11. terminlich fällig, bleiben aber nicht freigegeben. Artikel 08–12 sind noch nicht fällig; ihre HTTP-Erreichbarkeit erlaubt keine automatische Bearbeitung oder Veröffentlichung. Die nachfolgenden Aussagen, dass einzelne Rechercheagenten keine globalen Tests durchführten, gelten weiterhin für deren eigenen Umfang; die hier dokumentierten Abschlussprüfungen ergänzen sie.

## Ergebnis, Zeitbezug und Freigabegrenzen

**Alle zwölf Artikel-/Arbeitsmittelpaare haben einen fertigen lokalen Pflegebefund und einen Einzelbericht.** Die übergebene Fehlschlagliste ist leer; es fehlen keine Pflege-Items. Fertig ist die dokumentierte redaktionelle Quellenpflege, **nicht** die Fachprüfung oder Veröffentlichungsfreigabe. Sämtliche Artikel und Arbeitsmittel bleiben nicht freigegeben. Laut Einzelberichten lauten beide Frontmatter-Standwerte jedes Paars exakt **15. November 2026**; geschützte SEO-Felder, Slugs, Termine und ursprüngliche Fachprüfungsmarker wurden erhalten. Die Originalmarker bleiben ausdrücklich offen.

Die Einzelpflege bezog auch ältere, für die Evergreen-Texte relevante Quellen ein. Das engere Newsfenster gilt für neue Wochenmeldungen, nicht für jeden Pflegebeleg. Die tatsächlichen Quellenrückgaben am 15. November erfolgten nach 09:00 CET. Die Newsberichte dokumentieren Originalrückgaben **09:05:57–09:08:20 CET**, ergänzende lokale Lektüre bis 09:08:22. Artikel 11 dokumentiert weitere Fetch-Rückgaben bis **09:10:50** und generische HTTP-Rückgaben bis **09:10:56**; Artikel 12 ergänzende lokale Quellenlektüre bis **09:11:19 CET**. Abruf-/Befundzeiten sind weder Publikationsdaten noch ein rückwirkender Nachweis des Seitenwortlauts exakt um 09:00.

Quellenumfang, lesbarer Inhalt und lokale Metadaten sind **keine externe Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Vertragsfreigabe**. Für diese Zusammenfassung wurden ausschliesslich die zwei beauftragten Ergebnisdateien geschrieben, keine Artikelvolltexte neu überschrieben und keine neue Recherche oder zusätzliche QA-Delegation ausgeführt. CMS-Abgleich, globale Validatorprüfung und heutige öffentliche Linkchecks sind hier **nicht durchgeführt und nicht als erfolgreich ausgewiesen**; separate Befunde des koordinierenden Elternlaufs bleiben zu ergänzen. Frühere HTTP-Werte werden nicht als heutige Paketprüfung übernommen.

## 01. Ransomware: erste 60 Minuten

**Änderungen:** Im Abschnitt **Minute 0–15 / «Betroffene Systeme isolieren»** wurde die begrenzte Erfassung geschäftlicher Homeoffice-/Heimnetzverbindungen ergänzt. **Minute 45–60** trennt BACS-Weiterleitung auf Wunsch von tatsächlich erfüllter EDÖB-Meldung; die CSV ist direkt belegt. Technische Eindämmung und erforderliche Betroffeneninformation werden getrennt. Die Checkliste **B/E** enthält passende Erfassungs- und Übermittlungsnachweise; die datumsbasierte Version ist sichtbar auf 15. November abgeglichen.

**Offen:** Konkrete BACS-Unterstellung, CSV-Ausnahmen, Angriffstatbestand, Entdeckungszeitpunkt, DSG-Risiko, Informationsform sowie Forensik und sauberer Wiederanlauf. Kein Formular wurde übermittelt oder Meldeweg Ende zu Ende geprüft. Das BACS-KMU-Template mit Dateidatum 11.11. blieb in diesem Einzelabruf nur Base64-/ZIP-Inhalt; interne Version und materielle Änderungen sind ungeprüft. 18 Artikel- und 15 Checklistenreferenzen waren im verwendeten Umfang lesbar; dieser Zusatzblocker bleibt bestehen. [Einzelbericht 01](artikel-01-quellen-und-aenderungen.md).

## 02. CEO-Betrug/BEC und Zahlungsprüfprotokoll

**Änderungen:** **«Warnzeichen, die eine Zahlung stoppen müssen»** ergänzt EHRA- und ESTV-Behördenimitation. **Prävention / «E-Mail-Identitäten und Versanddomain schützen»** ordnet Microsofts Q3-Beobachtung und Schutz-Ausnahmen begrenzt ein; der 63-Prozent-Wert wird nicht verallgemeinert. **«Datenschutz und Meldungen»** trennt technische Behebung und Betroffeneninformation. Im Protokoll wurden **B Stoppsignale**, **E kompromittiertes E-Mail-Konto** und neue **F Anwendungshinweise** erweitert; die materielle Datumsrevision ist sichtbar abgeglichen.

**Offen:** Zahlungsrollen und Bankvorgaben, Mailbox-Forensik, Tenant-/Schutzausnahmen, betroffene Personendaten und Informationsbedarf. DSG-/DSV-`/changes` lieferten nur JavaScript-Hinweise; lesbare Chronologien/XML sind separate Nachweise. 18 Artikel-/10 Arbeitsmittelreferenzen sind lesbar, nicht alle Zusatzansichten. Keine heutige öffentliche Link- oder CMS-Prüfung. [Einzelbericht 02](artikel-02-quellen-und-aenderungen.md).

## 03. Datenpanne melden in der Schweiz

**Änderungen:** **Frage 3**, neuer Unterabschnitt **«Betroffene informieren: Technische Behebung und Informationsform getrennt prüfen»**, **Schritt 6** und Fehlerübersicht präzisieren die eigenständige Informationsprüfung. Sie ist nicht allein von der hohen Risikoschwelle der EDÖB-Meldung abhängig. Mitteilung vom 6. November und Urteil A-3790/2024 wurden differenziert eingebunden. Arbeitsmittel **Schema B/Entscheidregeln und C3** ergänzt Schutzhandlungen, Erreichbarkeit, Form und Ausnahmebegründung; materielle Revision 2 ist sichtbar abgeglichen.

**Offen:** Konkretes Risiko, Verantwortlichenrollen/Datenflüsse, Adressaten und Informationsform sowie BACS-Unterstellung/Ausnahmen. DSG-/DSV-Änderungsansichten bleiben unlesbar. Die auffällige Buchstabenreferenz in **E. 6.3.8** ist dokumentiert; eine amtliche Berichtigung ist nicht nachgewiesen. Keine allgemeine öffentliche Bekanntmachungspflicht abgeleitet. Alle 14 unterschiedlichen zitierten Originalquellen sind im verwendeten Umfang lesbar. [Einzelbericht 03](artikel-03-quellen-und-aenderungen.md).

## 04. Backup und Selbstcheck

**Änderungen:** **«RPO, RTO und Wiederanlauf»** ergänzt begrenzte Homeoffice-/Fernzugangsabhängigkeiten anhand der BACS-Heimnetzmeldung. **«Wiederherstellungsfähigkeit beweisen»** kennzeichnet die NIST-Recover-Seite als nicht mehr aktualisiert. Selbstcheck **Zweck, Anwendung und 6 Restore-Test** erweitert Nachweisgrenzen; materielle Datumsrevision und sichtbare Version stimmen laut Journal überein. Quellenmetadaten und Zitationsleerzeichen wurden gepflegt.

**Offen:** Backup-/Object-Lock-, Schlüssel- und Rechtearchitektur, Aufbewahrung/Löschung, Verträge, RPO/RTO sowie Sicherungssauberkeit und Forensik. Homeoffice-Zielumgebung ungeprüft. DSG-/DSV-`/changes` bleiben Inhaltsblocker; BACS-DOCX-Vorlagen mit sichtbarem Dateidatum 11.11. wurden hier nicht inhaltlich geprüft. 18 Artikel-/9 Arbeitsmittelreferenzen sind zitiert; 17 unterschiedliche zitierte Originalziele relevant lesbar. [Einzelbericht 04](artikel-04-quellen-und-aenderungen.md).

## 05. Microsoft 365: MFA, Passkeys und CYOT

**Änderungen:** **«Die Termine»** und **«Zuerst Inventar und Risiken»** unterscheiden aktive Global Administrators von nur eligible PIM-Zuweisungen sowie interne/externe Gäste, SSPR und Bedingungen blockierender Registrierung. Februar-/Juli-Hauptfristen 2027 bleiben unverändert. **Passkey-Pilot und Wiederherstellung** ergänzt Erstregistrierung, Gast-Recovery, TAP- und Android-Backupgrenzen. Checkliste **1/2/4/5/6** enthält entsprechende Prüfpunkte und getrennte CYOT-Evaluations-/Produktionsnachweise; Datumsrevision 15. November sichtbar abgeglichen.

**GA-Aussage und unmittelbare Quellengrenze:** Die [CYOT-FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq), Stand 11.11., bestätigt **GA seit 30.10.2026 nur für Workforce-Tenants in global Azure**, nicht External ID/B2C. Das ist keine neue November-GA und keine Schweizer Providerfreigabe. Ältere Vorschauformulierungen bleiben in Retirement-Hauptquelle/FAQ neben den aktuellen speziellen CYOT-Unterlagen bestehen. Der Novemberblog nennt Erstregistrierung als GA mit Rollout bis Februar 2027, während die ältere Detailanleitung vorherige MFA verlangt; keine universelle heutige Verfügbarkeit behauptet. Android-Backup ist für Januar 2027/persönliche Profile angekündigt, nicht bereits allgemein bestätigt.

**Offen:** Schweiz-/Provider-/Tenant-Eignung, Lizenzen, Rollenpopulationen, Conditional Access, Passkey-/TAP-/Notfallzugangs- und Failovertests. Roadmap **568076** liefert keinen auslesbaren spezifischen Eintrag. FAQ-Vorjournal nennt 26.10., Herstellerpatch als Altdatum 20.10.; vollständiger historischer Learn-Snapshot fehlt. PIM-Patch 02.11. und GCC-Patch 04.11. sind hingegen konkret belegt. 19/19 Artikel- und 14/14 Checklistenreferenzen sind benutzt und relevant lesbar. [Einzelbericht 05](artikel-05-quellen-und-aenderungen.md).

## 06. Microsoft-365-Sicherheitskonfiguration und Tenant-Prüfliste

**Änderungen:** **1 Identitäten/Notfallzugänge**, **2 Adminrollen / «Exponierte App-Secrets» / Herstellerintegrationen**, **4 Logging**, **6 Provider-Governance** und der **30-Tage-Plan** wurden ergänzt. Anwendungsobjekt, lokaler Dienstprinzipal und Single-/Multitenant-Reichweite sind getrennt; Workload-Conditional-Access-Lizenz, direkte Zuweisung und ausgeschlossene App-Typen eingegrenzt. Aktuelle ConnectWise-App-Liste und Wiederherstellungsstand vom 4. November ersetzen die abschliessende Vierer-Begrenzung. Prüfliste ergänzt **B9/B10, E7/F7**, Secret-Lebenszyklus, Logfristen, Sicherungslücke und Mail-Sicherheitsausnahmen; materielle Datumsrevision sichtbar abgeglichen.

**Offen:** Tatsächliche Tenant-/Lizenz-/Secret-/Providerverhältnisse, historische Nutzung, verbleibende Tokens, Vorfall und Datenschutz. Microsoft nennt vier Application IDs, Beispielabfragen enthalten drei; die Abweichung bleibt ausdrücklich offen und wird nicht als vollständige Liste übernommen. CVE-2026-109469 ist im Journal als vollständig durch Microsoft mitigierter Cloudfix ohne Kundenpatch eingeordnet, nicht als Kunden-Patchauftrag. 21 zitierte Originalquellen sind relevant lesbar; kein ungelöster Ausleseblocker in diesem Quellenlauf. [Einzelbericht 06](artikel-06-quellen-und-aenderungen.md).

## 07. Wiederherstellung testen und Restore-Testprotokoll

**Änderungen:** **«Der saubere Wiederanlauf»**, neue **Rückfallszenarien**, **Komponenten-/Patchnachweise** und **Melde-/Datenschutzfragen** trennen Sicherheitsentscheid, Beweissicherungsübergabe, KEV, Updates, Kompromittierungsbefund und Betroffeneninformation. Bedingte Homeoffice- und Kühl-/OT-Abhängigkeiten wurden ergänzt. Protokoll **4 Durchführung / Rückfall und Beweissicherungsübergabe** und **Grenzen/Eskalation** erweitert; materielle **Version 1.3** sichtbar abgeglichen. BACS-KMU-Downloaddatum 11.11. belegt; derselbe Binärabruf wurde hier erfolgreich dekodiert und gelesen.

**Offen:** Architektur, RTO/RPO, Rückfall, Gefahrenbeseitigung, Beweissicherung, saubere Sicherung und Anlagenabnahme sowie BACS-/DSG-Einzelfallfragen. Ein ergänzender Fedlex-Änderungszugang bleibt unlesbar. 15 Artikel-/12 Protokollreferenzen lesbar; der seit 12.11. fällige Termin ist keine Nutzungs- oder Publikationsfreigabe. [Einzelbericht 07](artikel-07-quellen-und-aenderungen.md).

## 08. IT-Sicherheitscheck und Risikoregister

**Änderungen:** **«Zuerst den Geschäftskontext erfassen»** grenzt CSRM von vollständiger Risikoanalyse und offiziellem Registerprüfkatalog ab. **Befund in Szenario übersetzen/Prioritäten** ergänzt datierte Evidenz, Exposition und getrennte Warnungs-/Lokalnachweise. Homeoffice und Kühl-/OT-Abhängigkeiten, unabhängige Agentenberechtigungen, Widerruf und geschützte Nachweise wurden aufgenommen. Register **Anwendung, Kontext/Evidenz, Risikoszenario und Schliesskontrollen** ergänzt; materielle **Version 1.4** sichtbar abgeglichen. SonicWall-/Apple-/WordPress-KEV bleibt datierter Prüfkontext, nicht neue Schweizer Pflicht.

**Offen:** Eigene Risikoskalen/-akzeptanz, Datenschutz, Homeoffice-Prüfbefugnisse, Modelle/Builds/Konfigurationen, OT-Wartung und tatsächliche Agentenkontrollen. BACS-KMU-DOCX blieb in diesem Einzelabruf kodierter Binärtext ohne Inhaltsprüfung. 22 Artikelreferenzen entsprechen 21 unterschiedlichen Original-URLs; 17 Vorlagenreferenzen relevant gelesen. Ausländische Low-Risk-Orientierung ist keine Hochrisiko-Freigabe. [Einzelbericht 08](artikel-08-quellen-und-aenderungen.md).

## 09. Schatten-KI und KI-Nutzungsregel

**Änderungen:** **Inventar/Datenklassen**, **Schutzmassnahmen**, **Prompt-Vorfall** und **30-Tage-Plan Tage 15–21** ergänzen NISTs Vorschlag vom 27.10. zu Delegationsgrenzen, regelbasierter unabhängiger Kontrolle, widerrufbaren Rechten und geschützten Logs. Er bleibt freiwillig und ist keine Schweizer Norm. EDÖB-Mitteilung vom 6.11. trennt Eindämmung und Informationsbedarf. Arbeitsmittel **Freigabekarte, Schutzkontrollen, Vorfall und Review** erweitert; materielle **Version 1.4** sichtbar und im Artikelverweis abgeglichen.

**Offen:** Tatsächliche Datenflüsse, Geheimhaltung, Anbietertraining/Opt-out, Verträge, Produkt-/Tenantprüfung sowie Identitäten, Delegation, Rechteentzug und Betriebsresilienz. EDÖB-Newsübersicht zeigt nur «werden geladen»; lesbare Jahresübersicht beseitigt diesen Inhaltsblocker nicht. 17 Artikel-/13 Arbeitsmittelreferenzen relevant lesbar. Keine allgemeine öffentliche Bekanntmachungspflicht. [Einzelbericht 09](artikel-09-quellen-und-aenderungen.md).

## 10. Krisenkommunikation und Holding Statement

**Änderungen:** **Phase 3 Bewältigungsabschluss**, **Holding Statement/Q&A** und neuer **Melde-/Informationsunterabschnitt** trennen technischen Abschluss, verbleibenden Schutzbedarf und Betroffeneninformation. Die Vorlage ergänzt **Anwendung, Kontrollpunkte, Schutzinformation, Handlungshinweise und Informationsentscheid**; materielle **Version 1.3** sichtbar abgeglichen. Ein allgemeines Holding Statement erfüllt eine erforderliche Betroffeneninformation nicht automatisch; SkySale-Ersatzinformation und individuell verfügte Zehntagesfrist werden nicht verallgemeinert.

**Offen:** Risiko, Rollen, Adressaten, Erreichbarkeit/Informationsform, CSV-Unterstellung, Forensik, Verträge und autorisierte Freigaben. Softech bleibt hängiger Verfahrenskontext. Fedlex-Änderungsübersicht und EDÖB-Newsliste sind Inhaltsblocker. Die BACS-DOCX-Hürde wurde hier durch Dekodierung behoben; mangels Vergleichsdatei ist keine materielle BACS-Versionsänderung nachgewiesen. Zwölf unterschiedliche Paarreferenzen einschliesslich sieben Vorlagenreferenzen lesbar. [Einzelbericht 10](artikel-10-quellen-und-aenderungen.md).

## 11. Lieferantenrisiken und Lieferantenfragebogen

**Änderungen:** **«Partner mit privilegiertem Zugriff»**, **«Anbieter von Hardware oder Software»**, **Verträge** und **Notfallwege** ergänzt vier datierte Kontexte: Anbieter-App-Secrets (05.11.), Kühlsteuerungen (10.11.), Technikersitzungen (13.11.) und KI-Modellartefakte (12.11.). Fragebogen **Teil A sowie D1/D3/D4** ergänzt Widerruf/Rotation, historische Nutzung, verbleibende Tokens, getrennte Fernwartungsgeräte, unabhängigen Vorfallkanal und Artefaktherkunft; materielle **Version 1.3** sichtbar abgeglichen. Kampagnenpublikation ist nicht Angriffsbeginn; KI-Forschung ist kein allgemeiner Befallsnachweis.

**Offen:** Datenschutz/Verträge und Unteraufträge, konkrete Secrets/Tenants, Fernwartungsforensik, Anlagen-/Supportstände und KI-Integritäts-/Toolkontrollen. Kanadische Tokenquelle ist per Fetch lesbar, generischer HTTP-Abruf aber erneut **403**: Zugriffsprofildifferenz ungeklärt. DSG-/DSV-`/changes` liefern nur JavaScript-Hüllen. Alle 16 zitierten Paarquellen, davon 13 im Fragebogen, inhaltlich geprüft; keine generische Erreichbarkeits- oder Go-live-Garantie. [Einzelbericht 11](artikel-11-quellen-und-aenderungen.md).

## 12. NIS2/DORA und Relevanzmatrix

**Änderungen:** **Kurzantwort**, **NIS2 / EU-Angebot ohne Niederlassung** und Matrix **C möglicher direkter Anwendungsbereich** ergänzen den bereits 2024 veröffentlichten Detailakt **EU 2024/2690**. Nationale Umsetzung allein reicht für diese Einordnung nicht; einschlägige EU-Durchführungsakte sind ebenfalls zu prüfen. Keine neue November-Rechtsänderung und keine pauschale Schweizer Unterstellung behauptet. Matrix materiell auf **Version 1.4**, sichtbar abgeglichen.

**Aktuelle ISG-Aussage und unmittelbare Abgrenzung:** Die ISG-Referenz bleibt **Fassung 1. Oktober 2025**, durch die im Einzelbericht dokumentierte [amtliche Chronologie](https://www.fedlex.admin.ch/eli/cc/2022/232/de/history) und vorhandene Oktober-XML bestätigt. April-2025-Erstabrufe im historischen Journal sind älter, nicht der heutige Rechtsquellenstand. Das ist keine neue November-Fassung oder Fachfreigabe. DSG 07.07.2025 und DSV 01.12.2025 sind ebenfalls Quellenstände, keine neuen Fachprüfungsdaten.

**Offen:** NIS2-Dienstkategorie, Grösse/Konzern, EU-Angebot, Hauptniederlassung/Vertreter, nationale Umsetzungen und Detailaktanwendung; DORA-Finanzkundenstatus, Funktionskritikalität versus ESA-Anbietereinstufung, Unteraufträge, Audit/Exit und Verträge; Schweizer ISG-/CSV-Einzelfallfragen. Der zusätzliche EUR-Lex-Verfahrenspfad `PI_COM:Ares%282024%294640447` lieferte eine Ausfallersatzseite. Separater EU-2024/2690-Volltext lesbar, ursprünglicher Blocker bleibt. 16 Artikel-/8 Matrixreferenzen lesbar; keine vollständige Länder-/Folgeaktprüfung. [Einzelbericht 12](artikel-12-quellen-und-aenderungen.md).

## Übergreifende Quellen- und Erreichbarkeitsblocker

- **Fedlex:** Mehrere DSG-/DSV-Änderungsansichten enthalten nur JavaScript-Hinweise. Lesbare Normtexte, Chronologien und vorhandene amtliche XML stützen konkrete Aussagen, machen unlesbare Änderungslisten aber nicht erfolgreich. Sichtbare Wartungsankündigungen belegen nicht automatisch die Ursache jeder Zugriffslücke.
- **BACS-DOCX:** Ausleseblocker beziehungsweise ungeprüfte Inhalte bei 01/04/08 bleiben artikelbezogen erhalten. Erfolgreiches Dekodieren in 07/10 und direkte Extraktion in 11 sind separate Befunde; sie heben diese offenen Einzelprüfungen nicht stillschweigend auf. Dateidatum 11.11. beweist allein keine materielle Template-Änderung.
- **Dynamische Übersichten:** EDÖB-Newsliste bei 09/10 und News01 nur Ladeanzeige; kein vollständiger Nichtfund. Microsoft Roadmap 568076 bei 05 nicht spezifisch auslesbar; eine allgemeine Seitenhülle belegt keine Funktion.
- **Weitere Zugriffe:** Kanada bei 11 Fetch-lesbar/HTTP 403; EUR-Lex-Verfahrenspfad bei 12 ohne Verfahrensinhalt. DORA-Kommissions-Themenseite in News05 ohne extrahierbaren Inhalt; EIOPA/EUR-Lex sind begrenzte Ersatzbelege, kein Vollständigkeitsnachweis.
- **Technische Newsgrenzen:** Danfoss-Software-/Readme-Paketstände widersprechen sich; sicherer aktueller Build und spätere Behebung der sechs CCB-Lücken offen. Google-Artikelkörper war per Fetch zunächst nicht lesbar, wurde im fertigen News03-Befund aus offiziellem HTML per HTTP gelesen; diese konkrete Hürde ist behoben. MSRC-Monatsgesamtzahl hat einen späteren Fussstand und wird nicht als gesicherte Patch-Tuesday-Zahl verwendet. Kein Gerät, Tenant oder Anlagenbetrieb geprüft.

## Newsauswahl, zurückgestellte Meldungen und nächste Termine

Die [Branchennews KW 46](../../news/2026-11-15_DKSchV_Branchennews.md) priorisieren sechs Themen: Outlook/Chromium, Kühlsteuerungen, ScreenConnect, vergiftetes Modellnachtraining, ENISA/CERT-EU-Codeprüfung und KI-Fakeshops. Technische Sicherheit und KI sind ausgewogen vertreten. Die Grundlage bilden [News01 Behörden](../../news/qa/2026-11-15/news01.md), [News02 Microsoft](../../news/qa/2026-11-15/news02.md), [News03 Schwachstellen](../../news/qa/2026-11-15/news03.md), [News04 KI/Agenten](../../news/qa/2026-11-15/news04.md) und [News05 Regulierung](../../news/qa/2026-11-15/news05.md).

ESTV-Phishing, Windows-Server-Qualitätskorrekturen und Rust-Forschung bleiben belegt, aber aus Platz-/Relevanzgründen zurückgestellt. Die DSA-Wahlleitlinienkonsultation vom 10.11. ist ein nachrangiger Entwurf für sehr grosse Plattformen/Suchmaschinen, keine neue allgemeine KMU-Pflicht. OpenSSHs neue KEV-Aufnahme vom 09.11. ist eine Vormerkung mit älterem Herstellerfix; eine Zurückstellung erlaubt später keine künstliche Neudatierung. Für NIS2/DORA/CRA/KI-Verordnung wurde im begrenzten News-Lauf keine neue substanzielle Wochenentwicklung belegt, nicht deren vollständige Abwesenheit bewiesen. Alte EDÖB-, NIST-, SSPR-, CYOT-GA-, Apple-/WordPress- und Juli-Rechtsmeldungen werden nicht neu etikettiert.

**Nächste Newsausgabe: 22. November 2026, KW 47. Nächste Vollpflege: 29. November 2026, KW 48.** Diese Angaben sind Redaktionsplanung, keine neu eingerichtete Automation. Bis dahin bleiben konkrete Fachprüfungen, Quellenblocker und Veröffentlichungsweg offen; CMS-, Validator- und öffentliche Linkcheckbefunde sind separat durch den Elternlauf zu ergänzen.
