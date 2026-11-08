---
status: "Entwurf – nicht freigegeben"
slug: "/wissen/microsoft-365-sicherheit-kmu"
meta_title: "Microsoft 365 sicher konfigurieren: KMU-Check | DKSchV"
meta_description: "Praxis-Check für Schweizer KMU zu Identitäten, Adminrollen, externen Freigaben, Protokollen, Wiederherstellung und Provider-Governance in Microsoft 365."
hauptkeyword: "Microsoft 365 Sicherheit KMU"
suchintention: "Informational – Microsoft-365-Tenant risikobasiert prüfen"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "05.11.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "Alle 15 eindeutigen, nach dieser Pflege in Artikel und zugehörigem Arbeitsmittel zitierten externen Originalquellen; zusätzlich BACS «Im Fokus», Microsoft Security Blog und einschlägige Microsoft-Learn-Referenzen vom 18.10. bis 01.11.2026. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS- oder Live-Linkprüfung."
quellenpruefung_status: "Vollständig für die 15 zitierten externen Originalquellen und die im Umfang genannten Übersichten; keine Fach-, Rechts-, Tenant-, Forensik-, Herstellerfreigabe- oder Publikationsfreigabe."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Microsoft 365 sicher konfigurieren: Der Praxis-Check für Schweizer KMU

> **Stand:** 1. November 2026. Die Quellenprüfung bestätigt allgemeine Hersteller- und Behördenaussagen, nicht die Einstellungen, Lizenzen oder Protokolle eines konkreten Tenants.

> **Kurzantwort:** Eine risikobewusste Microsoft-365-Konfiguration beginnt nicht mit einer einzelnen Einstellung, sondern mit klarer Verantwortung. Sichern Sie zuerst Identitäten und privilegierte Konten mit Mehrfaktor-Authentisierung (MFA), also mindestens zwei unabhängigen Anmeldefaktoren. Begrenzen und überprüfen Sie Administratorrollen. Regeln Sie externe Freigaben nach Datenart und Geschäftszweck. Stellen Sie sicher, dass relevante Anmelde-, Admin- und Freigabeereignisse protokolliert, aufbewahrt und im Notfall auswertbar sind. Definieren Sie zusätzlich, welche Daten und Konfigurationen Sie wie wiederherstellen müssen. Ein IT-Provider kann diese Aufgaben betreiben, die Geschäftsleitung und der datenschutzrechtlich Verantwortliche bleiben aber in der Pflicht. Priorisieren Sie die Lücken in einem 30-Tage-Plan, statt alle Funktionen gleichzeitig zu aktivieren.

Microsoft 365 bündelt E-Mail, Dateien, Teams-Besprechungen und Verwaltungsfunktionen in einer Cloud-Umgebung. Genau diese Konzentration macht den Tenant – die logisch abgegrenzte Microsoft-365-Organisation eines Unternehmens – zu einem geschäftskritischen Ziel. Ein kompromittiertes Konto, eine zu breite Adminrolle oder ein unkontrollierter Gastzugriff kann mehrere Dienste gleichzeitig betreffen.

Der folgende Praxis-Check richtet sich an Schweizer KMU mit bestehendem Microsoft 365. Er ersetzt weder eine technische Detailprüfung noch eine individuelle Rechtsberatung. Wo Personendaten, Auslandbekanntgaben oder Verträge beurteilt werden, ist **[FACHPRÜFUNG ERFORDERLICH]**.

## Cloud und Provider ändern die Verantwortung nicht

Microsoft stellt die Plattform bereit. Ihr Unternehmen entscheidet jedoch über Konten, Berechtigungen, Daten, Freigaben, Konfigurationen und die Zusammenarbeit mit einem IT-Provider. Das Bundesamt für Cybersicherheit (BACS) weist für ausgelagerte IT-Aufgaben ausdrücklich darauf hin, dass Zuständigkeiten für technische und organisatorische Sicherheitsmassnahmen klar geregelt sein müssen und Verantwortung nicht delegiert werden kann.[1] Der EDÖB ordnet Cloud-Anbieter bei einer Datenbearbeitung im Auftrag in der Regel als Auftragsbearbeiter ein; der verantwortliche Cloud-Nutzer bleibt dafür zuständig, dass die Bearbeitung datenschutzkonform erfolgt und Betroffenenrechte durch die Auslagerung nicht geschmälert werden.[2]

