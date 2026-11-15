# Schweizer Behördennews – 15. November 2026, ISO-KW 46

Im Newsfenster **08.11.2026, 09:00 bis 15.11.2026, 09:00 CET**, Europe/Zurich, sind drei relevante neue BACS-Meldungen durch geöffnete Originalquellen belegt. Die Publikationsdaten liegen innerhalb des Fensters. Alle tatsächlichen Quellenrückgaben erfolgten am 15.11.2026 **nach 09:00 CET**; ein historischer Seitenwortlaut exakt zum Redaktionsschluss ist nicht belegt. Die Auswahl ist begrenzt und kein Vollständigkeitsnachweis.

## 1. Kühl- und Kältesteuerungen: neue öffentliche BACS-Warnung

**Datum:** 10.11.2026. **Fakt:** Das BACS berichtet über in den vergangenen Wochen bekannt gewordene Angriffe in Europa und der Schweiz. Direkt aus dem Internet erreichbare Managementschnittstellen ermöglichen nach einer Kompromittierung Änderungen etwa an Temperaturen, Abtauzyklen und Alarmen. Als Systeme nennt die Behörde die End-of-Life-Produkte Danfoss AK-SM 800 und AK-SC 355, die Familie AK-SM 800A / AK-SM 8xxA mit veralteter Firmware sowie potenziell betroffene Copeland/Dixell-XWEB-Systeme. Neu im Fenster ist die öffentliche BACS-Warnung, nicht nachgewiesen der Angriffsbeginn oder eine neue Patchveröffentlichung.[1]

**Originalbeleg:** https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de – Fetch-Rückgabe am 15.11.2026 um **09:06:11 CET**, vollständig auslesbar. Der Im-Fokus-Überblick bestätigt das Datum; Rückgabe um **09:05:57 CET**, Auszug mit den neuesten Einträgen lesbar.[2]

**Fixumfang:** Das BACS empfiehlt Herstellerupdates für die unterstützte 800A-Familie sowie Abschottung und Ersatz nicht mehr unterstützter Systeme. Es nennt keine genaue Fixversion. Die Veröffentlichung vom 10.11. darf deshalb nicht als Datum eines neuen Firmware-Fixes ausgegeben werden.

Der Herstellerbeleg DSA-2025-08-01 wurde am 15.11.2026 um **09:07:43 CET** geöffnet. Danfoss nennt **4.3.1** als Fix für die älteren, nach Authentifizierung ausnutzbaren CVE-2025-41451 und CVE-2025-41452; der Veröffentlichungseintrag lautet **01.08.2025**. Das ist keine neue Patchveröffentlichung im Newsfenster und kein Nachweis, dass 4.3.1 alle aktuell diskutierten Lücken schliesst.[13] Die Hersteller-Advisoryübersicht, Abruf **09:07:35 CET**, zeigte für AK-SM 800A nur ältere Einträge; daraus folgt kein vollständiger Nichtfund neuer Herstellerinformationen.[14]

Die geöffnete Hersteller-Softwareseite, Abruf **09:07:35 CET**, bezeichnet ein Paket **5.3.x, Oktober 2026** als aktuell. Die dahinter verlinkte Readme, Abruf **09:07:45 CET**, ist hingegen auf Release 5.0.x/5.1.x ausgerichtet und verweist im Downloadlink auf **SM800A-5.1.1.spk**. Dieser Unterschied bleibt ungeklärt. Keine Lizenz wurde bestätigt, kein Paket heruntergeladen oder installiert. **Eine genaue aktuell sichere Buildversion ist dadurch nicht bestätigt.** Die Readme erklärt zudem, dass bei Updates von bereits installierten 4.x-Versionen auf 5.0.x die Sicherheitseinstellungen unverändert bleiben; HTTPS beziehungsweise Strict Mode sind somit zusätzlich konfigurationsbezogen zu prüfen.[15] [16]

**Wichtige ergänzende Unsicherheit vom 12.11.2026:** Das offizielle belgische CCB meldet sechs weitere, vor Authentifizierung ausnutzbare Lücken für AK-SM800A bis einschliesslich **5.3.2**. Laut dieser Mitteilung waren CVE-Nummern noch ausstehend und zum Publikationszeitpunkt keine Patches verfügbar; Firmwareupdate, Passwortwechsel und Strict Mode allein genügen laut CCB nicht für öffentlich exponierte Steuerungen. Der Hinweis wurde am 15.11.2026 um **09:07:43 CET** geöffnet. Er ist keine zusätzliche eigenständige Schweizer News und belegt keine neuen Schweizer Vorfälle, verhindert aber eine pauschale Entwarnung nach einem älteren Update.[17] Es ist hier weder eine spätere neue Patchveröffentlichung noch eine CISA-Katalogaufnahme für diese sechs Lücken belegt. Die CCB-Aussage zum damaligen Patchstand wird nicht ungeprüft als minutengenau bestätigter Herstellerstand vom 15.11. um 09:00 ausgegeben.

