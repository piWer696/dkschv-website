# Quellen- und Änderungsbericht – Artikel 01 und 60-Minuten-Checkliste

Artikel 01 und sein Arbeitsmittel wurden am **15. November 2026, ISO-KW 46**, gezielt lokal gepflegt. Die allgemeine Erstreaktion bleibt durch die geöffneten BACS- und CISA-Quellen gestützt. Ergänzt wurden eine begrenzte Homeoffice-Erfassung, die ausdrücklich getrennte Prüfung einer BACS-Weiterleitung und die Abgrenzung von technischer Behebung und Betroffeneninformation. Keine neue Schweizer Pflicht wurde aus einer US-Meldung oder CISA KEV abgeleitet. [1] [5] [15] [16] [18] [29]

Geändert wurden ausschliesslich `/home/ubuntu/dkschv-audit/blog-paket/articles/01-ransomware-erste-60-minuten.md`, `/home/ubuntu/dkschv-audit/blog-paket/resources/01-60-minuten-checkliste.md` und dieser Bericht. Grundlage waren die vollständig gelesenen Ausgangstexte, das Wartungsmanifest, die Vorwochennews und der Laufstatus vom 08.11. sowie die Einzelprüfung vom 01.11.2026. Alle Original-FACHPRÜFUNG-Marker und die historischen Statusfelder wurden erhalten. Die Ausgangsdateien enthalten weder `rechtsstand` noch `fachlich_geprüft_am`; keines dieser Felder wurde neu angelegt.

**Tatsächliche Abrufe:** Die Fetch-Rückgaben erfolgten am 15.11.2026 zwischen **09:06:08 und 09:07:53 CET**, Europe/Zurich, UTC+01:00. Die Suchantworten kamen um 09:06:19 CET; die lokale Inhaltsprüfung ergänzender gespeicherter Extraktionen erfolgte bis 09:08:09 CET. Alle Abrufe lagen nach 09:00. Die Prüfung verwendet für aktuelle Meldungen das Fenster seit 01.11.2026, behauptet aber keinen historisch exakten Seitenwortlaut am heutigen Redaktionsschluss. Die nachstehenden Einzelzeiten sind tatsächliche Werkzeug-Rückgabezeiten, keine erfundenen Veröffentlichungs- oder Abrufstartzeiten.

**Umfang und Blocker:** Insgesamt wurden 36 unterschiedliche externe Original-URLs geöffnet: 18 im fertigen Artikel verwendete Quellen, davon 15 auch im Arbeitsmittel, und 18 ergänzende Originalquellen. Bei 35 URLs war der relevante Inhalt lesbar. Bei **einer zusätzlichen Quelle**, dem neu datierten BACS-KMU-Template, kam nur Base64-/ZIP-Inhalt zurück. Erreichbarkeit ist hier kein erfolgreicher Inhaltsnachweis. Dieser Ausleseblocker steht ausdrücklich in beiden Frontmattern und in Eintrag 31. Ein vollständiger inhaltlicher Vergleich des Templates ist offen. [31]

Es erfolgte keine CMS-, Browser-, Login-, Credential-, Import- oder Versandoperation. Kein System, Tenant, Produkt, Backup oder tatsächlicher Vorfall wurde untersucht. Erreichbarkeit, Seiteninhalt und allgemeine Orientierung sind keine Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe.

## Quellenjournal: jede externe Originalquelle

Die Nummern 1–18 entsprechen den fertigen Artikelreferenzen. Checklistenreferenzen sind jeweils separat genannt. «Ohne Seitenstand» bedeutet: Im geöffneten Inhalt war kein eigener Veröffentlichungs- oder Änderungsstand sichtbar. Die Aussage ist dann nur zum tatsächlichen Abruf belegt. Bei partiellen Werkzeugantworten wurden die relevanten Abschnitte über vorhandene amtliche XML-Fassungen oder die gespeicherte vollständige Extraktion gelesen; eine abgeschnittene Vorschau wurde nicht als vollständiger Textnachweis behandelt.

1. **BACS – Ransomware: Was nun?** Original-URL: [1]. Rückgabe 15.11.2026, **09:06:08 CET**, lesbar, ohne eigenen Seitenstand. Deckt umgehende Netztrennung, Sicherung der Logs, frühen Forensikentscheid und fachkundige Sicherung vor Neustart/Reparatur, Neuinstallation vor Datenwiederherstellung, Kantonspolizei am Geschäftssitz und Abraten von Lösegeld. Nennt auch 24 Stunden und 14 Tage sowie EDÖB. Behördenorientierung, kein Forensikplan und keine konkrete Meldeentscheidung. Artikel [1], Checkliste [1].

2. **BACS – Informationen zur Meldepflicht.** Original-URL: [2]. Rückgabe **09:06:08 CET**, lesbar, ohne eigenen Seitenstand; Inkraftsetzung 01.04.2025 genannt. Stützt bestimmte kritische Infrastrukturen, ISG/CSV, 24 Stunden ab Entdeckung und Vervollständigung innert 14 Tagen. Erfasst nicht automatisch jedes KMU. Artikel [2], Checkliste [3].

3. **Fedlex – DSG, SR 235.1.** Original-URL: [3]. Rückgabe **09:06:09 CET**, relevante Fassung lesbar; Vorschau partiell, zusätzlich amtliches XML geprüft. Sichtbarer Stand **07.07.2025**. Art. 5 und 24 stützen Datensicherheitsverletzung, voraussichtlich hohes Risiko, Meldung so rasch als möglich und gesonderte Betroffeneninformation. Wartungshinweis für 13.11., 20:00 bis 15.11., 20:00 sichtbar, aber beim Abruf kein Inhaltsausfall. Kein individuelles Rechtsgutachten. Artikel [3], Checkliste [5]. [19] [20]

