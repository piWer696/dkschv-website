---
thema: "Microsoft-Sicherheit und Identitäten"
datum: "25.10.2026"
iso_woche: "KW 43"
berichtsfenster: "18.10.2026, 09:00 CEST bis 25.10.2026, 09:00 CET, Europe/Zurich"
abrufstand: "25.10.2026, 09:06–09:08 CET (nach der Zeitumstellung)"
zielgruppe: "Schweizer KMU"
---

# Quellenbefund – Microsoft-Sicherheit und Identitäten

## Ausgewählte Meldungen

### 1. Storm-0940: Microsoft meldet Missbrauch kompromittierter ConnectWise-Anwendungen in Microsoft-365-Tenants

**Publiziert:** 21.10.2026. **Herstellerquelle:** Microsoft Security Blog, *AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise*.[1]

Microsoft schreibt, dass Storm-0940 nach der Übernahme von Identitäten mehrerer ConnectWise-Cloudanwendungen über bereits berechtigte Anwendungen auf Microsoft-365-Kundenumgebungen zugriff. Microsoft beobachtete in mehreren Umgebungen anschliessende Microsoft-Graph- und Verzeichnisaktivitäten, darunter Erkundung, Änderungen an Anmeldeinformationen von Anwendungen sowie versuchte Berechtigungsänderungen. Die Aktivität beruhe laut Microsoft **nicht** auf einer Kompromittierung oder Schwachstelle in Microsoft-Produkten oder -Diensten.[1]

Für möglicherweise betroffene Umgebungen verlangt Microsoft unter anderem, die betroffenen ConnectWise-Anwendungsanbindungen bis zu formellen Wiederherstellungsanweisungen des Anbieters deaktiviert zu halten, die vier im Beitrag aufgeführten Application IDs (nicht nur Anzeigenamen) in aktuellen und früher autorisierten Tenants zu inventarisieren, und Beweise vor irreversiblen Änderungen zu sichern. Zu prüfen sind insbesondere erfolgreiche und fehlgeschlagene Dienstprinzipal-Anmeldungen sowie Entra-Auditdaten zu Anmeldeinformationen, Berechtigungen, Owners, Zustimmungen und privilegierten Rollen. Microsoft nennt zusätzlich Microsoft-365-Audits für ungewöhnlichen Mail- oder Dateizugriff, Downloads, Weiterleitungen, Postfach- oder Transportregeln und delegierte Berechtigungen.[1] Die verlinkte Entra-Leitlinie bestätigt, dass Anwendungs- und Dienstprinzipal-Änderungen in Entra-Auditprotokollen zu überwachen sind; die Purview-Referenz erläutert den Umfang von Microsoft-365-Aktivitäten und weist auf Retentions- und Erfassungsgrenzen hin.[2] [3]

**Einschränkung unmittelbar neben dem Befund:** Das Vorhandensein einer betroffenen Anwendung oder eine erfolgreiche Anmeldung belegt laut Microsoft weder Datenzugriff noch Datenabfluss. Diese Recherche hat keine Tenant-, App-ID-, Log- oder Lizenzprüfung durchgeführt; ob ein einzelnes KMU betroffen ist, bleibt offen. Die Herstelleranweisung, die Anbindung deaktiviert zu lassen, bezieht sich nur auf die von Microsoft konkret benannten betroffenen ConnectWise-Anwendungen.[1]

**Vormerkung für Pflege 01.11.2026:** **06 – Microsoft 365 sicher konfigurieren: Der Praxis-Check für Schweizer KMU.** Nur als prüfbarer Incident-/Lieferantenintegrations-Abschnitt: Inventar und Monitoring hochberechtigter Enterprise Apps bzw. Dienstprinzipale, Beweissicherung vor Löschung und organisationsspezifische Freigabe. Dies ist keine heutige Aussage über den Quellenstand oder die Freigabe des Entwurfs.

### 2. Microsoft Learn: Neue Anleitung zur Ursachenklärung bei widerrufenen Anmeldeinformationen von Anwendungen

