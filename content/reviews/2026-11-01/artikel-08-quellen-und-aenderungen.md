# Quellen- und Änderungsprüfung – Artikel 08

**Artikel:** IT-Sicherheitscheck für Schweizer KMU: So wird aus Befunden ein priorisiertes Cyber-Risikoregister  
**Arbeitsmittel:** Risikoregister-Vorlage für Cyberrisiken im KMU  
**Prüfdatum:** 1. November 2026, ISO-KW 44  
**Recherchefenster:** neue Meldungen vom 18. Oktober 2026 bis zum Abruf am 1. November 2026; besonders betrachtet: Newsfenster 25. Oktober 2026, 09:00 CET bis 1. November 2026, 09:00 CET, Europe/Zurich.  
**Tatsächliche Recherche und Abrufe:** Suche ab 09:04 CET; direkte Originalabrufe am 1. November 2026 von 09:05 bis 09:07 CET. Das sind Abrufzeitpunkte, keine behaupteten historischen Stände um 09:00.  
**Lokaler Status:** Artikel `Entwurf`; Arbeitsmittel `Arbeitsvorlage – nicht freigegeben`.  
**Bearbeitungsumfang:** Ausschliesslich der Artikel, das Arbeitsmittel und dieser Bericht. Kein CMS, keine Live-Seite, kein Manifest und keine QA- oder globale Datei wurden bearbeitet.

> **Ergebnis:** Alle 13 Quellenreferenzen des Artikels mit 12 unterschiedlichen externen Original-URLs sowie alle 8 Quellenreferenzen des Arbeitsmittels wurden direkt über die Originalquellen abgerufen. Die acht Quellen des Arbeitsmittels sind im Inventar der zwölf Artikelquellen enthalten. Zusätzlich wurden die Fedlex-Chronologien und die amtlichen XML-Fassungen abgerufen. Keine der direkt geprüften Original-URLs lieferte einen Abruffehler. Die geltenden, für die Texte verwendeten Fassungen waren beim Abruf zugänglich: DSG mit letzter Chronologiezeile vom 7. Juli 2025 sowie DSV mit letzter Chronologiezeile vom 1. Dezember 2025. Die technische Zugänglichkeit der Fedlex-Seiten und XML-Fassungen wurde als Zugang zu amtlichem Text bewertet, nicht als Rechts- oder Fachfreigabe.
>
> Zwei begrenzte, dauerhaft verwendbare Ergänzungen waren materiell: erstens die Inventarisierung eingebetteter Komponenten samt Betreiber-Fixbestätigung und überprüfbarem tatsächlichem Lauf- oder Paketstand. Zweitens Kontrollpunkte für KI-abhängige Prozesse und Agenten: Kapazität, Budget- und Warnschwellen, Ausweichablauf, Auftrag, Identität, Werkzeug- und Netzwerkzugriffe sowie menschliche Freigaben bei folgenschweren Handlungen. Die Ergänzungen sind organisationsbezogene Prüfpunkte. Sie behaupten weder Betroffenheit eines bestimmten KMU noch eine Agenten-CVE, eine aktive Ausnutzung oder einen bestimmten Patchstand.

Der `stand` vom **1. November 2026** bezeichnet ausschliesslich die Quellenprüfung. Er ist kein Rechtsstand, keine Fachprüfung und keine Veröffentlichungsfreigabe. Die bestehenden `[FACHPRÜFUNG ERFORDERLICH]`-Marker, Entwurfs- und Nichtfreigabestatus bleiben unverändert.

## Quellenprüfung und Reichweite

Die folgenden Einträge dokumentieren **alle externen Original-URLs**, die als Quellenreferenzen in den zwei nach der Pflege vorliegenden Dateien verwendet werden, sowie die zusätzlichen Original-URLs, die zur rechtlichen Verifikation und zur Neuigkeitsprüfung tatsächlich geöffnet wurden. «Erreichbar» bedeutet nur, dass der Inhalt beim genannten Abruf mit dem stateless Abruf zugänglich war. Bei undatierten Webseiten kann daraus kein minutengenauer, historischer Wortlaut abgeleitet werden.

### Zitierte Originalquellen

