# Artikel 11 – Quellenprüfung und Änderungen

**Prüfdatum:** 15. November 2026, ISO-KW 46, Europe/Zurich, CET.  
**Autor:** Manus AI.  
**Gegenstand:** Ausschliesslich Artikel 11 «Lieferantenrisiken im Griff: BACS-Kreislauf für Cloud-, IT- und kritische Dienstleister in Schweizer KMU» und das Arbeitsmittel «Lieferantenfragebogen und Priorisierungsmatrix».  
**Veröffentlichungsstatus:** Artikel `Entwurf`; Arbeitsmittel `Arbeitsvorlage – nicht freigegeben`. Der unveränderte Veröffentlichungstermin des Artikels ist 10.12.2026 und am Prüftag noch nicht erreicht. Keine Fach-, Rechts-, Vertrags-, Datenschutz-, Forensik-, Incident-Response-, Tenant-, Produkt- oder Veröffentlichungsfreigabe.

## Belegte Änderungen und verbleibende Einschränkungen

Die zwölf bisherigen externen Originalreferenzen wurden direkt auf Inhalt und Erreichbarkeit geprüft. Vier neue Originalquellen sind passend zitiert: Microsoft vom 5. November zu Anbieter-App-Secrets und nachgelagerten Kundentenants, BACS vom 10. November zu extern gewarteten Kühlsteuerungen, Microsoft vom 13. November zu Fernwartung und Technikersitzungen sowie Microsoft vom 12. November zu KI-Modellartefakten. Der Verbund enthält damit 16 eindeutige zitierte externe Originalquellen, davon alle 16 im Artikel und 13 im Arbeitsmittel. Die Ergänzungen sind bedingte, risikobasierte Prüffragen, keine pauschale neue Schweizer Pflicht und kein Befund gegen eine konkrete Organisation.[13] [14] [15] [16]

Zusätzlich wurden elf externe Prüfziele geöffnet: sechs Fedlex-Zusatzendpunkte und fünf aktuelle Orientierungs-, Auffindungs- oder Abgrenzungsquellen. Insgesamt sind unten 27 eindeutige externe Originalziele dokumentiert. Von diesen liefern 25 einen fachlich relevanten lesbaren Inhalt, teils erst über die direkte DOCX-Extraktion; zwei Fedlex-Änderungsübersichten liefern nur einen JavaScript-Hinweis. Der generische HTTP-Abruf der kanadischen Quelle erhält zudem weiterhin 403, obwohl der getrennte Inhaltsabruf lesbar ist. Diese Einschränkungen werden nicht als erfolgreiche Erreichbarkeitsprüfung ausgegeben.[12] [18] [21]

**Tatsächliche Abrufe:** Die erste Suchantwort erfolgte am 15. November 2026 um 09:06:15 CET. Die unten verwendeten Fetch-Rückgaben erfolgten zwischen 09:06:08 und 09:10:50 CET; generische HTTP-Anfragen zwischen 09:06:46 und 09:10:56 CET. Bei der ersten HTTP-Serie wurden Startzeiten je Anfrage und die gemeinsame späteste Rückgabe um 09:06:53 protokolliert, keine erfundenen einzelnen Endzeiten. Bei der zweiten Serie sind Start und Ende je Anfrage protokolliert. Diese Zeiten bezeichnen heutige Abrufe nach 09:00, nicht den historischen Wortlaut um 09:00. Bei unversionierten Seiten ist kein minutengenauer rückwirkender Seitenstand belegt.

Die Wartungsbasis, Vorwochennews, Vormerkungen und der Einzelbericht vom 1. November wurden vollständig gelesen. Die Suche mit deutschen und englischen Varianten diente der Auffindung aktueller BACS-/Microsoft-/EDÖB-Lieferantenmeldungen seit 1. November. Verwendete neue Aussagen wurden am geöffneten Original geprüft, nicht aus Suchsnippets übernommen. BACS «Im Fokus» und die aktuellen verlinkten Microsoft-Meldungen wurden ergänzend direkt geöffnet. Dieser begrenzte Quellenraum ist keine vollständige Internet- oder Nichtfundzusage; nach den klar dokumentierten Zugriffsgrenzen erfolgten keine Wiederholungsschleifen.[23] [26]

## Quellenstand je zitierter externer Originalquelle

### 1. BACS – Cybersicherheit in der Lieferkette

**Original-URL:** https://www.bacs.admin.ch/de/supply-chain-de. **Quellendatum:** Die Seite selbst ist undatiert; die verlinkten Word-Arbeitsmittel sind mit 18. März 2025 ausgewiesen. **Heutiger Abruf:** Fetch 09:06:08 CET inhaltlich erfolgreich; generischer HTTP-Abruf ab 09:06:46 CET, 200. **Aussage:** C-SCRM, bestmögliche Transparenz, drei Lieferantentypen, Business Impact und der siebenstufige Kreislauf von Bestandesaufnahme bis Vertragsprüfung sind lesbar und tragen den bestehenden Haupttext. **Einschränkung:** Keine publizierte Seitenhistorie und keine organisationsbezogene Lieferantenbewertung; keine materielle Änderung des Kreislaufs gegenüber den dokumentierten Aussagen vom 1. November belegt.[1]

### 2. BACS – Lieferantenverträge: Best Practice

**Original-URL:** https://www.bacs.admin.ch/dam/de/sd-web/iXNmDC-pccRC/best_practice_lieferantenvertrag_de.docx. **Quellendatum:** 18. März 2025 laut Lieferkettenseite. **Heutiger Abruf:** Fetch 09:06:10 CET liefert den DOCX-Container, keinen sinnvoll dekodierten Vertragstext. Direkter HTTP-Abruf ab 09:06:46 CET: 200, 145’124 Bytes; ZIP/XML-Inhalt vollständig extrahiert. SHA-256 `00af669d445acddb68938792fd323a1cf84e794cc4d1bf41089ea0801057da2a`, identisch mit dem im Einzelbericht vom 1. November dokumentierten Wert. **Aussage:** Risikoangemessener Schutz, Verschlüsselung, Zugriffstransparenz, Vorfall-/Schwachstellenmeldung, Patchen, Unterlieferanten, Nachweise, Incident Response sowie mögliche Haftungsthemen. **Einschränkung:** Die Word-Vorlage nennt mögliche Vertragselemente, keine automatisch anwendbaren Fristen oder Haftungsfolgen. Die Fetch-Auslesegrenze wurde durch tatsächliche Binärextraktion geklärt, nicht als lesbarer Fetch umformuliert.[1] [2]

### 3. BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz

**Original-URL:** https://www.bacs.admin.ch/de/notfallkonzept. **Quellendatum:** Seite undatiert; beide IT-Notfallplan-Templates werden heute mit 11. November 2026 ausgewiesen, gegenüber 18. Mai 2026 für das KMU-Template im Vorbericht. **Heutiger Abruf:** Fetch 09:06:08 CET lesbar, generischer HTTP-Abruf ab 09:06:46 CET: 200. **Aussage:** Vier Phasen, Lieferkettenblick, zentrale Kontakte, Verantwortlichkeiten und Debriefing bleiben belegt. **Einschränkung:** Der neue angezeigte Downloadstand beweist ohne frühere Datei keinen vollständigen materiellen Versionsvergleich. Das aktuelle KMU-Template wurde zusätzlich direkt geprüft, siehe Quelle 25. Keine neue pauschale Melde- oder Wiederanlaufvorgabe in Artikel 11 daraus abgeleitet.[3] [25]

