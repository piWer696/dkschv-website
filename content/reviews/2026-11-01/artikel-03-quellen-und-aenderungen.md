# Prüfbericht – Artikel 03: Datenpanne melden Schweiz

- **Prüfdatum:** 1. November 2026, ISO-KW 44. Die Originalquellen wurden am 1. November 2026 nach 09:00 CET abgerufen. Die dokumentierten Tool-Rückläufe lagen zwischen **09:05:22 und 09:07:11 CET**. Das ist der tatsächliche Abrufzeitraum, nicht eine behauptete Website-Fassung zu einem früheren Stichtag.
- **Newsfenster:** 25. Oktober 2026, 09:00 CET bis 1. November 2026, 09:00 CET. Für die turnusmässige Quellenpflege wurde zusätzlich die Änderungslage seit der letzten Einzelprüfung vom 18. Oktober 2026 nach 09:00 CEST abgeglichen.
- **Gegenstand:** Artikel `/wissen/datenpanne-melden-schweiz` und Arbeitsmittel `/resources/03-datenpanne-entscheidungsbaum`.
- **Abrufmethode:** Ausschliesslich stateless Recherche mit `search` und Abruf der Originalquellen mit `fetch`. Es wurden weder ein Browser noch ein CMS geöffnet, keine Anmeldung verwendet und keine Live-Änderung vorgenommen.
- **Umfang:** Alle **12 unterschiedlichen, in den beiden Dateien zitierten externen Originalquellen** wurden direkt abgerufen und auf Erreichbarkeit sowie auf die konkret verwendeten Aussagen abgeglichen. Zusätzlich wurden die amtlichen Fedlex-Historien und -Änderungsseiten sowie die amtliche ISG-XML-Fassung abgerufen. Die offiziellen EDÖB- und BACS-Übersichten und die seit dem letzten Review potenziell einschlägigen Originalmeldungen wurden gezielt gesichtet. Das ist keine Vollständigkeitszusage für jede Publikation im Internet und keine minutengenaue historische Wortlautgarantie für undatierte Seiten.

## Befund für die Meldewege und den Rechtsstand

Die amtlich ausgewiesenen Fassungen von DSG, DSV, ISG und CSV bestätigen die bisherige materielle Einordnung. Art. 24 DSG verpflichtet den Verantwortlichen, eine Datensicherheitsverletzung bei voraussichtlich hohem Risiko so rasch als möglich dem EDÖB zu melden. Der Auftragsbearbeiter meldet die Verletzung so rasch als möglich dem Verantwortlichen. Art. 15 DSV konkretisiert die Angaben und erlaubt das rasche Nachreichen fehlender Informationen.[1] [2]

Die Fedlex-Historien zeigen keine seit dem letzten Einzelreview neu geltende Fassung: DSG **Stand 7. Juli 2025**, DSV **Stand 1. Dezember 2025**, ISG **Stand 1. Oktober 2025** und CSV **Stand 1. April 2025**. Die DSG-Änderungsseite weist für Art. 24 die bereits seit 1. April 2025 geltenden BACS-bezogenen Änderungen aus. Die DSV-Änderungsseite weist seit dem damaligen Stand keine Änderung von Art. 15 aus.[13] [14] [15] [16] [17] [19]

Der direkte stateless Abruf der ISG-ELI-Seite war zwar erreichbar, lieferte jedoch nur den Javascript-Hinweis statt des Normtexts. Das ist **keine fehlende Rechtsfassung**: Die amtliche Fedlex-Chronologie und die verlinkte amtliche XML-Fassung waren direkt erreichbar. Sie bestätigen insbesondere Art. 74a bis 74f ISG: Unterstellung, Auskunft und Verfügung durch das BACS, den Katalog nach Art. 74b, die vier Meldekriterien nach Art. 74d, die Erstmeldung innert 24 Stunden nach Entdeckung sowie das sichere Übermittlungssystem.[17] [18]