1. **BACS, CSRM – Artikel [1], Arbeitsmittel [1].**  
   Original-URL: <https://www.bacs.admin.ch/de/cybersicherheits-und-resilienzmethode-csrm>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die Seite beschreibt die fünf Schritte: wichtige Tätigkeiten und Geschäfts- beziehungsweise Produktionsprozesse; zugehörige Informatikmittel und Informatikschutzobjekte; Schutzbedarf; Sicherheitskonzept; technische und organisatorische Massnahmen. Sie erlaubt ausdrücklich ein prioritätsgesteuertes und iteratives Vorgehen. Das verlinkte CSRM-PDF trägt das Datum 24. November 2025; die Webseite weist auf eine laufende Weiterentwicklung hin, ohne datierte Änderungshistorie. Die Quelle trägt weiterhin die Prozess-, Schutzobjekt- und Priorisierungslogik im Artikel und Arbeitsmittel.[1]

2. **NIST CSRC, Risk Assessment – Artikel [2].**  
   Original-URL: <https://csrc.nist.gov/glossary/term/risk_assessment>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die Glossarseite definiert Risikobewertung unter anderem als systematische Untersuchung, die Entscheidungsträgern laufende Bewertung, Priorisierung und Minderungs- oder Behandlungsstrategien ermöglicht. Eine Seitenversionsnummer oder datierte Änderungshistorie ist nicht ausgewiesen. Sie stützt die allgemeine Einordnung der Risikobewertung, nicht organisationsspezifische Schwellenwerte.[2]

3. **NIST, Cybersecurity Framework 2.0 – Artikel [3].**  
   Original-URL: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** NIST CSWP 29 datiert vom 26. Februar 2024. Die Funktion `Govern` umfasst Organisationskontext, Risiko-Management-Strategie, Rollen, Richtlinien, Aufsicht und Lieferkettenrisiken. Das Framework betont zudem, dass die Ergebnisse keine starre Checkliste und je nach Organisation, Risiko und Risikotoleranz unterschiedlich umzusetzen sind. Die bereits vorhandenen Aussagen zu Führung, Priorisierung und Risikotoleranz bleiben tragfähig.[3]

4. **NIST, CSF 2.0 Small Business Quick-Start Guide – Artikel [4], Arbeitsmittel [3].**  
   Original-URL: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** NIST SP 1300, Februar 2024, ist ein freiwilliger Leitfaden für kleinere Organisationen. Er empfiehlt unter anderem, interne und externe Cyberbedrohungen und Reaktionen in einem Risikoregister zu dokumentieren sowie Hardware, Software, Systeme und Dienste zu inventarisieren. Der Leitfaden ist keine Norm und keine individuelle Anweisung. Er trägt die Register- und Inventarhinweise in beiden Dateien.[4]

5. **Fedlex, DSG – Artikel [5] und [7].**  
   Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/491/de>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Art. 8 verlangt von Verantwortlichem und Auftragsbearbeiter geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit. Art. 24 Abs. 1 verlangt die Meldung einer Verletzung der Datensicherheit an den EDÖB «so rasch als möglich», wenn voraussichtlich ein hohes Risiko für Persönlichkeit oder Grundrechte besteht. Die Artikelstelle wurde zusätzlich mit der Chronologie und amtlichen XML-Fassung geprüft. Sie stützt die begrenzten Aussagen im Artikel, nicht die Beurteilung eines konkreten Meldefalls.[5] [6] [7]

6. **Fedlex, DSV – Artikel [6], Arbeitsmittel [2].**  
   Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/568/de>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die angezeigte amtliche Fassung lautet «Stand am 1. Dezember 2025». Art. 1 nennt Schutzbedarf, Risikoursachen, hauptsächliche Gefahren, ergriffene oder vorgesehene Massnahmen sowie Wahrscheinlichkeit und Schwere einer Datensicherheitsverletzung. Art. 2 nennt Vertraulichkeit, Verfügbarkeit, Integrität und Nachvollziehbarkeit; Art. 3 enthält unter anderem Systemsicherheit und Wiederherstellung. Die Stelle wurde zusätzlich mit Chronologie und amtlicher XML-Fassung geprüft. Die Quelle stützt die begrenzte Datenschutzperspektive, nicht die Angemessenheit konkreter Massnahmen.[8] [9] [10]

7. **BACS, Notfallkonzept – Artikel [8].**  
   Original-URL: <https://www.bacs.admin.ch/de/notfallkonzept>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die Seite beschreibt vier Phasen: Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung. Sie hebt für die Bewältigung klar zugeordnete Verantwortlichkeiten hervor; ein verlinktes KMU-Template trägt das Datum 18. Mai 2026. Die Hauptseite hat keine ausgewiesene Version oder Änderungshistorie. Die Verknüpfung der Top-Risiken mit Notfallplanung bleibt sachlich gedeckt.[11]