### 4. Fedlex – Datenschutzgesetz DSG, SR 235.1

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de. **Quellenstand:** Anzeige «in Kraft», Stand 7. Juli 2025. **Heutiger Abruf:** Fetch 09:06:08 CET liefert Rechtsinhalt und Fassungsverweise; generischer HTTP-Abruf ab 09:06:46 CET: 200, aber HTTP allein ist kein Inhaltsnachweis. **Aussage:** Art. 8 risikoangemessene Datensicherheit, Art. 9 Voraussetzungen und Vergewisserung bei Auftragsbearbeitung sowie vorgängige Genehmigung für Dritte, Art. 16 Auslandbekanntgabe. **Einschränkung:** Keine konkrete rechtliche Zulässigkeitsprüfung. Die Seite zeigt eine Wartungsankündigung für 13. November 20:00 bis 15. November 20:00; dennoch waren die genannten heutigen Inhaltsabrufe erfolgreich. Chronologie und vorhandene amtliche XML wurden gesondert gelesen. Die Änderungsübersicht ist heute nicht inhaltlich auslesbar, siehe Quelle 18.[4] [17] [18] [19]

### 5. Fedlex – Datenschutzverordnung DSV, SR 235.11

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de. **Quellenstand:** Anzeige «in Kraft», Stand 1. Dezember 2025. **Heutiger Abruf:** Fetch 09:06:11 CET liefert Rechtsinhalt; generischer HTTP-Abruf ab 09:06:46 CET: 200. **Aussage:** Art. 1 laufende Prüfung von Schutzbedarf, Risiko und Massnahmen; Art. 2 Schutzziele; Art. 3 unter anderem Wiederherstellung und Systemsicherheit; Art. 7 spezifische/allgemeine Genehmigung und Information/Widerspruch bei Unterauftragsbearbeitung. **Einschränkung:** Keine individuelle Rechtsfreigabe. Die Information bei allgemeiner Genehmigung ist in DSV Art. 7 geregelt, weshalb im Vertragsabsatz des Artikels die vorhandene Zitation [5] ergänzend gesetzt wurde. Die Änderungsübersicht liefert keine auslesbaren Daten, siehe Quelle 21.[5] [20] [21] [22]

### 6. EDÖB – Cloud-Computing

**Original-URL:** https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud. **Quellendatum:** Kein eigenes Änderungs-/Publikationsdatum in der gelesenen Seite. **Heutiger Abruf:** Fetch 09:06:11 CET lesbar; generischer HTTP-Abruf ab 09:06:46 CET: 200. **Aussage:** Rollenlage, Hauptverantwortung des Verantwortlichen, Weisungen, Sicherheit, Unterauftragsbearbeitung, Auslandbekanntgaben, Rückgabe/Löschung, Mitwirkung und Audits. **Einschränkung:** Cloud-Nutzer können auch selbst Auftragsbearbeiter sein. Die bestehende Rollenabgrenzung bleibt erhalten; keine Prüfung konkreter AGB, Datenorte oder Verträge. Kein belegter materieller Änderungsbedarf.[6]

### 7. EDÖB – Outsourcing, Auftragsdatenbearbeitung

**Original-URL:** https://www.edoeb.admin.ch/de/outsourcing-auftragsdatenbearbeitung. **Quellendatum:** Undatiert in der gelesenen Seite. **Heutiger Abruf:** Fetch 09:06:11 CET lesbar; generischer HTTP-Abruf ab 09:06:48 CET: 200. **Aussage:** Verantwortlichkeit bleibt beim Verantwortlichen; sorgfältige Auswahl, angemessene Instruktion und soweit nötige Überwachung. Genehmigung, Geheimhaltung, Mitwirkung und Auslandbekanntgaben bleiben relevante Prüffelder. **Einschränkung:** Kein Vertrag und kein konkreter Datenfluss geprüft; keine historische Wortlautgarantie und kein neuer materieller Änderungsbedarf belegt.[7]

### 8. NIST – SP 800-161 Rev. 1, Update 1

**Original-URL:** https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final. **Quellenstand:** Mai 2022 mit Updates per 1. November 2024; Dokumenthistorie 1. November 2024, Planungsnotiz 2. Dezember 2025 zum ausfüllbaren Fragebogen. **Heutiger Abruf:** Fetch 09:06:11 CET lesbar; generischer HTTP-Abruf ab 09:06:48 CET: 200. **Aussage:** Identifikation, Bewertung und Minderung von Lieferkettenrisiken, integriert ins Risikomanagement. **Einschränkung:** Ausländische Orientierung, keine Schweizer Norm; keine neue Revision an der geöffneten Publikationsseite belegt. Der Haupttext zur NIST-Einordnung bleibt erhalten.[8]

### 9. BACS – Kritische Schwachstellen in PHP

**Original-URL:** https://www.bacs.admin.ch/de/warnung-php-de. **Publikation:** 21. Oktober 2026. **Heutiger Abruf:** Fetch 09:06:12 CET lesbar; generischer HTTP-Abruf ab 09:06:49 CET: 200. **Aussage:** Eingebettete und extern betriebene Anwendungen mitprüfen; tatsächliche Paketstände und Herstellerinformationen bei Backports berücksichtigen; laufende Behebung kontrollieren; Update beseitigt keine bereits erfolgte Kompromittierung. **Einschränkung:** Keine konkrete PHP-Installation, Versionslinie oder frühere Kompromittierung geprüft. Die bestehenden dauerhaften Inventar-/Fixnachweis-Passagen bleiben unverändert; neue Kühlsteuerungsfragen sind davon getrennt.[9]

### 10. EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant

**Original-URL:** https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein. **Publikation:** 23. Oktober 2026. **Heutiger Abruf:** Fetch 09:06:12 CET lesbar; generischer HTTP-Abruf ab 09:06:49 CET: 200. **Aussage:** Formelle Untersuchung gegen PK Softech nach gemeldetem Angriff; Klärung der Personendaten, rechtlichen Rahmenbedingungen, tatsächlichen Umsetzung der Übertragungen und des Abflussumfangs. Der aktuelle Text nennt weiterhin hängige Verfahren. **Einschränkung:** Kein abschliessender Verstossbefund und kein aktueller eigener Verfahrensabschluss belegt; keine Übertragung auf andere Lieferanten. Rollen- und Kontaktpassagen bleiben erhalten.[10]

### 11. Microsoft – ARTEX und ConnectWise-Lieferkettenkompromittierung

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/. **Publikation:** 21. Oktober 2026; kein gesondertes Aktualisierungsdatum in der gelesenen Fassung. **Heutiger Abruf:** Fetch 09:06:13 CET lesbar; generischer HTTP-Abruf ab 09:06:49 CET: 200. **Aussage:** Bestimmte kompromittierte Anbieteranwendungen, privilegierte Zugänge, Dienstprinzipale, Berechtigungen, nachgelagerte Aktivitäten und Beweissicherung vor irreversiblen Änderungen. Anwesenheit einer App oder erfolgreiche Authentifizierung allein beweisen keinen Datenabfluss. **Einschränkung:** Konkrete Massnahmen gelten für die betroffenen Anwendungen; keine Tenant- oder ConnectWise-Prüfung ausgeführt. Die bestehende Einordnung bleibt; die neue Meldung vom 5. November ist separat zitiert.[11] [13]