Das Schweizer Datenschutzgesetz (DSG) verlangt vom Verantwortlichen und vom Auftragsbearbeiter eine dem Risiko angemessene Datensicherheit. Bei einer Auftragsbearbeitung muss sich der Verantwortliche insbesondere vergewissern, dass der Auftragsbearbeiter die Datensicherheit gewährleisten kann.[3] Das ist keine Aussage darüber, ob eine bestimmte Microsoft-365-Konfiguration rechtmässig ist. Es ist der Grund, warum Geschäftsleitung, IT und Provider ihre Aufgaben, Entscheidungsrechte und Nachweise schriftlich festlegen sollten.

### Das hypothetische Praxisbeispiel: Viel Schutz, aber keine Steuerung

Ein hypothetisches Handels-KMU nutzt Microsoft 365 mit einem externen IT-Provider. Die Geschäftsleitung geht davon aus, dass «der Provider Microsoft 365 absichert». Tatsächlich verwaltet er mehrere globale Administratoren, ehemalige Mitarbeitende werden verspätet bereinigt und Projektteams teilen Dateien per Link mit Externen. Die Audit-Protokolle sind verfügbar, doch niemand hat festgelegt, welche Ereignisse geprüft und wie lange sie aufbewahrt werden müssen.

Das ist keine Produktlücke, sondern eine Steuerungslücke. Sichtbar werden müssen zuerst Eigentümer, Rollen, kritische Konten, externe Zusammenarbeit, Protokollierung und Wiederherstellungsziele. Danach folgen passende technische Kontrollen.

## 1. Identitäten zuerst: Konten, MFA und Wiederherstellung

Eine **Identität** ist im Tenant ein Benutzer-, Gast-, Dienst- oder Anwendungskonto, das Zugriff erhalten kann. Erfassen Sie daher nicht nur Mitarbeitende, sondern auch externe Gäste, gemeinsam genutzte Postfächer, technische Konten, Anwendungen und Konten des Providers. Ordnen Sie jedem Konto einen Eigentümer, einen Zweck, eine Berechtigungsstufe und ein Austritts- oder Überprüfungsdatum zu.

MFA sollte für alle Benutzer und zwingend für alle administrativen Konten gelten. Microsoft setzt seit Februar 2025 MFA für Konten, die im Microsoft-365-Admincenter administrative Vorgänge durchführen, schrittweise durch; dies schützt jedoch nicht automatisch jede Benutzeranmeldung und ersetzt keine eigene Zugriffspolitik für die Geschäftsdienste.[4] Prüfen Sie deshalb explizit, wie Ihre Benutzerkonten, Gastkonten, Admins und automatisierten Zugriffe abgesichert sind. **Conditional Access** ist Microsofts regelbasierte Zugriffskontrolle, die Anmeldebedingungen wie MFA oder Gerätezustand durchsetzen kann. Ihre Verfügbarkeit hängt von der Entra-Lizenz ab; wenn sie nicht einsetzbar ist, nennt Microsoft Security Defaults als Alternative für einen grundlegenden Schutz.[4]

Bei der Umsetzung genügt es nicht, eine Regel einzuschalten. Ermitteln Sie zuerst Anwendungen, Geräte und technische Prozesse, die dadurch betroffen sein können. Führen Sie neue Regeln mit einer kleinen Pilotgruppe ein. Halten Sie einen getesteten Weg für Kontowiederherstellung bereit. Für die Weiterentwicklung der Anmeldemethoden hilft der Beitrag [Microsoft 365 MFA und Passkeys für Schweizer KMU](/wissen/microsoft-365-mfa-passkeys).

### Notfallzugänge schützen – und trotzdem testbar halten

Ein **Notfallzugang** (oft als Break-Glass-Konto bezeichnet) ist ein hochprivilegiertes Konto, das nur verwendet wird, wenn reguläre Adminzugänge nicht funktionieren. Microsoft empfiehlt mindestens zwei cloudnative Notfallkonten mit dauerhaft aktiver Global-Administrator-Rolle. Sie sollen unabhängig von föderierten oder synchronisierten Identitäten funktionieren und eine phishing-resistente, von den normalen Admin-Konten unterschiedliche Anmeldung mit Passkey (FIDO2) oder zertifikatbasierter Authentisierung verwenden. Sie sind zu überwachen und mindestens alle 90 Tage zu testen.[5]