**Publiziert/letzte Aktualisierung:** 22.10.2026. **Herstellerquelle:** Microsoft Learn, *Troubleshoot revoked application credentials*.[4]

Microsoft dokumentiert neue Fehlercodes für widerrufene Client Secrets, Client Assertions und föderierte Anmeldeinformationen. Der Eintrag stellt klar, dass ein Widerrufsfehler allein nicht nachweist, dass Microsoft die Anmeldeinformation widerrufen hat: Auch ausreichend berechtigte Anwendungsbesitzer oder Administratoren können dies tun. Für die Ursachenklärung sollen berechtigte Teams die `tokenRevocations` sowohl am Application- als auch am Service-Principal-Objekt mit derselben Application ID abfragen und die Entra-Auditdaten zum passenden Update-Ereignis prüfen.[4]

Für den Microsoft-initiierten Widerruf nennt die Dokumentation zwei belegbare Prüfwege: den dort angegebenen Ausstellerwert in `auditDetails.issuedBy` oder ein zugehöriges Update-Ereignis, das von *Azure Active Directory Protection Services* ausgelöst wurde. Bei tatsächlich kompromittierter Anmeldeinformation empfiehlt Microsoft Ersatz und Umstellung der Workload auf die neue Anmeldeinformation; die kompromittierte Anmeldeinformation soll widerrufen bleiben. Danach sind zusätzlich eingebrachte Anmeldeinformationen oder Zugriffe zu entfernen.[4]

**Einschränkung unmittelbar neben dem Befund:** Bereits ausgegebene Tokens können bei einzelnen Microsoft-Ressourcen nach einem Widerruf noch bis zum Ablauf funktionieren, laut Microsoft bis zu 24 Stunden. Das Löschen eines Widerrufs macht eine weiterhin gültige Anmeldeinformation wieder verwendbar, rotiert sie aber nicht und entfernt keine Kopie eines Angreifers. Die konkreten Graph-Beispiele verwenden den `/beta`-Endpunkt; sie sind keine Aufforderung zu einer ungetesteten Produktivänderung. Auch hier erfolgte keine Tenant-Prüfung.[4]

**Vormerkung für Pflege 01.11.2026:** **06 – Microsoft 365 sicher konfigurieren: Der Praxis-Check für Schweizer KMU.** Einen klar abgegrenzten Incident-Hinweis für Workload Identities ergänzen: Widerruf nicht mit vollständiger Beendigung allen Zugriffs gleichsetzen; Application- und Service-Principal-Objekt sowie Auditnachweis getrennt prüfen. Nur nach fachlicher und organisationsbezogener Prüfung übernehmen; der Entwurf bleibt unverändert als nicht freigegeben anzusehen.

### 3. Microsoft kündigt zusätzliche Entra-Identitäts- und Containment-Funktionen für KI-Agenten an

**Publiziert:** 19.10.2026. **Herstellerquelle:** Microsoft Security Blog, *Agents are your newest insiders. Security must move at their speed*.[5]

Microsoft kündigt für den Umgang mit KI-Agenten zusätzliche Agent-Identitätstypen sowie *Dynamic Permissions*, *Dynamic Agent Risk* und *Dynamic Conditional Access for agents* an. Der Sicherheitsansatz ist, Agenten nicht die gesamte dauerhafte Berechtigung ihrer Sponsoren zu vererben: Berechtigungen sollen auf Aufgabe und Zeit begrenzt sein, bei höherem Risiko reduziert oder zurückgezogen werden können und für folgenreiche Schritte eine nachweisbare menschliche Genehmigung verlangen können.[5]

Der Beitrag nennt eine Ausweitung der Erkennung auf 35 weitere lokale Agententypen, insgesamt 60 unterstützte lokale Agenten. Die vorhandene Learn-Produktseite grenzt die Ankündigung ein: Entra Agent ID ist für alle Entra-Kunden verfügbar, die Erweiterung der Entra-Sicherheitsfunktionen auf Agenten setzt jedoch Microsoft Agent 365 voraus. Agent 365 ist laut dieser Seite in Microsoft 365 E7 enthalten und als Add-on zu E5/A5/Business Premium oder Defender Suite plus Purview Suite verfügbar.[6]