Der von BACS verlinkte CERT-FR-Beleg wurde am 15.11.2026 um **09:07:17 CET** geöffnet. Er weist eine Erstfassung vom **12.10.2026** und eine letzte Fassung vom **16.10.2026** aus. Er bleibt Hintergrund zur Exposition und Migration, nicht eine neue Wochenmeldung oder ein neuer Patchbeleg.[18]

**KMU-Relevanz:** Betroffen sein können unter anderem Restaurants, Hotels, Metzgereien, Apotheken, Labors und Lagerbetriebe. Die Warnung betrifft auch durch externe Dienstleister betriebene Kälteanlagen.[1]

**Prüfpunkt:** Inventar, Modell, Firmware und externe Wartungszugänge mit dem zuständigen Anlagen- und IT-Dienstleister abgleichen; direkte und indirekte Internet-Erreichbarkeit sowie Ersatzplanung für End-of-Life-Systeme beurteilen lassen. Dies ist nur allgemeine Orientierung, kein Scan, kein eigener Betroffenheits- oder Kompromittierungsnachweis und keine technische Betriebsfreigabe.

**Unsicherheit:** Keine konkret identifizierten Schweizer KMU, Fallzahlen oder Angriffsdaten sind in der BACS-Meldung genannt. Eine Betriebssanierung oder Integrität nach einem Update ist hier nicht geprüft.

## 2. KI-Fakeshops und Paket-Phishing vor Black Friday

**Datum:** 10.11.2026, BACS-Wochenrückblick 45. **Fakt:** Das BACS verzeichnet in den vergangenen Tagen mehr Meldungen zu Fakeshops und Phishing im Namen von Logistikunternehmen. Die Behörde beschreibt zunehmend KI-generierte, regional angepasste Texte, Produktbilder und Rezensionen sowie kopierte Schweizer Händlerlayouts. Paketnachrichten nutzen angebliche Zollgebühren oder Adressbestätigungen als Köder zum Abgriff von Kreditkartendaten oder für Abofallen.[3]

**Originalbeleg:** https://www.bacs.admin.ch/de/26w45-de – Fetch-Rückgabe am 15.11.2026 um **09:06:10 CET**, vollständig auslesbar. Der Im-Fokus-Überblick führt ebenfalls den 10.11.2026.[2]

**Fixumfang:** Kein Softwarefix, keine CVE und keine Katalogaufnahme. Die neue Wochenmeldung ist eine saisonale Warnung mit Beobachtungen und Präventionsempfehlungen; die Maschen selbst sind nicht neu entstanden.

**KMU-Relevanz:** Einkauf, Empfang und Mitarbeitende mit Bestell- und Lieferbezug können plausibel wirkenden Shop- oder Paketnachrichten begegnen. Dies ist eine allgemeine Prozessrelevanz, keine gemessene Schweizer KMU-Inzidenz.

**Prüfpunkt:** Unbekannte Shops und ungewöhnliche Zahlungswege vor Bestellungen prüfen; Lieferstatus über selbst aufgerufene offizielle Transportseiten beziehungsweise die direkt vom Händler erhaltene Tracking-Nummer nachsehen. Kundenrezensionen sind im KI-Kontext nicht alleiniger Vertrauensnachweis. Keine Links oder Zahlungsaufforderungen aus unerwarteten Nachrichten ungeprüft übernehmen.[3]

**Unsicherheit:** Die Meldung quantifiziert den Anstieg nicht und trennt keine KI-Anteile anhand einer veröffentlichten Messmethode. Ein KMU-Schaden, Kontozugriff oder konkreter Phishing-Fall wurde hier nicht untersucht.

## 3. ESTV-Imitation sammelt persönliche Daten

**Datum:** 09.11.2026. **Fakt:** Das BACS erhält viele Phishing-Meldungen im Namen der Eidgenössischen Steuerverwaltung. Die Köder sind angebliche Rückerstattungen oder eine Systemumstellung. Abgefragt werden unter anderem Geburtsdatum, Telefonnummer und Bankkonto statt der üblichen Passwörter oder Kreditkartendaten. Das BACS vermutet eine Sammlung von Daten für weitere Betrugsversuche; das ist eine behördliche Einschätzung, kein hier nachgewiesener Folgeangriff.[4]

