---
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/06-m365-tenant-pruefliste"
titel: "Microsoft-365-Tenant-Prüfliste für Schweizer KMU"
meta_title: "Microsoft-365-Tenant-Prüfliste für Schweizer KMU | DKSchV"
meta_description: "Arbeitsvorlage zur Priorisierung von Identitäten, Adminrollen, Freigaben, Protokollen, Wiederherstellung und Provider-Governance."
suchintention: "Arbeitsmittel – Microsoft-365-Tenant strukturiert prüfen"
zielgruppe: "Geschäftsleitungen, interne IT und IT-Provider Schweizer KMU"
version: "Stand 1. November 2026"
bezug: "/wissen/microsoft-365-sicherheit-kmu"
quellenpruefung_umfang: "Alle 15 eindeutigen, nach dieser Pflege in Arbeitsmittel und zugehörigem Artikel zitierten externen Originalquellen; zusätzlich BACS «Im Fokus», Microsoft Security Blog und einschlägige Microsoft-Learn-Referenzen vom 18.10. bis 01.11.2026. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS- oder Live-Linkprüfung."
quellenpruefung_status: "Vollständig für die 15 zitierten externen Originalquellen und die im Umfang genannten Übersichten; keine Fach-, Rechts-, Tenant-, Forensik-, Herstellerfreigabe- oder Publikationsfreigabe."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Microsoft-365-Tenant-Prüfliste für Schweizer KMU

> **Version:** Stand 1. November 2026. Die Vorlage ist eine Arbeitsgrundlage; ihr Ausfüllen belegt keine Tenant-, Fach-, Rechts- oder Veröffentlichungsfreigabe.

## Zweck

Diese Prüfliste unterstützt Geschäftsleitung, interne IT und IT-Provider dabei, den Sicherheitszustand eines bestehenden Microsoft-365-Tenants strukturiert zu erfassen und Massnahmen zu priorisieren. Ein **Tenant** ist die logisch abgegrenzte Microsoft-365-Organisation eines Unternehmens. Die Liste konzentriert sich auf Identitäten, Administratorrechte, externe Zusammenarbeit, Protokollierung, Wiederherstellung und Provider-Governance.

Sie ist ein Arbeitsmittel zur Bestandsaufnahme und ersetzt keine technische Sicherheitsanalyse, keinen Wiederherstellungstest und keine individuelle Rechtsberatung. Bei Personendaten, Auftragsbearbeitung, Datenbekanntgaben ins Ausland oder Vertragsbestimmungen ist **[FACHPRÜFUNG ERFORDERLICH]**.[1] [2]

## Anwendung

Füllen Sie die Prüfliste gemeinsam mit der fachlich verantwortlichen Person für Microsoft 365 und – soweit vorhanden – dem IT-Provider aus. Bewerten Sie jeden Punkt mit **erfüllt**, **teilweise erfüllt**, **nicht erfüllt**, **nicht anwendbar** oder **ungeprüft**. Ein «erfüllt» ist nur angemessen, wenn ein nachvollziehbarer Nachweis vorliegt, beispielsweise eine Konfiguration, ein Protokollauszug, ein Verfahren oder ein Testprotokoll.

Ordnen Sie offene Punkte einer Priorität zu. **Kritisch** bedeutet: Es besteht ein unmittelbarer, nicht akzeptierter Schutz- oder Steuerungsmangel bei privilegierten Zugängen, kritischen Daten oder Wiederherstellbarkeit. **Wichtig** bedeutet: Die Kontrolle fehlt oder ist lückenhaft und soll risikobasiert eingeplant werden. **Optimierend** bedeutet: Die Kontrolle verbessert Transparenz, Konsistenz oder Effizienz, ohne dass aus der Checkliste allein ein unmittelbares hohes Risiko folgt.

### Stammdaten

| Feld | Eintrag |
|---|---|
| Unternehmen / Organisationseinheit |  |
| Microsoft-365-Tenant-Domain |  |
| Prüfdaten / Zeitraum |  |
| Durchgeführt durch |  |
| Fachlicher Tenant-Eigentümer |  |
| Vertretung |  |
| IT-Provider / Kontakt |  |
| Nächster Überprüfungstermin |  |
| Genehmigt durch |  |