Die BACS-Seiten bestätigen unverändert die getrennte BACS-Prüfung für Betreiberinnen und Betreiber kritischer Infrastrukturen. Das BACS beschreibt die Erstmeldung innert 24 Stunden nach Entdeckung. Bei unvollständiger Erstmeldung besteht eine Frist von 14 Tagen zur Vervollständigung. Der CSH-Meldeweg und die alternative Meldemöglichkeit über den Meldebutton bleiben erreichbar; das Formular kann auf Wunsch an weitere Behörden wie EDÖB oder FINMA weiterleiten.[7] [8]

Die seit dem letzten Review relevante Mitteilung des EDÖB vom 23. Oktober betrifft den Cyberangriff auf die PK Softech AG. Der EDÖB teilt mit, dass er gegen Softech am 22. Oktober eine formelle Untersuchung eröffnet hat. Abzuklären sind unter anderem die von Vorsorgeeinrichtungen an das Softwareunternehmen übermittelten Personendaten, die rechtlichen Rahmenbedingungen und tatsächliche Umsetzung der Datenübertragungen sowie der Umfang abgeflossener Informationen. **Das Verfahren ist hängig.** Weitere Angaben dazu gibt der EDÖB nicht. Die Meldung belegt daher **keinen abschliessend festgestellten Verstoss** und **keine neue allgemeine Meldefrist**.[12]

Die Mitteilung ist dennoch für die allgemeine Vorbereitung eines Vorfalls nützlich. Sie stützt eine begrenzte Ergänzung zur Rollen- und Datenflussklärung: Datenbearbeiterbeziehungen, Datenkategorien, tatsächliche oder mögliche Übermittlungen, vertragliche Vorfallkontakte und der tatsächliche Erreichbarkeitsweg gehören in die Ereignisakte. Die Einordnung, wer im konkreten Verhältnis Verantwortlicher oder Auftragsbearbeiter ist, und die Einzelfallfolgen bleiben fachlich zu prüfen.[1] [4] [12]

## Alle zitierten Originalquellen der beiden Dateien

**Erreichbarkeitshinweis:** «Erreichbar» bedeutet in dieser Tabelle, dass der direkte stateless Abruf am genannten Zeitpunkt mit dem Tool-Status `success` gelang. Das Tool weist dabei nicht für jede Quelle einen separaten HTTP-Statuscode aus; es wird deshalb kein nicht beobachteter HTTP-200-Code behauptet. Alle hier aufgeführten URLs waren ohne Anmeldung abrufbar. Bei den undatierten Behörden-Webseiten besteht keine öffentliche lückenlose Änderungshistorie.