Ein solcher Zugang ist kein Freipass. Dokumentieren Sie, wer die Zugangsmittel in einem gesicherten Verfahren verwenden darf, wie eine Nutzung freigegeben wird und welche Nachprüfung danach erfolgt. Schliessen Sie diese Konten nur von Conditional-Access-Regeln aus, wenn sie sonst im Notfall blockiert wären. Die Ausnahme muss eng dokumentiert sein und die Anmeldung muss einen Alarm auslösen.[5]

## 2. Adminrollen, Enterprise Apps und Workload Identities steuern

Eine **Adminrolle** gibt einem Konto Verwaltungsrechte. Die Global-Administrator-Rolle kann fast alle Einstellungen in Entra ID und Microsoft 365 verändern. Microsoft empfiehlt deshalb das Prinzip der geringsten Rechte: eine Rolle mit nur den benötigten Berechtigungen, im benötigten Bereich und für die benötigte Zeit. Als Richtwert nennt Microsoft weniger als fünf Global Administrators und weniger als zehn Zuweisungen privilegierter Rollen.[6]

Behandeln Sie diese Richtwerte nicht als Ersatz für Ihr eigenes Risikourteil. Entscheidend sind Aufgaben, Stellvertretung und Kontrolle. Prüfen Sie mindestens vierteljährlich:

- Wer ist Global Administrator, Privileged Role Administrator, Exchange-, SharePoint- oder Intune-Administrator?
- Welchen geschäftlichen Auftrag erfüllt jede Zuweisung, und wer genehmigte sie?
- Werden Alltagstätigkeiten mit einem separaten, nicht privilegierten Konto erledigt?
- Sind Providerzugänge und eine zeitlich begrenzte Aktivierung privilegierter Rechte festgelegt?

Microsoft Entra Privileged Identity Management (PIM) kann berechtigte Adminrechte bei Bedarf zeitlich aktivieren und danach wieder entziehen. Die Funktion erfordert eine passende Lizenz.[6] Wenn sie nicht verfügbar ist, bleiben eine schriftliche Rollenliste, kurze Freigabewege, getrennte Adminkonten und regelmässige manuelle Reviews wertvolle Kontrollen.

Eine **Enterprise App** beziehungsweise ein Dienstprinzipal (Service Principal) kann Berechtigungen erhalten und als Workload Identity ohne interaktive Benutzeranmeldung auf Dienste zugreifen. Führen Sie deshalb neben Konten und Adminrollen ein Inventar dieser Anwendungen: Eigentümer, Geschäftszweck, Hersteller- oder Providerbezug, Berechtigungen, Genehmigung, Lebenszyklus sowie die Application ID. Halten Sie bei wichtigen Integrationen zusätzlich die tenant-spezifische Objekt-ID des Dienstprinzipals fest. Überwachen Sie insbesondere neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses.[13]

### Herstellerintegrationen und widerrufene Anmeldeinformationen ohne vorschnelles Löschen

Microsoft berichtete am 21. Oktober 2026, dass Storm-0940 kompromittierte Identitäten mehrerer ConnectWise-Cloudanwendungen für Zugriffe über bereits berechtigte Anwendungen nutzte. Die spezifische Herstelleranweisung, die betroffenen Anbindungen bis zu formellen Wiederherstellungsanweisungen von ConnectWise deaktiviert zu halten, gilt nur für die vier im Bericht genannten Application IDs – nicht pauschal für jedes ConnectWise-Produkt oder jede Enterprise App. Wenn eine dieser Application IDs aktuell oder früher autorisiert war, soll die zuständige, hierzu berechtigte Incident-Response-Fachstelle die aktuelle und frühere Autorisierung nach Application ID statt nach Anzeigename abklären und die lokale Dienstprinzipal-Objekt-ID festhalten. Das Vorhandensein einer solchen Anwendung oder eine erfolgreiche Anmeldung belegt für sich weder einen Missbrauch noch Datenzugriff oder Datenabfluss.[14]

Sichern Sie Konfiguration und verfügbare Entra-Anmelde- und Auditdaten, Purview-Auditdaten sowie gegebenenfalls SIEM-Daten vor einer irreversiblen Änderung. Microsoft rät ausdrücklich davon ab, Enterprise Apps als erste Reaktion zu löschen. Bei bestätigten unbefugten Anmeldeinformationen, Zustimmungen, Eigentümern, Zuweisungen oder Identitäten sollen diese erst nach der Beweissicherung durch eine angemessen berechtigte Fachstelle entfernt werden; dringliche Eindämmung darf jedoch nicht auf Exporte warten.[14] Diese allgemeine Prüfliste ordnet keine App-Deaktivierung, Löschung, Credential-Rotation oder Tenant-Freigabe an.