### 12. Canadian Centre for Cyber Security – AI token consumption

**Original-URL:** https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125. **Quellenstand:** «October 2026», «Date modified: 2026-10-22». **Heutiger Inhaltsabruf:** Fetch-Rückgabe 09:06:13 CET lesbar; vollständige gespeicherte Extraktion einschliesslich Änderungsdatum um 09:06:44 CET gelesen. **Heutiger HTTP-Status:** Generische Python-requests-Anfrage ab 09:06:49 CET, vor 09:06:53 abgeschlossen: **403**, 179 Bytes. **Aussage:** Verbrauch, Raten-/Budgetlimiten, Tokenerschöpfung, Kosten und Verfügbarkeit, Monitoring, Warnungen, Drittanbieterlimiten und manuelle/andere Ausweichabläufe tragen die bisherigen KI-Passagen. **Einschränkung und Blocker:** Zugriffsprofilabhängige Erreichbarkeit bleibt ungelöst; keine generische 200-Erreichbarkeit oder Go-live-Linkprüfung behauptet. Inhalt bleibt belegt und als freiwillige ausländische Orientierung erhalten. Der heutige 403 ist ein neuer tatsächlicher Messwert, keine kopierte historische Messung.[12]

### 13. Microsoft – Exponierte Secrets und App-Credentials

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/. **Publikation:** 5. November 2026. **Heutiger Abruf:** Fetch 09:06:14 CET; vollständige Extraktion 09:07:36 CET gelesen; generischer HTTP-Abruf ab 09:06:50 CET: 200. **Aussage:** Agentische Suche nach Secrets, auch am Anbieter kompromittierte Multitenant-App-Zugangsdaten mit Zugriff auf Kundentenants; entsprechende Folgeaktivitäten bereits ab 28. Oktober. Entfernen der Offenlegung ersetzt Widerruf/Rotation nicht; historische Nutzung prüfen, bereits ausgestellte Tokens bleiben laut Quelle bis zum Ablauf gültig. MSPs sollen Kundenbeziehungen und Benachrichtigung nach Vereinbarungen prüfen. **Einschränkung:** Keine neue Angriffsstartzeit am Publikationstag, keine konkrete Schweizer Betroffenheit, keine universelle Tenantmassnahme. Produkt-/Lizenzvoraussetzungen der Hersteller-Eindämmung wurden nicht als allgemeine Pflicht übernommen. Neu zitiert im Artikel [13] und Arbeitsmittel [10].[13]

### 14. BACS – Kühl- und Kältesteuerungen

**Original-URL:** https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de. **Publikation:** 10. November 2026. **Heutiger Abruf:** Fetch 09:07:35 CET lesbar; generischer HTTP-Abruf 09:10:51–09:10:53 CET: 200. **Aussage:** Angriffe auch in der Schweiz, betriebliche Folgen manipulierter Temperaturen/Alarme, Inventarisierung einschliesslich externer Wartung, Erreichbarkeit, Firmware, Supportende und Hersteller-/Ersatzwege. **Einschränkung:** Nur bei eingesetzten relevanten Steuerungen; keine pauschale Verwundbarkeit und kein konkreter Anlagenbefund. Keine exakten Produktfixstände im Artikel vorgegeben, keine geschützte CSH-Plattform geöffnet. Neu zitiert im Artikel [14] und Arbeitsmittel [11].[14]

### 15. Microsoft – SCKit, ScreenConnect und Technikersitzungen

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/. **Publikation:** 13. November 2026; laut Bericht meldete ConnectWise die Kampagne ab 11. November. **Heutiger Abruf:** Fetch 09:07:58 CET mit lesbaren für die Ergänzung relevanten Passagen; generischer HTTP-Abruf 09:10:51–09:10:53 CET: 200. **Aussage:** Managementinstanz/Erweiterungs-API, Kundenendgerät und Technikerclient sind unterschiedliche Angriffsflächen; unerlaubte Clients können unabhängig von der legitimen Konsole bestehen, Technikersitzungen werden angegriffen. Konsole und Technikerclient werden getrennt aktualisiert; unabhängiger Untersuchungskanal, Persistenz und Sitzungen beachten. **Einschränkung:** Initiale Eintrittsmethode bleibt laut Quelle in Untersuchung. Keine konkret installierte Erweiterung, Clientversion oder Sitzung geprüft; keine Weitergabe von Forensik-/Bereinigungskommandos und keine pauschale Anweisung zum Entfernen legitimer Clients. Neu zitiert im Artikel [15] und Arbeitsmittel [12].[15]

### 16. Microsoft – Post-Training-Lieferketten und Coding-Agenten

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/. **Publikation:** 12. November 2026. **Heutiger Abruf:** Fetch 09:07:58 CET liefert Studienbeschreibung und relevante Schutzpassagen; generischer HTTP-Abruf 09:10:51–09:10:54 CET: 200. **Aussage:** Zwei Forschungsstudien zu Dataset-/Checkpoint-Poisoning; Herkunft, Version, Hash/Review, Evaluation in der eingesetzten Agentenkonfiguration und Grenzen ausserhalb des Modells. Normale Benchmarks können verborgene Verhaltensweisen übersehen. **Einschränkung:** Forschungsangriffe setzen unterschiedlichen Angreiferzugriff auf Trainingsdaten oder Modelle voraus; keine Inzidenzstatistik, kein Befund gegen alle Modelle/Anbieter und keine Schweizer Norm. Studienquoten wurden nicht verallgemeinert. Neu zitiert im Artikel [16] und Arbeitsmittel [13].[16]

## Zusätzliche externe Prüfziele, einschliesslich nicht auslesbarer Quellen

### 17. Fedlex – DSG-Chronologie

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/history. **Abruf:** Fetch 09:06:41 CET lesbar; generisches HTTP 09:10:51–09:10:54 CET: 200. **Quellenstand/Aussage:** Letzte aufgeführte Fassung 7. Juli 2025, Berichtigung BK. **Einschränkung:** Chronologie belegt den aufgeführten Konsolidierungsstand, nicht das Ergebnis einer heutigen individuellen Rechtsprüfung; nicht mit einer lesbaren Änderungsübersicht gleichsetzen.[17]

### 18. Fedlex – DSG-Änderungsübersicht: Inhaltsblocker

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes. **Abruf:** Fetch 09:06:35 CET meldet technisch «success», liefert aber ausschliesslich einen mehrsprachigen JavaScript-Hinweis, **keine Änderungsdaten**. Generisches HTTP 09:10:51–09:10:54 CET: 200 mit Anwendungshülle. **Quellenstand/Aussage:** Kein aktueller inhaltlicher Änderungsstand aus diesem Ziel ermittelbar. **Einschränkung:** Konkreter Ausleseblocker bleibt offen. Lesbare ELI-/Chronologie-/XML-Inhalte belegen die genannten Fassungen, ersetzen aber nicht die Behauptung einer vollständig gelesenen Änderungsübersicht.[18] [17] [19]

### 19. Fedlex – Amtliche DSG-XML

