# News 01 · BACS, EDÖB und Fedlex · 22. November 2026

Zwei neue BACS-Meldungen sind für Schweizer KMU relevant: personalisiertes Phishing vom **17. November 2026** und die Java4Shell-Warnung vom **18. November 2026**. Neu sind die Behördenpublikationen; die im Phishingbericht beschriebenen Oktoberereignisse werden nicht als neue Datenpanne dieser Woche ausgegeben. Für EDÖB sowie die geprüften DSG-/DSV-/ISG-/CSV-Fassungen ist keine neue artikelrelevante Meldung beziehungsweise Fassung im Newsfenster belegt. Das ist ein begrenzter Recherchebefund, keine Vollständigkeitsgarantie. [1] [2] [5] [8] [9] [10] [11] [12] [13]

**Newsfenster:** 15. November 2026, 09:00 Uhr bis 22. November 2026, 09:00 Uhr CET; Europe/Zurich, ISO-KW 47. **Autor:** Manus AI. Die tatsächlichen Originalrückgaben lagen am 22. November zwischen **09:04:15 und 09:05:33 Uhr CET**, also nach dem Redaktionsschluss. Die Zeiten unten stammen aus den Tool-Rückgaben. Sie garantieren weder den historischen Wortlaut um 09:00 Uhr noch eine minutengenaue Veröffentlichung. Quellen ohne versionierte Historie werden nicht rückdatiert.

Vorwochennews und Pflegemanifest wurden gelesen. Ausgeschlossen sind insbesondere KI-Fakeshops/Paket-Phishing und die Kühlwarnung vom 10. November; auch EHRA-/ESTV-Phishing, SkySale und die BLT-Verfügung sind keine neuen Wochenmeldungen. Die Vollpflege erfolgte am **15. November**; dieser Lauf enthält ausschliesslich News und Vormerkungen für **29. November 2026, KW 48**. Die 24 Inhaltsentwürfe und Manifeste blieben unverändert. Keine Browser-, Login-, CMS-, Meldeportal- oder Liveaktion wurde ausgeführt.

## 1. Sicherheitswarnungen und echte Kundendaten als Phishingköder

**Veröffentlichung:** BACS-Wochenbericht vom 17. November 2026. Ein gesondertes Aktualisierungsdatum oder eine genaue Veröffentlichungszeit ist nicht ausgewiesen. Der neue Bericht beschreibt zwei Muster: Eine angebliche PHP-Sicherheitsaktualisierung führt auf eine Phishingseite für Zugangsdaten zum Administrations-Tool eines Webauftritts. In einem zweiten Beispiel wurden nach einem früheren Datenabfluss personalisierte Kreditkarten-Phishingmails im Namen eines Schweizer Haushaltshilfe-Dienstleisters versendet. [1]

Die Datenabflussinformation stammt nach dem BACS aus **7. Oktober 2026**, die betrügerischen Mails aus **24. Oktober 2026**. Namen, Adressen und AHV-Nummern machten die Nachrichten glaubwürdig; das Ziel waren Kreditkartendaten einschliesslich Sicherheitscode. Der Bericht zeigt den möglichen Folgemissbrauch schon abgeflossener Daten. Er belegt keine neue Datenpanne zwischen 15. und 22. November, keine bezifferte aktuelle Schweizer KMU-Schadenquote und keine neu eingeführte Meldepflicht. Die Verbindung zu früheren Datenabflüssen wird im Einstieg als mutmasslich beschrieben; eine eigene forensische Herkunftsprüfung liegt nicht vor. [1]

**Konkrete KMU-Bedeutung:** Mitarbeitende, Websiteverantwortliche und Zahlungsfreigebende sollten richtige Kundendaten nicht als Echtheitsnachweis behandeln. Sicherheitsupdates sind über offizielle Herstellerkanäle oder etablierte Administrationsprozesse zu beziehen. Dienste werden über bekannte, selbst aufgerufene Adressen geöffnet, nicht über Links aus dringlichen Warnmails. Die technische Behebung eines Datenabflusses und der Schutz vor späterem Betrug sind unterschiedliche Aufgaben. Diese Warnung ergänzt die bereits am 15. November gepflegten Themen BEC und Betroffeneninformation, ohne Rechtsstand oder Fachfreigabe zu erhöhen. [1]