**Originalbeleg:** https://www.bacs.admin.ch/de/warnung-estv-de – Fetch-Rückgabe am 15.11.2026 um **09:06:11 CET**, vollständig auslesbar. Der Im-Fokus-Überblick bestätigt das Publikationsdatum.[2]

**Fixumfang:** Kein Softwarepatch und keine CVE. Es handelt sich um eine neue öffentliche Phishing-Warnung.

**KMU-Relevanz:** Für Administration, Buchhaltung und Empfang eignet sich die Behördenimitation als aktuelles Sensibilisierungsbeispiel. Die BACS-Seite nennt keine nachgewiesene spezifische KMU-Zielgruppe.

**Prüfpunkt:** Unerwartete Steueranfragen über selbst recherchierte offizielle Kontaktwege verifizieren; keine Daten über Links aus der Nachricht eingeben. Das BACS empfiehlt, nicht darauf einzugehen, die Nachricht dem BACS zu melden und zu löschen. Der extrahierte Meldeportal-Link enthält einen Formatfehler; dessen Funktion wurde nicht geprüft und er wird nicht als geprüfter Meldeweg übernommen.[4]

**Unsicherheit:** Keine quantifizierte Kampagnengrösse, keine konkrete Organisation und keine belegten Folgeangriffe in der Quelle. Nicht mit der EHRA-Warnung vom 06.11.2026 verwechseln oder diese neu datieren.

## EDÖB: begrenzter Nichtfund

Die Suche vom 15.11.2026, Rückgabe **09:05:52 CET**, führte zur offiziellen Newsseite. Der Fetch von https://www.edoeb.admin.ch/de/overview/news um **09:05:57 CET** lieferte jedoch nur «werden geladen», keine Mitteilungsliste.[5] Ein gezielter Ersatzabruf der offiziellen Startseite https://www.edoeb.admin.ch/de um **09:06:11 CET** war vollständig auslesbar. Dort ist die jüngste sichtbare Mitteilung weiterhin SkySale vom **06.11.2026**, gefolgt von Bodycams vom 05.11.2026.[6]

In diesem begrenzten Quellenumfang ist **keine neue EDÖB-Mitteilung im Newsfenster belegt**. Die Startseite ist kein vollständiger Archiv- oder Änderungshistoriennachweis. SkySale wird nicht neu aufgenommen; eine neue Entwicklung nach dem 08.11.2026 um 09:00 CET ist hier nicht belegt. Die Vorwochenvormerkung zur getrennten Beurteilung von technischer Behebung und Betroffeneninformation bleibt erhalten; daraus folgt weder eine allgemeine öffentliche Bekanntmachungspflicht noch eine Einzelfallfreigabe.

## Fedlex: keine neue Entwicklung in den geöffneten Chronologien belegt

Die amtlichen Haupteinträge waren über Fetch am 15.11.2026 auslesbar. DSG um **09:06:13 CET**: Stand **07.07.2025**, sichtbare Fassungen 07.07.2025, 01.04.2025 und 01.09.2023.[7] DSV um **09:06:13 CET**: Stand **01.12.2025**, sichtbare Fassungen 01.12.2025, 01.04.2025, 15.09.2024 und 01.09.2023.[8] ISG um **09:06:14 CET**: Stand **01.10.2025**, sichtbare Fassungen 01.10.2025, 01.04.2025, 01.01.2024 und 01.05.2022.[9]

Die amtlichen Chronologien wurden zusätzlich vollständig ausgelesen: DSG und DSV am 15.11.2026 um **09:07:12 CET**, ISG um **09:07:13 CET**. Die jüngste aufgeführte DSG-Berichtigung hat Beschlussdatum 02.07.2025 und Inkrafttreten 07.07.2025; die jüngste DSV-Änderung Beschlussdatum 29.10.2025 und Inkrafttreten 01.12.2025. Beim ISG ist die jüngste Fassung auf 01.10.2025 datiert; die zugehörigen Einträge nennen den Beschluss vom 18.03.2025 beziehungsweise die Änderung vom 29.09.2023.[10] [11] [12]

In den geöffneten Textständen und Chronologien ist **kein neuer Änderungsakt oder neues Inkrafttreten im Newsfenster belegt**. Das ist ein begrenzter Nichtfund in diesen drei amtlichen Einträgen, kein Nachweis, dass im gesamten Bundesrecht oder in allen laufenden Gesetzgebungsverfahren nichts publiziert wurde. Chronologiedaten sind nicht mit einer minutengenauen Seitenänderungshistorie gleichzusetzen.