4. **EDÖB – Leitfaden nach Art. 24 DSG.** Original-URL: [4]. Rückgabe **09:06:09 CET**, PDF-Text lesbar; restliche Informationspflichtpassagen aus vollständiger Extraktion um **09:07:53 CET** gelesen. Version **1.2, 23.04.2025**, Erstpublikation 06.02.2025. Stützt frühe Risikoanalyse ohne Abwarten langwieriger Abklärungen, sichere Pflichtmeldung und von der Meldeschwelle unabhängige Prüfung der Betroffeneninformation. Öffentliche Bekanntmachung als Ausnahme, nicht allgemeine Pflicht. Auslegungshilfe, keine Risikoentscheidung. Artikel [4], Checkliste [6].

5. **CISA – I've Been Hit By Ransomware!** Original-URL: [5]. Rückgabe **09:06:09 CET**, vollständig lesbar. Verweist auf den im Mai 2023 aktualisierten StopRansomware Guide. Stützt koordinierte Isolation, externen Kommunikationskanal, Ausschalten nur bei unmöglicher anderer Trennung, Wahrung flüchtiger Evidenz und Wiederherstellung aus Offline-Backups ohne Reinfektion. Internationale Orientierung, keine Schweizer Meldenorm. Artikel [5], Checkliste [2].

6. **BACS – Notfallkonzept.** Original-URL: [6]. Rückgabe **09:06:09 CET**, lesbar, ohne eigenen Seitenstand. Rollen, Krisenkommunikation, Kontakte und vier Phasen unverändert gestützt. Die Seite datiert KMU- und Gemeinde-Templates nun mit **11.11.2026**, statt des in der Vorprüfung genannten KMU-Downloadstands 18.05.2026. Nur der neue Link-/Datumsstand ist belegt; das KMU-Template selbst war nicht auslesbar. Artikel [6], Checkliste [7]. [31]

7. **NIST SP 800-61 Rev. 3.** Original-URL: [7]. Rückgabe **09:06:09 CET**, lesbar. Final April 2025, Dokumenthistorie **03.04.2025**. Stützt Incident Response als Bestandteil laufenden Cyberrisikomanagements. Keine Schweizer Rechtsquelle und keine konkrete technische Freigabe. Nur Artikel [7].

8. **Fedlex – ISG, SR 128.** Original-URL: [8]. Rückgabe **09:06:09 CET**, Fassung lesbar, Vorschau partiell; amtliche XML zusätzlich gelesen. Sichtbarer Stand **01.10.2025**. Art. 74b–74f stützen Erfassung, Ausnahmenrahmen, Angriffstatbestände, 24-Stunden-Frist, Ergänzung und sichere Übermittlung. Anders als der im Vorbericht beschriebene Leerabruf war der relevante Inhalt diesmal verfügbar. Keine konkrete Unterstellungsentscheidung. Artikel [8], Checkliste [4]. [21] [22] [23]

9. **Suisse ePolice – Cyberkriminalität anzeigen.** Original-URL: [9]. Rückgabe **09:06:16 CET**, öffentliche Kategorien lesbar, ohne Seitenstand. Unterscheidet Strafanzeige von nationaler Meldung. Cookie-/Interaktionsschritte wurden nicht bedient; kein vollständiger Anzeigeprozess getestet. Die Kantonspolizei am Geschäftssitz ist zusätzlich durch BACS belegt. Nur Artikel [9]. [1]

10. **BACS – Malwareverdacht, Woche 40.** Original-URL: [10]. Rückgabe **09:06:10 CET**, lesbar, publiziert **06.10.2026**. Einzelne unspezifische Symptome sind kein Infektionsbeweis; mehrere Auffälligkeiten oder Warnungen rechtfertigen Untersuchung; bei Geschäftsgeräten Arbeitgeber/IT informieren. Keine Diagnose eines bestimmten Geräts. Artikel [10], Checkliste [8].

11. **BACS – aktuelle Meldeoberfläche.** Original-URL: [11]. Rückgabe **09:06:16 CET**, lesbar, ohne Seitenstand. Freiwillige Meldemöglichkeit; für Pflichtmeldungen E-Mail-Alternative `incidents@ncsc.ch`, Anerkennung als Erstmeldung innert 24 Stunden, Schlussmeldung innert 14 Tagen und Empfehlung CSH. Nur Inhaltsabruf: weder Formular durchlaufen noch E-Mail versendet, Konto erstellt oder Übermittlung bestätigt. Nur Artikel [11].

12. **BACS – PHP-Warnung.** Original-URL: [12]. Rückgabe **09:06:10 CET**, lesbar, publiziert **21.10.2026**. Bestätigt ausdrücklich: Ein Update beseitigt keine bereits erfolgte Kompromittierung. Nur diese allgemeine Abgrenzung bleibt im Text verwendet. Keine Versions-, CVE-, Produkt- oder Neustartempfehlung aus dem PHP-Kontext in den Ransomware-Akutablauf übertragen. Artikel [12], Checkliste [9].

13. **EDÖB – DataBreach.** Original-URL: [13]. Rückgabe **09:06:17 CET**, lesbar, ohne Seitenstand; Leitfadenlink 23.04.2025. Sicheres Online-Formular für Verantwortliche, hohe Risikoschwelle und getrennter Kontaktweg für Betroffene. Bestätigung zum Herunterladen nach Absenden beschrieben, aber nicht tatsächlich getestet. Artikel [13], Checkliste [10].

14. **Fedlex – DSV, SR 235.11.** Original-URL: [14]. Rückgabe **09:06:17 CET**, Fassung lesbar, Vorschau partiell; Art. 15 zusätzlich per vorhandenem amtlichem XML gelesen. Sichtbarer Stand **01.12.2025**. Stützt Meldeangaben, Nachreichen, Informationsinhalt und Dokumentation. Art. 15 Abs. 4 nennt mindestens zwei Jahre Aufbewahrung ab Meldung. Keine organisationsbezogene Aufbewahrungsfreigabe. Artikel [14], Checkliste [11]. [24] [25]