**Vormerkung für 29. November, artikelbezogen:** Bei Artikel 02 `/wissen/ceo-betrug-business-email-compromise` im Schutz- und Verifizierungsabschnitt prüfen, ob «echte Personendaten sind kein Echtheitsnachweis» und der Missbrauch von Sicherheitswarnungen als Aktualisierungsanlass ausreichend abgedeckt sind. Das ist kein Nachweis eines klassischen CEO-Betrugs oder einer Rechnungsmanipulation im geschilderten Fall. Bei Artikel 03 `/wissen/datenpanne-melden-schweiz` und Artikel 10 `/wissen/cyberangriff-kommunikation` den bestehenden Schutzbedarf nach Eindämmung mit dem neuen BACS-Beispiel abgleichen; die Informationsentscheidung bleibt getrennt von der Behördenmeldung. Bei Artikel 01 `/wissen/ransomware-erste-60-minuten` allenfalls nur einen knappen Folgebetrugshinweis prüfen, nicht das Beispiel als Ransomwarefall umdeuten. [1]

**Offene Fragen:** Welche Personen und Daten sind im konkreten KMU-Vorfall betroffen? Welche unabhängigen Kontakt- und Warnkanäle bestehen? Welche Schutzhandlungen sind noch möglich? Der BACS-Bericht identifiziert den Haushaltshilfe-Dienstleister nicht namentlich; eine Namenszuordnung wird nicht spekuliert. Eine automatische neue EDÖB-Meldung oder pauschale öffentliche Bekanntmachung folgt aus diesem Wochenbericht nicht. [1]

## 2. Java4Shell: eingebettete Laufzeiten und Dienstleister mitprüfen

**Veröffentlichung:** Die direkt geöffnete deutsche und englische BACS-Warnung tragen **18. November 2026**. Das abweichende Suchsnippet mit dem 17. November wird nicht als Datumsbeleg übernommen. Oracle nennt für sein November-Advisory die Erstveröffentlichung **17. November 2026, Revision 1**. OpenJDK datiert sein Advisory ebenfalls auf den 17. November und nennt als letzte Aktualisierung **17:44 UTC**. [2] [3] [4] [17]

Laut BACS ermöglicht **CVE-2026-114938, Java4Shell**, unter den erforderlichen Bedingungen die Ausführung von Schadcode über das Netzwerk, teilweise ohne Anmeldung. Betroffen ist die Java-Laufzeit; die konkrete Angreifbarkeit hängt von Java-Version, Prozessor und Datenverarbeitung der Anwendung ab. Das BACS verweist auf Demonstrationen von Calif unter anderem bei zentralen Anmeldediensten und Entwicklungsplattformen. Dies sind Demonstrationen, kein Beleg für erfolgreiche Angriffe auf die jeweiligen KMU-Installationen. Sicherheitsupdates sind verfügbar. [2]

**Konkrete KMU-Bedeutung:** Die Erfassung muss auch Java in Branchenlösungen, Geräten und Containern sowie interne Dienste umfassen. Aus dem Internet erreichbare Anwendungen, zentrale Anmeldedienste und geschäftskritische Systeme haben bei der Prüfung Priorität. Softwareanbieter beziehungsweise IT-Dienstleister sollen Betroffenheit und Behebung je Produkt bestätigen. Nach dem Update sind Prozesse neu zu starten und Container gegebenenfalls neu bereitzustellen; entscheidend ist die tatsächlich laufende korrigierte Java-Version. Ein Sicherheitsupdate beseitigt laut BACS keine bereits erfolgte Kompromittierung. Übergangsmassnahmen sind herstellerbezogen abzustimmen und kein Ersatz für Updates. [2]

**Unsicherheit zu Versionen und Ausnutzung:** Keine pauschale Aussage «alle Java-Versionen sind betroffen» und kein universeller sicherer Build. Die OpenJDK-Matrix markiert diese CVE in den Linien 17, 21, 25 und 27, nicht in 8 und 11. Oracle führt zusätzlich die besondere Ausgabe **8u511b33-perf** sowie mehrere GraalVM-Ausgaben auf. Die im Advisory genannten betroffenen Versionsstände sind nicht automatisch die korrigierten Zielversionen. Diese Unterschiede müssen anhand der tatsächlichen Distribution, Architektur und Lieferantenvorgaben geklärt werden. Die hier geprüften BACS-/Oracle-/OpenJDK-Aussagen belegen keine aktive Ausnutzung in einem bestimmten Schweizer KMU. [2] [3] [4]