**Einschränkung unmittelbar neben dem Befund:** Der Security-Blog ist eine Ankündigung und bezeichnet die Funktionen nicht als allgemein verfügbaren, lizenzunabhängigen Standard für jedes KMU. Die Produktseite datiert vor dem Berichtsfeld und dient nur zur Lizenz-/Produktabgrenzung. Ohne Inventar eingesetzter Agenten, Architektur- und Lizenzprüfung ist keine Aussage zur Verfügbarkeit oder zur konkreten Einführung in einem Tenant möglich.[5] [6]

**Vormerkung für Pflege 01.11.2026:** **09 – Schatten-KI im Schweizer KMU: Generative KI sicher nutzen, ohne vertrauliche Daten preiszugeben** und **06 – Microsoft 365 sicher konfigurieren: Der Praxis-Check für Schweizer KMU.** Prüfen, ob die getrennte Agentenidentität, aufgaben- und zeitgebundene Berechtigung sowie menschliche Freigaben als produktneutrale Gestaltungsprinzipien aufgenommen werden können. Microsoft-spezifische Funktions-, Lizenz- und Verfügbarkeitsaussagen nur nach aktueller, tenant- und vertragsbezogener Prüfung nutzen. Dies ist keine heutige Aktualisierung eines Entwurfs.

## Geprüfte Originalquellen und Abrufstand

Alle unten stehenden Seiten wurden am **25.10.2026 nach 09:00 CET**, tatsächlich zwischen **09:06 und 09:08 CET**, direkt abgerufen. Der Abruf erfolgte nach Ende des Berichtsfensters und nach der Zeitumstellung in Europe/Zurich. Bei nicht versionierten Webseiten belegt er keinen minutengenauen historischen Wortlaut zum Fensterende und keine Vollständigkeit aller Veröffentlichungen.

* Microsoft Security Blog – Übersichtsseite: https://www.microsoft.com/en-us/security/blog/ – abgerufen 25.10.2026, 09:06 CET. Im relevanten Zeitraum sichtbare, direkt geöffnete Beiträge: 19., 21. und 23. Oktober.
* Microsoft Security Blog – Storm-0940/ConnectWise: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ – publiziert 21.10.2026; abgerufen 25.10.2026, 09:07 CET.
* Microsoft Security Blog – Agenten/Entra Agent ID: https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/ – publiziert 19.10.2026; abgerufen 25.10.2026, 09:07 CET.
* Microsoft Learn – Widerrufene Anwendungsanmeldeinformationen: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials – letzte Aktualisierung 22.10.2026; abgerufen 25.10.2026, 09:07 CET.
* Microsoft Learn – Entra security operations guide for applications: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications – ohne belastbar im Abruf ausgewiesenes neues Publikationsdatum im Fenster; als von Microsoft verlinkte Vorgehensreferenz geöffnet am 25.10.2026, 09:07 CET.
* Microsoft Learn – Audit log activities: https://learn.microsoft.com/en-us/purview/audit-log-activities – `ms.date` 15.10.2026 und `updated_at` 19.10.2026 im Seitenmetadaten-Abruf; als von Microsoft verlinkte Aktivitätsreferenz geöffnet am 25.10.2026, 09:07 CET. Ein Metadatenzeitstempel allein belegt keine materielle Inhaltsänderung.
* Microsoft Learn – What is Microsoft Entra Agent ID?: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id – letzte Aktualisierung 24.06.2026; als Produkt-/Lizenzabgrenzung geöffnet am 25.10.2026, 09:07 CET.
* MSRC Blog – Übersicht: https://www.microsoft.com/en-us/msrc/blog/ – abgerufen 25.10.2026, 09:06 CET.
* MSRC – *Using risk cohorts to prioritize security updates*: https://www.microsoft.com/en-us/msrc/blog/2026/10/using-risk-cohorts-to-prioritize-security-updates – publiziert 13.10.2026, somit vor dem Berichtsfenster; geöffnet am 25.10.2026, 09:07 CET. Nicht als neue Meldung aufgenommen.
* MSRC – *Introducing Complete and Not Complete report assessments across Microsoft bounty programs*: https://www.microsoft.com/en-us/msrc/blog/2026/10/introducing-complete-and-not-complete-report-assessments-across-microsoft-bounty-programs – publiziert 20.10.2026; geöffnet am 25.10.2026, 09:07 CET. Betrifft Melde-/Bounty-Prozesse für Forschende, nicht die operative M365-/Entra-Sicherheit eines KMU; nicht aufgenommen.
* MSRC – Oktober-Sicherheitsupdate: https://www.microsoft.com/en-us/msrc/blog/2026/10/202610-security-update – publiziert 12.10.2026; geöffnet am 25.10.2026, 09:06 CET. Das Oktober-Patch-Tuesday-Thema und CVE-2026-96951 stehen bereits in der Vorwochenausgabe; eine neue belegte materielle Entwicklung im Berichtsfenster wurde nicht festgestellt und daher nicht wiederholt.
* Microsoft Learn – Entra-Veröffentlichungsübersicht: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new – geöffnet am 25.10.2026, 09:06 und 09:08 CET. Die aktuell abgerufene Seite führt nur Monate bis Juni 2026 und belegt keine neue, für dieses Feld relevante Oktober-Mitteilung.
* Microsoft Security Blog – LiteLLM 1.107.0: https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/ – publiziert 23.10.2026; geöffnet am 25.10.2026, 09:07 CET. Microsoft beschreibt eine Python-Paketkompromittierung samt möglichem Zugriff auf Cloud- und Entwickler-Anmeldeinformationen. Wegen fehlendem spezifischem M365-/Entra-Hauptbezug und der Begrenzung auf drei Meldungen nicht ausgewählt; nur bei Einsatz von LiteLLM 1.107.0 wäre dies als separates Software-Lieferketten-Thema zu prüfen.