Diese Stände sind keine neuen Wochenmeldungen. Die bereits in der Wartungsbasis belegte ISG-Fassung vom 01.10.2025 wird nicht als neue Rechtsänderung ausgegeben. Der DSG-Abruf zeigte einen Wartungshinweis für 13.11.2026, 20:00 bis 15.11.2026, 20:00. Das ist keine Gesetzesänderung und erklärt nicht automatisch jeden Abrufunterschied.[7]

## Vormerkungen und unveränderte Sperren

Die BACS-Neumeldungen eignen sich als redaktionelle Vormerkungen für Phishing-Sensibilisierung, Lieferanten-/Fernzugangsrisiken und Inventarisierung. Artikeldateien, Arbeitsmittel und globale Manifeste wurden nicht geändert. Die Heimnetzmeldung vom 03.11.2026 und die EHRA-Warnung vom 06.11.2026 liegen gemäss dem geöffneten Im-Fokus-Überblick ausserhalb des Fensters; keine echte neue Entwicklung dazu ist hier belegt.[2]

Für eine spätere Kühlsteuerungs-Einordnung sind die genaue Hersteller-Fixmatrix zu den sechs vom CCB gemeldeten Lücken, die abweichenden Firmware-/Readmeangaben und ein geschützter Wartungszugang vorzumerken. Kein Wiederanlauf, Factory Reset oder Erhalt der Anlagenintegrität ist durch diesen Recherchelauf freigegeben. Die gezielte Herstellerrecherche vom 15.11.2026 lieferte ihre Suchantwort um **09:07:17 CET**; verwendete Aussagen stammen aus den danach geöffneten Originalen, nicht nur aus Snippets. Die Fedlex-Suchantwort kam um **09:05:59 CET**. Die tatsächlichen verwendeten Fetch-Rückgaben reichen insgesamt von **09:05:57 bis 09:07:45 CET**.

Keine CMS- oder Browseroperation, kein geschützter Hub-Aufruf und keine Zugangsdatenverwendung. Die erreichbaren Quellen und Empfehlungen ersetzen keine Fach-, Rechts-, Forensik-, Tenant- oder Produktprüfung und begründen keine Veröffentlichungserlaubnis. Bestehende Fachmarker aus der Wartungsbasis und dem Laufstatus bleiben unverändert.

## References

[1]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS: Kühl- und Kältesteuerungen, 10. November 2026"
[2]: https://www.bacs.admin.ch/de/im-fokus "BACS: Im Fokus, abgerufen am 15. November 2026"
[3]: https://www.bacs.admin.ch/de/26w45-de "BACS: Woche 45, KI-Fakeshops und Paket-Phishing, 10. November 2026"
[4]: https://www.bacs.admin.ch/de/warnung-estv-de "BACS: Phishing im Namen der ESTV, 9. November 2026"
[5]: https://www.edoeb.admin.ch/de/overview/news "EDÖB: News, dynamische Liste beim Abruf nicht auslesbar"
[6]: https://www.edoeb.admin.ch/de "EDÖB: Startseite mit aktuellen Mitteilungen, abgerufen am 15. November 2026"
[7]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex: DSG, sichtbarer Stand 7. Juli 2025"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex: DSV, sichtbarer Stand 1. Dezember 2025"
[9]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex: ISG, sichtbarer Stand 1. Oktober 2025"
[10]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex: DSG-Chronologie, abgerufen am 15. November 2026"
[11]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex: DSV-Chronologie, abgerufen am 15. November 2026"
[12]: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history "Fedlex: ISG-Chronologie, abgerufen am 15. November 2026"
[13]: https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/ "Danfoss: DSA-2025-08-01, Fix 4.3.1 für zwei ältere Lücken"
[14]: https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/ "Danfoss: Sicherheitsadvisoryübersicht, abgerufen am 15. November 2026"
[15]: https://www.danfoss.com/en-us/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/ "Danfoss: AK-SM 800A Softwareseite, Paketbezeichnung 5.3.x Oktober 2026"
[16]: https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/ "Danfoss: Verlinkte Readme mit abweichendem Downloadlink 5.1.1"
[17]: https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action "CCB: Sechs weitere Danfoss-Lücken, Mitteilung vom 12. November 2026"
[18]: https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/ "CERT-FR: Kühlsteuerungswarnung, letzte Fassung 16. Oktober 2026"