| Nr. | Original-URL | Abruf am 1.11.2026 nach 09:00 CET | Erreichbarkeit / technischer Befund | Version oder Datum | Konkret geprüfter Aussagegehalt und Verwendung |
|---:|---|---|---|---|---|
| 1 | `https://www.fedlex.admin.ch/eli/cc/2022/491/de` | 09:05:24 | Erreichbar; Normtext und Fassungsübersicht geliefert. | DSG, Stand 7. Juli 2025. | Art. 5 definiert Personendaten, Verantwortlichen, Auftragsbearbeiter und Datensicherheitsverletzung. Art. 24 stützt hohes Risiko, «so rasch als möglich», Meldeweg Verantwortlicher, Mitteilung des Auftragsbearbeiters und getrennte Betroffeneninformation.[1] |
| 2 | `https://www.fedlex.admin.ch/eli/cc/2022/568/de` | 09:05:25 | Erreichbar; Normtext und Fassungsübersicht geliefert. | DSV, Stand 1. Dezember 2025. | Art. 15 Abs. 1 nennt Inhalt der EDÖB-Meldung; Abs. 2 erlaubt das rasche Nachreichen; Abs. 3 betrifft die Angaben bei erforderlicher Information betroffener Personen.[2] |
| 3 | `https://www.edoeb.admin.ch/de/databreach` | 09:05:22 | Erreichbar; vollständiger Seiteninhalt geliefert. | Undatierte aktuelle Behördenseite; verlinkt Leitfaden vom 23. April 2025. | Sicheres digitales Formular für Verantwortliche; nach Absenden kann eine Bestätigung heruntergeladen werden. Das Formular ist ausdrücklich nicht für betroffene Personen bestimmt.[3] |
| 4 | `https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf` | 09:05:25 | Erreichbar; PDF-Inhalt extrahiert. | Leitfaden Version 1.2; auf der DataBreach-Seite mit 23. April 2025 datiert. | Meldung und Betroffeneninformation obliegen dem Verantwortlichen. Der Auftragsbearbeiter informiert unabhängig von der Risikoeinschätzung über jede Datensicherheitsverletzung. Der Leitfaden stützt die Beurteilung von Schwere und Wahrscheinlichkeit, die Berücksichtigung nachweisbarer Sofortmassnahmen und das Nichtzuwarten bei nicht kurzfristig ausschliessbarem hohen Risiko.[4] |
| 5 | `https://www.fedlex.admin.ch/eli/cc/2022/232/de` | 09:05:28 | Erreichbar, aber stateless nur Javascript-Hinweis; deshalb Normaussagen mit amtlicher XML und Chronologie abgesichert. | ISG, amtliche aktuelle Fassung Stand 1. Oktober 2025.[17] [18] | Referenz für Art. 74a–74f ISG. Die belastbaren Textbefunde stammen aus der amtlichen XML-Fassung: Unterstellung, Auskunft/Verfügung, Art. 74b-Katalog, Art. 74d-Kriterien, 24 Stunden nach Entdeckung, sichere Übermittlung.[18] |
| 6 | `https://www.fedlex.admin.ch/eli/cc/2025/169/de` | 09:05:28 | Erreichbar; Normtext und Fassungsübersicht geliefert. | CSV, Stand 1. April 2025; einzige amtlich ausgewiesene Fassung.[19] | Art. 12 enthält Ausnahmen. Die CSV ist die Ausführungsverordnung zur BACS-Meldepflicht; sie stützt in Verbindung mit Art. 74e ISG die präzisierte Darstellung der Ergänzungsfrist.[6] |
| 7 | `https://www.bacs.admin.ch/de/informationen-zur-meldepflicht` | 09:05:28 | Erreichbar; vollständiger Seiteninhalt geliefert. | Undatierte aktuelle Behördenseite. | Meldepflicht seit 1. April 2025 für kritische Infrastrukturen, 24 Stunden nach Entdeckung, 14 Tage zur Vervollständigung bei unvollständiger Erstmeldung, Beispiele für Kriterien und Verweis auf den Meldeprozess.[7] |
| 8 | `https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden` | 09:05:29 | Erreichbar; vollständiger Seiteninhalt geliefert. | Undatierte aktuelle Behördenseite. | CSH-Formular, alternative Meldemöglichkeit über den Meldebutton und mögliche Weiterleitung an weitere meldezuständige Behörden, beispielsweise EDÖB oder FINMA.[8] |
| 9 | `https://www.bacs.admin.ch/de/ransomware-was-nun` | 09:05:34 | Erreichbar; vollständiger Seiteninhalt geliefert. | Undatierte aktuelle Behördenseite. | Netztrennung, Log-Sicherung und forensische Sicherungen durch Fachpersonen vor Reparaturversuchen oder Neustarts. Die Seite wiederholt auch die getrennten BACS- und EDÖB-Meldewege.[9] |
| 10 | `https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679` | 09:05:40 | Erreichbar; amtlicher PDF-Text extrahiert. | Verordnung EU 2016/679, Amtsblatt vom 4. Mai 2016. | Art. 33 Abs. 1 enthält die EU-Regel «möglichst binnen 72 Stunden». Sie dient im Artikel ausschliesslich als Vergleich, um diese Frist nicht fälschlich als Schweizer DSG-Frist auszugeben.[10] |
| 11 | `https://www.bacs.admin.ch/de/26w40-de` | 09:06:03 | Erreichbar; vollständiger Seiteninhalt geliefert. | Veröffentlicht am 6. Oktober 2026. | Ein einzelnes Anzeichen beweist keine Infektion; mehrere ungewöhnliche Beobachtungen sollen genauer untersucht werden. Bei geschäftlicher Nutzung empfiehlt das BACS die Information von Arbeitgeber oder IT-Abteilung. Keine neue Meldepflicht.[11] |
| 12 | `https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein` | 09:06:12 | Erreichbar; vollständiger Seiteninhalt geliefert. | Veröffentlicht am 23. Oktober 2026. | Hängige formelle Untersuchung zu PK Softech AG; Gegenstand sind unter anderem Personendaten, Rechtsgrundlagen, tatsächliche Datenübertragungen und Umfang abgeflossener Informationen. Keine abschliessende Feststellung, keine neue allgemeine Frist.[12] |