**Original-URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml. **Abruf:** Fetch 09:06:38 CET relevant selektierter Rechtsinhalt lesbar; generisches HTTP 09:10:51–09:10:54 CET: 200. **Quellenstand/Aussage:** Amtliche Fassung 7. Juli 2025; DSG Art. 8, 9, 16 direkt bestätigt. **Einschränkung:** Vorhandene URL aus letzter Prüfung und aktueller ELI-/Chronologieverlinkung, keine erfundene Fassung. Keine Rechtsfreigabe.[19]

### 20. Fedlex – DSV-Chronologie

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de/history. **Abruf:** Fetch 09:06:42 CET lesbar; generisches HTTP 09:10:53–09:10:56 CET: 200. **Quellenstand/Aussage:** Letzte aufgeführte Fassung 1. Dezember 2025, Änderung vom 29. Oktober 2025. **Einschränkung:** Keine neuere Konsolidierung an diesem Ziel belegt; keine vollständig gelesene Änderungsübersicht oder Einzelfallentscheidung.[20]

### 21. Fedlex – DSV-Änderungsübersicht: Inhaltsblocker

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes. **Abruf:** Fetch 09:06:42 CET technisch «success», tatsächlich nur JavaScript-Hinweis ohne Änderungsdaten; generisches HTTP 09:10:53–09:10:56 CET: 200 mit Anwendungshülle. **Quellenstand/Aussage:** Aktueller Inhalt aus diesem Endpunkt nicht auslesbar. **Einschränkung:** Offener Ausleseblocker, nicht als erfolgreiche Änderungsprüfung gewertet. Keine Browseroperation zur Umgehung vorgenommen.[21]

### 22. Fedlex – Amtliche DSV-XML

**Original-URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml. **Abruf:** Fetch 09:06:44 CET relevant selektierter Rechtsinhalt lesbar; generisches HTTP 09:10:54–09:10:56 CET: 200. **Quellenstand/Aussage:** Amtliche Fassung 1. Dezember 2025, Art. 1–3 und 7 korrespondieren mit lesbarer ELI-Anzeige. **Einschränkung:** Vorhandene Alternative, nicht konstruierte URL; keine automatische Rechts- oder Vertragsfreigabe.[22] [5]

### 23. BACS – Im Fokus

**Original-URL:** https://www.bacs.admin.ch/de/im-fokus. **Abruf:** Fetch 09:06:43 CET lesbar. Kein separater heutiger generischer HTTP-Test. **Quellenstand/Aussage:** Aktuelle Übersicht mit Meldungen vom 2., 3., 6., 9. und 10. November; liefert die direkt geöffneten Links zur Kühlanlagenwarnung und Cyberresilienzmeldung. **Einschränkung:** Dient als Auffindungsübersicht, nicht als Ersatz für die Originalmeldungen. Phishing-Themen der Übersicht liefern für sich keinen neuen C-SCRM-Vertragsprüfpunkt; kein vollständiger Nichtfund für alle Behördenmeldungen behauptet.[23] [14] [24]

### 24. BACS – Handlungsfähig bleiben im Ernstfall

**Original-URL:** https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de. **Publikation:** 2. November 2026. **Abruf:** Fetch 09:07:36 CET lesbar; kein separater generischer HTTP-Test. **Aussage:** Kritische Prozesse, externe IT-/OT-Dienstleister und eingeübte Notfall-/Wiederherstellungspläne. **Einschränkung:** Veranstaltungs-/Orientierungsbeitrag; die bestehende Notfallpassage trägt den Punkt bereits. Keine zusätzliche Artikelreferenz und keine Teilnahme-/Leistungsfreigabe.[24]

### 25. BACS – Aktuelles KMU-Notfallplan-Template

**Original-URL:** https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx. **Quellendatum:** Download auf Notfallkonzeptseite mit 11. November 2026 ausgewiesen; die internen Beispieldaten zur Erstellungs-/Genehmigungshistorie sind Musterdaten, keine reale Freigabe. **Abruf:** Direkte HTTP-Anfrage 09:07:37–09:07:41 CET: 200, 315’545 Bytes; vollständige Word-XML-Extraktion. Fetch 09:10:50 CET liefert Binär-/Base64-Daten, keinen sinnvollen Text. **Aussage:** Kritische IT-Abhängigkeiten/externe Partner, Kontakte, Rollen, Wiederanlaufpriorisierung und Notfallübungen vorhanden. **Einschränkung:** Kein früheres Dateiexemplar für materiellen Vollvergleich herangezogen; keine Musterdaten, Fristen oder gesetzlichen Vereinfachungen als neue pauschale Vorgabe übernommen. Keine Anpassung des tatsächlichen Notfallplans eines KMU; bestehender Artikeltext bleibt hierfür ausreichend.[3] [25]

### 26. Microsoft – ARTEX im Finanzsektor

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/. **Publikation:** 6. November 2026. **Abruf:** Fetch 09:07:36 CET lesbar; kein separater generischer HTTP-Test. **Aussage:** Storm-3358, automatisierte Angriffe im Finanzsektor, allgemeine Schutz-/Erkennungsorientierung; aktuelle weiterführende Links auf die direkt geöffneten Meldungen vom 11., 12. und 13. November. **Einschränkung:** Keine zusätzliche spezifische C-SCRM-Pflicht aus dieser Meldung. Keine Schweizer KMU-Inzidenz und keine Produktwirksamkeit geprüft; nur im Journal zitiert.[26]

### 27. Microsoft – GSocket und fortbestehender Fernzugriff

**Original-URL:** https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/. **Publikation:** 11. November 2026. **Abruf:** Fetch 09:07:58 CET relevant selektierter Inhalt lesbar; kein separater generischer HTTP-Test. **Aussage:** Persistenter Fernzugriff auf kompromittierten Linux-Servern kann nach dem Patchen des ursprünglichen Angriffswegs bestehen bleiben. **Einschränkung:** Die bestehende PHP-Passage grenzt Update und Kompromittierungsbeseitigung schon ab. Keine zusätzlichen Zahlen, IOCs, Befallsvermutungen oder Bereinigungsschritte aufgenommen; nur im Journal zitiert.[27] [9]

## Rechtsquellenstand und historische Fachfelder

Die lesbaren aktuellen ELI-Anzeigen, Chronologien und vorhandenen amtlichen XML-Fassungen zeigen DSG 7. Juli 2025 und DSV 1. Dezember 2025. Daraus ist keine neue materielle Änderung der hier herangezogenen Vorschriften seit 1. November belegt. Beide Änderungsübersichten sind heute nicht auslesbar; eine lückenlos gelesene heutige Änderungsübersicht wird ausdrücklich nicht behauptet.[4] [5] [17] [18] [19] [20] [21] [22]

In den Ausgangsfrontmattern bestehen weder `rechtsstand` noch `fachlich_geprüft_am` oder `fachlich_geprueft_am`. Es wurden keine solchen Felder angelegt. Der Rechtsquellenstand steht nur in diesem Journal; `fachprüfung_status` bleibt in beiden Dateien wortgleich `[FACHPRÜFUNG ERFORDERLICH]`. Quellenpflege ist kein neues Fachprüfdatum.

## Unveränderte Abschnitte und Paketziele