8. **BACS, Woche 40 zu Schadsoftwareverdacht – Artikel [9], Arbeitsmittel [4].**  
   Original-URL: <https://www.bacs.admin.ch/de/26w40-de>  
   Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Veröffentlicht am 6. Oktober 2026. Die Meldung stellt klar, dass kein einzelnes Anzeichen für sich allein eine Infektion beweist, und dass mehrere ungewöhnliche Beobachtungen eine nähere Untersuchung auslösen sollen. Sie empfiehlt bei Verdacht eine Untersuchung durch eine Fachperson sowie die Information der zuständigen IT bei geschäftlich verwendeten Geräten. Der bestehende Befundstatus-Hinweis bleibt unverändert belegt.[12]

9. **BACS, PHP-Warnung – neu Artikel [10], Arbeitsmittel [5].**  
   Original-URL: <https://www.bacs.admin.ch/de/warnung-php-de>  
   Abruf: 1. November 2026, 09:06 CET. **Erreichbar, kein Fehler.** Veröffentlicht am 21. Oktober 2026. BACS verlangt, nicht nur Webserver, sondern auch PHP als integrierte Komponente in Verwaltungsoberflächen, Fachanwendungen, Hosting-Plattformen, Containern und Appliances zu prüfen. Es empfiehlt, Produkte, Versionen, Erreichbarkeit und Betreiber zu erfassen, Fixe bei Hosting- und Herstellerprodukten bestätigen zu lassen sowie den tatsächlich laufenden korrigierten Stand zu prüfen. Bei zurückportierten Korrekturen ist die Hauptversion nicht allein ausschlaggebend; ein Update beseitigt keine bereits erfolgte Kompromittierung. Die Quelle begründet die neue, generische Komponenten- und Betreiberkontrolle. Sie belegt keine Betroffenheit in einer konkreten Umgebung.[13]

10. **CISA, Managing AI Token Consumption for Operational Resilience – neu Artikel [11], Arbeitsmittel [6].**  
    Original-URL: <https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience>  
    Abruf: 1. November 2026, 09:06 CET. **Erreichbar, kein Fehler.** Die CISA-Seite ist als externe Veröffentlichung vom 22. Oktober 2026 gekennzeichnet und verweist auf die gemeinsame kanadische Originalorientierung. Sie ordnet unkontrollierten Tokenverbrauch als Risiko für Kosten, Leistung, Zugang zu kritischen Diensten und Verfügbarkeit ein. Sie nennt Priorisierung, effiziente Abläufe, Monitoring und Planung für eingeschränkte Verfügbarkeit. Die Seite ist Orientierung, keine Schweizer Rechtsvorgabe und keine Meldung über einen konkreten Angriff.[14]

11. **Canadian Centre for Cyber Security, Managing AI Token Consumption – neu Artikel [12], Arbeitsmittel [7].**  
    Original-URL: <https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125>  
    Abruf: 1. November 2026, 09:06 CET. **Erreichbar, kein Fehler.** Die Seite trägt «Date modified: 2026-10-22». Sie erläutert steigende oder unvorhersehbare Kosten, verringerte Verfügbarkeit, unzureichende Transparenz, Tokenerschöpfung sowie absichtlich herbeigeführte Verbrauchsspitzen. Sie empfiehlt als mögliche Massnahmen einen governanceübergreifenden Ansatz, Arbeitslastbewertung, Kapazitäts- und Ausweichplanung, Dashboards, Schwellenwerte und Warnungen sowie Budget- und Kapazitätsprognosen. Diese Quelle stützt die neuen Kontrollpunkte nur für KI-abhängige Prozesse und ihre Betriebsresilienz.[15]

12. **Canadian Centre for Cyber Security, Careful adoption of agentic AI – neu Artikel [13], Arbeitsmittel [8].**  
    Original-URL: <https://www.cyber.gc.ca/en/guidance/careful-adoption-agentic-ai>  
    Abruf: 1. November 2026, 09:06 CET. **Erreichbar, kein Fehler.** Die Seite trägt «Date modified: 2026-09-10» und liegt damit zeitlich vor dem betrachteten Neuigkeitszeitraum. Sie wurde als direkt verlinkte fachliche Grundlage der am 22. Oktober publizierten Token-Orientierung erneut geprüft. Sie empfiehlt unter anderem eigene Agentenidentitäten, auf autorisierte Aufgaben begrenzte Rechte, Begrenzung von Werkzeugen und Netzwerken, menschliche Freigaben bei folgenschweren oder schwer rückgängig zu machenden Handlungen, Protokollierung und Überwachung. Daraus wurden ausschliesslich organisationsbezogene Prüfpunkte abgeleitet. Es gibt keine Aussage über eine konkrete Agenten-CVE, eine aktive Ausnutzung oder eine verfügbare Herstellerkorrektur.[16]