## Amtliche Fassungs- und Änderungszugänge bei Fedlex

Diese URLs gehören nicht als separate Ziffern in die beiden Publikationsdateien. Sie wurden zusätzlich eröffnet, weil die Pflege bei Rechtsquellen die öffentlich ausgewiesene Fassung und Änderungen verifizieren muss. Insbesondere ersetzt ein Javascript-Leerabruf des ISG nicht die amtlich vorhandene Rechtsfassung.

| Original-URL | Abruf am 1.11.2026 nach 09:00 CET | Erreichbarkeit / Version | Befund |
|---|---:|---|---|
| `https://www.fedlex.admin.ch/eli/cc/2022/491/de/history` | 09:06:41 | Erreichbar; Chronologie. | DSG: oberste aktuelle Fassung 7. Juli 2025, Berichtigung; keine Fassung nach dem letzten Review.[13] |
| `https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes` | 09:06:41 | Erreichbar; Änderungen. | Art. 24 weist die bereits geltenden Änderungen vom 29. September 2023 mit Inkrafttreten per 1. April 2025 aus; die Berichtigung 2025 betrifft nur den italienischen Text von Art. 57.[14] |
| `https://www.fedlex.admin.ch/eli/cc/2022/568/de/history` | 09:06:41 | Erreichbar; Chronologie. | DSV: oberste aktuelle Fassung 1. Dezember 2025; keine Fassung nach dem letzten Review.[15] |
| `https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes` | 09:06:43 | Erreichbar; Änderungen. | Änderungen der geltenden Fassung betreffen zuletzt Art. 4, 8, 37a und 46; Art. 15 ist nicht neu geändert ausgewiesen.[16] |
| `https://www.fedlex.admin.ch/eli/cc/2022/232/de/history` | 09:06:02 | Erreichbar; Chronologie. | ISG: aktuelle Fassung 1. Oktober 2025. Die Chronologie dokumentiert die Meldepflicht-Änderungen und die Inkraftsetzungen 2025.[17] |
| `https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20251001/de/xml/fedlex-data-admin-ch-eli-cc-2022-232-20251001-de-xml-1.xml` | 09:06:08 | Erreichbar; amtlicher XML-Normtext. | Art. 74a–74f wurden direkt im amtlichen XML abgeglichen. Damit ist der stateless Javascript-Hinweis der ELI-Ansicht technisch erklärt, nicht als fehlender Rechtszugang behandelt.[18] |
| `https://www.fedlex.admin.ch/eli/cc/2025/169/de/history` | 09:06:09 | Erreichbar; Chronologie. | CSV: einzige Fassung, Stand 1. April 2025; keine spätere Fassung ausgewiesen.[19] |

## Seit dem 18. Oktober gesichtete offizielle Originalmeldungen und Übersichten

Die nachstehenden Originalseiten wurden zusätzlich auf einen möglichen materiellen Einfluss auf Artikel 03 geprüft. Nur die Softech-Mitteilung ist für die allgemeine Rollen- und Datenflussklärung hinreichend nah am Gegenstand. Die anderen Befunde wurden nicht als künstliche Wochennews oder als ungenutzte Quellen in den Evergreen-Text eingefügt.

