# Prüfbericht – Artikel 01: Ransomware im KMU: Die ersten 60 Minuten richtig handeln

- **Prüfdatum:** 1. November 2026, ISO-KW 44, Europe/Zurich (CET, UTC+01:00).
- **Prüf- und Newsfenster:** 25. Oktober 2026, 09:00 CET bis 1. November 2026, 09:00 CET. Zusätzlich wurde die einschlägige Quellenlage seit der letzten Einzelprüfung vom 18. Oktober 2026 abgeglichen.
- **Tatsächliche Abrufe:** Die erfolgreichen stateless Abrufe der Originalquellen erfolgten am 1. November 2026 zwischen **09:05 und 09:06 CET**. Die lokale Konsistenzprüfung der fertigen Dateien lief um **09:08:41 CET**. Das Prüfdatum ist kein behaupteter historischer Seitenstand um 09:00 und keine Fach-, Rechts- oder Veröffentlichungsfreigabe.
- **Geprüfte und gepflegte Dateien:**
  - Artikel: `/home/ubuntu/dkschv-audit/blog-paket/articles/01-ransomware-erste-60-minuten.md`
  - Arbeitsmittel: `/home/ubuntu/dkschv-audit/blog-paket/resources/01-60-minuten-checkliste.md`
- **Wartungsgrundlage:** Eintrag zu Artikel 01 im Wartungsmanifest sowie die Vormerkung vom 25. Oktober 2026. Die Vormerkung verlangte insbesondere, die Aussage einzuordnen, dass ein Patch eine frühere Kompromittierung nicht beseitigt. Sie verlangte keine organisationsspezifische Forensik- oder Wiederanlaufanweisung.
- **Keine Liveänderung:** Es wurde kein CMS geöffnet, keine Anmeldung verwendet, kein Import ausgeführt und kein öffentlicher DKSchV-Link als live behauptet oder geprüft. Interne relative Slugs verbleiben Planungswerte.

## Ergebnis

Die **14 von 14 externen Quellenreferenzen** des Artikels wurden im Original abgerufen und auf Erreichbarkeit sowie Aussagegehalt geprüft. Die **11 von 11 Quellenreferenzen** des Arbeitsmittels sind eine Teilmenge davon und wurden ebenfalls vollständig geprüft. Alle Referenzen waren beim Abruf erreichbar. Bei der dynamischen ISG-Hauptseite liefert ein stateless Abruf nur die JavaScript-Hinweisseite; das ist kein fehlender Rechtsquellennachweis. Die amtliche Fedlex-Chronologie und die amtliche XML-Fassung wurden deshalb zusätzlich direkt abgerufen. [8] [17] [18]

Die gesetzlichen Aussagen im Artikel wurden erneut anhand amtlicher Fassungen verifiziert. Die DSG-Chronologie nennt als letzte Fassung eine Berichtigung mit Inkrafttreten am 7. Juli 2025; die ISG-Chronologie führt die aktuelle Fassung seit 1. Oktober 2025; für die DSV weist die Chronologie die aktuelle Fassung seit 1. Dezember 2025 aus. In den am 1. November abrufbaren amtlichen Chronologien ist keine spätere Fassung enthalten. [15] [17] [19]

Die Erstreaktion bleibt in der bestehenden Form durch BACS und CISA gedeckt: koordinierte Netzisolation, Wahrung von Protokollen und flüchtigen Spuren, früher Fachentscheid, Schutz der Backups und Wiederherstellung erst auf einer sauberen Grundlage. [1] [5] Es wurde keine neue, allgemein geltende Erstreaktionspflicht, keine neue BACS- oder EDÖB-Meldefrist und keine Änderung der gesetzlichen Meldeschwellen belegt.

Materiell ergänzt wurden nur drei klar abgegrenzte Punkte. Erstens dokumentiert der Artikel nun den von der aktuellen BACS-Meldeoberfläche genannten alternativen E-Mail-Weg für die fristwahrende BACS-Erstmeldung, einschliesslich der dort genannten Schlussmeldung innert 14 Tagen. Zweitens enthält Artikel und Checkliste nun die im Gesetz bereits geltenden, aber für das Arbeitsmittel nützlichen DSV-Angaben zur EDÖB-Meldung und Vorfalldokumentation. Drittens steht nach der ersten Stunde sowie im Grenzenblock der Checkliste ausdrücklich, dass ein nachträgliches Sicherheitsupdate keine bereits erfolgte Kompromittierung beseitigt. Diese Aussage geht auf die BACS-Warnung vom 21. Oktober zurück und wird ausdrücklich nicht als technische Untersuchungsvorgabe ausgegeben. [11] [14] [12]