### Zusätzlich geöffnete Originalquellen zur Rechts- und Neuigkeitsprüfung

13. **Fedlex-Chronologie DSG.**  
    Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/491/de/history>  
    Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die Chronologie führt als jüngste Zeile eine Berichtigung der Bundeskanzlei vom 2. Juli 2025 mit Inkrafttreten am 7. Juli 2025. Für die verwendeten Artikel 8 und 24 war keine spätere Fassung ausgewiesen. Obwohl die Seite einen JavaScript-Hinweis enthält, lieferte der stateless Abruf die Chronologietabelle; der Nachweis wurde mit der amtlichen XML-Fassung ergänzt.[6]

14. **Amtliche DSG-XML-Fassung.**  
    Original-URL: <https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml>  
    Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die XML-Fassung bestätigt die am 7. Juli 2025 geltende Fassung von Art. 8 und Art. 24. Der maschinenlesbare Zugang wurde als amtliche Volltextquelle verwendet. Ein etwaiger technischer Darstellungsunterschied der Webanwendung wurde deshalb nicht als fehlende Rechtsfassung interpretiert.[7]

15. **Fedlex-Chronologie DSV.**  
    Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/568/de/history>  
    Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die Chronologie weist als jüngste Änderung vom 29. Oktober 2025 ein Inkrafttreten am 1. Dezember 2025 aus. Für die verwendeten Art. 1 bis 3 ist keine spätere Fassung ausgewiesen. Der stateless Abruf lieferte die Chronologie trotz JavaScript-Hinweis; die amtliche XML-Fassung wurde ergänzend geöffnet.[9]

16. **Amtliche DSV-XML-Fassung.**  
    Original-URL: <https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml>  
    Abruf: 1. November 2026, 09:05 CET. **Erreichbar, kein Fehler.** Die XML-Fassung bestätigt die am 1. Dezember 2025 geltende Textfassung der Art. 1 bis 3. Der amtliche Volltext bestätigt insbesondere Schutzbedarf, Risiko, TOM, Wiederherstellung, Systemsicherheit und Nachvollziehbarkeit.[10]

17. **BACS, Im Fokus.**  
    Original-URL: <https://www.bacs.admin.ch/de/im-fokus>  
    Abruf: 1. November 2026, 09:06 CET. **Erreichbar, kein Fehler.** Die beim Abruf sichtbare Übersicht reichte bis zur Woche-43-Meldung vom 27. Oktober 2026. Sie führte die PHP-Warnung und die BACS-Meldung zur KMU-Studie vom 22. Oktober. Die Meldung vom 27. Oktober zu gekaperten WhatsApp-Konten betrifft das allgemeine Phishing- und Kontenschutzthema, liefert aber keine materielle Änderung für den Aufbau dieses Risikoregisters. Eine minutengenaue Vollständigkeit des Seitenverlaufs bis 09:00 ist nicht ableitbar.[17]

18. **BACS, «KMU Cybersicherheit 2026».**  
    Original-URL: <https://www.bacs.admin.ch/de/26-kmustudie-de>  
    Abruf: 1. November 2026, 09:07 CET. **Erreichbar, kein Fehler.** Veröffentlicht am 22. Oktober 2026. Die Mitteilung nennt organisatorische Lücken bei Inventar, Notfallplänen, Sicherheitsaudits, Lieferantenprüfungen und Wiederherstellungstests. Sie bestätigt die redaktionelle Relevanz des vorhandenen Artikels, war aber keine notwendige Grundlage für einen neuen Tatsachen- oder Zahlenabschnitt. Um keine unnötige Wochenmeldung in einen Evergreen-Text einzubauen, wurde sie nicht als neue Artikelquelle aufgenommen.[18]

### Quellenreichweite, Aktualität und rechtliche Einordnung

Die direkte Quellenprüfung deckt **100 % der 13 im Artikel zitierten Referenzen** ab; wegen der Wiederholung des DSG entsprechen sie 12 unterschiedlichen URLs. Sie deckt ebenso **100 % der 8 im Arbeitsmittel zitierten Referenzen** ab. Alle dort verwendeten URLs sind auch im Artikelquelleninventar enthalten. Die zusätzlichen Fedlex-Chronologien und XML-Fassungen wurden nicht als Textreferenzen in den Entwürfen ergänzt, weil sie die bestehende amtliche Quelle methodisch verifizieren und keine zusätzliche Sachbehauptung benötigen.