| Original-URL | Abruf am 1.11.2026 nach 09:00 CET | Erreichbarkeit / Datum | Aussagegehalt und Entscheidung für Artikel 03 |
|---|---:|---|---|
| `https://www.edoeb.admin.ch/de/2026-de` | 09:06:12 | Erreichbar; aktuelle EDÖB-Jahresübersicht. | Die Übersicht führt am 23. Oktober die Softech-Mitteilung, am 22. Oktober die rechtskräftige Add-Conti-Verfügung und am 21. Oktober einen Stimmerkennungsentscheid. Für Meldewege ist daraus nur Softech als begrenzte Rollenklärung einschlägig.[20] |
| `https://www.bacs.admin.ch/de/im-fokus` | 09:06:16 | Erreichbar; aktuelle Übersicht. | Abgefragt auf neue Hinweise zu Meldepflicht, Datenabfluss und kritischen Infrastrukturen. Der gelieferte relevante Auszug ergab keine neue Verfahrensregel für Artikel 03. Wegen unversionierter Übersichtsseite keine vollständige historische Wortlautgarantie.[21] |
| `https://www.bacs.admin.ch/de/medienmitteilungen` | 09:06:17 | Erreichbar; aktuelle Übersicht. | Die relevante Übersichtsauswahl zeigte im Jahr 2026 zuletzt den 25. September zum geplanten neuen Cybersicherheitsgesetz. Das ist ein Auftrag für eine Vorlage bis Juni 2027, keine heute geltende Änderung von ISG/CSV oder des Meldewegs.[22] |
| `https://www.bacs.admin.ch/de/wer-muss-melden` | 09:06:19 | Erreichbar; undatierte aktuelle Behördenseite. | Bestätigt die Orientierung an Art. 74b ISG und CSV-Ausnahmen. Keine neue Unterstellungskategorie oder Frist; nicht zusätzlich zitiert, weil ISG/CSV die stärkeren Primärbelege bleiben.[23] |
| `https://www.bacs.admin.ch/de/was-muss-gemeldet-werden` | 09:06:19 | Erreichbar; undatierte aktuelle Behördenseite. | Bestätigt Funktionsfähigkeitsgefährdung, Manipulation, Informationsabfluss sowie Erpressung, Drohung oder Nötigung; keine Änderung gegenüber Art. 74d ISG.[24] |
| `https://www.bacs.admin.ch/de/26w42-de` | 09:07:11 | Erreichbar; veröffentlicht am 20. Oktober 2026. | Hotelbuchungs-Phishing mit mutmasslich kompromittierten Buchungs- oder E-Mail-Systemen und möglichen Kundendatenzugriffen. Das BACS formuliert daraus keine DSG-/DSV- oder BACS-Meldewegsänderung. Kein Einbau in den Evergreen-Text.[25] |
| `https://www.bacs.admin.ch/de/26w43-de` | 09:07:11 | Erreichbar; veröffentlicht am 27. Oktober 2026. | WhatsApp-Kontoübernahmen mit möglichem Zugriff auf Chatverläufe, Gruppen, Fotos und vertrauliche Informationen. Kein neuer Meldeweg und keine neue allgemeine Frist; nicht als wöchentlicher Fall in Artikel 03 ergänzt.[26] |
| `https://www.edoeb.admin.ch/de/edoeb-verbietet-add-conti-gmbh-die-datenbearbeitung-zu-werbezwecken-und-ordnet-umfassende-loeschung-an` | 09:07:11 | Erreichbar; veröffentlicht am 22. Oktober 2026. | Rechtskräftige Verfügung zur rechtswidrigen Werbedatenbearbeitung, Löschung und Verantwortung trotz behaupteter Auslagerung. Kein Datenpannen- oder Meldewegfall. Nicht als Quelle ergänzt, um den Artikel nicht vom Gegenstand wegzuführen.[27] |

Die Recherche über die offiziellen Übersichten und die direkten Originalmeldungen liefert keine belegte Änderung von DSG, DSV, ISG, CSV, DataBreach oder dem BACS-Meldeverfahren im Newsfenster. Sie ersetzt keine Vollständigkeitszusage für sämtliche Drittseiten oder eine Aussage über den exakten historischen Wortlaut einer unversionierten Seite um 09:00 CET.

## Änderungen im Artikel

### Frontmatter und Quellenstand

