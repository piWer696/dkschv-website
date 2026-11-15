---
titel: "DKSchV-Branchennews"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
datum: "25.10.2026"
berichtsfenster: "18.10.2026, 09:00 CEST bis 25.10.2026, 09:00 CET Europe/Zurich"
abrufstand: "25.10.2026 nach 09:00 CET; recherchierte Originalquellen ca. 09:06–09:08 CET"
zielgruppe: "Schweizer KMU"
---

# DKSchV-Branchennews – Sonntag, 25. Oktober 2026

## PHP: kritische Schwachstellen auch in eingebetteten Komponenten prüfen

Das BACS warnt am 21. Oktober vor **CVE-2026-109618 und CVE-2026-109619**, die auf betroffenen Servern nicht authentisierte Schadcodeausführung ermöglichen können. Korrigierte PHP-Releases sind laut BACS und PHP **8.5.12, 8.4.27, 8.3.36 und 8.2.35**. Zu prüfen sind nicht nur eigene Webserver, sondern auch PHP-Komponenten in Fachanwendungen, Appliances und Hosting-Angeboten. Die Meldung belegt verfügbare Fixe, keine pauschale Betroffenheit oder aktive Ausnutzung bei einem bestimmten KMU. [1] [2]

**Für KMU:** Betreiber und Lieferanten nach dem konkreten Fixnachweis fragen und den tatsächlich laufenden Stand nach der Aktualisierung verifizieren. Bei Distributionen mit zurückportierten Sicherheitskorrekturen ist die bestätigte Paketversion des Anbieters entscheidend, nicht allein die angezeigte PHP-Hauptversion. [1] [2]

## Microsoft 365: kompromittierte ConnectWise-Anwendungen als Zugangspfad

Microsoft berichtet am 21. Oktober über Storm-0940: Der Akteur nutzte übernommene Identitäten mehrerer ConnectWise-Cloudanwendungen, um über bereits berechtigte Anwendungen auf Microsoft-365-Umgebungen zuzugreifen. Beobachtet wurden unter anderem Verzeichniserkundung und Änderungen an Anwendungsanmeldeinformationen. Microsoft ordnet dies **nicht als Schwachstelle oder Kompromittierung von Microsoft-Produkten** ein. Eine betroffene Anwendung oder erfolgreiche Anmeldung allein beweist weder Datenzugriff noch Datenabfluss. [3]

**Für KMU:** Falls eine der im Originalbericht konkret gelisteten ConnectWise-Anwendungen aktuell oder früher autorisiert war, die zuständige IT-/Incident-Response-Fachstelle einbeziehen. Microsoft empfiehlt für genau diese Anwendungen die Prüfung der Application IDs, Beweissicherung vor irreversiblen Änderungen sowie die Untersuchung von Dienstprinzipal- und Auditaktivitäten. Die Empfehlung, betroffene Anbindungen bis zu formellen Wiederherstellungsanweisungen deaktiviert zu halten, gilt nicht pauschal für jedes ConnectWise-Produkt. Es wurde kein DKSchV- oder Kundentenant geprüft. [3]

## Neue CISA-KEV-Einträge: Betriebsmodell und Herstellerfix abgleichen

Der direkt geprüfte CISA-Katalog führt diese neu aufgenommenen, aktiv ausgenutzten Schwachstellen. Die Angaben sind produktbezogen; eine Aufnahme beweist keinen Angriff auf die eigene Installation. US-Bundesfristen begründen keine Schweizer Rechtsfrist. [4]

- **Plex Media Server:** Am 20. Oktober wurden CVE-2026-96652, -96654, -96655 und -96656 aufgenommen. Laut Plex können die vier Lücken verkettet nicht authentisierte Codeausführung ermöglichen; **1.43.3.10861 und neuer** ist nicht betroffen. Ältere, internet-erreichbare Installationen benötigen neben dem Update eine fachliche Prüfung möglicher Kompromittierung. Für Managed-Betrieb ist der Fixstand beim Betreiber abzuklären. [4] [5]
- **Arista VeloCloud Orchestrator On-Prem:** CVE-2026-114625 wurde am 23. Oktober aufgenommen. Arista bestätigt eine Rechteausweitung für bereits authentifizierte Nutzer. Betroffene Zweige benötigen mindestens **5.2.3.18, 6.1.3.10 beziehungsweise 6.4.2.12**. Hosted-/Dedicated-Angebote sind laut Arista gepatcht; Drittbetreiber müssen dies für die konkrete Instanz bestätigen. Eine Beschränkung des Administrationszugriffs ist kein Ersatz für den Fix. [4] [6]
- **Nextcloud mit `richdocumentscode`:** CVE-2026-110447 wurde am 23. Oktober aufgenommen. Die Command Injection betrifft die Built-in-CODE-App vor **26.4.303**, wenn der eingebaute CODE-Server nicht läuft. App aktualisieren oder entfernen; blosses Deaktivieren reicht laut Advisory nicht. Standalone-Collabora-Online-Server sind nicht betroffen. Bei Managed-Nextcloud App-Einsatz und Patchstatus erfragen. [4] [7]

## Hotelbuchungs-Phishing: richtige Reisedaten sind kein Vertrauensbeweis