## Kontrollpunkte

### A. Identitäten und Anmeldung

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| A1 | Kritisch | Es gibt ein aktuelles Inventar aller Benutzer-, Gast-, Dienst- und Anwendungskonten mit Zweck und Eigentümer. |  |  |  |  |
| A2 | Kritisch | Nicht mehr benötigte, nicht zuordenbare oder ausgeschiedene Konten sind deaktiviert oder entfernt; der Austrittsprozess ist dokumentiert. |  |  |  |  |
| A3 | Kritisch | MFA (Mehrfaktor-Authentisierung) ist für alle Administratorkonten wirksam. Ausnahmen sind dokumentiert, befristet und genehmigt. |  |  |  |  |
| A4 | Wichtig | MFA und Zugriffsvorgaben für Benutzer, Gäste und technische Zugriffe sind nach Risiko festgelegt und auf Auswirkungen getestet. |  |  |  |  |
| A5 | Wichtig | Kontowiederherstellung, verlorene Authentisierungsmittel und Helpdesk-Prüfungen sind dokumentiert und praktisch erprobt. |  |  |  |  |
| A6 | Kritisch | Mindestens zwei cloudnative Notfallzugänge bestehen, sind geschützt, überwacht und periodisch getestet. |  |  |  |  |
| A7 | Optimierend | Risiko- oder Ausnahmeregeln für Anmeldungen werden regelmässig auf Notwendigkeit und Nebenwirkungen geprüft. |  |  |  |  |

**Prüfnotiz zu A6:** Microsoft empfiehlt mindestens zwei cloudnative Notfallkonten. Sie sollen unabhängig von föderierten oder synchronisierten Identitäten sein und eine phishing-resistente, von normalen Admin-Konten unterschiedliche Anmeldung mit Passkey (FIDO2) oder zertifikatbasierter Authentisierung verwenden. Die Konten sind zu überwachen und mindestens alle 90 Tage zu testen.[3]

### B. Administratorrechte und Anwendungen

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| B1 | Kritisch | Alle Zuweisungen von Global Administrator und anderen privilegierten Rollen sind mit Person, Zweck und Genehmigung dokumentiert. |  |  |  |  |
| B2 | Kritisch | Für jede Aufgabe wird die am wenigsten weitgehende geeignete Rolle verwendet; dauerhafte Global-Administrator-Rechte sind begründet. |  |  |  |  |
| B3 | Wichtig | Administrative Tätigkeiten erfolgen mit separaten Adminkonten, nicht mit dem alltäglichen Benutzerkonto. |  |  |  |  |
| B4 | Wichtig | Privilegierte Rollen und Providerzugänge werden mindestens vierteljährlich überprüft; nicht benötigte Rechte werden entfernt. |  |  |  |  |
| B5 | Wichtig | Zeitlich begrenzte oder genehmigungspflichtige Aktivierung privilegierter Rechte wird genutzt oder die Abweichung ist begründet. |  |  |  |  |
| B6 | Kritisch | Enterprise Apps, Dienstprinzipale und andere Workload Identities sind mit Eigentümer, Zweck, Hersteller- oder Providerbezug, Application ID, Berechtigungen, Genehmigung und Lebenszyklus inventarisiert. |  |  |  |  |
| B7 | Kritisch | Für einen begründeten Untersuchungshinweis zu einer Herstellerintegration sind aktuelle und frühere Autorisierungen nach Application ID sowie die tenant-spezifische Dienstprinzipal-Objekt-ID, verfügbare Anmelde- und Auditdaten und die Konfiguration vor irreversiblen Änderungen gesichert oder als Lücke dokumentiert. Eindämmung folgt dem berechtigten Notfallprozess. |  |  |  |  |
| B8 | Optimierend | Der Tenant nutzt Gruppen, klar abgegrenzte Bereiche oder andere Mechanismen, um Verwaltungsrechte strukturiert zu delegieren. |  |  |  |  |

**Prüfnotiz zu B2:** Microsoft empfiehlt das Prinzip der geringsten Rechte und nennt als Richtwerte weniger als fünf Global Administrators sowie weniger als zehn Zuweisungen privilegierter Rollen. Die angemessene Zahl muss jedoch aus Aufgaben, Stellvertretung und Risiko der eigenen Organisation abgeleitet werden.[4]