Ein Fehler für eine widerrufene Client-Anmeldeinformation belegt ebenfalls nicht, dass Microsoft den Widerruf ausgelöst hat: Dazu können auch ausreichend berechtigte Anwendungsbesitzer oder Administratoren fähig sein. Prüfen Sie bei einer fachlich begründeten Untersuchung die Widerrufseinträge am Application- **und** Service-Principal-Objekt mit derselben Application ID sowie das zugehörige Entra-Auditereignis. Ein Widerruf verhindert neue Tokens mit dieser Anmeldeinformation, beendet aber nicht zwingend jeden bereits ausgegebenen Zugriff sofort; bei einzelnen Ressourcen können Tokens bis zu 24 Stunden bis zum Ablauf weiter funktionieren. Ist eine Anmeldeinformation tatsächlich kompromittiert, empfiehlt Microsoft Ersatz und Umstellung der Workload auf die neue Anmeldeinformation; die kompromittierte Anmeldeinformation bleibt widerrufen.[15] **[FACHPRÜFUNG ERFORDERLICH]** Die Einordnung eines Verdachts, Beweissicherung, Eindämmung und Wiederherstellung einer konkreten Anbieterintegration gehören in den aktuellen Notfallprozess und zu den zuständigen Fachstellen.

## 3. Externe Freigaben gezielt statt pauschal öffnen

Externe Zusammenarbeit ist oft nötig, beispielsweise mit Treuhand, Kunden oder Projektpartnern. Das Risiko liegt nicht in jeder externen Freigabe, sondern in fehlendem Zweck, fehlender Begrenzung und fehlender Übersicht. Prüfen Sie SharePoint, OneDrive, Teams und die Einstellungen für Microsoft-Entra-Gäste als zusammenhängenden Prozess.

SharePoint und OneDrive erlauben auf Organisationsebene Freigabestufen von «Nur Personen in Ihrer Organisation» bis zu «Jeder». «Jeder»-Links sind ohne Anmeldung nutzbar; bei Weitergabe kann nicht nachvollzogen werden, wer Zugriff hat. Die Einstellungen auf einzelnen Websites dürfen nur gleich restriktiv oder restriktiver als die Organisationseinstellung sein. OneDrive darf nicht offener als SharePoint konfiguriert werden.[7]

Für ein KMU ist eine daten- und partnerbezogene Regel meist besser als ein pauschales Verbot. Definieren Sie beispielsweise, welche Daten über Teams mit Gästen geteilt werden dürfen, ob anonym nutzbare Links überhaupt zulässig sind und wer eine Ausnahme genehmigt. Wo die Zusammenarbeit auf bekannte Partner beschränkt werden kann, prüfen Sie spezifische Personen, Gastablauf und zugelassene E-Mail-Domains. Microsoft bietet dafür unter anderem eingeschränkte Domains, Freigabe nur durch bestimmte Sicherheitsgruppen und Ablaufdaten für Gastzugriffe.[7]

Behandeln Sie die Eingabe interner Inhalte, Personendaten oder Geschäftsgeheimnisse in ein KI-Tool nicht wie einen gewöhnlichen Freigabelink. Das BACS empfiehlt, vor jeder Eingabe auf sensible oder persönliche Daten zu prüfen und diese zu anonymisieren; wenn möglich sollen Unternehmens- statt Privatkonten verwendet und Trainingsnutzung sowie vorhandene Opt-out-Möglichkeiten geprüft werden.[11] Welche Datenflüsse und Einstellungen ein konkret eingesetzter Microsoft-365- oder KI-Dienst erlaubt, bleibt vor dessen Nutzung **[FACHPRÜFUNG ERFORDERLICH]**.

Überprüfen Sie Gäste, extern freigegebene Sites und sensible Datenbereiche mindestens halbjährlich. Entfernen Sie nicht mehr benötigte Gäste und prüfen Sie Projekt-Sites nach Abschluss. Das dient datenschutzfreundlichen Voreinstellungen: Das DSG verlangt, die Bearbeitung standardmässig auf das nötige Mindestmass zu begrenzen.[3]

## 4. Logging so planen, dass es im Vorfall hilft