Die neue CISA-Warnung zu SafePay vom 20. Oktober 2026 wurde als aktuelle Ransomware-Originalmeldung geprüft. Sie bestätigt abstrakt bereits vorhandene Themen wie Isolation, Logauswertung und Abgrenzung einer möglichen Vor-Kompromittierung. Sie enthält jedoch gruppen- und produktbezogene technische Details, führt nicht zu einer Schweizer Meldepflichtänderung und rechtfertigt keinen künstlichen CVE- oder Akteurseinschub in den Evergreen-Text. [25]

## Quellenprüfung: Referenzen in Artikel und Arbeitsmittel

| Nr. | Original-URL | Abruf/Erreichbarkeit | Nachweisbarer Stand oder Version | Geprüfter Aussagegehalt und Reichweite |
|---:|---|---|---|---|
| 1 | [BACS – Ransomware: Was nun?][1] | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbares Veröffentlichungs- oder Änderungsdatum | Deckt Netztrennung, Log-Sicherung, frühen Entscheid über Forensik vor Neustart/Reparatur, Neuinstallation vor Wiederherstellung, Kantonspolizei bei Strafanzeige und Abraten von Lösegeld. Die Seite nennt 24 Stunden für die Erstmeldung und 14 Tage zur Vervollständigung; sie ist Behördenorientierung, keine organisationsspezifische Freigabe. |
| 2 | [BACS – Informationen zur Meldepflicht][2] | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbarer eigener Seitenstand; Inkraftsetzung per 01.04.2025 genannt | Bestätigt Meldepflicht für bestimmte kritische Infrastrukturen, 24 Stunden ab Entdeckung sowie ISG-/CSV-Grundlage. Die Seite ersetzt weder die Prüfung der Erfassung noch die amtlichen Gesetzesfassungen. |
| 3 | [Fedlex – DSG, SR 235.1][3] | 01.11.2026, 09:05 CET; erreichbar | Aktuelle Fassung gemäss Chronologie 07.07.2025 | Art. 5 definiert die Verletzung der Datensicherheit. Art. 24 verlangt bei voraussichtlich hohem Risiko die EDÖB-Meldung so rasch als möglich, nennt Mindestinhalt und unterscheidet die Betroffeneninformation. Inhalt zusätzlich per amtlichem XML gegengeprüft. |
| 4 | [EDÖB – Leitfaden nach Art. 24 DSG][4] | 01.11.2026, 09:05 CET; erreichbar | Version 1.2; EDÖB-DataBreach verweist auf 23.04.2025 | Bestätigt, dass bei nicht innert kurzer Zeit ausschliessbarem voraussichtlich hohem Risiko nicht auf lange Abklärungen gewartet werden darf. Ransomware kann nach Umständen diese Schwelle erreichen. Dies ist eine Auslegungshilfe, keine konkrete Risikoentscheidung. |
| 5 | [CISA – I’ve Been Hit By Ransomware!][5] | 01.11.2026, 09:05 CET; erreichbar | Seite verweist auf den im Mai 2023 aktualisierten #StopRansomware Guide | Deckt koordinierte Isolation, externen Kommunikationsweg, Ausschalten nur bei fehlender anderer Netztrennung, Sicherung flüchtiger Evidenz und Wiederherstellung aus Offline-Backups ohne Reinfektion. US-Behördenorientierung, keine Schweizer Rechtsquelle. |
| 6 | [BACS – Notfallkonzept][6] | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbarer eigener Seitenstand; KMU-Template datiert 18.05.2026 | Bestätigt Krisenorganisation, Kommunikation, Kontakte und die vier Phasen Vorbereitung, Eintritt, Bewältigung und Nachbearbeitung. |
| 7 | [NIST SP 800-61 Rev. 3][7] | 01.11.2026, 09:05 CET; erreichbar | Final veröffentlicht April 2025; Dokumenthistorie 03.04.2025 | Bestätigt die Einbettung der Incident Response in laufendes Cyberrisikomanagement. Internationale Fachorientierung, keine Schweizer Meldenorm. |
| 8 | [Fedlex – ISG, SR 128][8] | 01.11.2026, 09:05 CET; technisch erreichbar, Inhalt im stateless HTML nicht geladen | Aktuelle Fassung gemäss Chronologie 01.10.2025; amtliche XML-Fassung zusätzlich abgerufen | Art. 74b–74e stützen Erfassungs- und Ausnahmenprüfung, Tatbestände, 24-Stunden-Frist und Ergänzung mit neuen Informationen. Der Gesetzestext ist nicht durch die stateless JavaScript-Leerseite entfallen. |
| 9 | [Suisse ePolice – Cyberkriminalität anzeigen][9] | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbares Veröffentlichungs- oder Änderungsdatum | Bestätigt Kategorien für Cyberanzeigen und verweist für blosse Meldungen an die nationale Plattform. Die konkrete Zuständigkeit für eine Strafanzeige stützt zusätzlich die BACS-Ransomware-Seite. |
| 10 | [BACS – Woche 40: Mythen zu Schadsoftware][10] | 01.11.2026, 09:05 CET; erreichbar | Veröffentlicht 06.10.2026 | Bestätigt: Einzelne unspezifische Symptome beweisen keine Infektion; mehrere Auffälligkeiten oder Sicherheitswarnungen sollen untersucht werden. Die bereits vorhandene begrenzte Verdachtsklarstellung bleibt korrekt. |
| 11 | [BACS – Freiwillige Meldung eines Cybervorfalls][11] | 01.11.2026, 09:05 CET; erreichbar | Aktuelle BACS-Meldeoberfläche ohne sichtbaren Seitenstand | Zeigt die freiwillige Meldemöglichkeit. Für meldepflichtige Stellen nennt sie `incidents@ncsc.ch` als alternative Übermittlung, erkennt die E-Mail als Erstmeldung innert 24 Stunden an und nennt die Schlussmeldung innert 14 Tagen. Dies ist ein aktuell zu prüfender Meldeweg, keine pauschale Einzelfallentscheidung. |
| 12 | [BACS – Kritische Schwachstellen in PHP][12] | 01.11.2026, 09:05 CET; erreichbar | Veröffentlicht 21.10.2026 | Neue einschlägige Originalmeldung aus der Vormerkung. Sie sagt ausdrücklich, dass ein Update keine bereits erfolgte Kompromittierung beseitigt. Verwendet wurde nur dieser allgemeine Grundsatz, nicht die CVE-, Produkt- oder Übergangsmassnahmen. |
| 13 | [EDÖB – DataBreach][13] | 01.11.2026, 09:05 CET; erreichbar | Aktuelle Seite ohne sichtbaren eigenen Seitenstand; verlinkter Leitfaden 23.04.2025 | Bestätigt das sichere Online-Formular für Meldungen von Verantwortlichen, die hohe Risikoschwelle und die getrennte Kontaktaufnahme von betroffenen Personen. |
| 14 | [Fedlex – DSV, SR 235.11, Art. 15][14] | 01.11.2026, 09:05 CET; erreichbar | Aktuelle Fassung gemäss Chronologie 01.12.2025 | Art. 15 nennt die Meldeangaben, das Nachreichen fehlender Angaben so rasch als möglich und die zweijährige Dokumentationspflicht. Inhalt zusätzlich per amtlichem XML gegengeprüft. |