| Betroffene Passage | Vorher | Nachher | Grund |
|---|---|---|---|
| `rechtsstand` | `4. Oktober 2026` | `1. November 2026 (DSG, DSV, ISG und CSV amtlich verifiziert)` | Der Rechtsstand wurde nur angehoben, weil die vier einschlägigen Erlasse über amtliche Fassungen, Historien und bei ISG zusätzlich XML verifiziert wurden.[1] [2] [13] [15] [17] [18] [19] |
| `stand` | `18. Oktober 2026` | `1. November 2026` | Tatsächliches Datum dieser Quellenpflege. |
| `quellenpruefung_umfang` | «Manifestierte Primärquellen sowie alle zitierten externen Originalquellen dieses Artikels und des zugehörigen Arbeitsmittels; BACS-Im-Fokus seit 4. Oktober 2026» | «Alle 12 zitierten externen Originalquellen dieses Artikels und des zugehörigen Arbeitsmittels; einschliesslich amtlicher Fedlex-Historien und ISG-XML bei stateless Leerabruf sowie einschlägiger EDÖB-/BACS-Originalmeldungen seit 18. Oktober 2026» | Nennt den wirklich geprüften Anteil und den technischen ISG-Befund präzise. |
| `quellenpruefung_status` | «Vollständig für die zitierten externen Originalquellen geprüft am 18. Oktober 2026; keine Fachfreigabe» | «Vollständig für die 12 zitierten externen Originalquellen geprüft am 1. November 2026; keine Fachfreigabe» | Das Prüfdatum und die Zahl der unterschiedlichen Referenzen sind belegbar. Keine Fachfreigabe wurde behauptet. |

### Rollenklärung nach der Softech-Mitteilung

| Betroffene Passage | Vorher | Nachher | Belegte Abgrenzung |
|---|---|---|---|
| Abschnitt «1. Sind Personendaten betroffen und liegt eine Datensicherheitsverletzung vor?» nach dem Absatz zu Verantwortlichem und Auftragsbearbeiter | Kein Fallbezug nach dem Satz, wonach der Auftragsbearbeiter den Verantwortlichen unabhängig von der Risikoeinschätzung informieren muss. | Neuer Absatz zur Mitteilung vom 23. Oktober 2026: Anlass, Datenbearbeiterbeziehungen vorab greifbar zu machen; Prüfung von Personendaten, Rechtsgrundlagen, tatsächlichen Übertragungen und Informationsumfang; Ereignisakte zu Datenflüssen, Rollen, Verträgen, Meldewegen und erreichbaren Vorfallkontakten. | Der Text nennt ausdrücklich, dass das Softech-Verfahren hängig ist und weder einen festgestellten Datenschutzverstoss noch eine neue allgemeine Meldefrist darstellt.[12] |
| Quellenverzeichnis | Ziffern 1–11. | Neue Ziffer 12 für die Softech-Mitteilung, im neuen Absatz verwendet. | Jede neue Quelle ist mit einer passenden Inlinezitation und Definition verbunden.[12] |