Im Artikel bleiben H1, Kurzantwort und Einleitung, «Warum Lieferantenrisiken bei der Geschäftsleitung beginnen», «Die Lieferantenlandkarte: Daten, Zugänge und Abhängigkeiten sichtbar machen», «Anbieter kritischer Dienstleistungen», «Kritikalität bewerten und die Prüfung passend zuschneiden», «Risikobasiert prüfen: erst eigene Antworten, dann das Lieferantengespräch», «Typische Fehler, die den Kreislauf aushebeln», «Umsetzung in sieben Schritten» und «Nächster Schritt» unverändert. In den drei um neue Absätze ergänzten Fachabschnitten bleibt jeder ursprüngliche Absatz erhalten. Im Vertragsabschnitt wird nur die ergänzende vorhandene DSV-Zitation gesetzt, kein Wortlaut oder Fachmarker geändert.

Im Arbeitsmittel bleiben H1, Zweck, Anwendung, Ausfüllhinweis, sämtliche ursprünglichen Tabellenzeilen, Teil B, Teil C, D2, Teil E und «Grenzen des Arbeitsmittels» unverändert. Teil A, D1, D3 und D4 erhalten ausschliesslich die unten genau dokumentierten Ergänzungen. Artikelquellen [1]–[12] und Arbeitsmittelquellen [1]–[9] bleiben unverändert definiert.

SEO-Felder `meta_title` und `meta_description`, Slugs, Autor, Zielgruppe, Suchintention, Hauptkeyword, Veröffentlichungstermin, Entwurfsstatus und Fachstatus des Artikels bleiben unverändert. Passender Artikel, Arbeitsmittelname, Slug und Nichtfreigabestatus der Vorlage bleiben unverändert. Jeder ursprüngliche Fachmarker bleibt einschliesslich seines zugehörigen Fachprüfhinweises wortgleich; weiterhin je vier Marker, davon je einer im Frontmatter und drei im sichtbaren Text.

Die internen Artikel-/Arbeitsmittelziele `/wissen/backup-wiederherstellung-testen`, `/wissen/nis2-dora-schweiz`, `/wissen/lieferantenrisiken-cybersecurity` und `/resources/11-lieferantenfragebogen` sind im lokalen Paket über vorhandene Slugs belegt. Keine neuen internen Links gesetzt. Die vorhandenen Serviceziele `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/notfallplanung`, `/unsere-dienstleistungen/sicherheitsanalyse` und `/kontakt` bleiben erhalten; ihre heutige Live-Erreichbarkeit wurde nicht geprüft. Kein historischer HTTP-403-/404-Befund des Pakets wird als heutige Messung ausgegeben.

## Konkrete offene Fachfragen und Veröffentlichungsblocker

Datenschutz-/Rechtsfachpersonen müssen für den tatsächlichen Einsatz die Rolle jeder beteiligten Einheit, zulässige Weisungen und eigene Zwecke, Geheimhaltung, Unterauftragsgenehmigung, Änderung/Widerspruch, Datenorte, Auslandbekanntgaben, Rückgabe/Löschung und Vertragsklauseln beurteilen. Die Fragebogenantworten ersetzen das nicht. Welche Vertragsfristen, Nachweise oder Haftungsfolgen zu einer bestimmten Dienstleistung passen, bleibt offen.[2] [4] [5] [6] [7]

Für privilegierte Integrationen bleiben tatsächliche Application-/Tenant-IDs, Dienstprinzipale, Consent und Berechtigungen, Secret-Verantwortung, Offenlegungen, vorhandene Protokolle, historische Nutzung, bereits ausgestellte Tokens und weitere Persistenz offen. Bei einem tatsächlichen Vorfall sind Eindämmung, Beweissicherung, Rotation und Verifikation der verbliebenen Zugänge Sache autorisierter Fachstellen, nicht Bestandteil dieses Quellenlaufs.[11] [13]

Bei Fernwartung bleiben konkrete Instanzen, Erweiterungen, Technikerclient-Versionen, verwaltete Geräte, legitime Verbindungsziele, exponierte Sitzungen, unabhängige Untersuchungswege und Bereinigungsnachweise offen. Beim Kühlanlagenbetrieb fehlen konkrete Modelle, Firmware-/Supportstände, Erreichbarkeit und ein durch Anlagenfachpersonen geprüfter sicherer Änderungs-/Ersatzweg. Keine reale Installation wurde geprüft.[14] [15]

Für KI-Angebote bleiben tatsächliche Quoten, Budgets, Warnungen, Notbetrieb, Modell-/Datensatzherkunft, Integritätsnachweise, deployed Agentenkonfiguration, technische Toolgrenzen und menschliche Genehmigungen ungeprüft. Ein Hash oder guter Funktionstest allein ist keine Fachfreigabe.[12] [16]

**Technische Quellenblocker:** Kanadische Quelle heute Fetch-lesbar, generisches HTTP 403; Ursache und Eignung für weitere generische Abrufe ungeklärt. DSG- und DSV-Änderungsübersichten heute nur JavaScript-Hinweis; ihre aktuellen Änderungsdaten wurden nicht gelesen. Diese drei Einschränkungen stehen auch in beiden Frontmattern. Erreichbarkeit, Inhalt und allgemeine Orientierung sind keine tatsächliche Einzelfallprüfung.[12] [18] [21]

**Kein CMS-/Browserbetrieb:** Keine Browseroperation, Anmeldung, Zugangsdatenverwendung, CMS-Prüfung, Import, Liveänderung oder Veröffentlichung. Es wurden nur die beiden freigegebenen Artikel-11-Dateien und dieser Bericht geändert. Globale Manifeste, QA-Skripte, andere Artikel und andere Berichte bleiben durch diese Einzelpflege unberührt. Die gezielte lokale Dateiprüfung ist kein globaler Paketvalidator und keine Prüfung eines Zielsystems.

## Genau betroffene Abschnitte: vorher und nachher

Die folgende Passagendokumentation nennt die tatsächlich geänderten Metadaten und jeden neu hinzugefügten Absatz bzw. jede Tabellenzeile wortgetreu. Bei Ergänzungen bedeutet «vorher: nicht vorhanden», dass der angegebene Absatz bzw. die Zeile fehlte; die vorhandenen Nachbarabsätze bleiben erhalten. Sie folgt auf den lokalen Inhalts-/Zitationsabgleich.

### Artikel 11 – wortgetreue lokale Änderungen

#### Frontmatter

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -10,5 +10,5 @@
 veröffentlichungsdatum: "10.12.2026"