Im Wochenrückblick vom 20. Oktober beschreibt das BACS Phishing mit echten Buchungsdetails, nachgeahmten Hotelwebseiten und vorgetäuschtem Cashback. Die Angreifer versuchen, E-Banking-Zugangsdaten und die Freigabe eines zweiten Faktors zu erhalten; betroffen sein kann auch die Verknüpfung eines TWINT-Kontos. Die Meldung belegt keine Kompromittierung eines bestimmten Hotels oder KMU. [8]

**Für KMU:** Reisende und Zahlungsfreigabestellen sensibilisieren. Rückerstattungs- oder Verifizierungsaufforderungen über eine bekannte App oder unabhängig ermittelte Kontaktdaten prüfen, nicht über den Nachrichtlink. Bei bereits offengelegten Zahlungsdaten umgehend das Finanzinstitut beziehungsweise den Kartenanbieter kontaktieren. [8]

## EDÖB: Untersuchung nach Angriff auf Softwarelieferant

Der EDÖB teilte am 23. Oktober mit, dass er nach dem Cyberangriff auf die PK Softech AG eine formelle Untersuchung eröffnet hat. Nach seinen Angaben wurden Daten mehrerer Vorsorgeeinrichtungen abgezogen. Geklärt werden sollen unter anderem übermittelte Personendaten, Rechtsgrundlagen, tatsächliche Datenübertragungen und der Umfang abgeflossener Informationen. **Das Verfahren ist hängig; es liegt keine abschliessende Feststellung eines Datenschutzverstosses vor.** [9]

**Für KMU:** Der Fall ist Anlass, kritische Software-/Datenbearbeiterbeziehungen zu prüfen: Datenflüsse, Rollen, Verträge, Sicherheitsnachweise und erreichbare Vorfallkontakte müssen nachvollziehbar sein. Aus dem Einzelfall folgen keine pauschale neue Meldefrist und kein Befund gegen andere Lieferanten. Eigene Vorfälle bleiben konkret datenschutzrechtlich zu beurteilen.

## KI-Workflows: Tokenverbrauch ist auch ein Betriebsrisiko

CISA verweist seit dem 22. Oktober auf die gemeinsame Behördenorientierung **«Managing AI Token Consumption for Operational Resilience»**. Die verlinkte kanadische Originalpublikation beschreibt, wie lange Eingaben, Connector-Daten und mehrstufige Agentenabläufe unerwartete Kosten oder Verbrauchslimits verursachen können. Auch absichtlich herbeigeführte Verbrauchsspitzen können Kosten und Verfügbarkeit beeinträchtigen. Dies ist freiwillige Orientierung für Organisationen jeder Grösse, **kein Bericht über einen konkreten Angriff und keine Schweizer Rechtsvorgabe**. [10] [11]

**Für KMU:** Bei freigegebenen KI-Anwendungen Verbrauch überwachen, angemessene Budgets und Warnungen festlegen und für kritische Prozesse Ausweichabläufe vorsehen. Anbieterlimits und Verträge konkret prüfen. Kostenkontrollen ersetzen weder Datenminimierung noch die Prüfung von Toolrechten, Personendaten und zulässigen Eingaben. [10] [11]

## Laufstatus

**KW 43 ist ungerade:** Heute keine vollständige turnusmässige Artikelpflege. Der letzte Quellenpflegestand der zwölf Artikel und zwölf Arbeitsmittel bleibt **18.10.2026**; ihre Dateien sind unverändert. Der heutige Paketvalidator meldet **0 Fehler und 0 Warnungen**, keine Fachfreigabe.

**Live-Synchronisierung blockiert:** Der aktuelle Sandbox-Webador-Zugriff zeigt die Anmeldung. Alle 24 vorgesehenen Artikel-/Arbeitsmittel-URLs liefern HTTP 404; Fachprüfungsmarker bleiben offen. Nichts wurde veröffentlicht oder live geändert. Genaue Blocker und Vormerkungen stehen im [Laufstatus](2026-10-25_DKSchV_Laufstatus.md).

**Nächste News und vollständige Blogpflege:** 01.11.2026, KW 44. Originalquellen wurden nach 09:00 CET abgerufen; die Auswahl ist keine Vollständigkeitszusage und belegt keinen minutengenauen historischen Website-Wortlaut.

## Quellen

[1]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21.10.2026"
[2]: https://www.php.net/archive/2026.php "PHP – Herstellerarchiv mit Sicherheitsreleases vom 21.10.2026"
[3]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise, 21.10.2026"
[4]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – KEV-JSON-Katalog, geprüfter Stand 23.10.2026"
[5]: https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319 "Plex – Important Security Update for Plex Media Server v1.43.2 and earlier"
[6]: https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199 "Arista – Security Advisory 0199, 22.10.2026"
[7]: https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh "Collabora Online – richdocumentscode Command Injection, GHSA-g3vx-3m76-fghh"
[8]: https://www.bacs.admin.ch/de/26w42-de "BACS – Woche 42: Hotelbuchungs-Phishing zielt auf TWINT-Konten, 20.10.2026"
[9]: https://www.edoeb.admin.ch/de/edoeb-leitete-nach-cyberangriff-auf-softwarelieferant-abklaerungen-ein "EDÖB – Abklärungen nach Cyberangriff auf Softwarelieferant, 23.10.2026"
[10]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA – Managing AI Token Consumption for Operational Resilience, 22.10.2026"
[11]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience"