**Unverändert im Artikel:** Slug `/wissen/datenpanne-melden-schweiz`, ursprüngliches Veröffentlichungsdatum `15.10.2026`, Status «Entwurf – nicht freigegeben», `fachprüfung_status`, H1, SEO-Felder, sämtliche bestehenden internen relativen Slugs und alle **4** bisherigen `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Der Artikel enthält nach der Änderung 2'311 Wörter und damit weiterhin deutlich mehr als die verlangten 1'400 Wörter.

## Änderungen im Arbeitsmittel

### Versions- und Standhinweise

| Betroffene Passage | Vorher | Nachher | Grund |
|---|---|---|---|
| Frontmatter `version` | `Rechtsstand 4. Oktober 2026` | `Rechtsstand 1. November 2026 (DSG, DSV, ISG und CSV amtlich verifiziert)` | Konsistente und belegte Anhebung des Rechtsstands, ohne Fachfreigabe.[1] [2] [17] [18] [19] |
| Frontmatter `stand` | `18. Oktober 2026` | `1. November 2026` | Tatsächlicher Pflegezeitpunkt. |
| Frontmatter `quellenpruefung_umfang` und `quellenpruefung_status` | Bezug auf den Stand 18. Oktober 2026 ohne Quellenanzahl. | Bezug auf alle 12 unterschiedlichen zitierten Originalquellen, amtliche Historien/XML und die zielgerichteten neuen EDÖB-/BACS-Meldungen; Prüfung am 1. November 2026, keine Fachfreigabe. | Ehrliche Quellenreichweite und konsistent mit dem Artikel. |
| Sichtbarer Kopf, Zeilen «Quellenprüfung» und «Rechtsstand» | Quellenprüfung 18. Oktober 2026; Rechtsstand 4. Oktober 2026. | Quellenprüfung 1. November 2026, mit tatsächlichem Abruffenster 09:05–09:07 CET; Rechtsstand 1. November 2026 mit amtlich verifizierten Erlassen. | Arbeitsmittelversion und sichtbare Hinweise sind mit dem Frontmatter und Artikel konsistent. |

### Neue Rollen- und Datenflussnotiz

| Betroffene Passage | Vorher | Nachher | Belegte Abgrenzung |
|---|---|---|---|
| Abschnitt C1, unmittelbar nach dem Kontrollfeld «Auftragsbearbeiter meldete dem Verantwortlichen am / um» | Direkt anschliessend begann C2 «Risiko für Betroffene begründen». | Neue hervorgehobene Arbeitsanweisung: pro betroffenem Dienstleister Datenkategorien, Übermittlungen, Verantwortlicher, Auftragsbearbeiter, vertragliche Vorfallkontakte und tatsächlicher Erreichbarkeitsweg notieren. Anschliessend klare Erklärung, dass die Softech-Mitteilung eine hängige Untersuchung und keinen festgestellten Verstoss oder eine neue allgemeine Frist betrifft. | Praktische Strukturierung nach dem dokumentierten Untersuchungsgegenstand; kein vorweggenommener Befund oder Einzelfallentscheid.[12] |
| Quellenverzeichnis | Ziffern 1–9. | Neue Ziffer 10 für die Softech-Mitteilung, im neuen C1-Absatz verwendet. | Quellenintegrität gewahrt.[12] |

**Unverändert im Arbeitsmittel:** Slug `/resources/03-datenpanne-entscheidungsbaum`, Status «Arbeitsvorlage – nicht freigegeben», Bezug zum Artikel, H1, SEO-Felder, interne relative Verlinkung und alle **6** bisherigen `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Das Arbeitsmittel enthält nach der Änderung 2'252 Wörter. Es bleibt eine allgemeine Arbeitsvorlage und entscheidet keine Meldepflicht.

## Metadaten, Referenzintegrität und Veröffentlichung

An `meta_title` und `meta_description` wurde in keiner der beiden Dateien etwas geändert. Die geprüfte Ergänzung betrifft die operative Rollen- und Datenflussklärung, nicht den Gegenstand der vorhandenen Suchfelder. Deshalb wurden auch keine Vorschlagsfelder angelegt.

Die Referenzprüfung nach der Bearbeitung ergab im Artikel **12** Quellenziffern und im Arbeitsmittel **10** Quellenziffern. Jede verwendete Ziffer hat eine Definition, und keine Definition ist ungenutzt. Alle externen Quellen-URLs im Artikel und Arbeitsmittel verwenden bereits keine unkodierten URL-Klammern.

**Keine Liveänderung:** Kein CMS wurde geöffnet oder bearbeitet. Es gab keine Anmeldung, keinen Import, keine Veröffentlichung und keinen geänderten Live-Abschnitt. Die internen relativen Slugs wurden als Planungswerte unverändert erhalten; ihre öffentliche Erreichbarkeit war nicht Gegenstand dieser Ausführung und wird hier nicht als gegeben behauptet.

## Verbleibende genaue Fach- und Veröffentlichungsblocker