**Prüfnotiz zu B6–B7:** Anwendungen und Dienstprinzipale können weitreichende Berechtigungen erhalten. Microsoft empfiehlt, neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und privilegierte Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses zu überwachen.[12] Der Herstellerbericht zu Storm-0940 vom 21. Oktober 2026 verlangt bei den **vier dort konkret genannten ConnectWise-Application-IDs**, nicht bloss beim Anzeigenamen, ein Inventar in aktuell und früher autorisierten Tenants. Die eingeschränkte Anweisung, diese betroffenen Anbindungen bis zu formellen Wiederherstellungsanweisungen von ConnectWise deaktiviert zu halten, gilt nicht pauschal für andere ConnectWise-Produkte oder Anwendungen. Enterprise Apps sollen nicht als erste Reaktion gelöscht werden: Verfügbare Konfiguration und Beweise sind vor irreversiblen Änderungen zu sichern; dringliche Eindämmung darf nicht auf Exporte warten.[13]

**Prüfnotiz zu widerrufenen Anmeldeinformationen:** Ein Widerrufsfehler beweist nicht, dass Microsoft die Anmeldeinformation widerrufen hat. Prüfen Sie bei einer fachlich begründeten Untersuchung die `tokenRevocations` am Application- und Service-Principal-Objekt mit derselben Application ID sowie das passende Entra-Auditereignis. Ein Widerruf verhindert neue Tokens, kann aber je nach Ressource bereits ausgestellte Tokens bis zu 24 Stunden weiterwirken lassen. Bei bestätigter Kompromittierung empfiehlt Microsoft Ersatz und Umstellung der Workload; die kompromittierte Anmeldeinformation bleibt widerrufen.[14] **[FACHPRÜFUNG ERFORDERLICH]** Diese Notiz ordnet keine App-Deaktivierung, Löschung, Credential-Rotation oder Wiederaktivierung eines Widerrufs an.

### C. Externe Zusammenarbeit und Freigaben

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| C1 | Kritisch | Die erlaubte externe Zusammenarbeit nach Datenart, Empfängerkreis und Geschäftszweck ist schriftlich festgelegt. |  |  |  |  |
| C2 | Kritisch | Die organisationsweiten Freigabestufen in SharePoint und OneDrive entsprechen dieser Regel; davon abweichende Sites sind bekannt. |  |  |  |  |
| C3 | Wichtig | Der Standard-Linktyp ist risikogerecht festgelegt. Anonyme «Jeder»-Links sind deaktiviert, begrenzt oder nachvollziehbar begründet. |  |  |  |  |
| C4 | Wichtig | Ablaufdaten für Gastzugriffe und gegebenenfalls zugelassene Partner-Domains sind geprüft und eingestellt. |  |  |  |  |
| C5 | Wichtig | Gäste, extern freigegebene Sites und sensible Projekträume werden mindestens halbjährlich überprüft; nicht benötigte Zugriffe werden entfernt. |  |  |  |  |
| C6 | Optimierend | Das Verfahren für Freigabeausnahmen enthält Genehmigung, Ablaufdatum und spätere Überprüfung. |  |  |  |  |
| C7 | Wichtig | Für KI-Tools ist vor Eingaben geregelt, ob Personendaten, Kundendaten, Geschäftsgeheimnisse oder interne Dokumente zulässig sind; Sensibles wird vor einer Eingabe geprüft und gegebenenfalls anonymisiert. |  |  |  |  |

**Prüfnotiz zu C2–C4:** SharePoint und OneDrive kennen organisationsweite Freigabestufen. Einzelne Sites dürfen nur gleich restriktiv oder restriktiver eingestellt sein; OneDrive darf nicht offener als SharePoint sein. «Jeder»-Links sind ohne Anmeldung verwendbar und bei Weitergabe nicht personenbezogen nachvollziehbar.[5]