15. **BACS – Heimnetz, Woche 44.** Original-URL: [15]. Rückgabe **09:07:12 CET**, vollständig lesbar, publiziert **03.11.2026**. Neu geprüft aus der Vormerkung: exponierte verwundbare Heimnetz-Dienste können angegriffen werden; bei Infektion weitere Geräte im Netz untersuchen lassen. Hauptadressaten sind Privatpersonen. Der Homeoffice-Bezug im Paket ist eine ausdrücklich begrenzte Erfassungsorientierung, kein belegter Angriff auf eine Firma. Keine Plex-/PHP-Versionen, Passwortrezepte oder Routerkonfiguration übernommen. Neu Artikel [15], Checkliste [12].

16. **EDÖB – Mitteilung zur Informationspflicht der Onlineshop-Betreiberin.** Original-URL: [16]. Rückgabe **09:06:49 CET**, vollständig lesbar, publiziert **06.11.2026**. Urteil 08.04.2026 laut EDÖB rechtskräftig; im konkreten Fall ändern nachträgliche technische Massnahmen die Informationspflicht nicht. Neu ist die Mitteilung, nicht das Gesetz oder der Vorfall. Die konkrete öffentliche Bekanntmachung ist kein allgemeiner KMU-Standard. Neu Artikel [16], Checkliste [13]; Urteil zusätzlich geprüft. [30]

17. **Fedlex – CSV, SR 128.51.** Original-URL: [17], vom geöffneten BACS-Unterstellungsblatt tatsächlich verlinkt. Rückgabe **09:07:53 CET**, relevante Abschnitte lesbar; sichtbare einzige Fassung **01.04.2025**. Art. 12 nennt sektorabhängige Ausnahmen und teilweise Grössenschwellen. Direkter amtlicher Nachweis ergänzt die bereits bestehende Aussage, dass Ausnahmen konkret zu prüfen sind. Keine pauschale KMU-Ausnahme oder eigene Einzelfallprüfung. Neu Artikel [17], Checkliste [14]. [34]

18. **BACS – Wie muss gemeldet werden?** Original-URL: [18], in der geöffneten Meldepflichtseite verlinkt. Rückgabe **09:07:15 CET**, lesbar, ohne Seitenstand. CSH-Formular ermöglicht auf Wunsch Weiterleitung, etwa an FINMA oder EDÖB; 14-Tage-Vervollständigung und alternativer Meldeweg beschrieben. Belegt keine automatische Meldung an alle Behörden und keine erfolgreiche Übermittlung. Neu Artikel [18], Checkliste [15].

19. **Fedlex – DSG-Chronologie.** Original-URL: [19]. Rückgabe **09:06:45 CET**, vollständig lesbar. Oberste Fassung Berichtigung, Inkrafttreten **07.07.2025**. Keine spätere Zeile in der geöffneten Chronologie; das ist kein universaler Nachweis über nicht publizierte künftige Änderungen. Ergänzende Rechtsstandquelle, nur Journal.

20. **Fedlex – DSG-XML.** Original-URL: [20], bereits im Vorbericht vorhanden und in der amtlichen Hauptseite/Chronologie verlinkt. Rückgabe **09:06:41 CET**, relevante Art. 5 und 24 lesbar, Fassung **20250707**. Bestätigt Mindestinhalt, Auftragsbearbeitermeldung an Verantwortliche, Betroffeneninformation und deren Ausnahmegründe. Kein neuer Fachfreigabestand.

21. **Fedlex – ISG-Chronologie.** Original-URL: [21]. Rückgabe **09:06:39 CET**, vollständig lesbar. Oberste aktuelle Fassung **01.10.2025**. Wartungshinweis sichtbar, Inhalt trotzdem verfügbar. Aktuelle Chronologie verlinkt XML-Endung `xml-2.xml`; diese wurde tatsächlich geöffnet. Keine URL konstruiert.

22. **Fedlex – vorhandenes ISG-XML, Endung xml-1.** Original-URL: [22], aus Vorbericht und heutiger Hauptseite. Rückgabe **09:06:41 CET**, Art. 74a–74f lesbar, Fassung **20251001**. Stützt Gesetzesinhalt. Es wird nicht als alleinige neueste Manifestation ausgegeben, weil die Chronologie eine andere XML-Endung verlinkt. [23]

23. **Fedlex – von der Chronologie verlinktes ISG-XML, Endung xml-2.** Original-URL: [23]. Rückgabe **09:07:15 CET**, Art. 74a–74f lesbar, Fassung **20251001**. Für die verwendeten Meldeaussagen kein materieller Unterschied zur ebenfalls erreichbaren xml-1-Manifestation festgestellt. Dieser aktuelle Alternativnachweis gehört ins Journal, nicht in ein Fachfreigabedatum.

24. **Fedlex – DSV-Chronologie.** Original-URL: [24]. Rückgabe **09:06:46 CET**, vollständig lesbar. Oberste Fassung **01.12.2025**, keine spätere Zeile im geöffneten Stand. Keine allgemeine Zusage über künftige Rechtsänderungen.

25. **Fedlex – DSV-XML.** Original-URL: [25], bereits vorhanden und aktuell verlinkt. Rückgabe **09:06:49 CET**, Art. 15 vollständig lesbar, Fassung **20251201**, Endung `xml-2.xml`. Angaben, Nachreichen, einfache Informationssprache und Vorfalldokumentation bestätigt. Keine individuelle Risikobeurteilung.