## Abgrenzungen und offene Lücken

* Die Passkey-/SMS-/Voice- und Telephony-Provider-Verfügbarkeit ab **30.10.2026** ist laut Wartungsmanifest ein früher veröffentlichter, bevorstehender Termin. Sie wurde weder als neue Nachricht noch als Tenant-Prüfung behandelt. Der zusätzlich versuchte Abruf der vermuteten Learn-Telefonie-URL lieferte keine extrahierbaren Inhalte; daraus wird keine negative Hersteller- oder Verfügbarkeitsaussage abgeleitet.
* Es wurde keine Recherche in Tenants, keine App-ID-Inventarisierung und keine Analyse von Entra-, Purview-, Defender- oder Microsoft-Graph-Logs vorgenommen. Die genannten Prüfungen sind Herstellerempfehlungen für potenziell betroffene Umgebungen, kein Befund für ein bestimmtes Schweizer KMU.
* Die Prüfung deckt die zugeteilten Herstelleroberflächen Microsoft Security Blog, MSRC und Microsoft Learn anhand der geöffneten Originalseiten ab, bietet aber keine Vollständigkeitszusage über nicht auffindbare, nachträglich geänderte oder nicht versionierte Inhalte.
* Neben den drei aufgenommenen Meldungen wurde im Berichtsfenster keine durch Originalquelle belegte materielle Änderung eines M365-/Entra-Sicherheitsadvisory ermittelt. Die MSRC-Patch-Tuesday-Veröffentlichung lag vor dem Fenster und wurde entsprechend der Vorgabe nicht nochmals als Neuigkeit verwendet.

## Quellen

[1]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft Security Blog – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise"
[2]: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications "Microsoft Learn – Microsoft Entra security operations guide for applications"
[3]: https://learn.microsoft.com/en-us/purview/audit-log-activities "Microsoft Learn – Audit log activities"
[4]: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials "Microsoft Learn – Troubleshoot revoked application credentials"
[5]: https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/ "Microsoft Security Blog – Agents are your newest insiders Security must move at their speed"
[6]: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id "Microsoft Learn – What is Microsoft Entra Agent ID"