Die Rechtsaussagen wurden mit den amtlichen Fassungen, Chronologien und XML-Volltexten abgeglichen. Daher wird im Bericht der gesetzliche Quellenstand benannt: DSG letzte Chronologiezeile 7. Juli 2025, DSV letzte Chronologiezeile 1. Dezember 2025. Es wurde **kein** neues Feld `rechtsstand` angelegt, da keines vorhanden war und keine materiell neue Rechtsaussage erforderlich wurde. Die Prüfung ist keine individuelle rechtliche Beurteilung, insbesondere nicht zur DSG-Unterstellung, Rollenverteilung, Angemessenheit von TOM oder konkreten Art.-24-DSG-Meldepflicht.

Der Newszeitraum begann am 25. Oktober um 09:00 CET. Die betrachteten PHP- und CISA-Meldungen vom 21. und 22. Oktober lagen vor diesem Nachrichtenfenster, waren jedoch ausdrücklich als Vormerkungen aus der Vorwoche für die vollständige Quellenpflege seit dem 18. Oktober vorgegeben. Die sichtbare BACS-Übersicht enthielt bis 27. Oktober keine weitere Meldung mit materieller Wirkung auf Artikel 08. Diese Recherche ist keine Vollständigkeitszusage für alle weltweiten Sicherheits- oder Rechtsmeldungen. Insbesondere erlauben unversionierte BACS-, NIST- und CISA-Webseiten keine Garantie des genauen Wortlauts zu einem früheren Stichtag oder um 09:00.

## Änderungen in den lokalen Dateien

### Artikel 08

**Datei:** `/home/ubuntu/dkschv-audit/blog-paket/articles/08-it-sicherheitscheck-kmu.md`

- **Front Matter `stand`**  
  Vorher: `18. Oktober 2026`  
  Nachher: `1. November 2026`  
  Grund: Tatsächliches Datum dieser Quellenprüfung. Der Wert ist ausdrücklich keine Fach-, Rechts- oder Publikationsfreigabe.

- **Front Matter `quellenpruefung_umfang` und `quellenpruefung_status`**  
  Vorher: 9 Artikelreferenzen mit 8 unterschiedlichen Original-URLs und 4 Referenzen des Arbeitsmittels; BACS Im Fokus bis 15. Oktober 2026. Der Status nannte die vollständige Prüfung der bisherigen Quellen und die Nichtprüfung interner geplanter Live-Links.  
  Nachher: 13 Artikelreferenzen mit 12 unterschiedlichen Original-URLs und 8 Referenzen des Arbeitsmittels; direkte Prüfung, Fedlex-Chronologien und amtliche XML-Fassungen sowie einschlägige BACS- und CISA-Originalmeldungen bis 27. Oktober 2026. Der Status nennt vollständig geprüfte externe Quellen sowie die weiterhin nicht als Live-URLs geprüften internen relativen Links.  
  Grund: Der Eintrag bildet den tatsächlich erreichten Umfang ab. Die Reichweite wird nicht über die sichtbare BACS-Übersicht vom 27. Oktober hinaus behauptet.

- **Sichtbarer Standhinweis nach der H1**  
  Vorher: Kein sichtbarer Quellenstand.  
  Nachher: `Stand: 1. November 2026 (Quellenprüfung; keine Fach- oder Rechtsfreigabe)`.  
  Grund: Der sichtbare Text und das Front Matter sind konsistent. Der Hinweis macht den Charakter des Datums transparent.

- **Abschnitt «Zuerst den Geschäftskontext erfassen», nach dem Absatz zu externen Abhängigkeiten**  
  Vorher: Externe Abhängigkeiten wie Cloud-Dienste, Fernwartung, Zahlungsplattformen und Softwarepartner erfassen.  
  Nachher: Zusätzlich eingebettete Komponenten in Produkten und Diensten inventarisieren: Produkt, Komponente, tatsächlicher Lauf- oder Paketstand, Erreichbarkeit und Betreiber. Bei externen Lösungen eine konkrete Betreiber-Fixbestätigung sowie einen überprüfbaren Nachweis des tatsächlich behobenen Stands einfordern; Hauptversionsangaben bei zurückportierten Korrekturen nicht isoliert bewerten.  
  Grund: Die BACS-PHP-Warnung nennt genau diese Komponentenarten und empfiehlt Betreiberklärung, Fixbestätigung und Prüfung der tatsächlich laufenden korrigierten Version.[13]