26. **BACS – Im Fokus.** Original-URL: [26]. Rückgabe **09:06:46 CET**, relevante November-Einträge lesbar; vollständige Extraktion gespeichert. Jüngste sichtbare Einträge **10.11.2026**. Seit 01.11. sichtbar: Cyberresilienzveranstaltung 02.11., Heimnetz 03.11., EHRA-Phishing 06.11., ESTV-Phishing 09.11., Kühlanlagen und Black-Friday-Betrug 10.11. Nur Heimnetz und Kühlanlagen wurden für Artikel-01-Relevanz im Original vertieft; die Übersicht allein ist kein Fachnachweis der übrigen Meldungen und kein vollständiger Nichtfundnachweis.

27. **BACS – Aktuelle Vorfälle.** Original-URL: [27]. Rückgabe **09:06:46 CET**, lesbar. Jüngster Eintrag **10.11.2026** zu Kühlanlagen; daneben ESTV/EHRA und ältere PHP-Warnung. Kein neuer generischer Ransomware-Erststundenablauf in der geöffneten Übersicht belegt. Keine Wiederholungsschleife nach Nichtfund.

28. **CISA – erweitertes Cybermeldeformular.** Original-URL: [28], aus der Suche geöffnet. Rückgabe **09:06:49 CET**, lesbar, publiziert **09.11.2026**. US-Formular nun mit detaillierteren Vorfalls-/Verhaltensfragen. Keine Änderung des Schweizer BACS-/EDÖB-Verfahrens; nicht als neue Quelle in Evergreen-Artikel oder Arbeitsmittel aufgenommen. Das US-Portal wurde nicht bedient.

29. **CISA – Alerts & Advisories.** Original-URL: [29], aus der Suche geöffnet. Rückgabe **09:06:49 CET**, aktuelle Ergebnisliste lesbar, jüngster Eintrag **13.11.2026**. Zeigt im Fenster insbesondere KEV-Alerts und die Kühlkettenorientierung vom 05.11.; keine neue generische Ransomware-Erstreaktionsleitlinie auf dieser Ergebnisansicht belegt. Der technische Listentext enthält zudem «No result», obwohl darunter aktuelle Ergebnisse erscheinen; nur die tatsächlich sichtbare Liste wird ausgewertet. Keine Schweizer Pflicht aus KEV abgeleitet und keine pauschale Aussage, es gebe weltweit keine neuere Quelle.

30. **BVGer – Urteil A-3790/2024.** Original-URL: [30], aus Vorwochennews und EDÖB-Mitteilung tatsächlich verlinkt. Rückgabe **09:06:50 CET**, relevante Textabschnitte lesbar; gespeicherte Gründe zusätzlich bis **09:08:09 CET** gelesen. Urteil **08.04.2026**. E. 6.2.3 und 6.3 behandeln technische Massnahmen, Schutzbedarf, Ausnahmen und vergleichbar wirksame öffentliche Information. Der Text diskutiert gerade keine allgemeine ausdrückliche Bekanntmachungspflicht. Einzelfallentscheid, kein Rechtsgutachten für Artikeladressaten.

31. **BACS – KMU-Notfallplan-Template.** Original-URL: [31], direkt aus der Notfallkonzeptseite. Rückgabe **09:06:52 CET**, technisch geliefert, aber nur Base64-/ZIP-Zeichen statt auslesbarem Fachtext. Die verlinkende Seite datiert den Download mit **11.11.2026**; Inhalt, tatsächliche interne Version und materielle Änderungen sind **nicht geprüft**. Konkreter zusätzlicher Ausleseblocker, nicht als erfolgreich inhaltlich geprüft gezählt, nicht als Inhaltsbeleg im Artikel oder der Checkliste verwendet. Kein wiederholter Download, keine Browserumgehung und keine fiktive Templateprüfung. [6]

32. **BACS – Kühl- und Kältesteuerungen.** Original-URL: [32], aus der aktuellen Übersicht geöffnet. Rückgabe **09:07:12 CET**, lesbar, publiziert **10.11.2026**. Beschreibt bekannte Angriffe auch in der Schweiz auf exponierte Managementschnittstellen, Manipulation und Geschäftsfolgen sowie produktspezifische Schutzmassnahmen. Keine Ransomware-Erststundenanweisung. Kein produktbezogener Einschub im Evergreen-Text, keine pauschale Abschalt-/Firmwarefreigabe. Bestehender Schutz kritischer Prozesse bleibt allgemeine Orientierung.

33. **EDÖB – DataBreach-Portal.** Original-URL: [33], von der EDÖB-Seite tatsächlich verlinkt. Rückgabe **09:07:15 CET**, öffentliche Einleitung lesbar, ohne Versionsstand, im Abruf englisch. Neue/Folgemeldung, Verantwortlichenrolle sowie getrennter Hinweis für Betroffene und Auftragsbearbeiter sichtbar. Keine Eingabe, kein Versand, keine Sprachwahl oder Bestätigung getestet. Stützt Erreichbarkeit der öffentlichen Einstiegsinformation, nicht Ende-zu-Ende-Funktionsfähigkeit.

34. **BACS – Wer muss melden?** Original-URL: [34], bereits im Vorbericht und heute verlinkt. Rückgabe **09:07:16 CET**, lesbar, ohne Seitenstand. Verweist auf Art. 74b ISG und CSV-Ausnahmen. Die hier konkret verlinkte CSV wurde geöffnet. Keine Organisation eingestuft. [17]

35. **BACS – Was muss gemeldet werden?** Original-URL: [35], bereits vorhanden und aktuell verlinkt. Rückgabe **09:07:16 CET**, lesbar, ohne Seitenstand. Funktionsfähigkeit, Manipulation, Abfluss, Erpressung und Beispiele einschliesslich Verschlüsselungstrojaner. Vollständiger Gesetzeswortlaut, auch längere Unentdecktheit, anhand ISG geprüft. Kein realer Angriff beurteilt. [23]