-stand: "1. November 2026"
-quellenpruefung_umfang: "Alle zwölf eindeutigen externen Quellenreferenzen in Artikel und Arbeitsmittel (acht bestehende, vier neu aufgenommene) sowie einschlägige BACS-Originalmeldungen seit 18. Oktober 2026 gezielt geprüft; interne Paketlinks nur erhalten, nicht live geprüft."
-quellenpruefung_status: "Alle externen Quellenreferenzen als Originalquellen geprüft; Fedlex zusätzlich über Chronologie, Änderungen und amtliche XML-Fassungen. Vier kontextbezogene Prüfpunkte ergänzt; keine neue pauschale Rechts-, Vertrags- oder technische Pflicht abgeleitet."
+stand: "15. November 2026"
+quellenpruefung_umfang: "Alle 16 eindeutigen externen Originalreferenzen des Artikelverbunds, davon 16 im Artikel und 13 im Arbeitsmittel, direkt inhaltlich geprüft; zwölf bestehende und vier neue Quellen sowie aktuelle BACS-/Microsoft-Meldungen seit 1. November 2026. Fedlex zusätzlich über zwei Chronologien, zwei amtliche XML-Fassungen und zwei nicht auslesbare Änderungsübersichten geprüft; interne Paketziele nur lokal abgeglichen, nicht live geprüft."
+quellenpruefung_status: "16 Originalreferenzen inhaltlich lesbar; BACS-DOCX direkt per ZIP/XML extrahiert. Drei technische Einschränkungen: kanadische KI-Quelle per Fetch lesbar, generischer HTTP-Abruf 403; beide Fedlex-Änderungsübersichten nur JavaScript-Hinweis, Chronologien/XML lesbar. Vier kontextbezogene Ergänzungen; keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe."
 fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
```

#### Lieferantenrisiken im Griff: BACS-Kreislauf für Cloud-, IT- und kritische Dienstleister in Schweizer KMU

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -1,3 +1,3 @@
 
-**Quellenstand: 1. November 2026.**
+**Quellenstand: 15. November 2026.**
 
```

#### 1. Partner mit privilegiertem Zugriff

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -7 +7,5 @@
 
+Ergänzen Sie bei solchen Integrationen die Verantwortung für Anwendungszugangsdaten, sogenannte App-Secrets: Wer schützt sie vor Veröffentlichung, erkennt eine Offenlegung, veranlasst Widerruf oder Rotation und untersucht die historische Nutzung? Microsoft beschreibt am 5. November 2026 auch kompromittierte Zugangsdaten einer anbietereigenen Multitenant-Anwendung, die Zugriffe auf nachgelagerte Kundentenants ermöglichten; entsprechende Aktivitäten wurden bereits ab 28. Oktober beobachtet. Die Meldung belegt keine Betroffenheit Ihres Unternehmens. Klären Sie im Lieferantengespräch, wie betroffene Kunden informiert werden und wie Anbieter- und kundenseitige Berechtigungen sowie verbleibende Zugänge geprüft werden. Das Löschen eines Secrets aus einem Repository macht es nicht ungültig; bereits ausgestellte Tokens bleiben laut Microsoft bis zum Ablauf gültig. Eindämmung, Rotation und die Beurteilung verbliebener Zugänge gehören deshalb in die zuständige Fachprüfung, nicht in eine automatische Fragebogenfreigabe. Tragen Sie keine Secret-Werte in die Landkarte ein.[13]
+
+Bei Fernwartungsanbietern sollten Managementkonsole, Erweiterungen, Technikerarbeitsplätze und verwaltete Kundenendgeräte getrennt erfasst werden. Microsoft beschreibt am 13. November 2026 SCKit-Aktivitäten im ScreenConnect-Kontext: Unbefugte Fernzugangsclients können unabhängig von der legitimen Supportinstanz fortbestehen; auch Technikersitzungen sind ein eigener Prüfbereich. Die initiale Eintrittsmethode der gemeldeten Kampagne war laut Quelle noch in Untersuchung. Lassen Sie sich daher für relevante Fernwartung die zugelassenen Instanzen und Verbindungsziele, Zuständigkeit und Stand der Technikerclients sowie einen unabhängigen Vorfallkanal erläutern. Ein Konsolenupdate allein bestätigt weder aktuelle Clients noch die Beseitigung einer Kompromittierung. Diese Fragen sind kein Befund gegen einen bestimmten Lieferanten und keine Anleitung zur eigenständigen Bereinigung.[15]
+
```

#### 2. Anbieter von Hardware oder Software

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -5 +5,3 @@
 
+Die Landkarte umfasst bei entsprechender Nutzung auch durch Dienstleister gewartete Kühl- und Kältesteuerungen. Das BACS warnt am 10. November 2026 vor Angriffen und nennt ausdrücklich extern gewartete oder betriebene Systeme. Klären Sie mit Anlagen- und Wartungsverantwortlichen Modell, Firmware, Supportende, direkte oder indirekte Internet-Erreichbarkeit, Fernzugangsweg und Ersatzplanung. Manipulationen können Temperaturen und Alarme verändern und temperatursensible Güter sowie den Betrieb beeinträchtigen. Die Warnung begründet keine pauschale Verwundbarkeit aller Anlagen; konkrete Updates oder Zugangsbeschränkungen müssen zum eingesetzten Produkt und sicheren Anlagenbetrieb passen.[14]
+
```

#### Verträge: Nachweisbare Pflichten statt pauschaler Sicherheitsversprechen

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -5,3 +5,3 @@
 
-Bei Personendaten darf ein Auftragsbearbeiter die Bearbeitung nur mit vorgängiger Genehmigung des Verantwortlichen einem Dritten übertragen. Bei einer allgemeinen Genehmigung muss der Auftragsbearbeiter über geplante Änderungen informieren, damit der Verantwortliche widersprechen kann.[4] Findet eine Bekanntgabe von Personendaten ins Ausland statt, sind die Voraussetzungen von Art. 16 DSG zu prüfen; ohne Angemessenheitsentscheid können unter anderem vertragliche Klauseln oder anerkannte Standarddatenschutzklauseln relevant sein.[4] **[FACHPRÜFUNG ERFORDERLICH]** Datenschutzvereinbarung, Unterauftragsbearbeitung und grenzüberschreitende Datenflüsse sind vor Vertragsabschluss oder wesentlichen Änderungen durch Datenschutz- und Rechtsfachpersonen zu prüfen.
+Bei Personendaten darf ein Auftragsbearbeiter die Bearbeitung nur mit vorgängiger Genehmigung des Verantwortlichen einem Dritten übertragen. Bei einer allgemeinen Genehmigung muss der Auftragsbearbeiter über geplante Änderungen informieren, damit der Verantwortliche widersprechen kann.[4] [5] Findet eine Bekanntgabe von Personendaten ins Ausland statt, sind die Voraussetzungen von Art. 16 DSG zu prüfen; ohne Angemessenheitsentscheid können unter anderem vertragliche Klauseln oder anerkannte Standarddatenschutzklauseln relevant sein.[4] **[FACHPRÜFUNG ERFORDERLICH]** Datenschutzvereinbarung, Unterauftragsbearbeitung und grenzüberschreitende Datenflüsse sind vor Vertragsabschluss oder wesentlichen Änderungen durch Datenschutz- und Rechtsfachpersonen zu prüfen.
 
```

#### Notfallwege mit dem Lieferanten planen und üben

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -9 +9,3 @@
 
+Wenn Ihr Lieferant Drittanbieter-Modellstände oder Fine-Tuning-Daten für einen handlungsfähigen KI-Agenten übernimmt, reicht eine gute normale Testantwort als Sicherheitsnachweis nicht aus. Microsoft zeigt am 12. November 2026 in zwei Forschungsstudien Risiken manipulierter Trainingsdaten und Modell-Checkpoints auf. Fragen Sie bei solchen Angeboten nach Herkunft, Version, verfügbarem Integritätsnachweis und Reviewstatus der übernommenen Artefakte sowie nach einer Evaluation in der tatsächlich vorgesehenen Agentenkonfiguration. Zusätzlich sind ausserhalb des Modells durchgesetzte Toolrechte, isolierte Ausführung und menschliche Genehmigung folgenreicher Aktionen zu klären. Die Forschungsergebnisse sind kein Befund gegen alle KI-Anbieter oder gegen Ihr eingesetztes Modell und keine Schweizer Norm.[16]
+
```