**Logging** bedeutet, sicherheitsrelevante Ereignisse als Protokolle festzuhalten. Protokolle sind erst dann nützlich, wenn geklärt ist, wer sie liest, welche Ereignisse einen Alarm auslösen, wie lange sie verfügbar bleiben und wie sie im Vorfall gesichert werden. Beginnen Sie mit vier Fragen: Wer meldet sich an? Wer verändert Adminrollen und Richtlinien? Wer lädt Apps hoch oder erteilt ihnen Berechtigungen? Wer erstellt oder verändert externe Freigaben?

Microsoft Purview Audit erfasst und macht Tausende Benutzer- und Adminaktivitäten aus Microsoft-Diensten durchsuchbar. Audit (Standard) ist für Organisationen mit passendem Abonnement standardmässig aktiviert und bewahrt Auditdaten grundsätzlich 180 Tage auf.[8] Audit (Premium) bietet je nach Lizenz längere Standardaufbewahrung für Entra-, Exchange-, OneDrive- und SharePoint-Auditdaten sowie konfigurierbare Aufbewahrungsrichtlinien. Ob diese Funktionen, die zugrunde liegende Lizenzierung und die Aufbewahrungsdauer Ihre Anforderungen erfüllen, muss im jeweiligen Tenant geprüft werden.[8] [9]

Verlassen Sie sich deshalb nicht auf eine angenommene Aufbewahrungsfrist. Dokumentieren Sie für Ihren Tenant die tatsächlich verfügbaren Audit- und Anmeldeprotokolle, die verantwortliche Rolle für die Auswertung und die Aufbewahrungsanforderung aus Notfall-, Vertrags- und Datenschutzsicht. Bei einem Sicherheitsvorfall sollten relevante Protokolle zeitnah gesichert werden. Ergänzen Sie den Ablauf in Ihrer [IT-Notfallplanung](/unsere-dienstleistungen/notfallplanung) und testen Sie eine Recherche nach einer Adminrollenänderung oder einer externen Freigabe.

## 5. Backup-Verantwortung: Wiederherstellung konkret definieren

Microsoft 365 enthält Funktionen zur Aufbewahrung, Versionierung und Wiederherstellung in einzelnen Diensten. Diese Funktionen beantworten aber nicht automatisch Ihre Geschäftsfrage: **Welche Daten, Konten, Einstellungen und Arbeitsabläufe müssen nach Löschung, Fehlkonfiguration, Kontoübernahme oder Ransomware in welchem Zustand wiederherstellbar sein?**

Das BACS empfiehlt bei Cloud-Diensten, dass Daten exportierbar und als Offline-Backup gegen Ransomware gesichert werden können.[10] Bei Cloud- und Providerverträgen fordert es zudem, Backup-Konzept und erfolgreiche Wiederherstellungstests ausdrücklich zu klären.[1] Daraus folgt für das KMU: Entscheiden und dokumentieren Sie Ihre Wiederherstellungsanforderungen, statt «Backup vorhanden» als Nachweis zu akzeptieren.

Definieren Sie für Mail, OneDrive, SharePoint, Teams-Daten sowie wichtige Konfigurationen und Identitäten eine Wiederanlaufreihenfolge. Legen Sie den akzeptierten Datenverlustzeitraum und die akzeptierte Wiederherstellungsdauer je Geschäftsprozess fest. Diese Ziele werden häufig als **Recovery Point Objective (RPO)** und **Recovery Time Objective (RTO)** bezeichnet. Prüfen Sie danach, ob Microsoft-Bordmittel, ein separates Sicherungsprodukt oder eine Kombination die Anforderungen tatsächlich abdecken. Führen Sie eine dokumentierte Wiederherstellungsprobe durch. Der Artikel [Ransomware-resistente Backups](/wissen/ransomware-resistente-backups) und der Leitfaden zum [Backup-Wiederherstellung testen](/wissen/backup-wiederherstellung-testen) helfen bei der Vertiefung.

Ein Wiederherstellungstest legt nicht fest, wie ein konkreter Malwareverdacht zu behandeln ist. Das BACS empfiehlt, ein geschäftlich verwendetes Gerät bei Verdacht der zuständigen IT zu melden und es durch eine Fachperson untersuchen zu lassen; bei bestätigter Infektion nennt es das Neuaufsetzen und anschliessende Passwortwechsel.[12] Dieser Artikel ordnet keine Einzelfallmassnahmen für einen Vorfall an. Untersuchung, Protokollsicherung und Wiederanlauf sind mit dem aktuellen Notfallprozess und den zuständigen Stellen abzustimmen.