36. **CISA – SafePay Ransomware.** Original-URL: [36], aus Vorbericht und Suche. Rückgabe **09:07:14 CET**, relevante Reaktions- und Versionspassagen lesbar. Publiziert und laut Version History initial **20.10.2026**, keine spätere Versionszeile sichtbar. Akteurbezogen Isolation und Sammlung relevanter Artefakte und Logs; kein neuer generischer Erststundenablauf, keine Schweizer Meldepflicht. Nicht als neue Artikel-/Checklistenreferenz verwendet.

## Aktuelle Meldungen und materielle Einordnung

Die Suche nach der Heimnetz-/Homeoffice-Vormerkung lieferte zunächst unpassende Resultate zum gleichnamigen US-Anbieter BACS. Diese Snippets wurden nicht als Belege verwendet. Die korrekte Schweizer Original-URL wurde aus der geöffneten amtlichen BACS-Übersicht gewonnen und direkt gelesen. Der Beitrag stützt das Erfassen bekannter Heimnetz-Verbindungen bei geschäftlicher Nutzung, nicht die Annahme einer konkreten Infektion. Er rechtfertigt keine ungeprüfte Privatrouter-, VPN- oder Produktänderung in der ersten Stunde. [26] [15]

Die EDÖB-Mitteilung vom 06.11.2026 und das ältere Urteil stützen die neu ausdrücklich formulierte Trennung: Technische Behebung erledigt eine erforderliche Betroffeneninformation nicht automatisch. Die bestehende Risikoschwelle für die Meldung an den EDÖB ist damit nicht geändert. Auch die Frage, ob direkte Information, Aufschub oder ausnahmsweise öffentliche Bekanntmachung zulässig ist, bleibt konkret offen. [16] [30] [4] [20]

Der BACS-CSH bietet Weiterleitung auf Wunsch. Diese Möglichkeit wird nicht als automatische Doppelmeldung behandelt. Die Artikelergänzung und der Checklistenpunkt verlangen separate Prüfung von Empfänger, Angaben und tatsächlicher Übermittlungsbestätigung. Im Auftrag selbst fand keine Übermittlung statt. [18] [13] [23]

Die aktuelle CISA-Ransomwareprüfung umfasst auch die SafePay-Originalmeldung. Ihre Version History zeigt nur den 20.10.2026. Sie bestätigt akteurbezogen Isolation und Log-/Artefaktsammlung, ändert den generischen Erststundenablauf aber nicht. Die bereits im Paket verwendete generische CISA-Checkliste bleibt der passende Beleg; keine akteur- oder produktbezogenen Gegenmassnahmen wurden als Schweizer KMU-Standard übernommen. [36] [5]

Die CISA-Meldung vom 09.11. betrifft einen US-Meldeprozess, die BACS-Kühlanlagenwarnung produktspezifische Industrie-/IoT-Risiken. Beide wurden nicht künstlich an den Artikel angehängt. Die geöffnete CISA-Liste reicht bis 13.11., die BACS-Liste bis 10.11. Das ist kein umfassender Nichtfundnachweis für jede denkbare November-Meldung. [28] [29] [32]

## Genau betroffene Abschnitte: Artikel vorher und nachher

**Frontmatter `stand`:** Vorher `1. November 2026`; nachher exakt `15. November 2026`.

**Frontmatter `quellenpruefung_umfang`:** Vorher `14 von 14 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft`. Nachher `18 von 18 externen Quellenreferenzen inhaltlich geprüft; zusätzlich Fedlex-History/XML und einschlägige BACS-/EDÖB-/CISA-Primärmeldungen seit 1. November 2026; Abrufe nach 09:00 CET`.

**Frontmatter `quellenpruefung_status`:** Vorher `Vollständig für die Quellenreferenzen; Fedlex-Historie und amtliche XML-Fassungen zusätzlich geprüft; interne relative Ziele nicht live geprüft`. Nachher `18 Referenzen lesbar; 1 zusätzlicher Ausleseblocker: BACS-KMU-Template vom 11.11.2026 nur als Base64/ZIP, Inhalt ungeprüft; keine Fachfreigabe oder Einzelfallprüfung; interne Ziele nur lokal abgeglichen, nicht live geprüft`.

**Minute 0–15, Unterabschnitt 2 «Betroffene Systeme isolieren – nicht reflexartig ausschalten»:** Vorher kein Homeoffice-Absatz. Nachher nach dem unveränderten Absatz über koordinierte Schutzmassnahmen:

> Erfassen Sie bei einem geschäftlich genutzten Homeoffice-Gerät auch den Arbeitsort und bekannte Verbindungen zu Heimnetz-Diensten wie einem Netzwerkspeicher. Das BACS warnt seit dem 3. November 2026 vor verwundbaren, aus dem Internet erreichbaren Heimnetz-Diensten und empfiehlt bei einer Infektion, weitere Geräte im selben Netz fachkundig untersuchen zu lassen. Die Meldung betrifft primär Privatnetze: Sie beweist weder eine Infektion Ihres Geschäftsgeräts noch einen Angriff auf das Unternehmensnetz. Geben Sie die Beobachtungen an die zuständige IT weiter; verändern Sie private Router oder andere Geräte nicht unkoordiniert im Zuge der Akutreaktion. [15] [10]

**Minute 45–60, BACS, erster Absatz:** Wortlaut vor/nach identisch bis auf die Quellenfolge: vorher `[2] [8]`, nachher `[2] [8] [17]`. Die konkret genannte CSV hat nun einen direkt geöffneten amtlichen Beleg; keine neue Unterstellungsaussage. [17]

**Minute 45–60, BACS, nach Absatz zur alternativen Erstmeldung:** Vorher kein Weiterleitungsabsatz. Nachher:

> Das BACS beschreibt im Cyber Security Hub eine Weiterleitung an weitere Behörden auf Wunsch, etwa an den EDÖB. Daraus folgt keine automatische Erfüllung einer EDÖB-Meldepflicht. Beurteilen Sie Empfänger, Meldeschwelle, benötigte Angaben und die tatsächlich bestätigte Übermittlung für jeden Meldeweg separat. [18] [3] [13]