- **Abschnitt «Zuerst den Geschäftskontext erfassen», neuer Absatz zu KI-abhängigen Prozessen**  
  Vorher: Kein Kontrollpunkt zu Betriebsverbrauch von KI-Diensten.  
  Nachher: Für KI-gestützte Geschäftsprozesse Anbieter, verfügbare Kapazität oder Quote, Budget- und Warnschwellen, Zuständigkeit sowie manuellen oder anderen Ausweichablauf im Risikoszenario festhalten. Der Text begrenzt die Angemessenheit auf Dienst, Vertrag, Prozess und Organisationsrisiko.  
  Grund: CISA und die verlinkte kanadische Orientierung behandeln unkontrollierten Tokenverbrauch als Betriebs-, Kosten- und Verfügbarkeitsrisiko und nennen Priorisierung, Monitoring, Warnschwellen und Ausweichplanung.[14] [15]

- **Abschnitt «Zuerst den Geschäftskontext erfassen», neuer Absatz zu KI-Agenten**  
  Vorher: Kein Kontrollpunkt für Agentenauftrag, Tool- oder Netzwerkzugriff.  
  Nachher: Für eingesetzte KI-Agenten Auftrag, eigene Identität, angebundene Daten und Werkzeuge, erlaubte Netzwerkverbindungen und mögliche externe Wirkungen erfassen. Für folgenschwere oder schwer rückgängig zu machende Handlungen menschliche Freigaben, Protokollierung und eng begrenzte Berechtigungen als risikobasierte Kontrollpunkte vorsehen. Der Absatz erklärt ausdrücklich, dass er keinen konkreten Agenten, keine Schwachstelle und keinen Patchstand behauptet.  
  Grund: Die kanadische Originalorientierung beschreibt Least Privilege, getrennte Agentenidentitäten, Tool- und Netzwerkgrenzen, menschliche Kontrolle sowie Protokollierung als mögliche Schutzmassnahmen.[16]

- **Quellenapparat**  
  Vorher: Quellen [1] bis [9].  
  Nachher: Quellen [10] bis [13] für PHP, CISA-Orientierung zu KI-Tokenverbrauch, deren kanadische Originalorientierung sowie die Orientierung zu agentischer KI ergänzt. Jede neue Quelle hat eine passende numerische Inlinezitierung.  
  Grund: Die Ergänzungen werden direkt belegt; keine Quelle wurde ungenutzt hinzugefügt.

Unverändert blieben `status: Entwurf`, `slug: /wissen/it-sicherheitscheck-kmu`, das ursprüngliche `veröffentlichungsdatum: 19.11.2026`, `fachprüfung_status`, beide bestehenden sichtbaren `[FACHPRÜFUNG ERFORDERLICH]`-Marker, H1, Meta-Title und Meta-Description. Es wurden keine Felder `meta_title_vorschlag` oder `meta_description_vorschlag` ergänzt, weil keine konkrete Quellenkorrektur eine Metadatenänderung begründet. Die Textdatei enthält nach der Aktualisierung 2’479 Wörter und übertrifft damit die Mindestvorgabe von 1’400 Wörtern.

### Zugehöriges Arbeitsmittel

**Datei:** `/home/ubuntu/dkschv-audit/blog-paket/resources/08-risikoregister-vorlage.md`

- **Front Matter `version` und sichtbare Versionszeile**  
  Vorher: `1.2` beziehungsweise `Version: 1.2 | Quellenstand: 18. Oktober 2026`.  
  Nachher: `1.3` beziehungsweise `Version: 1.3 | Quellenstand: 1. November 2026 (Quellenprüfung; keine Fach- oder Rechtsfreigabe)`.  
  Grund: Die Vorlage erhält neue erfassbare Felder und Kontrollpunkte. Front Matter und sichtbare Fassung sind gleichgezogen.

- **Front Matter `stand`, `quellenpruefung_umfang` und `quellenpruefung_status`**  
  Vorher: Stand 18. Oktober 2026, 4 Quellenreferenzen, BACS Im Fokus bis 15. Oktober 2026; vollständiger bisheriger Referenzstatus und nicht geprüfte interne Live-Links.  
  Nachher: Stand 1. November 2026, 8 direkt geprüfte Quellenreferenzen, zusätzliche Fedlex-Chronologien und XML-Fassungen sowie BACS- und CISA-Originalmeldungen bis 27. Oktober 2026; vollständiger externer Quellenstatus und weiterhin nicht geprüfte interne Live-Links.  
  Grund: Der tatsächlich geprüfte Anteil wird vollständig und ohne Live-Behauptung dokumentiert.

