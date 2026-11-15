---
titel: "DKSchV-Branchennews"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
datum: "18.10.2026"
berichtsfenster: "11.10.2026, 09:00 bis 18.10.2026, 09:00 Europe/Zurich"
recherchehinweis: "Quellenabrufe am 18.10.2026 nach 09:00 Europe/Zurich. Bei nicht versionierten Webseiten ist kein minutengenauer historischer Website-Stand belegt."
zielgruppe: "Schweizer KMU"
---

# DKSchV-Branchennews – Sonntag, 18. Oktober 2026

## Microsoft-Oktoberupdates: aktiv ausgenutzte Windows-Shell-Lücke priorisieren

Microsoft bestätigt für **CVE-2026-96951** eine Ausnutzung vor Verfügbarkeit der Updates und empfiehlt eine möglichst frühe Installation. Das Oktober-Bulletin umfasst neben Windows auch Komponenten aus Office, SharePoint, Exchange Server, SQL Server, .NET, Visual Studio, Dynamics, Azure und System Center. Die aktive Ausnutzung ist in dieser Meldung **nur für CVE-2026-96951** belegt; sie darf nicht pauschal auf alle im Bulletin genannten Schwachstellen übertragen werden. [1]

**Für KMU:** Den MSRC Security Update Guide und die verlinkten KBs gegen die eigene Produkt- und Versionsmatrix prüfen. Windows-Shell-Exposition sowie eingesetzte Exchange-, Office- und SharePoint-Komponenten priorisieren und bekannte Probleme je KB berücksichtigen. Daraus folgt keine Schweizer Rechtsfrist und keine Aussage über die Betroffenheit eines konkreten Tenants. [1]

## PAN-OS: Management-Schnittstelle bei begrenzter Ausnutzung absichern

Palo Alto Networks meldet eine **sehr begrenzte Ausnutzung** von **CVE-2026-0322**, einer authentifizierten Remote-Code-Ausführung im PAN-OS-Managementinterface. CISA nahm die Schwachstelle am 14. Oktober in den KEV-Katalog auf. Betroffen sein können die im Herstellerbulletin genannten PA-Series- und VM-Series-Firewalls sowie Panorama in bestimmten 10.2-, 11.1-, 11.2-, 12.1- und 12.2-Zweigen; Cloud NGFW und Prisma Access sind laut Hersteller nicht betroffen. [2] [3]

**Für KMU:** Plattform und PAN-OS-Zweig inventarisieren, Managementzugriff unverzüglich auf vertrauenswürdige Netze oder einen Jumphost beschränken und den passenden Herstellerfix einplanen. Vor dem Patch Logs und gegebenenfalls erforderliche Forensik prüfen. Die Threat-IDs 510046/510047 decken den Herstellerangaben zufolge nur begrenzt ab und ersetzen kein Update. [2]

## Atlassian Data Center: KEV-Eintrag zu unauthentifiziertem Dateizugriff

CISA nahm **CVE-2026-21589** am 15. Oktober neu in den KEV-Katalog auf. Atlassian beschreibt eine kritische, unauthentifizierte Schwachstelle für beliebigen Dateizugriff in mehreren selbst betriebenen Data-Center-Produkten, darunter Bitbucket, Confluence, Jira, Bamboo, Crowd, Crucible und Fisheye. Cloud-Produkte sind laut Atlassian gepatcht; die Fixstände unterscheiden sich je Produkt und Versionszweig. [4] [3]

**Für KMU:** Bei selbst betriebenen Data-Center-Instanzen Produkt, Version und Internet-Exposition sofort abgleichen und auf den zugehörigen Fixstand aktualisieren. Ist das nicht sofort möglich, Instanzen vom Internet trennen oder die im Originalbulletin beschriebenen produktbezogenen WAF-/Proxy- beziehungsweise Rewrite-Massnahmen prüfen. Workarounds sind kein Ersatz für den Fix; Logs sollten auch auf URL-dekodierte Traversal-Muster geprüft werden. [4]

## BeyondTrust Remote Support: Patchstatus nach Betriebsmodell prüfen

Für **CVE-2026-102764** in BeyondTrust Remote Support nennt das Herstellerbulletin einen Patch für selbst betriebene Appliances. CISA nahm die Schwachstelle am 16. Oktober in den KEV-Katalog auf; damit ist aktive Ausnutzung belegt. Betroffen sind laut Hersteller Versionen bis einschliesslich 26.2.3. SaaS-Kunden wurden laut BeyondTrust bereits am 9. Oktober aktualisiert, während Self-hosted-Kunden den passenden BT26-05-RS-Patch benötigen. [3] [6]

**Für KMU:** Zuerst SaaS oder Self-hosted sowie den tatsächlichen Versionsstand feststellen. Bei Self-hosted den Patch installieren beziehungsweise automatische Aktualisierungen verifizieren; sehr alte Versionen müssen laut Hersteller zunächst auf einen unterstützten Zweig gebracht werden. Bei Verdacht benötigte Logs und Spuren vor einer verändernden Massnahme mit der zuständigen Incident Response sichern; Appliance-Logs auf ungewöhnliche Dateioperationen prüfen. Das Bulletin nennt keinen separaten Hersteller-Workaround; Abschottung darf nicht als gleichwertiger Fix ausgegeben werden. [6]