**Minute 45–60, EDÖB, nach dem unveränderten Risiko-/Fachprüfungsabsatz:** Vorher kein Absatz zu technischer Behebung und der November-Mitteilung. Nachher:

> Technische Eindämmung und Information betroffener Personen sind getrennte Entscheide. Die EDÖB-Mitteilung vom 6. November 2026 zum Urteil A-3790/2024 bestätigt im dortigen Fall, dass nachträgliche technische Massnahmen die erforderliche Betroffeneninformation nicht aufheben. Neu ist die Mitteilung, nicht Art. 24 DSG. Ob eine direkte Information oder ausnahmsweise eine öffentliche Bekanntmachung geeignet und zulässig ist, muss konkret geprüft werden; daraus entsteht keine allgemeine Pflicht jedes KMU zur öffentlichen Bekanntmachung. [16] [3] [4]

**«Grenzen dieses Sofortleitfadens», Anfang:** Vorher `Diese Anleitung ist eine allgemeine operative Orientierung für Schweizer KMU auf dem Stand der Quellenprüfung vom 1. November 2026; dieser Stand ist keine Fachfreigabe. Sie ersetzt weder ...`. Nachher `Diese Anleitung ist eine allgemeine operative Orientierung für Schweizer KMU auf dem Stand der Quellenprüfung vom 15. November 2026; dieser Stand ist keine Fachfreigabe. Erreichbare Quellen und allgemeine Empfehlungen belegen keine tatsächliche Einzelfallprüfung. Sie ersetzt weder ...`. Der gesamte danach folgende Beratungsvorbehalt, Fachmarker und Schluss zur Checkliste/Entscheidungslog blieb wortgleich.

**«Quellen»:** Vorher Definitionen [1]–[14]. Nachher [1]–[18]. Alle ursprünglichen URLs und Titel bleiben erhalten; hinzugefügt sind die tatsächlich verwendeten Quellen Heimnetz [15], EDÖB-Mitteilung [16], CSV [17] und BACS-Meldeprozess [18]. Keine ungenutzte Quelle hinzugefügt.

## Genau betroffene Abschnitte: Arbeitsmittel vorher und nachher

**Frontmatter `version`:** Vorher `Stand 1. November 2026`, nachher `Stand 15. November 2026`. Die Versionsdatumsänderung ist durch die materiellen Homeoffice-/Meldeprüfpunkte begründet, nicht nur durch Metadatenpflege. **Frontmatter `stand`:** vorher nicht vorhanden; nachher exakt `15. November 2026`. **Sichtbar nach H1:** vorher keine Versionszeile; nachher `**Version: Stand 15. November 2026**`, wortgleich zur Frontmatter-Version.

**Frontmatter `quellenpruefung_umfang`:** Vorher `11 von 11 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft`. Nachher `15 von 15 externen Quellenreferenzen inhaltlich geprüft; zusätzlich Fedlex-History/XML und einschlägige BACS-/EDÖB-/CISA-Primärmeldungen seit 1. November 2026; Abrufe nach 09:00 CET`.

**Frontmatter `quellenpruefung_status`:** Vorher wie die ursprüngliche Artikelstatuszeile. Nachher `15 Referenzen lesbar; 1 zusätzlicher Ausleseblocker: BACS-KMU-Template vom 11.11.2026 nur als Base64/ZIP, Inhalt ungeprüft; keine Fachfreigabe oder Einzelfallprüfung; interne Ziele nur lokal abgeglichen, nicht live geprüft`.

**B «Minute 0–15: Eindämmung und Führung», letzter Checkpunkt:** Vorher nicht vorhanden. Nachher `- [ ] Bei geschäftlicher Nutzung im Homeoffice: Arbeitsort und bekannte Verbindungen zu Heimnetz-Diensten erfasst; zuständige IT informiert, keine unkoordinierten Änderungen an privaten Geräten ausgelöst.`

**B, nach dem unveränderten Hinweis zum unspezifischen Infektionszeichen:** Vorher kein Heimnetzhinweis. Nachher:

> Das BACS warnt seit dem 3. November 2026 vor verwundbaren, aus dem Internet erreichbaren Heimnetz-Diensten und empfiehlt bei Infektion eine fachkundige Untersuchung weiterer Geräte im selben Netz. Dies ist kein Beleg für die Betroffenheit Ihres Homeoffice-Geräts oder Unternehmensnetzes und keine Router- oder Produktfreigabe. [12]

**E «Minute 45–60: Meldungen und nächste Entscheidung», Betroffeneninformation:** Vorher `- [ ] Betroffene Personen nicht vorschnell informiert; Informationsbedarf fachlich geprüft.` Nachher `- [ ] Informationsbedarf betroffener Personen getrennt von der technischen Behebung fachlich geprüft; zuständige Person und nächster Termin bestimmt, notwendige Information nicht wegen der Behebung als erledigt betrachtet.` Dieser ersetzt die potenziell missverständliche Verzögerungsorientierung durch einen ausdrücklich getrennten, zeitlich verantworteten Entscheid. [16] [4]

**E, direkt folgender neuer Checkpunkt:** Vorher nicht vorhanden. Nachher `- [ ] Bei genutzter BACS-Weiterleitung: Empfänger, übermittelte Angaben und Bestätigung separat dokumentiert; EDÖB-Pflicht nicht automatisch als erfüllt markiert.` [18]

**E, BACS-Hinweistext:** Wortlaut identisch; vorher Quellenfolge `[3] [4]`, nachher `[3] [4] [14]`, letzteres ist die neue Checklistenreferenz zur CSV.

**E, nach dem unveränderten EDÖB-Portal-/DSV-Absatz:** Vorher kein Weiterleitungs-/Behebungsabsatz. Nachher:

> Das BACS bietet im Cyber Security Hub eine Weiterleitung an weitere Behörden auf Wunsch an. Eine BACS-Meldung ist damit nicht automatisch ein Nachweis der erfüllten EDÖB-Meldung. [15] Die EDÖB-Mitteilung vom 6. November 2026 bestätigt im dortigen Fall, dass nachträgliche technische Massnahmen die erforderliche Betroffeneninformation nicht aufheben. Empfänger, Informationsform und Ausnahmen bleiben konkret zu prüfen; eine öffentliche Bekanntmachung ist keine allgemeine KMU-Pflicht. [13] [5] [6]

**«Grenzen und fachliche Prüfung», Anfang:** Vorher Quellenprüfdatum `1. November 2026`, nachher `15. November 2026`. Nach dem ersten Satz neu `Erreichbare Quellen und allgemeine Empfehlungen belegen keine tatsächliche Einzelfallprüfung.` Alle folgenden Sätze einschliesslich Patch-Abgrenzung, bisherigem Fachmarker und Fachpersonenhinweis bleiben wortgleich.

**«Quellen»:** Vorher [1]–[11], nachher [1]–[15]. Ursprüngliche URLs und Titel unverändert. Neue Checklistenreferenzen Heimnetz [12], EDÖB-Mitteilung [13], CSV [14] und BACS-Meldeprozess [15] sind sämtlich im Arbeitsmittel zitiert.

## Unveränderte Abschnitte und lokale Konsistenz

Im Artikel bleiben Kurzantwort, H1, Einleitung, die übrigen Inhalte der Minute 0–15, sämtliche Inhalte Minute 15–30 und Minute 30–45, Polizeiabschnitt, bestehende gesetzliche Meldeschwellen und Fristen, hypothetisches Beispiel, Lösegeldabschnitt, typische Fehler, Nachbearbeitung einschliesslich Patch-Abgrenzung und «Nächster Schritt» unverändert. Keine SafePay-, Kühlanlagen-, CVE- oder KEV-Liste wurde eingeschoben. Alle internen Paketziele wurden erhalten.

Im Arbeitsmittel bleiben Zweck, Anwendung, Warnkasten, A-Kontaktfelder, C-Forensikteil, D-Backups, Tabellen und F-Entscheidungslog vollständig erhalten. Ausser den oben genau genannten Punkten bleibt auch E unverändert; insbesondere wurden keine Meldetexte, Empfängerfreigaben oder tatsächlichen Entscheide vorbefüllt. Der abschliessende Notfallkonzeptabsatz blieb unverändert.

Slug, Meta-Title, Meta-Description, Veröffentlichungsdatum **01.10.2026**, Autor **DKSchV Redaktion**, Artikelstatus **Entwurf – nicht freigegeben**, Arbeitsmittelstatus **Arbeitsvorlage – nicht freigegeben**, Fachstatus und sämtliche Originalmarker blieben wortgleich. Das Arbeitsmittel hatte kein Autor- oder Veröffentlichungsdatumsfeld; keines wurde erfunden.

Die punktuelle lokale Prüfung lief um **09:09:45 CET**, ohne globales QA-Skript und ohne Änderungen an Manifesten. Ergebnis: Artikel **18 definierte und 18 zitierte Quellen**, Arbeitsmittel **15 definierte und 15 zitierte Quellen**, `defined = cited`, keine ungenutzte oder undefinierte numerische Referenz, kein Eszett. Artikel **2'653 Haupttextwörter** und **2'997 Gesamtwörter**, Checkliste **1'580 Haupttextwörter** und **1'885 Gesamtwörter**, gezählt nach Leerraumtrennung, jeweils ohne Quellenabschnitt/Frontmatter für Haupttext. Beide bleiben über 1'400 Wörtern. Artikel **4**, Arbeitsmittel **2** ursprüngliche FACHPRÜFUNG-Marker erhalten.

Die Artikel-/Arbeitsmittel-Slugs für Backups, Wiederherstellungstest, Datenpanne und Checkliste sind in den vorhandenen lokalen Paketdateien bestätigt. Es wurden keine neuen internen Links eingefügt. Die bestehenden Service-/Kontaktlinks wurden unverändert übernommen; ihre lokale Wiederverwendung ist kein heutiger Live-Erreichbarkeitsnachweis. In den einmal gezielt durchsuchten README-/Manifest-/Begleitdateien wurde kein eigener neuer Slugnachweis für diese Serviceziele gefunden; es wurde keine Wiederholungsschleife angeschlossen. Die Wartungsbasis beschreibt diese Service-/Kontaktziele als bereits bestehende historische Ziele. Es erfolgte kein öffentlicher Linktest.

## Offene konkrete Fachfragen und Veröffentlichungsstatus

**BACS:** Untersteht die konkrete Organisation Art. 74b ISG? Greift eine sektorbezogene Ausnahme nach Art. 12 CSV? Betrifft der Angriff nur nicht erfasste Tätigkeiten? Welcher Tatbestand ist belegt, wann wurde der Angriff entdeckt und welche Angaben liegen vor? Diese Fragen wurden nicht entschieden. [23] [17]

**EDÖB und betroffene Personen:** Welche Personendaten und Verantwortlichen-/Auftragsbearbeiterrollen sind betroffen? Besteht ein voraussichtlich hohes Risiko? Welche direkte Information ist zum Schutz erforderlich, welche Form oder Ausnahme ist zulässig und wie wird sie zeitnah umgesetzt? Die November-Mitteilung beantwortet diese Fragen nur für ihren Fall, nicht für die Leserorganisation. [20] [4] [16] [30]

**Meldewege:** Ist eine gewählte Weiterleitung tatsächlich an den vorgesehenen Empfänger erfolgt und mit ausreichenden Angaben bestätigt? Die blosse Portalbeschreibung oder BACS-Erstmeldung ist dafür kein Nachweis. Keine Pflichtmeldung, E-Mail oder Betroffeneninformation wurde im Auftrag erstellt oder versendet. [18] [11] [33]