**Vormerkung für 29. November, artikelbezogen:** Bei Artikel 08 `/wissen/it-sicherheitscheck-kmu` einen datierten, distributions- und architekturspezifischen Java-Befund prüfen: Produkt, eingebettete Laufzeit, laufender Prozess, betroffener Stand, korrigierter Herstellerstand, Exposition und Behebungsnachweis. Bei Artikel 11 `/wissen/lieferantenrisiken-cybersecurity` Nachweise externer Betreiber und Verantwortung für eingebettete Java-Komponenten ergänzungsweise prüfen. Bei Artikel 07 `/wissen/backup-wiederherstellung-testen` kontrollieren, ob wiederhergestellte Images/Container vor Wiederanlauf einen verifizierten korrigierten Laufzeitstand erhalten und kompromittierte Zustände nicht als saubere Wiederherstellung gelten. Keine automatische Produktivfreigabe aus einem Paketdownload ableiten. [2]

**Offene Fragen:** Welche Anwendungen, Container und Geräte enthalten Java? Welche Distribution und Prozessorarchitektur laufen tatsächlich? Welche Herstellerupdates sind für das konkrete Produkt freigegeben? Wurden Prozesse nachweisbar umgestellt? Ist eine bereits erfolgte Kompromittierung auszuschliessen oder fachlich zu untersuchen? Für Artikel 01 bleibt der reale Vorfallumfang, für Artikel 03 und 10 die separate Datenpannen- und Kommunikationsbeurteilung offen; die Schwachstellenwarnung allein löst keine pauschale DSG-/ISG-Meldung aus. [2]

## EDÖB und Fedlex: kein zusätzlicher Newsartikel, Zugangsgrenzen offen

Die deutsche EDÖB-Mitteilungsübersicht und die englische Newsübersicht beginnen mit der SkySale-Mitteilung vom **6. November** und dem BLT-Update vom **5. November**. Daraus wird keine Neuigkeit für das aktuelle Fenster gemacht. Die Medienübersicht lieferte trotz Publisher-Parameter eine allgemeine Bundesnews-Liste mit «Alle Organisationen» und 2'889 Ergebnissen. Sie ist deshalb **kein belastbarer vollständig gefilterter EDÖB-Nichtfundnachweis**. Es wird nur festgehalten, dass in den gezielt geprüften Mitteilungen keine neue passende Meldung belegt ist. [5] [6] [19]

Fedlex zeigt weiterhin **DSG Stand 7. Juli 2025**, **DSV Stand 1. Dezember 2025**, **ISG Stand 1. Oktober 2025** und **CSV Stand 1. April 2025**. Die heute lesbaren DSG-/DSV-Änderungslisten nennen keine neue Novemberänderung. Ihr Hinweis begrenzt die Listen auf Änderungen, die zurzeit in Kraft sind; geplante oder noch nicht wirksame Änderungen sind damit nicht vollständig ausgeschlossen. Die Websiteversionsanzeige «19.11.2026» bezeichnet die Fedlex-Anwendung, nicht den Erlassstand. [8] [9] [10] [11] [12] [13]

Der Bundesblatt-Novemberindex lieferte Einträge bis **18. November**. Die darin sichtbare Vorprüfung einer Volksinitiative zur digitalen Identität vom 17. November ist kein in Kraft gesetztes Datenschutzrecht und kein direkter Anpassungsgrund für die zwölf Artikel. Die Amtliche Sammlung im November war dagegen nicht inhaltlich auslesbar: lediglich 1'205 Zeichen Javascript-Hinweis. Somit bleibt eine vollständige Sichtung neuer AS-Publikationen, insbesondere auch vom 19. bis 22. November, offen. Unterschiedliche Fedlex-Anwendungsstände und alte Wartungshinweise in einzelnen Rückgaben werden nicht als technisch erklärte Ursache ausgegeben. [7] [12] [13] [16]