## 6. Provider-Governance: Leistung, Zugriff und Exit kontrollieren

**Provider-Governance** bedeutet, einen externen IT- oder Cloud-Dienstleister nicht nur auszuwählen, sondern dessen Zugriff, Pflichten und Leistungen fortlaufend zu steuern. Sie braucht eine verantwortliche Person im KMU, auch wenn der Provider technisch arbeitet. Der EDÖB empfiehlt für Cloud-Nutzer unter anderem, vertragliche Weisungsbindung, Sicherheitsmassnahmen, Unterauftragsbearbeiter, Länder der Datenbearbeitung, Unterstützung bei Betroffenenanfragen und Unterstützung bei einer allfälligen Meldung einer Datensicherheitsverletzung zu prüfen.[2]

Für Microsoft 365 sollte Ihr Vertrag oder Ihre dokumentierte Leistungsvereinbarung mindestens fünf Punkte regeln: erstens die beantragten, überprüften und bei Personalwechseln entfernten Providerzugänge; zweitens Freigaben für Apps, Zugriffspolitiken und Sicherheitsausnahmen; drittens Meldewege, Protokollsicherung und Eskalation im Vorfall; viertens Sicherungsumfang und Wiederherstellungstests; fünftens Unterauftrag, Datenorte und die Herausgabe von Daten, Konfigurationen und Unterlagen beim Exit.

**[FACHPRÜFUNG ERFORDERLICH]** Die datenschutzrechtliche Tragfähigkeit von Auftragsbearbeitungsvertrag, Datenflüssen und Auslandbekanntgaben muss bei Ihrem konkreten Sachverhalt fachlich geprüft werden. Das DSG erlaubt die Übertragung an Auftragsbearbeiter nur unter seinen Voraussetzungen; eine Weiterübertragung an Dritte setzt die vorgängige Genehmigung des Verantwortlichen voraus.[3]

Nutzen Sie die Providersteuerung als Teil Ihres [Cyber-Risikomanagements](/unsere-dienstleistungen/risikomanagement). Bewerten Sie dabei nicht nur Technik, sondern auch Abhängigkeit, Ersatzmöglichkeiten und Verantwortlichkeiten. Ein vereinbartes Ticket-System allein ist noch kein Notfallprozess. Die erreichbaren Stellen und Entscheidungswege sollten intern griffbereit dokumentiert sein; halten Sie dazu auch den offiziellen [Kontakt](/kontakt) sowie externe Notfallkontakte in Ihrer Notfallunterlage aktuell.

## Typische Fehler, die im Praxis-Check auffallen

**«MFA ist aktiviert, also sind wir fertig.»** MFA ersetzt nicht die Überprüfung von Gastkonten, Adminrollen, Anwendungen und Wiederherstellungswegen.

**«Der Provider ist Global Administrator, das ist einfacher.»** Eine breite Dauerberechtigung reduziert zwar kurzfristig Aufwand, vergrössert aber die Auswirkungen eines kompromittierten oder falsch verwendeten Kontos. Weisen Sie möglichst spezifische Rollen zu und überprüfen Sie sie.

**«Externe Links sind nur praktisch.»** Anonyme Links können weitergegeben werden. Stellen Sie Freigabestufe, Standard-Linktyp, Ablauf und Domänenregel auf den geschäftlichen Zweck ein.

**«Audit ist standardmässig aktiv, also ist die Forensik gelöst.»** Prüfen Sie verfügbare Protokolle, Suchberechtigungen, Aufbewahrung und Alarmierung.

**«Der Cloud-Dienst sichert das schon.»** Definieren Sie Wiederherstellungsziele und testen Sie die technische Abdeckung.

## Ihr 30-Tage-Prioritätenplan

### Tage 1–7: Lagebild und Eigentümer schaffen

Benennen Sie einen fachlichen Tenant-Eigentümer und eine Vertretung. Exportieren oder erfassen Sie Konten, Gäste, Enterprise Apps und Dienstprinzipale mit Application ID, Adminrollen, externe Freigabestufen, vorhandene Regeln und Providerzugänge. Kennzeichnen Sie kritische Geschäftsprozesse und Datenbereiche. Halten Sie offene Fragen in der [Microsoft-365-Tenant-Prüfliste](/resources/06-m365-tenant-pruefliste) fest.