**Forensik und Wiederanlauf:** Welche Systeme, Heimnetz-Verbindungen, Konten, Persistenzmechanismen und Datenabflüsse sind tatsächlich betroffen? Welche Sicherungsart ist geeignet, wer wahrt Originale und Beweiskette, wann darf bereinigt oder neu aufgebaut werden und welcher Backupstand ist sauber wiederherstellbar? Keine dieser Fragen wurde technisch geprüft oder freigegeben. [1] [5] [15]

**Template-Ausleseblocker:** Die am 11.11.2026 neu datierte BACS-KMU-Vorlage muss vor einer Aussage über ihren Inhalt mit einem geeigneten, autorisierten Dokumentleseverfahren tatsächlich ausgelesen werden. Der vorliegende Base64-/ZIP-Abruf erfüllt das nicht. Die Vorlage bleibt ein offener konkreter Inhaltsblocker; sie wird nicht durch den lesbaren BACS-Seitentext als geprüft ausgegeben. [31] [6]

**Lösegeld, Polizei, Sanktionen, Verträge und Versicherungen:** Konkrete Zahlungs-, Straf-, Sanktions-, Vertrags- und Versicherungsfolgen sowie kantonale Kontaktwege wurden nicht beurteilt. Das BACS-Abraten und die Empfehlung der Abstimmung mit der Kantonspolizei bleiben allgemeine Orientierung. [1]

**Veröffentlichung:** Artikel 01 ist seit dem vorgesehenen Termin 01.10.2026 terminlich fällig, bleibt aber **nicht freigegeben**. Auch die Arbeitsvorlage bleibt **nicht freigegeben**. Kein CMS wurde geprüft oder verändert, keine Anmeldung versucht, kein Import ausgeführt und kein Live-/Publikationsstatus behauptet. Die lokale Quellenpflege behebt weder offene Fachfragen noch eine Publikationssperre. Die Rechtsquellenstände DSG 07.07.2025, ISG 01.10.2025, DSV 01.12.2025 und CSV 01.04.2025 gehören ausschliesslich in dieses Quellenjournal; sie sind keine neuen Fachfreigabedaten.

## References

[1]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[2]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz DSG"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden Art. 24 DSG Version 1.2"
[5]: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware "CISA – Ransomware Response Checklist"
[6]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Notfallkonzept"
[7]: https://csrc.nist.gov/pubs/sp/800/61/r3/final "NIST – SP 800-61 Rev. 3 Final"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Informationssicherheitsgesetz ISG"
[9]: https://www.suisse-epolice.ch/cybercrime-case "Suisse ePolice – Cyberkriminalität anzeigen"
[10]: https://www.bacs.admin.ch/de/26w40-de "BACS – Malwareverdacht Woche 40"
[11]: https://www.report.ncsc.admin.ch/de/chat?path=406%3E407%3E1 "BACS – aktuelle Meldeoberfläche"
[12]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – PHP-Warnung vom 21. Oktober 2026"
[13]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach"
[14]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung DSV"
[15]: https://www.bacs.admin.ch/de/26w44-de "BACS – Heimnetz Woche 44 vom 3. November 2026"
[16]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB – Informationspflicht der Onlineshop-Betreiberin"
[17]: https://www.fedlex.admin.ch/eli/cc/2025/169/de "Fedlex – Cybersicherheitsverordnung CSV"
[18]: https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden "BACS – Wie muss gemeldet werden?"
[19]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG Chronologie"
[20]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – DSG XML vom 7. Juli 2025"
[21]: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history "Fedlex – ISG Chronologie"
[22]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20251001/de/xml/fedlex-data-admin-ch-eli-cc-2022-232-20251001-de-xml-1.xml "Fedlex – vorhandenes ISG XML vom 1. Oktober 2025"
[23]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20251001/de/xml/fedlex-data-admin-ch-eli-cc-2022-232-20251001-de-xml-2.xml "Fedlex – von Chronologie verlinktes ISG XML vom 1. Oktober 2025"
[24]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV Chronologie"
[25]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml "Fedlex – DSV XML vom 1. Dezember 2025"
[26]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[27]: https://www.bacs.admin.ch/de/aktuelle-vorfaelle "BACS – Aktuelle Vorfälle"
[28]: https://www.cisa.gov/news-events/news/cisa-announces-enhanced-reporting-form-cyber-incidents "CISA – erweitertes Cybermeldeformular vom 9. November 2026"
[29]: https://www.cisa.gov/news-events/cybersecurity-advisories "CISA – Cybersecurity Alerts and Advisories"
[30]: https://www.edoeb.admin.ch/dam/de/sd-web/ZjhZ9UBOprVL/Urteil%20BVGer%20A_3790_2024%20vom%208.%20April%202026%20betreffend%20Verf%C3%BCgung%20vom%2028.%20Mai%202024.pdf "BVGer – Urteil A-3790/2024 vom 8. April 2026"
[31]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS – KMU-Template mit offenem Ausleseblocker"
[32]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen vom 10. November 2026"
[33]: https://databreach.edoeb.admin.ch/report "EDÖB – öffentlicher DataBreach-Portaleinstieg"
[34]: https://www.bacs.admin.ch/de/wer-muss-melden "BACS – Wer muss melden?"
[35]: https://www.bacs.admin.ch/de/was-muss-gemeldet-werden "BACS – Was muss gemeldet werden?"
[36]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a "CISA – SafePay Ransomware vom 20. Oktober 2026"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/01-ransomware-erste-60-minuten.md:** `/resources/01-60-minuten-checkliste` → `https://www.dkschv.ch/wissen/resources/01-60-minuten-checkliste.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/notfallplanung` → `https://www.dkschv.ch/notfallplanung.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