## Zusätzliche Originalquellen: Rechtsstand, Meldewege und Aktualitätscheck

| Original-URL | Abruf/Erreichbarkeit | Nachweisbarer Stand | Aussage und Reichweite für diese Pflege |
|---|---|---|---|
| [Fedlex – DSG-Chronologie][15] | 01.11.2026, 09:05 CET; erreichbar | Letzte Zeile: Berichtigung, Inkrafttreten 07.07.2025 | Amtlicher Nachweis, dass keine spätere DSG-Fassung in der abrufbaren Chronologie steht. |
| [Fedlex – DSG-XML vom 07.07.2025][16] | 01.11.2026, 09:06 CET; erreichbar | Amtliche XML-Fassung 20250707 | Stateless lesbarer Originaltext für Art. 5 und 24; bestätigt den im Artikel verwendeten Gesetzesinhalt. |
| [Fedlex – ISG-Chronologie][17] | 01.11.2026, 09:05 CET; erreichbar | Letzte aktuelle Fassung, Inkrafttreten 01.10.2025 | Amtlicher Nachweis des ISG-Fassungsstands, weil die Hauptseite im stateless Abruf JavaScript erfordert. |
| [Fedlex – ISG-XML vom 01.10.2025][18] | 01.11.2026, 09:06 CET; erreichbar | Amtliche XML-Fassung 20251001 | Direct-Source-Nachweis für Art. 74b–74e: Erfassung, Ausnahme, Tatbestände, Frist, Inhalt und Ergänzung. |
| [Fedlex – DSV-Chronologie][19] | 01.11.2026, 09:05 CET; erreichbar | Letzte Fassung, Inkrafttreten 01.12.2025 | Amtlicher Nachweis des DSV-Fassungsstands. |
| [Fedlex – DSV-XML vom 01.12.2025][20] | 01.11.2026, 09:06 CET; erreichbar | Amtliche XML-Fassung 20251201 | Direct-Source-Nachweis für Art. 15 DSV, insbesondere Angaben, Nachreichen und Dokumentation. |
| [BACS – Im Fokus][21] | 01.11.2026, 09:05 CET; erreichbar | Übersicht reicht beim Abruf bis 27.10.2026 | Zwischen 18. und 27.10. erscheinen unter anderem WhatsApp-Betrug, KMU-Studie, PHP-Warnung und Hotelbuchungs-Phishing. Ausser der PHP-Warnung keine neue, materielle Meldung zur Ransomware-Erstreaktion oder zum Meldeweg. |
| [BACS – Aktuelle Vorfälle][22] | 01.11.2026, 09:06 CET; erreichbar | Jüngster Eintrag 21.10.2026: PHP | Bestätigt die PHP-Warnung als aktuelle Vorfallsmeldung; keine neuere Ransomware-Erstreaktionsanweisung sichtbar. |
| [BACS – Was muss gemeldet werden?][23] | 01.11.2026, 09:06 CET; erreichbar | Kein sichtbarer eigener Seitenstand | Bestätigt die Tatbestände Funktionsfähigkeitsgefährdung, Manipulation, Informationsabfluss, längere Unentdecktheit sowie Erpressung, Drohung oder Nötigung; Verschlüsselungstrojaner ist Beispiel. Keine Textänderung nötig, da Art. 74d bereits korrekt abgebildet ist. |
| [BACS – Wer muss melden?][24] | 01.11.2026, 09:06 CET; erreichbar | Kein sichtbarer eigener Seitenstand | Verweist für Erfassung auf Art. 74b ISG und für Ausnahmen auf die CSV. Bestätigt den unverändert nötigen Einzelfallvorbehalt. |
| [CISA – #StopRansomware: SafePay Ransomware][25] | 01.11.2026, 09:06 CET; erreichbar | Veröffentlicht 20.10.2026 | Neue Ransomware-Originalmeldung seit 18.10. Sie ist akteurspezifisch; vorhandene generische Aussagen zur Isolation, Logauswertung und Bereinigung werden nicht materiell verändert. Kein Evergreen-CVE-/Akteurseinschub. |
| [BACS – Medienmitteilungen][26] | 01.11.2026, 09:06 CET; erreichbar | Übersicht enthält keine neue Oktober-/November-Meldung zur Ransomware-Erstreaktion | Ergänzende offizielle Übersicht. Der Abruf belegt keine neue materielle BACS-Meldepflicht- oder Reaktionsvorgabe im Newsfenster. |

Der Abruf aktueller Seiten ohne eigene Version oder vollständige Änderungschronologie belegt deren Inhalt zum tatsächlichen Abrufzeitpunkt, nicht zwingend jedes redaktionelle Zwischenstadium oder den Wortlaut um 09:00. Für DSG, ISG und DSV wurde diese Unsicherheit durch Chronologie und amtliche XML-Fassungen soweit wie möglich reduziert. [15] [16] [17] [18] [19] [20]

## Geprüfte aktuelle Originalmeldungen und Einordnung

Die BACS-Übersicht führt nach dem Stichtag 18. Oktober die PHP-Warnung vom 21. Oktober, Hotelbuchungs-Phishing vom 20. Oktober, eine KMU-Studie vom 22. Oktober sowie WhatsApp-Betrug vom 27. Oktober. Nur die PHP-Warnung hat einen direkten, aber begrenzten Bezug zur verlangten Abgrenzung von Sicherheitsupdates und Vor-Kompromittierung. [21] Die PHP-Warnung empfiehlt neben Aktualisierung und Verifikation des Fixstands ausdrücklich, Logs und Systeme auf Auffälligkeiten zu untersuchen, und stellt klar, dass ein Update keine bereits eingetretene Kompromittierung bereinigt. [12]

Diese Quelle rechtfertigt keinen Ablauf für ein bestimmtes PHP-System und keine pauschale forensische Massnahme. Deshalb wurden weder CVE-Nummern noch Versionslisten noch konkrete Übergangsmassnahmen in den Artikel oder die Checkliste übernommen. Der Text enthält nur die abstrakte, quellengetreue Grenze: Ein Patch ist kein Negativnachweis einer früheren Kompromittierung. Diese Grenze passt zum bestehenden Hinweis, dass Wiederherstellung nicht in eine möglicherweise noch kompromittierte Umgebung gestartet werden soll. [12] [1] [5]

Die SafePay-Warnung der CISA vom 20. Oktober beschreibt ebenfalls die Isolation kompromittierter Hosts, die Sichtung von Logs und weitere technische Reaktionsmöglichkeiten. Für verschlüsselte Systeme verweist sie auf die generische Ransomware-Checkliste. Ihre zahlreichen akteurs- und umgebungsspezifischen technischen Anweisungen werden bewusst nicht als Schweizer KMU-Standard, Forensikplan oder Patchanweisung ausgegeben. [25] [5]

Die seit dem 18. Oktober geprüften BACS-Meldungen zu Phishing, WhatsApp-Konten und der KMU-Studie haben keinen unmittelbaren Aussagegehalt für die Ransomware-Erstreaktion oder die getrennte BACS-/EDÖB-Meldeprüfung. Sie wurden nicht künstlich als ungenutzte Quellen angehängt. [21]

## Rechts- und Meldewegabgleich

Für erfasste Behörden und Organisationen kritischer Infrastrukturen verlangt Art. 74e ISG die Meldung innert 24 Stunden nach Entdeckung. Sind noch nicht alle Informationen bekannt, müssen sie ergänzt werden, sobald neue Informationen verfügbar sind. Der BACS-Webauftritt beschreibt die in der Praxis verwendete Frist zur Vervollständigung von 14 Tagen; die aktuelle BACS-Meldeoberfläche nennt den alternativen E-Mail-Weg und erklärt dessen Anerkennung als Erstmeldung. [18] [2] [11]

Die Ergänzung im Artikel trennt deshalb Gesetzestext und Prozesshinweis: Die gesetzliche Beurteilung der Erfassung, des Tatbestands und der Frist bleibt zwingend eine Einzelfallfrage. E-Mail-Adresse und Schlussmeldung sind ein aktueller praktischer Meldeweg, der vor der Übermittlung erneut an der BACS-Oberfläche zu prüfen ist. Daraus wurde keine allgemeine BACS-Meldepflicht für jedes KMU abgeleitet. [18] [11]

Für EDÖB-Meldungen bleibt die gesetzliche Schwelle unverändert: Der Verantwortliche meldet eine Verletzung der Datensicherheit so rasch als möglich, wenn ein voraussichtlich hohes Risiko für Persönlichkeit oder Grundrechte besteht. Die DSV konkretisiert die Meldedaten und die Dokumentation. Der DataBreach-Webauftritt bezeichnet das Online-Formular als Weg für Verantwortliche, nicht für betroffene Personen. [16] [20] [13]

Ein neues Frontmatter-Feld `rechtsstand` wurde nicht angelegt, weil die Dateien ein solches Feld bisher nicht enthalten. Die Rechtsaussagen im Text sind anhand der geltenden amtlichen Fassungen verifiziert. Daraus folgt keine Rechtsfreigabe und keine Entscheidung über die Meldepflicht einer bestimmten Organisation oder eines bestimmten Ereignisses.

## Dokumentierte Änderungen

### Artikel

Datei: `/home/ubuntu/dkschv-audit/blog-paket/articles/01-ransomware-erste-60-minuten.md`

| Betroffene Passage | Vorher | Nachher | Grund und Beleg |
|---|---|---|---|
| Frontmatter `stand` | `18. Oktober 2026` | `1. November 2026` | Sichtbarer Quellenprüfstand, keine Fachfreigabe. |
| Frontmatter `quellenpruefung_umfang` | `11 von 11 externen Quellenreferenzen geprüft; BACS Im Fokus auf neuere einschlägige Meldungen geprüft` | `14 von 14 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft` | Drei tatsächlich verwendete externe Quellen ergänzt und alle Quellen im Original abgerufen. |
| Frontmatter `quellenpruefung_status` | `Vollständig für die Quellenreferenzen; interne relative Ziele nicht live geprüft` | `Vollständig für die Quellenreferenzen; Fedlex-Historie und amtliche XML-Fassungen zusätzlich geprüft; interne relative Ziele nicht live geprüft` | Exakter zusätzlicher Prüfumfang; der stateless ISG-Leerabruf wurde durch amtliche Alternativzugänge abgesichert. [17] [18] |
| BACS-Abschnitt, nach 24-Stunden-Regel | Kein dokumentierter alternativer BACS-Erstmeldeweg | Sichere elektronische Übermittlung, `incidents@ncsc.ch` als aktuelle Alternative, Anerkennung der E-Mail als Erstmeldung sowie 14-Tage-Schlussmeldung ergänzt; erneute Prüfung unmittelbar vor Nutzung verlangt | Aktuelle offizielle BACS-Meldeoberfläche. Keine Änderung des Art.-74e-ISG-Wortlauts und keine Erfassungseinordnung. [11] [18] |
| EDÖB-Abschnitt, nach Art. 24 DSG | Mindestinhalt aus DSG genannt, DSV-Angaben und Portal nicht konkretisiert | Sichere DataBreach-Meldung für Verantwortliche, DSV-Angaben, Nachreichen fehlender Angaben und Vorfalldokumentation ergänzt | Präzisierung des bestehenden Arbeitsmittels anhand geltender DSV und EDÖB-Portal, ohne Risikoschwelle zu verändern. [13] [14] |
| Nach der ersten Stunde | Kein Satz zum Verhältnis von Patch und früherer Kompromittierung | Belegter Satz: Sicherheitsupdate schliesst bekannte Lücke, beweist aber nicht das Ausbleiben einer früheren Kompromittierung; keine organisationsspezifische Forensikanweisung | Begrenzte Umsetzung der Vormerkung vom 25.10. anhand BACS-PHP-Warnung. [12] |
| Grenzen dieses Sofortleitfadens | Quellenstand 18. Oktober 2026 | Quellenstand 1. November 2026 | Sichtbarer Stand an Frontmatter angepasst; Fachprüfungsmarker unverändert. |
| Quellen | Referenzen [1]–[11] | Referenzen [1]–[14] | [12] BACS-PHP, [13] EDÖB-DataBreach und [14] DSV ergänzt; jede Quelle ist im Text numerisch zitiert. |

Unverändert erhalten: Slug `/wissen/ransomware-erste-60-minuten`, Veröffentlichungsdatum `01.10.2026`, Status **«Entwurf – nicht freigegeben»**, Meta-Title, Meta-Description, H1, Artikelstruktur und alle vier bisherigen **[FACHPRÜFUNG ERFORDERLICH]**-Marker. Es wurde kein `fachlich_geprüft_am` angelegt. Der Artikel hat nach der Pflege 2'723 Wörter und liegt damit weiterhin deutlich über der Mindestanforderung von 1'400 Wörtern.

### Arbeitsmittel

Datei: `/home/ubuntu/dkschv-audit/blog-paket/resources/01-60-minuten-checkliste.md`

| Betroffene Passage | Vorher | Nachher | Grund und Beleg |
|---|---|---|---|
| Frontmatter `version` | `Stand 18. Oktober 2026` | `Stand 1. November 2026` | Sichtbare Versionsangabe konsistent zum Artikelstand aktualisiert; keine Freigabeaussage. |
| Frontmatter `quellenpruefung_umfang` | `8 von 8 externen Quellenreferenzen geprüft` | `11 von 11 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft` | Tatsächlich verwendete Quellen [9]–[11] ergänzt; alle 11 Quellen im Original geprüft. |
| Frontmatter `quellenpruefung_status` | `Vollständig für die Quellenreferenzen; interne relative Ziele nicht live geprüft` | `Vollständig für die Quellenreferenzen; Fedlex-Historie und amtliche XML-Fassungen zusätzlich geprüft; interne relative Ziele nicht live geprüft` | Prüfumfang transparent ergänzt. [15] [16] [17] [18] [19] [20] |
| Abschnitt E, Checkliste zur EDÖB-Beurteilung | Kein separates Feld für die verfügbaren Meldedaten | Ein einzelner Checkbox-Punkt für Art, Zeitpunkt, Dauer, Daten/Personen, Folgen, Massnahmen und Ansprechperson ergänzt | Arbeitsmittelbezug zu Art. 15 DSV. Der Punkt verlangt nur das Zusammenstellen verfügbarer Fakten für die Fachprüfung, nicht die Abgabe einer Meldung. [14] |
| Abschnitt E, Hinweistext | Kein Hinweis auf EDÖB-Portal und DSV-Nachreichen | Sicheres Formular für Verantwortliche, DSV-Angaben, Nachreichen und Dokumentation ergänzt | Geltende Prozessinformationen aus EDÖB-Portal und DSV. [13] [14] |
| Grenzen und fachliche Prüfung | Quellenstand 18. Oktober 2026; keine Patch-Abgrenzung | Quellenstand 1. November 2026; abstrakte Aussage, dass Sicherheitsupdates keine bereits erfolgte Kompromittierung beseitigen | Begrenzte Umsetzung der Vormerkung mit BACS-Beleg. Keine neue Forensik- oder Wiederanlaufanweisung. [12] |
| Quellen | Referenzen [1]–[8] | Referenzen [1]–[11] | BACS-PHP, EDÖB-DataBreach und DSV ergänzt und jeweils sichtbar verwendet. |

Unverändert erhalten: Slug `/resources/01-60-minuten-checkliste`, Status **«Arbeitsvorlage – nicht freigegeben»**, Titel, Meta-Title, Meta-Description, Bezug zum Artikel, Tabellen, Checklistenstruktur, beide bisherigen **[FACHPRÜFUNG ERFORDERLICH]**-Marker und der interne relative Bezug. Es wurde kein `fachlich_geprüft_am` angelegt.

## Endkontrolle der Dateien

Die lokale Endkontrolle um 09:08:41 CET ergab für den Artikel 14 Quellen-Definitionen und 14 verwendete Inlinezitate; für das Arbeitsmittel 11 Quellen-Definitionen und 11 verwendete Inlinezitate. Es gibt in beiden Dateien keine ungenutzte oder undefinierte numerische Referenz, kein `ß` und keine URL mit unkodierten Klammern. Die erhaltenen Fachmarker wurden gezählt: Artikel 4, Arbeitsmittel 2. Diese technische Konsistenzprüfung ist keine Rechts-, Fach- oder Veröffentlichungsfreigabe.

## Verbleibende genaue Blocker und offene Fachfragen

1. **BACS-Erfassung:** Ob eine konkrete Organisation nach Art. 74b ISG erfasst ist oder eine Ausnahme nach Art. 74c ISG beziehungsweise CSV greift, bleibt ungeprüft. Die Quellen nennen den Rahmen, ersetzen aber keine Sachverhaltsprüfung. [18] [24]
2. **Konkreter BACS-Meldefall:** Ob ein konkretes Ereignis einen Tatbestand nach Art. 74d ISG erfüllt, wann es tatsächlich entdeckt wurde und welche Angaben bei einer Erstmeldung verfügbar sind, wird durch diese Publikation nicht entschieden. [18] [23]
3. **Konkreter EDÖB-Meldefall:** Betroffene Personendaten, ein voraussichtlich hohes Risiko, die Information betroffener Personen, der vollständige Meldetext und die Rolle eines Auftragsbearbeiters verlangen eine einzelfallbezogene Datenschutz- oder Rechtsbeurteilung. [16] [4] [20]
4. **Forensik, Bereinigung und Wiederanlauf:** Es wurde keine Organisation, kein Produkt, kein Backup, kein Konto, keine Schwachstelle und kein Beweisbestand untersucht. Die neue Patch-Abgrenzung ist ausdrücklich keine Anweisung, wie ein realer Vorfall forensisch zu untersuchen oder ein Wiederanlauf freizugeben ist. [12] [5]
5. **Lösegeld, Straf-, Sanktions-, Vertrags- und Versicherungsfragen:** Die BACS-Abratempfehlung und der Hinweis auf die Kantonspolizei bleiben allgemeine Orientierung. Zahlungs-, Sanktions-, Straf- und Vertragsfolgen wurden nicht beurteilt. [1]
6. **Kontakt- und Organisationsreife:** Incident Lead, Stellvertretung, sichere Kommunikationskanäle, kantonale Polizeikontakte, Versicherer, externe Fachpersonen, Backup-Administrationswege und manuelle Ersatzprozesse sind je Organisation zu prüfen, zu vereinbaren und zu üben. Die Checkliste stellt keinen Nachweis dafür dar. [6]
7. **Interne und öffentliche Ziele:** Alle internen relativen Slugs wurden planungsgemäss erhalten. Ihr öffentlicher Bestand und die Live-Erreichbarkeit wurden nicht geprüft. Es erfolgte keine CMS-Änderung.
8. **Historischer Seitenwortlaut:** BACS-, EDÖB- und CISA-Webseiten bieten nicht durchgehend eine lückenlose redaktionelle Historie. Die Prüfung belegt erreichbaren Inhalt zu den genannten Abrufzeiten; sie garantiert keinen unveröffentlichten Zwischenstand und keinen Wortlaut um 09:00. Für die drei einschlägigen Rechtsquellen wurden Chronologien und amtliche XML-Fassungen herangezogen. [15] [16] [17] [18] [19] [20]

## Schlussfolgerung

Artikel und Arbeitsmittel bleiben Entwürfe ohne Freigabe. Die bestehende allgemeine Erstreaktion ist auf Basis der geprüften BACS-, CISA-, EDÖB- und Fedlex-Quellen weiterhin tragfähig. Die gezielten Ergänzungen verbessern die Dokumentation der aktuellen BACS- und EDÖB-Meldewege sowie die verlangte Patch-Abgrenzung, ohne neue organisationsspezifische Forensik-, Bereinigungs- oder Wiederanlaufvorgaben zu schaffen. Es gab keine Liveänderung.

## Quellen

[1]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[2]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, DSG SR 235.1"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen nach Art. 24 DSG"
[5]: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware "CISA – I've Been Hit By Ransomware! Response Checklist"
[6]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[7]: https://csrc.nist.gov/pubs/sp/800/61/r3/final "NIST SP 800-61 Rev. 3 – Incident Response Recommendations and Considerations"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Bundesgesetz über die Informationssicherheit, ISG SR 128"
[9]: https://www.suisse-epolice.ch/cybercrime-case "Suisse ePolice – Cyberkriminalität anzeigen"
[10]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion"
[11]: https://www.report.ncsc.admin.ch/de/chat?path=406%3E407%3E1 "BACS – Freiwillige Meldung eines Cybervorfalls"
[12]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen"
[13]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach: Meldung von Datensicherheitsverletzungen durch Verantwortliche"
[14]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz, DSV SR 235.11"
[15]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG Chronologie"
[16]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – DSG amtliche XML-Fassung vom 7. Juli 2025"
[17]: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history "Fedlex – ISG Chronologie"
[18]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20251001/de/xml/fedlex-data-admin-ch-eli-cc-2022-232-20251001-de-xml-1.xml "Fedlex – ISG amtliche XML-Fassung vom 1. Oktober 2025"
[19]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV Chronologie"
[20]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml "Fedlex – DSV amtliche XML-Fassung vom 1. Dezember 2025"
[21]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[22]: https://www.bacs.admin.ch/de/aktuelle-vorfaelle "BACS – Aktuelle Vorfälle"
[23]: https://www.bacs.admin.ch/de/was-muss-gemeldet-werden "BACS – Was muss gemeldet werden?"
[24]: https://www.bacs.admin.ch/de/wer-muss-melden "BACS – Wer muss melden?"
[25]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a "CISA – #StopRansomware: SafePay Ransomware"
[26]: https://www.bacs.admin.ch/de/medienmitteilungen "BACS – Medienmitteilungen"