1. **Fachfreigabe fehlt weiterhin.** Der Artikel bleibt «Entwurf – nicht freigegeben», das Arbeitsmittel «Arbeitsvorlage – nicht freigegeben». Die vier beziehungsweise sechs bestehenden Marker bleiben vollständig erhalten.
2. **EDÖB-Einzelfallentscheidung offen.** Für einen konkreten Vorfall muss fachlich beurteilt werden, ob unter den tatsächlichen Datenarten, Empfängern, Zugriffshinweisen, Schutzmassnahmen und möglichen Folgen ein voraussichtlich hohes Risiko nach Art. 24 Abs. 1 DSG besteht. Ebenfalls offen bleibt, ob und wie betroffene Personen zu ihrem Schutz zu informieren sind beziehungsweise ob eine gesetzliche Einschränkung, ein Aufschub oder ein Verzicht in Betracht kommt.[1] [4]
3. **Rollenklärung ist nicht abstrakt abschliessbar.** Der Verantwortliche und gegebenenfalls Auftragsbearbeiter müssen für das konkrete Verhältnis, die Weisungs- und Entscheidbefugnisse, Verträge, Unterauftragsbearbeitung, Datenflüsse und Ereigniskontakte festgestellt werden. Die Softech-Mitteilung ersetzt diese Prüfung nicht.[1] [4] [12]
4. **BACS-Unterstellung und Angriffstatbestand offen.** Es ist konkret zu klären, ob die Organisation unter Art. 74b ISG fällt, ob eine CSV-Ausnahme greift, ob sich der Angriff auf die relevante Tätigkeit in der Schweiz auswirkt, ob mindestens ein Kriterium von Art. 74d ISG erfüllt ist und wann der Angriff rechtlich massgeblich entdeckt wurde. Das BACS kann zur Unterstellung Auskunft geben und auf Antrag verfügen; dies wurde weder simuliert noch entschieden.[18] [19]
5. **Technik, Forensik und Kommunikation verlangen Einzelfallführung.** Die konkrete Beweissicherung, Eingrenzung, Wiederanlaufentscheidung, Meldungsinhalte, Weiterleitung, Betroffenenkommunikation sowie weitere vertragliche, aufsichtsrechtliche, strafrechtliche oder versicherungsbezogene Pflichten können aus diesem allgemeinen Text nicht freigegeben werden.[4] [8] [9]
6. **Veröffentlichung bleibt separat blockiert.** Eine Quellenprüfung und ein amtlich verifizierter Rechtsstand sind keine Rechts-, Fach-, Tenant- oder Publikationsfreigabe. Vor einer späteren Veröffentlichung sind die dann aktuellen Meldewege, die Fachmarker und die öffentlichen Zielseiten erneut zu prüfen.

## Quellen

[1]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz DSG"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz DSV"
[3]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zu Datensicherheitsverletzungen Version 1.2"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Informationssicherheitsgesetz ISG"
[6]: https://www.fedlex.admin.ch/eli/cc/2025/169/de "Fedlex – Cybersicherheitsverordnung CSV"
[7]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht"
[8]: https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden "BACS – Wie muss ein Cyberangriff gemeldet werden"
[9]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware Was nun"
[10]: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679 "EUR-Lex – Datenschutz-Grundverordnung Artikel 33"
[11]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40 Schadsoftwareverdacht und Massnahmen"
[12]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant"
[13]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG Chronologie"
[14]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex – DSG Änderungen"
[15]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV Chronologie"
[16]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes "Fedlex – DSV Änderungen"
[17]: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history "Fedlex – ISG Chronologie"
[18]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20251001/de/xml/fedlex-data-admin-ch-eli-cc-2022-232-20251001-de-xml-1.xml "Fedlex – ISG amtliche XML-Fassung Stand 1. Oktober 2025"
[19]: https://www.fedlex.admin.ch/eli/cc/2025/169/de/history "Fedlex – CSV Chronologie"
[20]: https://www.edoeb.admin.ch/de/2026-de "EDÖB – Mitteilungen 2026"
[21]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[22]: https://www.bacs.admin.ch/de/medienmitteilungen "BACS – Medienmitteilungen"
[23]: https://www.bacs.admin.ch/de/wer-muss-melden "BACS – Wer muss melden"
[24]: https://www.bacs.admin.ch/de/was-muss-gemeldet-werden "BACS – Was muss gemeldet werden"
[25]: https://www.bacs.admin.ch/de/26w42-de "BACS – Woche 42 Hotelbuchungs-Phishing"
[26]: https://www.bacs.admin.ch/de/26w43-de "BACS – Woche 43 WhatsApp-Kontoübernahmen"
[27]: https://www.edoeb.admin.ch/de/edoeb-verbietet-add-conti-gmbh-die-datenbearbeitung-zu-werbezwecken-und-ordnet-umfassende-loeschung-an "EDÖB – Add Conti Datenbearbeitung zu Werbezwecken"