- **Neuer Abschnitt «Zusätzliche Kontrollpunkte bei Komponenten und KI» nach «Anwendung»**  
  Vorher: Es gab keine Anleitung für eingebettete Komponenten, KI-Kapazität oder Agentenberechtigungen.  
  Nachher: Drei abgegrenzte Absätze zu Komponenten- und Betreiber-Fixnachweis, KI-Prozess mit Kapazitäts-, Budget-, Quoten- und Ausweichplanung sowie KI-Agent mit Identität, Auftrag, Daten, Werkzeugen, zulässigen Netzwerkverbindungen, möglichen externen Wirkungen und menschlicher Freigabe. Der Schluss stellt klar, dass daraus keine Agentenfreigabe, CVE- oder Patchbehauptung folgt.  
  Grund: Die Absätze setzen die durch BACS, CISA und kanadische Originalorientierungen gestützten organisationsbezogenen Prüfpunkte um.[13] [14] [15] [16]

- **Einzelblatt, Abschnitt «1. Kontext und Evidenz»**  
  Vorher: Felder für Systeme, Daten, Konten oder Dienstleister sowie Evidenz.  
  Nachher: Zusätzliche Felder für `Produkt / Komponente / Lauf- oder Paketstand / Betreiber` und für `Betreiber-Fixbestätigung und überprüfter Nachweis`, jeweils falls einschlägig.  
  Grund: Die generische Komponentenprüfung wird prüf- und nachweisbar, ohne eine konkrete Schwachstelle einzutragen.[13]

- **Einzelblatt, Abschnitt «2. Risikoszenario»**  
  Vorher: Bedrohung, Schwachstelle, Szenario und Geschäftsfolgen.  
  Nachher: Zusätzliche, als «falls einschlägig» gekennzeichnete Zeilen für KI-gestützte Prozesse mit Dienst, kritischer Funktion, Kapazitäts-, Budget- oder Quotenannahme, Warnschwellen, Ausweichablauf und Entscheidkontakt; ferner für KI-Agenten mit Identität, Auftrag, Daten und Werkzeugen, zulässigen Netzwerkverbindungen und möglichen externen Wirkungen.  
  Grund: Budget- und Verfügbarkeitsrisiken sowie Agentenzugriffe können bei passender Organisation als Risiko und nicht als allgemeine Produktbehauptung geführt werden.[15] [16]

- **Kontrollpunkte vor dem Schliessen**  
  Vorher: Acht Kontrollpunkte zu Szenario, Evidenz, Bewertung, Kontrollen, Rollen, Massnahme, Restrisiko, Notfallplanung und Fachprüfung.  
  Nachher: Zusätzlich drei «soweit einschlägig»-Kontrollpunkte zu Betreiberfix und Laufstand, KI-Kapazität/Budget/Warnschwellen/Ausweichablauf sowie KI-Agenten mit Werkzeug- und Netzwerkzugriff sowie menschlicher Freigabe.  
  Grund: Die neuen Felder werden erst beim Schliessen nachgehalten. Sie sind nicht als Pflicht zur Einführung von KI-Agenten formuliert.[13] [15] [16]

- **Quellenapparat**  
  Vorher: Quellen [1] bis [4].  
  Nachher: Quellen [5] bis [8] für BACS-PHP, CISA, kanadische Tokenverbrauchsorientierung und kanadische Agentenorientierung ergänzt. Jede Quelle wird im neuen Abschnitt genutzt.

Unverändert blieben `status: Arbeitsvorlage – nicht freigegeben`, `slug`, `passender_artikel`, `fachprüfung_status`, beide bestehenden sichtbaren `[FACHPRÜFUNG ERFORDERLICH]`-Marker und der bestehende fachliche sowie rechtliche Vorbehalt. Die Vorlage wurde nicht als freigegeben markiert.

## Metadaten, Links und keine Liveänderung

Der Meta-Title und die Meta-Description des Artikels wurden nicht geändert. Es gab keine belegte Korrektur des Suchversprechens; deshalb wurden auch keine Vorschlagsfelder für Metadaten angelegt. Slugs und das ursprüngliche Veröffentlichungsdatum blieben unverändert. Die vorhandenen internen relativen Links wurden erhalten. Sie sind Paket- und Planungswerte; ihre öffentliche Erreichbarkeit wurde nicht als gegeben behauptet und nicht mit CMS oder Browser geprüft.

