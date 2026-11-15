# Quellenbefund – Schweizer Behördennews für DKSchV / Schweizer KMU

**Berichtsfenster:** 18.10.2026, 09:00 CEST bis 25.10.2026, 09:00 CET, Europe/Zurich. Wegen der Zeitumstellung am 25.10. umfasst dieses lokale Zeitfenster tatsächlich 169 Stunden (18.10. 07:00 UTC bis 25.10. 08:00 UTC).

**Abrufstand:** Die hier dokumentierten Originalseiten wurden am 25.10.2026 zwischen 09:06 und 09:08 CET geöffnet; die abschliessende Kontrolle von BACS «Im Fokus» erfolgte um 09:08 CET. Die Abrufe liegen somit nach dem Ende des Berichtsfensters. Bei nicht versionierten Webseiten ist damit kein minutengenauer historischer Wortlaut um 09:00 CET nachweisbar. Der Befund ist keine Vollständigkeitszusage und keine Aussage über die Betroffenheit eines einzelnen KMU.

Die Vorwochenausgabe vom 18.10. wurde abgeglichen. Die gemeinsame EDÖB-/BACS-KI-Kampagne vom 16.10. ist bereits darin enthalten und wird nicht doppelt aufgenommen. Wartungsmanifest und Artikelstatus wurden nur für die nachfolgend nummerierten Vormerkungen zur Pflege vom 01.11. herangezogen; daraus folgt keine heutige Quellenstandsbehauptung zu den zwölf Entwürfen und keine CMS-Änderung.

## Ausgewählte Meldungen

### 1. Kritische PHP-Schwachstellen: Herstellerfixe und BACS-Updatehinweis

**Publiziert:** 21.10.2026 durch BACS; die PHP-Sicherheitsmeldung und beide Herstelleradvisories tragen ebenfalls den 21.10.2026.  
**Originale:** BACS [1]; PHP [2]; PHP Advisory CVE-2026-109618 [3]; PHP Advisory CVE-2026-109619 [4].

Das BACS warnt vor zwei kritischen PHP-Schwachstellen, **CVE-2026-109618** und **CVE-2026-109619**, die auf betroffenen Servern eine nicht authentisierte Ausführung von Schadcode ermöglichen können. Es nennt als korrigierte PHP-Releases 8.5.12, 8.4.27, 8.3.36 und 8.2.35 und weist darauf hin, dass auch eingebettete PHP-Komponenten in Anwendungen, Appliances und Hosting-Angeboten zu prüfen sind. [1]

Die PHP-Projektquellen bestätigen diese Fixstände und stufen beide Schwachstellen mit CVSS 4.0 9.2 ein. Sie bezeichnen ein Update als einzige vollständige respektive zuverlässige Behebung. Bei durch Distributionen zurückportierten Fixes ist daher nicht die sichtbare Hauptversion, sondern der vom jeweiligen Betriebssystem-, Hosting- oder Produktanbieter bestätigte Patchstand massgebend. [2] [3] [4]

**Einordnung für KMU:** Inventar mit Betrieb, integrierten Komponenten und externem Hosting abgleichen, Internet-exponierte und geschäftskritische Systeme priorisieren, Hersteller- oder Paketfix einspielen und laufende PHP-Dienste, Worker beziehungsweise Container nach dem Update tatsächlich auf den Fixstand prüfen. Das BACS nennt Übergangsmassnahmen nur als unvollständige Risikoreduktion; sie ersetzen keinen Fix. [1]

**Einschränkung direkt bei der Aussage:** Die geöffneten Originalquellen belegen kritische Schwachstellen und verfügbare Herstellerfixe, nicht aber eine aktive Ausnutzung in einem bestimmten KMU oder pauschal bei allen PHP-Konfigurationen. Für Managed Hosting, Distributionen und Appliances muss der zuständige Hersteller den konkreten Fix bestätigen.

**Vormerkung für Pflege 01.11.2026:**
1. Artikel 08: Prüfen, ob der Risikoregister-Teil einen technologiebezogenen Hinweis auf die Inventarisierung eingebetteter Komponenten und die Fixbestätigung durch Lieferanten benötigt.
2. Artikel 11: Prüfen, ob die Lieferantenabfrage um Nachweise zu sicherheitsgepflegten Web- und Appliance-Komponenten ergänzt werden sollte.
3. Artikel 01 und 07: Nur bei einer konkreten PHP-Betroffenheit prüfen, ob der Hinweis «Patch beseitigt keine allfällige frühere Kompromittierung» als technische Abgrenzung nützlich ist; keine allgemeine Behauptung über einen laufenden Angriff ergänzen.