**Prüfnotiz zu C7:** Das BACS empfiehlt im Berufsalltag, vor jeder KI-Eingabe auf sensible oder persönliche Daten zu prüfen und diese zu anonymisieren; wenn möglich sollen Unternehmens- statt Privatkonten verwendet und Trainingsnutzung sowie vorhandene Opt-out-Möglichkeiten geprüft werden.[10] **[FACHPRÜFUNG ERFORDERLICH]** Die konkrete Zulässigkeit, Datenflüsse und Einstellungen des eingesetzten Dienstes sind nicht mit dieser Vorlage beurteilt.

### D. Protokollierung, Alarmierung und Notfallbezug

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| D1 | Kritisch | Die verantwortliche Rolle für Auswertung und Eskalation von Anmelde-, Admin- und Freigabeereignissen ist benannt. |  |  |  |  |
| D2 | Wichtig | Die im Tenant verfügbaren Audit- und Anmeldeprotokolle, Suchberechtigungen und Aufbewahrungsfristen sind dokumentiert. |  |  |  |  |
| D3 | Wichtig | Eine Suche nach mindestens einer Adminrollenänderung, einer externen Freigabe, einer verdächtigen Anmeldung und einer Änderung an Anwendungsanmeldeinformationen oder Zustimmungen wurde getestet. |  |  |  |  |
| D4 | Kritisch | Die Nutzung eines Notfallzugangs löst eine Alarmierung aus und wird nachträglich überprüft. |  |  |  |  |
| D5 | Wichtig | Sicherheitsrelevante Protokolle, Konfigurationen und weitere verfügbare Beweise können im Vorfall nach einem dokumentierten Ablauf vor irreversiblen Änderungen gesichert werden. |  |  |  |  |
| D6 | Optimierend | Die Alarmregeln und Kontaktwege werden nach Änderungen von Rollen, Provider oder Notfallplan überprüft. |  |  |  |  |

**Prüfnotiz zu D2:** Microsoft Purview Audit (Standard) ist in Organisationen mit passendem Abonnement standardmässig aktiviert und bewahrt Auditdaten grundsätzlich 180 Tage auf. Audit (Premium) und die konkrete Lizenzierung können längere Aufbewahrung ermöglichen. Prüfen Sie die tatsächliche Verfügbarkeit und Aufbewahrung in Ihrem Tenant.[6] [7]

### E. Wiederherstellung und Backup-Verantwortung

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| E1 | Kritisch | Für kritische Geschäftsprozesse sind Daten, Konfigurationen, Konten und Abhängigkeiten benannt, die wiederherstellbar sein müssen. |  |  |  |  |
| E2 | Kritisch | Akzeptierter Datenverlustzeitraum (RPO) und akzeptierte Wiederherstellungsdauer (RTO) sind je kritischem Prozess dokumentiert. |  |  |  |  |
| E3 | Wichtig | Es ist entschieden und nachgewiesen, welche Microsoft-Bordmittel und/oder separate Sicherung die Wiederherstellungsanforderungen abdecken. |  |  |  |  |
| E4 | Wichtig | Datenexport, gesicherte Kopien und Zugriff auf Wiederherstellungsunterlagen sind auch bei Störung oder Providerwechsel berücksichtigt. |  |  |  |  |
| E5 | Kritisch | Ein Wiederherstellungstest mit Ziel, Umfang, Ergebnis, Abweichungen und Verbesserungsmassnahmen ist dokumentiert. |  |  |  |  |
| E6 | Optimierend | Die Wiederanlaufreihenfolge ist mit Geschäftsleitung, Fachbereichen und dem Notfallplan abgestimmt. |  |  |  |  |

**Prüfnotiz zu E3–E5:** Das BACS empfiehlt bei Cloud-Diensten, dass Daten exportierbar und als Offline-Backup gegen Ransomware gesichert werden können. Es empfiehlt ausserdem, Backup-Konzept und erfolgreichen Wiederherstellungstest mit dem Dienstleister ausdrücklich zu klären.[8] [9]

**Prüfnotiz zum Vorfallbezug:** Bei Malwareverdacht auf einem geschäftlich verwendeten Gerät empfiehlt das BACS, die zuständige IT zu informieren und eine Fachperson untersuchen zu lassen; bei bestätigter Infektion nennt es Neuaufsetzen und anschliessende Passwortwechsel.[11] Das ist kein Ersatz für eine organisationsspezifische forensische oder Wiederanlaufentscheidung.

### F. Provider-Governance und Datenschutz