## Generative KI am Arbeitsplatz: EDÖB und BACS sensibilisieren zu Datenrisiken

EDÖB und BACS haben am 16. Oktober im Cyber Security Month auf Datenschutz- und Informationssicherheitsrisiken generativer KI im Arbeitsalltag hingewiesen. Besonders bei der Eingabe von Personen- und Drittpersonendaten können mehr Informationen preisgegeben werden als beabsichtigt. Der EDÖB hält fest, dass das DSG auf solche Datenbearbeitungen anwendbar ist; das BACS verweist auf ergänzende Hinweise. Die Kampagne führt **keine neue gesetzliche Pflicht und keine neue Frist** ein. [7] [8]

**Für KMU:** KI-Anwendungsfälle, erlaubte Datenkategorien und freigegebene Tools intern klar festlegen. Eingaben mit Personen- oder vertraulichen Unternehmensdaten vorab prüfen und bestehende Datenschutz- sowie Sicherheitsprozesse anwenden. Konkrete Anbieter-, Datenfluss-, Vertrags- und Freigabeentscheide bleiben organisationsbezogen fachlich zu prüfen. [7] [8]

## BACS Woche 41: Schweizer Fassade ist kein ausreichender Shop-Nachweis

Das BACS warnt vor betrügerischen oder fragwürdigen .ch-Shops mit Schweizer Ortsnamen, aber ausländischem Sitz oder Lager, KI-generierten Produktbildern, hohen Rabatten und kostspieligen Rücksendungen nach Asien. Empfohlen werden Prüfungen von Impressum, tatsächlichem Vertragspartner, Rückgaberegeln, Bild-URLs und unabhängigen Erfahrungsberichten. Das BACS grenzt ab: Eine direkte Domain-Sperrung ist nach VID nur bei technischer Bedrohung möglich; irreführende Herkunftsangaben und Dropshipping-Betrug betreffen unter anderem UWG, Strafverfolgung und SECO. [9]

**Für KMU:** Bei unbekannten Shops vor Beschaffungen Vertragspartner, Sitz, Rücksendeort und Zahlungsbedingungen dokumentiert prüfen. Bei finanziellem Schaden die vom BACS genannten Stellen wie SECO und Polizei einbeziehen. Aus der Warnung keine pauschale technische Gefahrenbehauptung oder Domain-Sperrung ableiten. [9]

## Redaktioneller Status

Diese Ausgabe bündelt sechs priorisierte, im Berichtsfenster datierte Meldungen oder Änderungen. Sie ist **keine Vollständigkeitszusage**. Die NIST-/CISA-Hinweise zu freiwilliger Incident Readiness bei Super-Intelligence-Training wurden geprüft, wegen ihres primären Frontier-/Hochrisiko-Kontexts aber nicht als allgemeine KMU-Wochenmeldung priorisiert. Im geprüften EU-Regulierungsfeld wurde keine neue substanzielle Meldung im Zeitfenster aufgenommen.

Die zwölf Artikel und zugehörigen Arbeitsmittel wurden in der turnusmässigen Quellenpflege vom 18. Oktober bearbeitet und bleiben ausnahmslos **Entwürfe beziehungsweise nicht freigegebene Arbeitsvorlagen**. Dieser Newsentwurf behauptet keine CMS-Änderung, keine Authentifizierung und keine Veröffentlichung.

Der aktuelle Webador-Zugriff leitete zur Anmeldeseite um. Alle 24 vorgesehenen Artikel- und Arbeitsmittel-URLs liefern HTTP 404; Fachfreigaben bleiben offen. Die lokale Paketvalidierung meldet **0 Fehler und 0 Warnungen**, ersetzt aber keine Veröffentlichungsfreigabe. [Pflegebericht mit Einzelprotokollen](../reviews/2026-10-18/DKSchV_Pflegebericht_KW42.md).

**Nächste Sonntagsnews:** 25.10.2026. **Nächster gerader ISO-Wochentermin für die turnusmässige Pflege:** 01.11.2026 (KW 44).

## Quellen

[1]: https://www.microsoft.com/en-us/msrc/blog/2026/10/202610-security-update "MSRC – Monatliche Sicherheitsupdates Oktober 2026"
[2]: https://security.paloaltonetworks.com/CVE-2026-0322 "Palo Alto Networks – CVE-2026-0322: PAN-OS authenticated RCE in the Management Interface"
[3]: https://www.cisa.gov/known-exploited-vulnerabilities-catalog "CISA – KEV-Katalog; direkt geprüfter Datensatzstand 16.10.2026"
[4]: https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html "Atlassian – CVE-2026-21589: Arbitrary File Access Vulnerability impacts Multiple Products"
[6]: https://www.beyondtrust.com/trust-center/security-advisories/bt26-05 "BeyondTrust – Security Advisory BT26-05"
[7]: https://www.edoeb.admin.ch/de/csm-generative-ki-arbeitsplatz-datenschutzherausforderungen "EDÖB – Cyber Security Month: Generative KI am Arbeitsplatz: Datenschutzherausforderungen"
[8]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen, 16.10.2026"
[9]: https://www.bacs.admin.ch/de/26w41-de "BACS – Woche 41: Wenn der Bezug zur Schweiz täuscht – Online-Shops mit Rücksendeadressen in Asien, 13.10.2026"