**Vormerkung für 29. November:** Bei Artikel 03 den historischen DSG-/DSV-Änderungsseiten-Leseblocker vom 15. November anhand der heute benutzbaren Listen neu bewerten, aber erst während der Vollpflege die betreffenden Prüfmetadaten ändern. Auch Artikel 01, 06 `/wissen/microsoft-365-sicherheit-kmu`, 08, 09 `/wissen/schatten-ki-kmu`, 10, 11 und 12 `/wissen/nis2-dora-schweiz` behalten ihre bisherigen Fachmarker. Die heute geprüften Fassungen tragen keinen neuen allgemeinen Rechtsänderungsabsatz. Bei Artikel 12 die bestehende Oktober-2025-ISG-Fassung erhalten, sofern die Vollpflege keinen neuen amtlichen Stand ergibt. AS-Index und verlässlich gefilterte EDÖB-Medienmeldungen beim nächsten Turnus erneut prüfen. [8] [9] [10] [11] [12] [13] [16]

## Quellenbelege und tatsächliche Rückgaben

Die folgenden kurzen Belege sind aus den geöffneten Originalen, keine Suchsnippets. Die Angaben «success» und «partial» bezeichnen den Extraktionsstatus, keinen unabhängigen HTTP-, Portal- oder Funktionsnachweis.

**[1], 09:04:25 Uhr, success:** Deutscher BACS-Wochenbericht, «Veröffentlicht am 17. November 2026». Quellenbeleg: «Korrekte Namen, Adressen oder andere persönliche Angaben sind daher kein verlässlicher Echtheitsnachweis.» Inhalt und beide Oktoberdaten wurden vollständig gelesen. Die englische Fassung [18] kam um 09:04:15 Uhr mit übereinstimmendem Publikationsdatum zurück.

**[2], 09:04:25 Uhr, success:** Deutsche Java-Warnung, «Veröffentlicht am 18. November 2026». Quellenbeleg: «Ein Sicherheits-Update beseitigt keine bereits erfolgte Kompromittierung.» Betroffenheitsgrenzen, eingebettete Komponenten, Neustart und Container wurden gelesen. Die englische Fassung [17] kam um 09:04:15 Uhr mit demselben Datum zurück.

**[3], 09:04:26 Uhr, partial; gezielte Matrixrückgabe 09:05:33 Uhr, success:** Oracle-November-Advisory. Erstveröffentlichung in der Modification History: 17. November 2026, Revision 1. Die zweite Extraktion lieferte die CVE-2026-114938-Zeile mit Compilerkomponente, CVSS 8.1, hoher Angriffskomplexität und betroffenen produktspezifischen Ausgaben. Keine Hersteller-Loginseiten geöffnet. Vollständige erste Extraktion liegt zusätzlich in `news01-quellen/oracle-november.md`.

**[4], 09:04:50 Uhr, success:** OpenJDK-Advisory. Quellenbeleg: «Last update: 2026/11/17 17:44 UTC». CVE-spezifische Matrix gelesen; die pauschale Einleitung über alle in diesem Advisory behobenen Lücken wird nicht auf Java4Shell allein übertragen.

**[5], 09:04:50 Uhr, partial:** Deutsche EDÖB-Mitteilungen. Der aktuelle 2026-Abschnitt mit neuesten Einträgen vom 6./5. November ist lesbar. Vollständige Extraktion zusätzlich in `news01-quellen/edoeb-mitteilungen.md`. **[19], 09:04:15 Uhr, partial:** Englische Übersicht mit denselben neuesten Einträgen.

**[6], 09:04:51 Uhr, success:** EDÖB-Medienübersicht; allgemeine Liste statt belastbar gefilterter Behördensicht. Der negative EDÖB-Newsbefund wird entsprechend begrenzt. **[20], 09:04:25 Uhr, success:** EDÖB-Einstieg «Aktuell» mit Links zu Mitteilungen und Medienmeldungen.

**[7], 09:04:50 Uhr, success:** Bundesblatt-Novemberindex, gelieferter letzter Eintrag 18. November. Keine Garantie für vollständig aktuelle Monatsabdeckung.

**[8], 09:04:16 Uhr, partial:** DSG-Normseite mit Fassungen und Stand 7. Juli 2025; vollständige Extraktion zusätzlich in `news01-quellen/fedlex-dsg.md`. **[9], 09:04:26 Uhr, success:** DSG-Änderungsliste tatsächlich lesbar, nur geltende Änderungen. **[10], 09:05:08 Uhr, success:** DSV-Chronologie, neueste Fassung 1. Dezember 2025. **[11], 09:05:31 Uhr, success:** DSV-Änderungsliste tatsächlich lesbar, letzte genannte Änderung vom 29. Oktober 2025. **[12] und [13], jeweils 09:05:08 Uhr, success:** ISG- und CSV-Chronologien mit oben genannten Fassungsständen.