### Tage 8–14: Kritische Identitäten absichern

Schliessen Sie Lücken bei MFA für Admin- und Benutzerkonten. Bereinigen Sie nicht benötigte oder nicht zuordenbare Konten und reduzieren Sie Global-Administrator-Rollen. Richten Sie mindestens zwei getestete, überwachte Notfallzugänge nach einem dokumentierten Verfahren ein. Führen Sie neue Zugriffskontrollen zunächst mit einer Pilotgruppe ein.[5] [6]

### Tage 15–21: Zusammenarbeit und Sichtbarkeit ordnen

Entscheiden Sie die zulässige externe Freigabestufe. Deaktivieren oder begrenzen Sie nicht begründete anonyme Freigaben. Prüfen Sie Gäste, externe Sites und Linkeinstellungen. Verifizieren Sie die Auditprotokollierung und testen Sie Suchabfragen für Adminrollen, Anmeldungen, Freigaben sowie Änderungen an Anwendungsanmeldeinformationen und Zustimmungen. Bestimmen Sie, welche Ereignisse an wen eskaliert werden.[7] [8] [13]

### Tage 22–30: Wiederherstellung und Provider verbindlich machen

Dokumentieren Sie RPO, RTO und Wiederanlaufreihenfolge für die wichtigsten Prozesse. Planen Sie einen begrenzten Restore-Test. Klären Sie mit dem Provider Zugänge, Alarmierung, Protokollsicherung, Sicherungsumfang, Subunternehmer und Exit-Unterlagen. Überführen Sie verbleibende Lücken mit Eigentümer und Termin in Ihr Risikoregister. Bei Fragen zu Datenflüssen, Auftragsbearbeitung oder internationalen Datenübermittlungen veranlassen Sie vor der Freigabe eine fachliche Prüfung.[1] [2] [3]

> **Nächster Schritt:** Halten Sie Befunde, Nachweise und Eigentümer in der [Microsoft-365-Tenant-Prüfliste](/resources/06-m365-tenant-pruefliste) fest. Für eine Anfrage zur [DKSchV-Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) steht [Kontakt](/kontakt) zur Verfügung. Eine Analyse kann Prioritäten strukturieren, ersetzt aber weder Tenant-Tests noch rechtliche Einzelfallprüfungen.

## Fazit

Microsoft 365 wird nicht durch eine Checkliste «sicher». Sicherheit entsteht, wenn die Checkliste Entscheidungen sichtbar macht: Wer besitzt welche Identität? Wer darf welche Rolle aktivieren? Welche externe Zusammenarbeit ist erlaubt? Welche Ereignisse werden erkannt? Was muss nach einem Vorfall wiederherstellbar sein? Und welche Leistung schuldet der Provider nachvollziehbar?

Wenn Sie diese Fragen innerhalb von 30 Tagen priorisiert bearbeiten, schaffen Sie eine nachvollziehbare Grundlage für weitere Risikoentscheide. Ob und wie sich Risiken verändern, hängt von den tatsächlichen Einstellungen, deren Umsetzung und laufender Kontrolle ab. Wiederholen Sie den Check mindestens halbjährlich sowie nach relevanten Lizenz-, Provider- oder Architekturänderungen.

## Quellen

[1]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[2]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing: Datenschutzpflichten bei Cloud-Diensten"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 7–9"
[4]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication "Microsoft Learn – Mandatory multifactor authentication for Azure and admin portals"
[5]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID"
[6]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices "Microsoft Learn – Best practices for Microsoft Entra roles"
[7]: https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off "Microsoft Learn – Manage sharing settings for SharePoint and OneDrive in Microsoft 365"
[8]: https://learn.microsoft.com/en-us/purview/audit-solutions-overview "Microsoft Learn – Learn about auditing solutions in Microsoft Purview"
[9]: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies "Microsoft Learn – Manage audit log retention policies"
[10]: https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit "BACS – Cloud Computing und Cybersicherheit"
[11]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen, 16. Oktober 2026"
[12]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[13]: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications "Microsoft Learn – Microsoft Entra security operations guide for applications"
[14]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft Security Blog – AI-driven large-scale nation-state campaign using ARTEX enables supply chain compromise"
[15]: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials "Microsoft Learn – Troubleshoot revoked application credentials"