#### Quellen

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -13 +13,5 @@
 [12]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience, 22. Oktober 2026"
+[13]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft – Threat actors use agentic AI tooling to find and abuse exposed secrets, 5. November 2026"
+[14]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen, 10. November 2026"
+[15]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft – SCKit abuses ScreenConnect to deploy remote access and target technician sessions, 13. November 2026"
+[16]: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/ "Microsoft – Trained to betray: How post-training supply chain attacks hijack coding agents, 12. November 2026"
```

### Arbeitsmittel 11 – wortgetreue lokale Änderungen

#### Frontmatter

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -3,3 +3,3 @@
 passender_artikel: /wissen/lieferantenrisiken-cybersecurity
-version: "1.2"
+version: "1.3"
 status: "Arbeitsvorlage – nicht freigegeben"
@@ -7,4 +7,4 @@
 fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
-stand: "1. November 2026"
-quellenpruefung_umfang: "Alle neun eindeutigen externen Quellenreferenzen dieses Arbeitsmittels (fünf bestehende, vier neu aufgenommene) sowie die korrespondierenden Originalquellen des passenden Artikels gezielt geprüft; interne Paketlinks nur erhalten, nicht live geprüft."
-quellenpruefung_status: "Alle externen Quellenreferenzen als Originalquellen geprüft; Fedlex-Korrespondenz zusätzlich über Chronologie, Änderungen und amtliche XML-Fassungen geprüft. Vier kontextbezogene Prüfpunkte ergänzt; keine automatische Freigabe, Rechts- oder Tenantentscheidung."
+stand: "15. November 2026"
+quellenpruefung_umfang: "Alle 13 eindeutigen externen Originalreferenzen dieses Arbeitsmittels, neun bestehende und vier neue, sowie alle 16 Originalreferenzen des passenden Artikels direkt inhaltlich geprüft; aktuelle BACS-/Microsoft-Meldungen seit 1. November 2026 und sechs zusätzliche Fedlex-Endpunkte geprüft. Interne Paketziele nur lokal abgeglichen, nicht live geprüft."
+quellenpruefung_status: "13 Arbeitsmittelreferenzen inhaltlich lesbar; BACS-DOCX direkt per ZIP/XML extrahiert. Drei technische Einschränkungen im Verbund: kanadische KI-Quelle per Fetch lesbar, generischer HTTP-Abruf 403; beide Fedlex-Änderungsübersichten nur JavaScript-Hinweis, Chronologien/XML lesbar. Materielle Ergänzungen zu App-Secrets, Fernwartung, Kühlsteuerungen und KI-Artefakten; keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe."
```

#### Lieferantenfragebogen und Priorisierungsmatrix

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -1,3 +1,3 @@
 
-**Version 1.2 · Quellenstand: 1. November 2026 · Arbeitsvorlage – nicht freigegeben**
+**Version 1.3 · Quellenstand: 15. November 2026 · Arbeitsvorlage – nicht freigegeben**
 
```

#### Teil A – Lieferantenprofil und Landkarte

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -20,2 +20,6 @@
 | KI-gestützter Dienst, soweit anwendbar: unterstützter Prozess, Anbieter/Modell oder Agent, Connectoren/Toolrechte, bekannte Quoten oder Limiten |  |
+| App-Secrets, soweit anwendbar: zuständige Stelle für Schutz, Offenlegungserkennung, Widerruf/Rotation und Kundeninformation; keine Secret-Werte eintragen |  |
+| Fernwartung, soweit anwendbar: zugelassene Managementinstanzen und Verbindungsziele, Erweiterungen, Technikerclients und verantwortliche Stelle |  |
+| Kühl- oder Kältesteuerungen, soweit anwendbar: Anlagen-/Wartungsverantwortung, Modell, Firmware, Supportende, Erreichbarkeit und Ersatzplanung |  |
+| Drittanbieter-KI-Artefakte, soweit anwendbar: Modell-Checkpoint/Fine-Tuning-Daten, Herkunft, Version, verfügbarer Hash und Reviewstatus |  |
 
```

#### D1. Zugänge, Schutz und Betrieb

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -4,2 +4,6 @@
 Für hochberechtigte SaaS-Integrationen sind Anwendung, Mandant, Anwendungs- oder Dienstprinzipal, Berechtigungen und Zustimmungen getrennt vom üblichen Lieferantenkontakt zu dokumentieren. Ein Microsoft-Bericht vom 21. Oktober zu bestimmten ConnectWise-Cloudanwendungen begründet keine Vermutung gegen andere Produkte. Er stützt aber die kontextbezogene Prüfung weitreichender App-Berechtigungen, auffälliger anwendungsbasierter Aktivitäten und der Beweissicherung vor irreversiblen Änderungen.[8]
+
+Microsoft beschreibt am 5. November 2026 auch kompromittierte App-Zugangsdaten eines Anbieters mit Zugriff auf nachgelagerte Kundentenants; entsprechende Aktivität begann bereits vor November. Fragen Sie nach dem Secret-Lebenszyklus und der abgestimmten Kundeninformation. Das Entfernen eines Secrets aus einem Repository macht es nicht ungültig; bereits ausgestellte Tokens bleiben laut Quelle bis zum Ablauf gültig. Widerruf/Rotation, historische Nutzung und verbleibende Zugänge sind fachlich zu beurteilen. Weder diese Meldung noch eine Selbstauskunft belegt die Sicherheit oder Betroffenheit Ihrer Integration.[10]
+
+Bei Fernwartung unterscheidet Microsoft am 13. November Managementkonsole und Erweiterungen, Technikerclients sowie Kundenendgeräte. Ein Konsolenupdate bestätigt nicht den Stand jedes Technikerclients; unbefugte Clients und exponierte Sitzungen sind getrennte Vorfallfragen. Die initiale Eintrittsmethode der beschriebenen SCKit-Kampagne bleibt laut Quelle in Untersuchung.[12] Die BACS-Warnung vom 10. November nennt zudem extern gewartete Kühl- und Kältesteuerungen. Prüfen Sie diesen Anlagenkontext nur, wenn er für Ihre Leistung relevant ist; Änderungen erfordern die zuständigen Anlagen- und Sicherheitsfachpersonen.[11]
 
@@ -16,2 +20,6 @@
 | Können wir den Zugriff im Vorfall oder bei Vertragsende sperren oder beenden? | ☐ | ☐ | ☐ |  |
+| Sind für risikorelevante App-Secrets Schutz, Offenlegungserkennung, Widerruf/Rotation, historische Nutzungsprüfung und Kundeninformation einer zuständigen Stelle zugeordnet? | ☐ | ☐ | ☐ |  |
+| Ist bei einer kompromittierten Anbieterintegration die Prüfung von Kundenberechtigungen, bereits ausgestellten Tokens und weiteren verbliebenen Zugängen abgestimmt? | ☐ | ☐ | ☐ |  |
+| Sind bei Fernwartung zugelassene Instanzen, Verbindungsziele und Erweiterungen sowie die separat überprüften Technikerclient-Stände dokumentiert? | ☐ | ☐ | ☐ |  |
+| Sind bei relevantem Kühlanlagenbetrieb Modell, Firmware, Supportende, direkte oder indirekte Internet-Erreichbarkeit, Fernzugangsweg und Ersatzplanung mit der zuständigen Stelle geklärt? | ☐ | ☐ | ☐ |  |
 