**Keine Liveänderung:** Es wurde kein CMS geöffnet oder bedient, keine Anmeldung verwendet und keine Veröffentlichung, Änderung oder Synchronisierung einer Live-Seite veranlasst. Dieser Bericht dokumentiert ausschliesslich lokale Dateien. Weder der Quellenstand noch die Versionsnummer 1.3 ist eine Veröffentlichungs- oder Fachfreigabe.

## Verbleibende genaue Blocker

1. **Fachprüfung offen:** Die vorhandenen Fachprüfungsmarker in Artikel und Vorlage bleiben bestehen. Eine zuständige Datenschutz-, Sicherheits- und gegebenenfalls Rechtsfachperson muss die konkrete Verwendung prüfen.
2. **Datenschutz- und Rechtsanwendung offen:** Es fehlen die Tatsachen zu konkreter Datenbearbeitung, Rollen als Verantwortlicher oder Auftragsbearbeiter, Datenkategorien, Schutzbedarf, Verträgen, Auslandbezug und möglicher Verletzung der Datensicherheit. Deshalb kann weder die Angemessenheit von TOM noch eine Art.-24-DSG-Meldung allgemein entschieden werden.
3. **Sektorale und vertragliche Anforderungen offen:** Die betroffene Branche, regulatorischen Anforderungen, Kundenverträge, Versicherungs- und Meldewege sind nicht bekannt. Die allgemeine Registerskala ersetzt keine solche Einzelfallklärung.
4. **Organisationsentscheid offen:** Risikotoleranz, Eskalationsregel, Budget, Verantwortliche, Abnahmekriterien, Restrisikoakzeptanz sowie KI-Nutzungs- und Freigaberegeln müssen die zuständigen Stellen der Organisation festlegen.
5. **Komponenten- und Betreiberstatus offen:** Es wurde keine konkrete Anwendung, Appliance, Hosting-Instanz oder eingebettete PHP-Komponente abgefragt. Eine Betreiber-Fixbestätigung, Paketstandprüfung und Untersuchung von Auffälligkeiten müssen für die jeweilige Umgebung erfolgen. Ein Update beseitigt nicht automatisch mögliche Folgen einer früheren Kompromittierung; konkrete Forensik und Wiederanlauf gehören in zuständige Fachhände.
6. **KI- und Agentenkontext offen:** Kein KI-Dienst, Agent, Tool, Netzwerkzugriff, Budget, Vertrag, Identitätsmodell oder Produktionsprozess wurde geprüft. Die neue Vorlage ist nur ein möglicher Erfassungsrahmen, keine technische oder organisatorische Freigabe.
7. **Historische Webseitenstände beschränkt:** Undatierte oder laufend gepflegte BACS-, NIST- und CISA-Webseiten erlauben keinen garantierten Wortlaut zu früheren Zeitpunkten oder exakt um 09:00. Die rechtlichen Aussagen wurden dagegen mit beim Abruf zugänglichen amtlichen Chronologien und XML-Fassungen gegengeprüft.
8. **Vor Go-live:** Vor einer tatsächlichen Veröffentlichung müssen Fachfreigaben, die dann aktuellen Originalquellen und die öffentlichen Zielseiten der internen Links erneut geprüft werden. Dieser lokale Prüfbericht ersetzt keinen dieser Schritte.

## Referenzen

[1]: https://www.bacs.admin.ch/de/cybersicherheits-und-resilienzmethode-csrm "BACS – Cybersicherheits- und Resilienzmethode CSRM"
[2]: https://csrc.nist.gov/glossary/term/risk_assessment "NIST CSRC – Risk Assessment"
[3]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf "NIST – The Cybersecurity Framework CSF 2.0"
[4]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf "NIST – Cybersecurity Framework 2.0 Small Business Quick-Start Guide"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz DSG"
[6]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG Chronologie"
[7]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – DSG amtliche XML-Fassung vom 7. Juli 2025"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung DSV"
[9]: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history "Fedlex – DSV Chronologie"
[10]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/xml/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-xml-2.xml "Fedlex – DSV amtliche XML-Fassung vom 1. Dezember 2025"
[11]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[12]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40 Schadsoftwareverdacht"
[13]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP"
[14]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA – Managing AI Token Consumption for Operational Resilience"
[15]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI Token Consumption for Operational Resilience"
[16]: https://www.cyber.gc.ca/en/guidance/careful-adoption-agentic-ai "Canadian Centre for Cyber Security – Careful adoption of agentic AI"
[17]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[18]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026"