### 2. BACS Woche 42: Hotelbuchungs-Phishing zielt neu auf TWINT- und E-Banking-Konten

**Publiziert:** 20.10.2026 durch BACS.  
**Original:** BACS-Wochenrückblick [5].

Das BACS berichtet über aktuelle Phishingvarianten im Umfeld von Hotelbuchungen. Nach der Kompromittierung eines Buchungs- oder E-Mail-Systems nutzen Täter laut BACS echte Buchungsdetails, ähnlich benannte Domains und geklonte Hotelwebseiten. Ein vorgetäuschter Cashback soll dazu verleiten, Zugangsdaten und den zweiten Faktor auf gefälschten E-Banking-Seiten preiszugeben; als Ziel nennt das BACS insbesondere die Umschreibung des verknüpften TWINT-Kontos auf eine andere Telefonnummer, daneben auch direkte betrügerische E-Banking-Zahlungen. [5]

**Einordnung für KMU:** Bei vermeintlichen Rückerstattungen oder Kreditkartenverifizierungen den Vorgang ausschliesslich über die bekannte Hotel- oder Buchungs-App, die selbst recherchierte offizielle Webseite oder eine unabhängig recherchierte Telefonnummer prüfen. Codes, QR-Codes sowie Bankzugangsdaten dürfen nicht über einen Link aus der Nachricht eingegeben oder weitergegeben werden. Für geschäftliche Reisen ist dies vor allem ein Sensibilisierungs- und Zahlungsfreigabethema. [5]

**Einschränkung direkt bei der Aussage:** Dies ist ein BACS-Lage- und Präventionshinweis. Er belegt keine Kompromittierung eines bestimmten Hotels, Buchungssystems oder KMU und führt keine neue rechtliche Meldepflicht ein.

**Vormerkung für Pflege 01.11.2026:**
1. Artikel 02: Prüfen, ob das Szenario «Hotelbuchungs-Cashback» als aktuelles Beispiel für kontextbezogenes Phishing und die unabhängige Verifikation von Zahlungsaufforderungen ergänzt werden soll.
2. Artikel 05: Ausschliesslich als Abgrenzung prüfen, ob erklärt werden soll, dass ein zweiter Faktor durch Social Engineering zur Freigabe missbraucht werden kann; keine produkt- oder bankenspezifische Aussage ableiten.

### 3. EDÖB: Formelle Untersuchung nach Cyberangriff auf Softwarelieferant

**Publiziert:** 23.10.2026 durch den EDÖB.  
**Original:** EDÖB-Mitteilung [6].

Nach Angaben des EDÖB meldete die PK Softech AG am 08.10.2026 einen Cyberangriff auf ihre IT-Infrastruktur und mögliche Verletzungen der Datensicherheit. Der EDÖB schreibt, beim Angriff seien Daten mehrerer Vorsorgeeinrichtungen abgezogen worden. Nach einer informellen Vorabklärung bei Publica am 14.10. eröffnete er am 22.10. gegen die Softech AG eine formelle Untersuchung. Diese soll insbesondere die übermittelten Personendaten, die Rechtsgrundlagen und tatsächliche Umsetzung der Datenübertragungen sowie Umfang der abgeflossenen Informationen klären. [6]

**Einordnung für KMU:** Der Fall ist ein Anlass, bei kritischen Software- und Datenlieferanten Verantwortlichkeiten, Datenflüsse, Vertrags- und Sicherheitsnachweise sowie Melde- und Kommunikationswege vor einem Vorfall nachprüfbar zu halten. Die konkrete datenschutzrechtliche Einordnung eines eigenen Vorfalls richtet sich weiterhin nach dessen Umständen und den anwendbaren Regeln.

**Einschränkung direkt bei der Aussage:** Die EDÖB-Mitteilung beschreibt ein hängiges Verfahren. Sie stellt weder eine abschliessende Feststellung einer Datenschutzverletzung noch einen Befund gegen andere Softwarelieferanten dar. Der EDÖB erklärt ausdrücklich, zu hängigen Verfahren zurzeit keine weiteren Auskünfte geben zu können. [6]

**Vormerkung für Pflege 01.11.2026:**
1. Artikel 03: Prüfen, ob die Entscheidungsbaum- und Vorfall-Erhebung ausdrücklich die Daten- und Rollenklärung mit Softwarelieferanten vorsehen soll; keine aus dem hängigen Fall abgeleitete Meldefrist behaupten.
2. Artikel 10: Prüfen, ob die Kommunikationsvorlage bei einem Lieferantenvorfall die Abgrenzung bestätigter Fakten, laufender Abklärungen und offener Datenumfangsfragen hinreichend behandelt.
3. Artikel 11: Prüfen, ob Lieferantenverträge und das Notfallkonzept die Kontaktwege und Nachweispflichten bei Vorfällen eines Datenbearbeiters ausreichend konkretisieren.