```

#### D3. Vorfall, Kontinuität und Notfallweg

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -9,2 +9,3 @@
 | Wurde der interne Eskalations- und Kontaktweg geprüft oder geübt? | ☐ | ☐ | ☐ |  |
+| Ist bei Verdacht auf kompromittierte Fernwartung ein unabhängiger Vorfallkanal für Kundenendgeräte und Technikerarbeitsplätze vorgesehen, ohne diese Vorlage als Bereinigungsfreigabe zu verwenden? | ☐ | ☐ | ☐ |  |
 
```

#### D4. KI-gestützte Dienste, Quoten und Notbetrieb

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -2,2 +2,4 @@
 Füllen Sie diesen Abschnitt nur aus, wenn der Lieferant einen KI-gestützten Dienst, Agenten oder Connector für einen relevanten Prozess bereitstellt. Die kanadische Behördenorientierung vom 22. Oktober beschreibt Quoten- und Tokenerschöpfung als mögliches Kosten- und Verfügbarkeitsrisiko. Sie empfiehlt unter anderem Monitoring, abgestufte Warnungen, die Prüfung von Drittanbieterlimiten und manuelle oder anders unterstützte Ausweichabläufe. Das ist freiwillige ausländische Orientierung, keine Schweizer Rechtsvorgabe.[9]
+
+Für Angebote mit übernommenen Drittanbieter-Modell-Checkpoints oder Fine-Tuning-Daten ergänzt Microsoft am 12. November 2026 Herkunfts- und Integritätskontrollen sowie die Evaluation in der tatsächlichen Agentenkonfiguration. Die zwei Forschungsstudien zu manipulierten Artefakten sind kein Befund gegen alle Anbieter. Klären Sie ausserhalb des Modells durchgesetzte Toolrechte, isolierte Ausführung und menschliche Genehmigung folgenreicher Aktionen; eine gute normale Testantwort ist keine Sicherheitsfreigabe.[13]
 
@@ -10,2 +12,4 @@
 | Sind weitreichende Tool- und Connectorrechte auf das für die Aufgabe notwendige Mass beschränkt und überprüfbar? | ☐ | ☐ | ☐ |  |
+| Sind bei übernommenen Drittanbieter-KI-Artefakten Herkunft, Version, verfügbarer Integritätsnachweis und Reviewstatus dokumentiert? | ☐ | ☐ | ☐ |  |
+| Wurde der Agent in der vorgesehenen Konfiguration evaluiert, und bestehen ausserhalb des Modells wirksame Toolgrenzen, isolierte Ausführung und Genehmigung folgenreicher Aktionen? | ☐ | ☐ | ☐ |  |
 
```

#### Quellen

`-` bezeichnet vorher, `+` nachher; unveränderte Kontextzeilen sind nicht ersetzt.

```diff
--- vorher
+++ nachher
@@ -10 +10,5 @@
 [9]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience, 22. Oktober 2026"
+[10]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft – Threat actors use agentic AI tooling to find and abuse exposed secrets, 5. November 2026"
+[11]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen, 10. November 2026"
+[12]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft – SCKit abuses ScreenConnect to deploy remote access and target technician sessions, 13. November 2026"
+[13]: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/ "Microsoft – Trained to betray: How post-training supply chain attacks hijack coding agents, 12. November 2026"
```

### Gezielter lokaler Abgleich

- `blog-paket/articles/11-lieferantenrisiken-cybersecurity.md`: 2’930 Wörter vor dem Quellenabschnitt, 16 Definitionen = 16 verwendete Zitationen, vier wortgleich erhaltene Fachmarker.
- `blog-paket/resources/11-lieferantenfragebogen.md`: 1’917 Wörter vor dem Quellenabschnitt, 13 Definitionen = 13 verwendete Zitationen, vier wortgleich erhaltene Fachmarker.

Der unveränderte Volltext wurde nicht gekürzt. Beide sichtbaren Standhinweise stimmen mit `stand: "15. November 2026"` überein; Arbeitsmittelversion im Frontmatter und im sichtbaren Hinweis jeweils 1.3. Alle ursprünglichen Quellen bleiben definiert und benutzt, alle vier neuen Quellen haben passende Zitationen. Es wurden keine Slugs, SEO-Felder, Veröffentlichungstermine, Autoren- oder Fachstatusfelder geändert. Die ursprüngliche Artikelwortzahl betrug 2’529, die ursprüngliche Arbeitsmittelwortzahl 1’540; gezählt wurden Worttokens einschliesslich Tabellen, ohne Frontmatter und Quellenverzeichnis. Keine globale QA- oder CMS-Prüfung.

## Quellen

[1]: https://www.bacs.admin.ch/de/supply-chain-de "BACS – Cybersicherheit in der Lieferkette"
[2]: https://www.bacs.admin.ch/dam/de/sd-web/iXNmDC-pccRC/best_practice_lieferantenvertrag_de.docx "BACS – Lieferantenverträge: Best Practice"
[3]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz DSG"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung DSV"
[6]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing"
[7]: https://www.edoeb.admin.ch/de/outsourcing-auftragsdatenbearbeitung "EDÖB – Outsourcing und Auftragsdatenbearbeitung"
[8]: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final "NIST – SP 800-161 Rev. 1 Update 1"
[9]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP"
[10]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant"
[11]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft – ARTEX und ConnectWise-Lieferkettenkompromittierung"
[12]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – AI token consumption und Betriebsresilienz"
[13]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft – Exponierte Secrets und App-Credentials, 5. November 2026"
[14]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen, 10. November 2026"
[15]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft – SCKit und Technikersitzungen, 13. November 2026"
[16]: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/ "Microsoft – Post-Training-Lieferketten und Coding-Agenten, 12. November 2026"
[17]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG-Chronologie"
[18]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex – DSG-Änderungsübersicht: heute nicht auslesbar"
[19]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – Amtliche DSG-XML, 7. Juli 2025"
[20]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV-Chronologie"
[21]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes "Fedlex – DSV-Änderungsübersicht: heute nicht auslesbar"
[22]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml "Fedlex – Amtliche DSV-XML, 1. Dezember 2025"
[23]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[24]: https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de "BACS – Handlungsfähig bleiben im Ernstfall, 2. November 2026"
[25]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS – KMU-Notfallplan-Template, Downloadstand 11. November 2026"
[26]: https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/ "Microsoft – ARTEX im Finanzsektor, 6. November 2026"
[27]: https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/ "Microsoft – GSocket und fortbestehender Fernzugriff, 11. November 2026"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/11-lieferantenrisiken-cybersecurity.md:** `/resources/11-lieferantenfragebogen` → `https://www.dkschv.ch/wissen/resources/11-lieferantenfragebogen.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/notfallplanung` → `https://www.dkschv.ch/notfallplanung.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