| Nr. | Priorität | Kontrollpunkt | Status | Nachweis / Feststellung | Eigentümer | Termin |
|---:|---|---|---|---|---|---|
| F1 | Kritisch | Interne Verantwortlichkeiten und diejenigen des Providers für Betrieb, Konfiguration, Änderungen, Vorfälle und Wiederherstellung sind schriftlich abgegrenzt. |  |  |  |  |
| F2 | Kritisch | Providerzugänge sind auf konkrete Personen oder nachvollziehbare Verfahren beschränkt, regelmässig überprüft und bei Wechseln entzogen. |  |  |  |  |
| F3 | Wichtig | Vereinbart sind Meldewege für Sicherheitsvorfälle, Sicherung relevanter Protokolle, erreichbare Eskalationskontakte und Entscheidungsrechte. |  |  |  |  |
| F4 | Wichtig | Sicherungsumfang, Wiederherstellungstests, Datenexport und Übergabe bei Vertragsende sind überprüfbar vereinbart. |  |  |  |  |
| F5 | Wichtig | Auftragsbearbeitung, Unterauftragsbearbeiter, Datenbearbeitungsorte und Auslandbekanntgaben werden für den konkreten Sachverhalt fachlich geprüft. |  |  |  |  |
| F6 | Optimierend | Die vereinbarten Leistungen und Nachweise werden periodisch kontrolliert und Abweichungen nachverfolgt. |  |  |  |  |

**Prüfnotiz zu F5:** Das DSG verlangt, dass der Verantwortliche sich insbesondere vergewissert, dass der Auftragsbearbeiter die Datensicherheit gewährleisten kann. Eine Unterauftragsbearbeitung erfordert die vorgängige Genehmigung des Verantwortlichen.[1] Der EDÖB empfiehlt unter anderem die Prüfung von Weisungsbindung, Sicherheitsmassnahmen, Unterauftragsbearbeitern, Bearbeitungsländern und Unterstützung im Vorfall.[2] Diese Prüfliste kann keine rechtliche Einzelfallwürdigung ersetzen.

## Priorisierte Massnahmenliste

| Nr. | Befund / Risiko | Priorität | Beschlossene Massnahme | Verantwortlich | Zieltermin | Status / Restentscheidung |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |

## Grenzen und Fachprüfung

Ein ausgefülltes Arbeitsmittel belegt nur, dass die genannten Punkte zu einem bestimmten Zeitpunkt bearbeitet wurden. Es garantiert weder die Sicherheit des Tenants noch die Verhinderung oder Erkennung eines Cyberangriffs. Neue Produkteinstellungen, Lizenzen, Anwendungen, Providerzugänge und Datenflüsse können die Bewertung verändern.

Die Liste ist keine Zertifizierung, kein Auditbericht und keine Zusage zur Wiederherstellbarkeit. Ergänzen Sie sie durch technische Tests, einen risikobasierten Massnahmenplan und einen abgestimmten Notfallprozess. **[FACHPRÜFUNG ERFORDERLICH]** Bei Verarbeitung von Personendaten oder Auslagerung an Cloud- und IT-Provider ist insbesondere die konkrete Vereinbarung über Auftragsbearbeitung sowie eine allfällige Datenbekanntgabe ins Ausland fachlich zu prüfen.[1] [2]

## Quellen

[1]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 7–9"
[2]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing: Datenschutzpflichten bei Cloud-Diensten"
[3]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID"
[4]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices "Microsoft Learn – Best practices for Microsoft Entra roles"
[5]: https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off "Microsoft Learn – Manage sharing settings for SharePoint and OneDrive in Microsoft 365"
[6]: https://learn.microsoft.com/en-us/purview/audit-solutions-overview "Microsoft Learn – Learn about auditing solutions in Microsoft Purview"
[7]: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies "Microsoft Learn – Manage audit log retention policies"
[8]: https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit "BACS – Cloud Computing und Cybersicherheit"
[9]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[10]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen, 16. Oktober 2026"
[11]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[12]: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications "Microsoft Learn – Microsoft Entra security operations guide for applications"
[13]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft Security Blog – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise"
[14]: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials "Microsoft Learn – Troubleshoot revoked application credentials"