**[14], 09:04:15 Uhr, partial:** Deutsche BACS-Übersicht lieferte als neueste Einträge nur 10. November; sie wird nicht gegen die erfolgreich gelesenen neuen Einzelmeldungen als Vollständigkeitsbeweis verwendet. Extraktion zusätzlich in `news01-quellen/bacs-im-fokus.md`. **[15], 09:05:15 Uhr, error:** Ergänzender englischer Übersichtsabruf lieferte keinen extrahierten Inhalt. **[16], 09:05:16 Uhr, nominell success, inhaltlich blockiert:** AS-Novemberindex lieferte nur Javascript-Hinweis. Kein Browserersatz und keine Wiederholungsschleife.

Die Suchantworten kamen um **09:04:10 Uhr** sowie bei der gezielten Fedlex-Nachsuche um **09:04:28 Uhr CET** zurück. Relevante Originale wurden mit fetch geöffnet. Nicht verwendete Drittquellensnippets begründen keine Sachbehauptung. Dieses Newsjournal ist keine erneute Vollpflege aller Quellen der zwölf Artikel.

## References

[1]: https://www.bacs.admin.ch/de/26w46-de "BACS: Woche 46 – Personalisiertes Phishing aufgrund von abgeflossenen Daten, 17. November 2026"
[2]: https://www.bacs.admin.ch/de/warnung-java-2-de "BACS: Java4Shell – Kritische Schwachstelle in Java, 18. November 2026"
[3]: https://www.oracle.com/security-alerts/cspunov2026.html "Oracle: Critical Security Patch Update Advisory – November 2026"
[4]: https://openjdk.org/groups/vulnerability/advisories/2026-11-17 "OpenJDK: Vulnerability Advisory vom 17. November 2026"
[5]: https://www.edoeb.admin.ch/de/mitteilungen "EDÖB: Mitteilungen, aktuelle deutsche Übersicht"
[6]: https://www.edoeb.admin.ch/de/newnsb?publisherIDs=334&topicIDs=all&newsCategoryIDs=all&sort=dateDecreasing&display=list&start_date=2023-01-01 "EDÖB: Medienübersicht, Rückgabe mit allgemeiner Bundesnews-Liste"
[7]: https://www.fedlex.admin.ch/de/fga/index/2026/11 "Fedlex: Bundesblatt vom November 2026"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex: Datenschutzgesetz, Stand 7. Juli 2025"
[9]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex: Datenschutzgesetz, geltende Änderungen"
[10]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex: Datenschutzverordnung, Chronologie"
[11]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/changes "Fedlex: Datenschutzverordnung, geltende Änderungen"
[12]: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history "Fedlex: Informationssicherheitsgesetz, Chronologie"
[13]: https://www.fedlex.admin.ch/eli/cc/2025/169/de/history "Fedlex: Cybersicherheitsverordnung, Chronologie"
[14]: https://www.bacs.admin.ch/de/im-fokus "BACS: Im Fokus, deutsche Übersicht mit älterem sichtbarem Newsbestand"
[15]: https://www.bacs.admin.ch/en/in-focus "BACS: Ergänzender englischer Übersichtsabruf ohne extrahierten Inhalt"
[16]: https://www.fedlex.admin.ch/de/oc/index/2026/11 "Fedlex: Amtliche Sammlung November 2026, inhaltlich blockierter Abruf"
[17]: https://www.bacs.admin.ch/en/warnung-java-2-en "BACS: Java4Shell, englische Originalfassung vom 18. November 2026"
[18]: https://www.bacs.admin.ch/en/26w46-en "BACS: Personalised phishing attacks using leaked data, 17. November 2026"
[19]: https://www.edoeb.admin.ch/en/latest-news "EDÖB: Latest news, englische Übersicht"
[20]: https://www.edoeb.admin.ch/de/aktuell "EDÖB: Aktuell, Einstieg zu Mitteilungen und Medienmeldungen"