## Direkt geprüft, aber nicht als eines von höchstens drei News-Items ausgewählt

Das BACS veröffentlichte am 19.10. eine Technologiebetrachtung mit fünf Sicherheitsklassen für Authentifikationsverfahren. Sie dient laut BACS als praktische Orientierung und ausdrücklich nicht als Grundlage einer formalen Prüfung oder Zertifizierung. Wegen ihres grundsätzlichen Charakters und weil kein konkreter neuer KMU-Handlungsfall dargelegt wird, bleibt sie ausserhalb der Auswahl. [7]

Die BACS-Meldung «KMU Cybersicherheit 2026» vom 22.10. berichtet als Zusammenfassung einer Studie der Mobiliar und verschiedener Partner über technische sowie organisatorische Lücken, etwa bei Schulungen, Inventarisierung, Notfallplänen, Lieferantenprüfung und Restore-Tests. Sie ist für die redaktionelle Priorisierung der Artikelthemen nützlich, begründet aber keine amtliche Pflicht oder neue Vorgabe. Wegen der Drei-Item-Grenze und des dringlicheren PHP-Hinweises wurde sie nicht als eigenes News-Item aufgenommen. [8]

Im Cyber Security Month publizierte das BACS am 23.10. den Workshopbericht «Teilen mit Bedacht». Er richtet sich an Jugendliche sowie ältere Erwachsene und vermittelt insbesondere das Kombinieren öffentlich sichtbarer Informationen, Phishing- und Betrugsszenarien. Die Kampagne wurde direkt geprüft, aber wegen der primären Publikumsorientierung und fehlender neuer spezifischer KMU-Vorgabe nicht ausgewählt. Die vorangegangene KI-am-Arbeitsplatz-Meldung vom 16.10. liegt zudem vor dem Berichtsfenster und ist bereits in der Vorwochenausgabe enthalten. [9] [10]

Der EDÖB veröffentlichte am 22.10. eine rechtskräftige Verfügung gegen die Add Conti GmbH wegen Werbedatenbearbeitung ohne nachgewiesene gültige Einwilligung sowie am 21.10. eine Mitteilung zu zwei Urteilen über ausdrückliche Einwilligung für Stimmabdrücke bei PostFinance. Beide Originalmitteilungen wurden geöffnet. Sie enthalten keine neue Fassung von DSG oder DSV; wegen der Drei-Item-Grenze und ihres engeren Sachbezugs wurden sie nicht als allgemeines KMU-News-Item ausgewählt. [11] [12]

Die statische EDÖB-Jahresübersicht 2026 wurde direkt geprüft und listet für den Berichtszeitraum die Mitteilungen vom 21., 22. und 23.10.; die dynamische EDÖB-Newsübersicht lieferte beim Abruf nur «werden geladen». Die Jahresübersicht ist daher der belastbare amtliche Übersichtsbeleg für die EDÖB-Auswahl dieses Fensters. [13] [14]

Bei Fedlex wurden die geltenden Fassungen und die jeweiligen Änderungsseiten direkt geprüft. Das DSG steht dort als in Kraft mit **Stand am 07.07.2025**, die DSV mit **Stand am 01.12.2025**. Die sichtbaren Listen der geltenden Fassungen und der aktuell berücksichtigten Änderungen weisen keine im Berichtsfenster 18.–25.10.2026 in Kraft getretene neue DSG- oder DSV-Fassung aus. Die Fedlex-Anwendungsnotiz «Version 26.1.19-j – 12.10.2026» betrifft die Suchfunktion der Plattform, nicht den Rechtsstand der beiden Erlasse. Deshalb wird keine Rechtsänderung als News behauptet. [15] [16] [17] [18]

## Öffnungsprotokoll der Originalquellen

Alle folgenden Abrufe erfolgten am 25.10.2026 CET und nach Ende des Berichtsfensters:

- 09:06:46: BACS, Woche 42, publiziert 20.10.2026 – [5].
- 09:06:48 sowie Kontrollabruf 09:08:27: BACS «Im Fokus», Übersicht mit Einträgen vom 19.–23.10.2026 – [19].
- 09:06:49: BACS Medienmitteilungen, Übersicht; jüngster dort sichtbarer Eintrag vom 12.10.2026 – [20].
- 09:06:56: BACS Sensibilisierungskampagnen, CSM-Übersicht mit Einträgen 01., 05., 16. und 23.10.2026 – [10].
- 09:06:56: EDÖB statische Jahresübersicht 2026 mit den Einträgen vom 21., 22. und 23.10.2026 – [13]; zugleich EDÖB dynamische Newsübersicht geöffnet, die nur «werden geladen» zeigte – [14].
- 09:06:58: Fedlex DSV, geltende Fassung Stand 01.12.2025 – [17].
- 09:06:59: Fedlex DSG, geltende Fassung Stand 07.07.2025 – [15].
- 09:07:21: BACS PHP-Warnung, publiziert 21.10.2026 – [1]; BACS KMU-Studienmeldung, publiziert 22.10.2026 – [8]; BACS Technologiebetrachtung, publiziert 19.10.2026 – [7]; BACS CSM-Workshop, publiziert 23.10.2026 – [9].
- 09:07:22: EDÖB-Mitteilungen zum Softech-Verfahren (23.10.), Add Conti (22.10.) und zur Stimmerkennung (21.10.) – [6] [11] [12]; Fedlex-Änderungsseiten für DSG und DSV – [16] [18].
- 09:07:49: PHP-Herstelleradvisories zu CVE-2026-109618 und CVE-2026-109619, beide publiziert 21.10.2026 – [3] [4].
- 09:07:50: PHP-Newsarchiv mit Sicherheitsmeldung und Releases vom 21.10.2026 sowie Informationshinweis vom 23.10.2026 – [2].

## Offene Grenzen

Die Prüfung deckt die vorgegebenen Behördenquellen BACS, EDÖB und Fedlex ab und ergänzt die PHP-Meldung nur mit den direkt erreichbaren Herstellerquellen. Sie kann weder den exakten Seitenstand um 09:00 CET noch nicht indexierte oder nach dem Abruf publizierte Inhalte garantieren. Aus den Quellen ergeben sich keine neue DSG-/DSV-Fassung im Fenster, keine neue allgemeine Meldefrist und keine Aussage zur tatsächlichen Betroffenheit eines konkreten KMU. Für konkrete Patches, Datenpannen, Lieferanten- oder Vertragsverhältnisse ist eine organisations-, produkt- und fallbezogene Prüfung erforderlich.

## Quellen

[1]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen"
[2]: https://www.php.net/archive/2026.php "PHP – News Archive 2026"
[3]: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w "PHP – RCE via OOM corruption"
[4]: https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp "PHP – RCE via stale global state"
[5]: https://www.bacs.admin.ch/de/26w42-de "BACS – Woche 42: Neue Variante von Phishing in Zusammenhang mit Hotelbuchungen zielt auf TWINT-Konten"
[6]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – EDÖB leitete nach Cyberangriff auf Softwarelieferant Abklärungen ein"
[7]: https://www.bacs.admin.ch/de/26-tb-authentifizierung-de "BACS – Technologiebetrachtung: Sicher authentifizieren – Fünf Stufen für mehr Orientierung"
[8]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026: Cyberkriminalität wird zum Geschäftsrisiko für Schweizer KMU"
[9]: https://www.bacs.admin.ch/de/csm26-s4-de "BACS – Cyber Security Month 2026: Workshop Teilen mit Bedacht"
[10]: https://www.bacs.admin.ch/de/sensibilisierung-der-offentlichkeit "BACS – Sensibilisierungskampagnen"
[11]: https://www.edoeb.admin.ch/de/edoeb-verbietet-add-conti-gmbh-die-datenbearbeitung-zu-werbezwecken-und-ordnet-umfassende-loeschung-an "EDÖB – Add Conti GmbH: Verbot der Datenbearbeitung zu Werbezwecken und Löschung"
[12]: https://www.edoeb.admin.ch/de/authentifizierung-mittels-stimmerkennung-bvg-bestaetigt-haltung-edoeb "EDÖB – Authentifizierung mittels Stimmerkennung"
[13]: https://www.edoeb.admin.ch/de/2026-de "EDÖB – Jahresübersicht 2026"
[14]: https://www.edoeb.admin.ch/de/overview/news "EDÖB – Newsübersicht"
[15]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz DSG"
[16]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex – DSG Änderungen"
[17]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz DSV"
[18]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes "Fedlex – DSV Änderungen"
[19]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[20]: https://www.bacs.admin.ch/de/medienmitteilungen "BACS – Medienmitteilungen"
