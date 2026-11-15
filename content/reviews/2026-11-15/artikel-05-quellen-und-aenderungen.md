# Quellen- und Änderungsbericht – Artikel 05, 15. November 2026

Artikel 05 und die Passkey-Rollout-Checkliste sind lokal auf **15. November 2026** gepflegt. Materielle Anpassungen betreffen die aktive gegenüber nur eligible Global-Administrator-Rolle, den präzisen Umfang der blockierenden Registrierung, SSPR, die aktuelle CYOT-Profilanleitung und die Grenzen neuer Erstregistrierungs- und Backupmeldungen. **Die Hauptfristen 1. Februar und 1. Juli 2027 wurden nicht geändert.** Die CYOT-GA seit 30. Oktober 2026 bleibt auf Entra-ID-Workforce-Tenants in global Azure begrenzt. [1] [3] [15] [16] [17]

**Prüfdatum:** 15. November 2026, Europe/Zurich CET, ISO-KW 46. Tatsächliche Fetch-Rückgaben: **09:06:01–09:08:37 CET**, aus den Werkzeugantworten dokumentiert. Suche: Rückgabe 09:06:02 CET. Alle Abrufe erfolgten nach 09:00. Das ist kein historischer Nachweis des Seitenwortlauts um exakt 09:00. Keine Browser-, CMS-, Zugangsdaten-, Tenant- oder Provideroperation wurde ausgeführt. Erreichbarkeit, lesbarer Inhalt und allgemeine Herstellerorientierung sind keine tatsächliche Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt- oder Veröffentlichungsfreigabe.

**Einziger Änderungsumfang:**

- `/home/ubuntu/dkschv-audit/blog-paket/articles/05-microsoft-365-mfa-passkeys.md`
- `/home/ubuntu/dkschv-audit/blog-paket/resources/05-passkey-rollout-checkliste.md`
- Dieser Bericht: `/home/ubuntu/dkschv-audit/reviews/2026-11-15/artikel-05-quellen-und-aenderungen.md`

Wartungsmanifest, Vorwochennews, Laufstatus, Vorwochen-Microsoftbericht und Einzelprüfung vom 1. November wurden nur gelesen. Andere Artikel, Ressourcen, Manifeste und globale QA-Skripte wurden nicht verändert oder ausgeführt. Die zusätzliche Hersteller-Commitprüfung war ein gezielter Versionsvergleich, keine Suche nach beliebigen Meldungen oder vollständige Versionsarchäologie.

## Quellenjournal: jede externe Quelle mit Original-URL und Einschränkung

Die Nummern 1–19 entsprechen den nach der Pflege im Artikel zitierten Originalquellen. Die Checkliste verwendet 14 davon. Zusätzlich wurden acht URLs geprüft. **Bilanz: 19/19 zitierte Quellen relevant lesbar; 27 aktuelle Original-URLs insgesamt, davon 26 mit verwertbarem relevantem Inhalt und eine mit nicht auslesbarem spezifischem Eintrag.** Inline gekürzte Extraktionen sind nicht mit einem Zugriffsfehler gleichgesetzt: Für die Haupttermin-, Pilot-, Conditional-Access-, Notfallkonto- und TAP-Quelle wurden die gespeicherten vollständigen Extraktionen ergänzend gelesen. Angegebene Zeiten sind Fetch-Rückgaben, keine erfundenen Serverzeitpunkte. Fetch lieferte Inhaltsstatus, aber keine gesondert gemessenen HTTP-Codes; es wird deshalb kein HTTP 200 behauptet.

### 1. Microsoft: Passkeys by default / SMS und Voice retirement

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement  
**Abruf:** 15.11.2026, 09:06:01 CET; relevant lesbar, inline gekürzt, vollständige Extraktion ergänzend gelesen. **Sichtbarer Stand:** 23.09.2026.  
**Aussage:** Passkey-Aktivierung für SMS-/Voice-aktivierte Benutzer ab 01.09.2026; Februar- und Juli-Retirement, interne Gäste im Februar; blockierende Registrierung bei ausschliesslich SMS/Voice; kein Opt-out der Durchsetzung; Inventar und gestufte Kommunikation. **Einschränkung:** Der Text enthält weiterhin ältere CYOT-Vorschauformulierungen. Diese sind gegenüber den speziellen aktuellen CYOT-Quellen nicht als aktueller Bereitstellungsnachweis verwendet. Kein Tenantinventar oder PowerShell-Skript ausgeführt. [1]

### 2. Microsoft: Passkeys FIDO2

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2  
**Abruf:** 15.11.2026, 09:06:01 CET; lesbar. **Sichtbarer Stand:** 06.04.2026.  
**Aussage:** FIDO2/WebAuthn, herkunftsgebundene Public-Key-Kryptografie und lokale Entsperrung; gerätegebundene und synchronisierte Passkeys; synchronisierte Passkeys ohne Attestierung. **Einschränkung:** Keine Prüfung eingesetzter Geräte, Passkeyanbieter oder Attestierungsprofile. Herstellerzahlen über Verbraucherkonten werden nicht als Schweizer KMU-Ergebnis übernommen. [2]

### 3. Microsoft: SMS-/Voice-FAQ, Vormerkung vom 4. November

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq  
**Abruf:** 15.11.2026, 09:06:01 CET; vollständig lesbar. **Sichtbarer Stand:** 04.11.2026.  
**Aussage:** Juli-Frist nur bei aktiver Global-Administrator-Rolle; nur eligible via rollenzuweisbare PIM-Gruppe ohne Aktivierung bedeutet regulärer Benutzer mit Februar-Frist. Interne Gäste im Februar, externe Benutzer im Juli. Public Cloud einschliesslich GCC. Rückzug umfasst SSPR. B2B-/interne Gast-Passkeys bis Ende 2026 geplant, nicht als bereits verfügbar bestätigt. TOTP bleibt nach Februar unterstützt, aber nicht phishing-resistent; registrierte und genutzte TOTP-MFA löst nicht die Retirement-bedingte blockierende Registrierung aus. SMS-/Voice-Zielzuordnung kann dennoch aufschiebbare Kampagnenaufforderungen auslösen. **Einschränkung:** Keine konkrete Rollen- oder Gastklassifikation. Ältere Provider-Vorschaupassage weiterhin vorhanden; aktuelle CYOT-Unterlagen sind hierfür massgeblich. Der genaue neue Inhalt ist durch die Herstellerpatches unten abgegrenzt, nicht allein durch das Änderungsdatum. [3] [26] [27]

### 4. NIST SP 800-63B

**Original-URL:** https://pages.nist.gov/800-63-4/sp800-63b.html  
**Abruf:** 15.11.2026, 09:06:32 CET; relevante Abschnitte mit Abfrage zur Phishing-Resistenz lesbar; vollständige Extraktion gespeichert. **Sichtbarer Stand:** Kein seitenbezogenes Tages- oder Revisionsdatum im ausgewählten relevanten Abschnitt festgestellt.  
**Aussage:** Phishing-Resistenz verhindert Preisgabe von Geheimnissen oder gültigen Authenticator-Ausgaben an einen vorgetäuschten Verifier. Manuell eingegebene OTP-/Out-of-Band-Ausgaben sind nicht an die Sitzung gebunden und nicht phishing-resistent. **Einschränkung:** Technische US-Orientierung, keine Schweizer Rechts- oder konkrete Entra-Konfigurationsfreigabe. [4]

### 5. BACS: SharePoint-Phishing-Welle

**Original-URL:** https://www.bacs.admin.ch/de/26w5-de  
**Abruf:** 15.11.2026, 09:06:31 CET; lesbar. **Veröffentlicht:** 03.02.2026.  
**Aussage:** Echtzeit-Anmeldung und Weitergabe der Zweitfaktor-Abfrage; alternative Verifizierung unklarer Nachrichten und laufende Mitarbeitendeninformation. **Einschränkung:** Kein Nachweis eines Vorfalls in einer konkreten Organisation, keine aktuelle Novemberwelle daraus abgeleitet. [5]

### 6. CISA: Implementing Phishing-Resistant MFA

**Original-URL:** https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf  
**Abruf:** 15.11.2026, 09:06:31 CET; offizielle PDF als Text lesbar. **Dokumentstand:** Oktober 2022.  
**Aussage:** FIDO/WebAuthn als breit verfügbarer phishing-resistenter Ansatz; SMS/Voice anfällig für Phishing, SS7 und SIM-Swap; priorisierter Rollout und Eskalation nicht MFA-fähiger Systeme. **Einschränkung:** Keine Hersteller- oder Schweizer Rechtsfreigabe; nicht als aktuelle Produktmatrix verwendet. [6]

### 7. Microsoft: Conditional Access authentication strengths

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths  
**Abruf:** 15.11.2026, 09:06:31 CET; lesbar. **Sichtbarer Stand:** 24.10.2025.  
**Aussage:** Entra ID P1 für Conditional Access; integrierte phishing-resistente Stärke mit Windows Hello/Plattform-Anmeldedaten, FIDO2 und multifaktorieller CBA; Auswertung erst nach erster Authentisierung. **Einschränkung:** Keine Tenant-Lizenz, Methode oder Sitzung getestet. Die neue November-Roadmap wird nicht als bereits tenantweit verfügbare zusätzliche Funktion eingesetzt. [7]

### 8. Microsoft: Phishing-resistente Deploymentplanung

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication  
**Abruf:** 15.11.2026, 09:06:33 CET; inline gekürzt, relevante weitere Pilot-/Rolloutabschnitte und Datumszeile aus vollständiger Extraktion gelesen. **Sichtbarer Stand:** 26.03.2026.  
**Aussage:** Personenbasierte Planung; repräsentative Pilotbenutzer, eigene Entra-Gruppen, Authentication Methods Activity für Registrierung und Nutzung; gestufte Durchsetzung und Supportfeedback. **Einschränkung:** Betriebssystem-, Geräte- und Anwendungsbereitschaft nicht tatsächlich geprüft; keine pauschale Übernahme sämtlicher Detailvorgaben. [8]

### 9. Microsoft: Conditional-Access-Deployment

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access  
**Abruf:** 15.11.2026, 09:06:33 CET; inline gekürzt, Durchsetzungsabschnitte und Quelldatum ergänzend gelesen. **Sichtbarer Stand:** 01.06.2026.  
**Aussage:** Testgruppen, Kommunikation, Berichtsmodus, Anmeldeprotokolle und registrierte erforderliche Methoden vor Durchsetzung; Hinweis auf mindestens eine Woche Berichtsmodus. **Einschränkung:** Simulation ist kein tatsächlicher Test; keine konkrete Regel, Ausnahme oder angemessene Beobachtungsdauer freigegeben. [9]

### 10. Microsoft: Emergency Access

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access  
**Abruf:** 15.11.2026, 09:06:33 CET; relevante vollständige Inhalte lesbar, Datumszeile aus gespeicherter Extraktion. **Sichtbarer Stand:** 05.06.2026.  
**Aussage:** Mindestens zwei cloud-only Notfallkonten; permanent aktive, nicht eligible Global-Administrator-Rolle; unabhängige phishing-resistente Methode, sichere Verwahrung, Ausschluss blockierender/einschränkender CA-Regeln, Monitoring und Tests. **Einschränkung:** Kein Notfallkonto, Alert, Notfallarbeitsplatz oder Zugriffstest durchgeführt. Neu zusätzlich in der Checkliste zitiert, keine neue Quelle ausserhalb der 19 Paarreferenzen. [10]

### 11. BACS: Grundschutz

**Original-URL:** https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden  
**Abruf:** 15.11.2026, 09:06:33 CET; lesbar. **Sichtbarer Stand:** Kein sichtbares Publikations- oder Änderungsdatum.  
**Aussage:** Zusammenwirken technischer und organisatorischer Kontrollen; Cybersicherheit als Leitungsaufgabe; MFA und sichere Passwörter im Grundschutz. **Einschränkung:** Keine spezifische Entra-Richtlinie oder gesetzliche Einzelfallpflicht daraus abgeleitet. [11]

### 12. Microsoft: Temporary Access Pass

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass  
**Abruf:** 15.11.2026, 09:06:33 CET; relevante Abschnitte lesbar, Datumszeile ergänzend gelesen. **Sichtbarer Stand:** 04.03.2026.  
**Aussage:** Zeitbegrenzter ein- oder mehrfach nutzbarer TAP, Richtlinienumfang, Bootstrap und Recovery; Code nach Anzeige nicht erneut abrufbar. TAP für interne Gäste, nicht externe Gastkonten im Ressourcentenant; Heimtenant-TAP unter dortigen Anforderungen und Cross-Tenant-MFA-Vertrauen. **Einschränkung:** Identitätsprüfung, Ausgaberollen, Laufzeit, Cross-Tenant-Vertrauen und Sitzungsbehandlung nicht konkret geprüft. Gast-Recovery wird als gezielte Vollständigkeitspräzisierung ergänzt, nicht als neue Novemberfunktion ausgegeben. [12]

### 13. Fedlex: DSG, Art. 8

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de  
**Abruf:** 15.11.2026, 09:07:00 CET; Art. 8 und Fassungsangabe trotz inline gekürzter Gesamtausgabe lesbar. **Amtlicher Stand:** 07.07.2025, durch History und bestehende XML bestätigt.  
**Aussage:** Verantwortlicher und Auftragsbearbeiter gewährleisten mit geeigneten technischen und organisatorischen Massnahmen eine dem Risiko angemessene Datensicherheit; Massnahmen müssen Verletzungen vermeiden können. **Einschränkung:** Keine Bewertung der Angemessenheit einer konkreten Passkey-/TAP-/CYOT-Umsetzung. Sichtbarer Wartungshinweis vom 13.11., 20:00 bis 15.11., 20:00; die hier dokumentierten Abrufe waren lesbar. Wartung wird weder als heutiger Totalausfall noch als ignorierter Blocker dargestellt. [13] [21] [22]

### 14. Microsoft: CYOT-Übersicht

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers  
**Abruf:** 15.11.2026, 09:06:09 CET; vollständig lesbar. **Sichtbarer Stand:** 11.11.2026.  
**Aussage:** Aktueller Anbieterweg mit Soprano, Telesign und Infobip, Azure Function, Anbieterangebot, SMS-/Voice-Profil, Evaluation und stufenweiser Migration. Kundenverantwortung für Integration, Providerkonto und Schutz vor Telefoniebetrug; Provider- und Azure-Kosten getrennt. **Einschränkung:** Verfügbarkeit, Abdeckung, Preise und Konditionen variieren; kein Schweizer Angebot, Vertrag oder Providerportal geprüft. Gegenüber dem belegten Altartikel ist die Aussage, diese Übersicht beschreibe noch nur private Vorschau, nun materiell veraltet und entfernt. [14]

### 15. Microsoft: CYOT-FAQ

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq  
**Abruf:** 15.11.2026, 09:06:09 CET; vollständig lesbar. **Sichtbarer Stand:** 11.11.2026.  
**Aussage:** GA seit 30.10.2026 für Workforce-Tenants in global Azure; nicht Entra External ID/B2C. Evaluation lässt Microsoft weiter liefern, Produktionszustellung separat testen; stufenweise Verkehrsverlagerung. Mehrregionen-/Zweitproviderdesigns nur Beispielanleitungen, Failover testen. Kundenbetrieb einschliesslich Erneuerung von Integrationsnachweisen und Zertifikaten. **Einschränkung:** Kein Provider für die Schweiz freigegeben, kein Verfügbarkeits-/Failovernachweis im Einzelfall. GA ist Altbestand seit Oktober, nicht eine neue November-GA. [15]

### 16. Microsoft: aktuelle CYOT-Setup-Adresse

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/choose-your-own-telephony-set-up  
**Abruf:** 15.11.2026, 09:07:01 CET; vollständig lesbar. **Sichtbarer Stand:** 11.11.2026.  
**Aussage:** Anleitung im Entra admin center mit Anbieterangebot, Azure Function, spezifischen Berechtigungen und Profileinrichtung. Endpunkt und App-ID werden übernommen und verglichen; bestehende Include- und Exclude-Zielgruppen bewahren. Separate Evaluation und Produktionszustellung, nach jeder Erhöhung testen. **Einschränkung:** Nur gelesen, keine Einrichtung, Beschaffung, Appregistrierung oder Scriptausführung. Die URL stammt aus der geöffneten Herstellerquelle, nicht aus einer geratenen Adresse. Alte Referenz [20] unten dokumentiert. [16]

### 17. Microsoft Entra Blog: November 2026

**Original-URL:** https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-november-2026/4556457  
**Abruf:** 15.11.2026, 09:07:00 CET; gesamter relevanter redaktioneller Blogtext lesbar, nachfolgende technische Seitendaten inline gekürzt. **Publikation/Aktualisierung:** 06.11.2026, Version 2.0.  
**Aussage:** Erstregistrierung eines Passkeys oder passwortloser Option als erste MFA-Methode als GA mit laufendem Rollout bis Februar 2027. Windows Hello for Business/macOS Platform SSO als eigenständige MFA mit Rollout ab Anfang November angekündigt. Verbesserte Android-Passkeysicherung mit Rollout ab Januar 2027 und nur persönliche Profile. CYOT als GA mit den drei Anbietern zusammengefasst. **Einschränkung:** Übersichtsankündigung ist keine tenantweite Bereitstellung. Die pauschale Blog-Februarfrist wird nicht anstelle der detaillierten Juli-Ausnahmen benutzt. Verlinkte Roadmap nicht spezifisch auslesbar; Backup- und Erstregistrierungsdetailquellen enthalten noch ältere Anforderungen. Keine Behauptung bereits verfügbaren universellen Android-Backups oder vollständig ausgerollter Erstregistrierung. [17] [18] [19] [24]

### 18. Microsoft: Authenticator-Telefonwechsel

**Original-URL:** https://learn.microsoft.com/entra/identity/authentication/how-to-transfer-authenticator-new-phone  
**Abruf:** 15.11.2026, 09:07:25 CET; vollständig lesbar. **Sichtbarer Stand:** 07.07.2026.  
**Aussage:** Bei Arbeits-/Schulkonten wird nur der Kontoname übertragen und erneute Anmeldung nötig; Passkeys separat behandeln. Bei gerätegebundenem Passkey neuen Passkey einrichten/testen, bevor altes Gerät entfernt wird. Synchronisierte Passkeys können nach Anmeldung im Schlüsselmanager vorhanden sein, Verfügbarkeit überprüfen. **Einschränkung:** Die im Novemberblog angekündigte Google-One-/Januarfunktion ist in dieser Detailanleitung nicht als bereits verfügbar dokumentiert. Konkretes Backup, persönliches Profil oder Firmenarbeitsprofil nicht getestet. [18]

### 19. Microsoft: Passkeys aktivieren

**Original-URL:** https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2  
**Abruf:** 15.11.2026, 09:07:26 CET; relevante Abschnitte gezielt extrahiert, lesbar. **Sichtbarer Stand:** 15.05.2026.  
**Aussage:** Passkeys in allen Entra-ID-Editionen einschliesslich Free ohne Zusatzlizenz; Profile für Gruppen; im gelesenen Stand vorherige MFA innerhalb der letzten fünf Minuten vor Registrierung. **Einschränkung:** Detailanforderung steht neben neuerer Blogankündigung zur ersten MFA-Methode. Kein bereits universell verfügbarer neuer Registrierungspfad belegt; konkreten Pilot und Bootstrap verlangen. Keine Lizenzfreiheit für Conditional Access aus Passkey-Lizenzfreiheit abgeleitet. [19]

### 20. Microsoft: bisher zitierte CYOT-Setup-URL

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api  
**Abruf:** 15.11.2026, 09:06:09 CET; vollständig lesbar, liefert aktuellen Setuptext mit englischem Leselink auf die neue Adresse [16]. **Sichtbarer Stand:** 11.11.2026.  
**Aussage:** Gleicher aktueller Admin-Center-Profiltext wie [16]. **Einschränkung:** Keine gesonderte HTTP-Redirectkette oder API-Funktion gemessen. Die alte URL ist nicht als tot bezeichnet; Quellenziel und Titel werden auf die ausdrücklich verlinkte aktuelle Adresse umgestellt. Nur im Bericht geführt, nicht als ungenutzte Doppelreferenz im Artikel. [20]

### 21. Fedlex: DSG-History

**Original-URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/history  
**Abruf:** 15.11.2026, 09:06:59 CET; vollständig lesbar. **Stand:** Jüngster ausgewiesener Eintrag Berichtigung BK, Beschluss 02.07.2025, Inkrafttreten 07.07.2025, AS 2025 444.  
**Aussage:** Amtliche Fassungsreihe und ausdrücklicher vorhandener XML-Link. **Einschränkung:** Auch hier sichtbarer Wartungs-/JavaScript-Hinweis, aber verwertbare Chronologie; kein erfundener technischer Blocker und keine individuelle Rechtsprüfung. [21]

### 22. Fedlex: bereits vorhandene amtliche DSG-XML

**Original-URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml  
**Abruf:** 15.11.2026, 09:07:01 CET; Stand und Art. 8 vollständig im relevanten Ausschnitt lesbar. **Amtlicher Stand:** 07.07.2025.  
**Aussage:** Art. 8 Abs. 1–3 und Fassungsdatum bestätigt. **Einschränkung:** Keine neue Rechtsänderung belegt, keine Angemessenheits- oder Fachfreigabe. URL stammt unverändert aus der Vorprüfung und aus History, nicht konstruiert. [22]

### 23. Microsoft: Registrierungskampagne

**Original-URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign  
**Abruf:** 15.11.2026, 09:07:02 CET; relevante Abschnitte lesbar, Datum aus gespeicherter vollständiger Extraktion. **Sichtbarer Stand:** 12.10.2026.  
**Aussage:** Microsoft-managed Passkeykampagne mit unbegrenztem Aufschieben und Profil-/Benutzerberechtigung; Enabled-Zustand mit konfigurierbarer Begrenzung. **Einschränkung:** Keine tatsächliche Kampagne geprüft. Bestätigt vorhandene Unterscheidung zwischen Aktivierung, Aufforderung und Registrierung; keine unnötige weitere Referenz im Artikel angelegt. [23]

### 24. Microsoft Roadmap 568076 – spezifischer Quellenblocker

**Original-URL:** https://www.microsoft.com/microsoft-365/roadmap?id=568076  
**Abruf:** 15.11.2026, 09:07:27 CET; allgemeine Roadmapseite erreichbar, inline gekürzt, vollständige Extraktion lokal gezielt geprüft. **Spezifischer Stand:** Nicht feststellbar; Eintrag 568076, Windows-Hello-/Platform-SSO-Funktionsdetails nicht auslesbar.  
**Aussage:** Nur die allgemeine Roadmaperklärung zu geschätzten und veränderbaren Terminen ist lesbar. **Einschränkung/Blocker:** Kein verwertbarer spezifischer Eintragsnachweis. Einmalige lokale Stichwortprüfung ohne Treffer; keine Browseroperation, kein wiederholtes Nichtfundsuchen. Die Quelle gilt ausdrücklich **nicht als erfolgreich spezifisch geprüft**. Der Blogbefund ist nur Ankündigung; die bestehenden Authentisierungsstärkenpassagen werden nicht mit einer unbestätigten neuen tenantweiten Funktion umgeschrieben. [24]

### 25. MicrosoftDocs: FAQ-Commitliste

**Original-URL:** https://api.github.com/repos/MicrosoftDocs/entra-docs/commits?path=docs/identity/authentication/concept-sms-voice-retirement-faq.yml&per_page=5  
**Abruf:** 15.11.2026, 09:08:01 CET; lesbar. **Datierung:** Enthält Commits vom 04.11. und 02.11.2026 sowie ältere Einträge.  
**Aussage:** Liefert die konkreten Hersteller-Revisionsadressen für GCC und PIM. **Einschränkung:** Fünf Einträge, keine vollständige Historie und kein Snapshot der Learn-Seite um 09:00. Die Einzelpatches wurden separat geöffnet. [25]

### 26. MicrosoftDocs: PIM-Präzisierung vom 2. November

**Original-URL:** https://api.github.com/repos/MicrosoftDocs/entra-docs/commits/97f0076fa66905c007afed675278db5bae9e644d  
**Abruf:** 15.11.2026, 09:08:37 CET; vollständiger Patch lesbar. **Hersteller-Commitdatum:** 02.11.2026, 21:40:51 UTC.  
**Aussage:** Fügt die PIM-Frage und die zwei Antworten zur nur eligible beziehungsweise aktiven Rolle ein; Kontext enthält bereits die Juli-Frist und interne Gäste im Februar. **Einschränkung:** Hersteller-Revisionsdatum ist nicht ein minutengenauer Learn-Publikationsnachweis. Patch nennt als altes `ms.date` 20.10.2026, während das Vorjournal 26.10.2026 nennt; vollständiger damaliger Learn-Snapshot fehlt. Dieser Metadatenwiderspruch wird nicht wegerklärt. Die neu hinzugefügte Passage selbst ist eindeutig sichtbar. [26]

### 27. MicrosoftDocs: GCC-Präzisierung vom 4. November

**Original-URL:** https://api.github.com/repos/MicrosoftDocs/entra-docs/commits/4484dcdec83741a2980f114f44f41bd76b41ea51  
**Abruf:** 15.11.2026, 09:08:36 CET; vollständiger Patch lesbar. **Hersteller-Commitdatum:** 04.11.2026, 16:24:34 UTC.  
**Aussage:** Ersetzt genau «public cloud environments only» durch «public cloud environments, including GCC». Keine Änderung einer Hauptfrist in diesem Patch. **Einschränkung:** Keine komplette damalige Seitenfassung oder Tenant-Cloudprüfung; nicht als neue GA oder neue Februar-/Julifrist ausgegeben. [27]

## Belegter FAQ-Alttextvergleich statt Datumsinterpretation

Die Pflegevormerkung im gelesenen `news/qa/2026-11-08/02-microsoft.md`, Abschnitte «Weitere geprüfte Quellen und Ausschlüsse» und «Grenzen und Vormerkungen», verlangte diesen Vergleich. Der damalige Abruf vom 8. November ist nur historische Basis, keine heutige Messung. Die heutige FAQ ist tatsächlich mit sichtbarem Stand 04.11.2026 gelesen. [3]

**Belegter Altbestand im Artikel vom 1. November:**

> «Globale Administratoren und externe Benutzer haben für die von Microsoft bereitgestellten Telekommunikationsdienste eine spätere Frist bis **1. Juli 2027**.»

Die Einschränkung auf aktive Rollen fehlte im Artikel und in der Checkliste. Der Herstellerpatch vom **2. November**, nicht erst der Seitenstand 4. November, fügt nach dem bereits bestehenden Gast-/Julikontext die konkrete PIM-Frage ein. [26]

> «If you're eligible for the Global Administrator role through a role-assignable group in Microsoft Entra Privileged Identity Management (PIM) but haven't activated the role, you're treated as a regular user. The February 1, 2027 retirement date applies to you.»
>
> «The July 1, 2027 retirement date for Global Administrators applies only while your Global Administrator role is active. Being eligible for the role doesn't qualify you for the later date.»

**Exakter geänderter Quellensatz vom 4. November:**

> Vorher: «This timeline applies to public cloud environments only. Other cloud environments will follow on a later schedule, and we will provide advance communications to help customers prepare for the transition.»
>
> Nachher: «This timeline applies to public cloud environments, including GCC. Other cloud environments will follow on a later schedule, and we will provide advance communications to help customers prepare for the transition.» [27]

Damit sind zwei konkrete Präzisierungen belegt. Es ist keine Verschiebung der Haupttermine belegt. SSPR, temporärer Opt-out, interne/externe Gäste und TOTP werden als heute bestätigter Aussageumfang präzisiert, nicht pauschal als am 4. November neu entstanden ausgegeben. Die frühere Datumsangabe **26.10.2026 im Einzeljournal** und das alte **20.10.2026 im Git-Patch** stimmen nicht überein. Ein vollständiger historischer Learn-Alttext vom 26. Oktober wurde nicht gefunden beziehungsweise lag nicht vor; es wird kein solcher Snapshot behauptet. Der gezielte Patchbeleg reicht für die dokumentierte Rollen- und GCC-Ergänzung, nicht für eine umfassende Rekonstruktion aller damaligen Passagen. [3] [26] [27]

## Genau betroffene Abschnitte vorher und nachher

### Artikel: Frontmatter

**Vorher:** `stand: "1. November 2026"`; Quellenumfang «16/16 … stateless im Original abgerufen» mit Fedlex und BACS-Vormerkung; Status behauptete 16/16 am 1. November, 09:05–09:07 CET ohne Quellenblocker.

**Nachher:** `stand: "15. November 2026"`; Umfang 19/19 eindeutige, nach Pflege zitierte Paarquellen, direkt mit fetch gelesen, mit explizit benannten Zusatzabrufen. Status nennt die tatsächliche heutige Zeitspanne 09:06:01–09:08:37 CET, 19/19 relevante lesbare Zitate, einen spezifischen Roadmapblocker, die datierten FAQ-Patches, unveränderte Hauptfristen, eingeschränkte CYOT-GA, offenen Einzelfall und keine Freigabe. Die historische BACS-Vormerkung wird nicht als heute nochmals abgerufen ausgewiesen.

### Artikel: sichtbarer Produktstand unmittelbar unter Kurzantwort

**Vorher:** «Stand der Produktinformationen: 1. November 2026.»

**Nachher:** «Stand der Produktinformationen: 15. November 2026.» Der übrige Hinweis einschliesslich **[FACHPRÜFUNG ERFORDERLICH]** bleibt wortgleich. **H1 und Kurzantwort selbst bleiben vollständig unverändert.**

### Artikel: «Die Termine: Was Microsoft ändert – und was bis Februar erledigt sein muss»

**Erster Terminabsatz vorher:** «Für interne Benutzer und interne Gastbenutzer gilt … 1. Februar 2027 … Wer dann nur diese Methode hat … Globale Administratoren und externe Benutzer … 1. Juli 2027.»

**Nachher:** Interne Benutzer/Gäste ohne aktive GA-Rolle folgen Februar. Der blockierende Fall nennt ausdrücklich ausschliesslich verfügbare Microsoft-SMS/-Sprache und fehlende Migration zu eigenem Provider. Juli für GA nur bei aktiver Rolle; externe Benutzer Juli. Der belegte eligible-PIM-Gruppenfall ist ergänzt. Der risikobasierte Rat, auch Juli-Gruppen bis Februar zu planen, bleibt. Zitation jetzt [1] [3].

**Cloud-/CYOT-Absatz vorher:** «nur für die Public Cloud»; «am 1. November 2026» GA seit 30.10.; FAQ «am 30. Oktober aktualisiert»; «Die ältere Übersichtsseite [14] beschreibt noch den vorherigen privaten Vorschauzustand … neuere Quellen [15] und [16] massgeblich.»

**Nachher:** Public Cloud einschliesslich GCC; andere Clouds später. B2C-/External-ID-Abgrenzung erhalten. Eigener Absatz ergänzt die geplante B2B-/interne Gastunterstützung, TOTP-Unterstützung ohne Phishing-Resistenz und Bereinigung nicht mehr benötigter SMS-/Voice-Zuordnungen erst nach Ersatzmethodentest. CYOT-GA bleibt seit 30.10. im engen Scope; Übersicht/FAQ/Setup jetzt Stand 11.11. und drei Anbieter. Alte Vorschauhinweise befinden sich heute noch in Hauptterminquelle/Retirement-FAQ, nicht mehr in der neuen CYOT-Übersicht; Quellenpriorität entsprechend korrigiert. [1] [3] [14] [15] [16]

**CYOT-/Opt-out-Absatz vorher:** Vertrag, Azure Function, Hinterlegen von Endpunkt/App-ID «in der bestehenden SMS- oder Voice-Richtlinie»; zuerst Evaluation, dann schrittweise Produktion; allgemeine Betriebsverantwortung; temporärer Opt-out ohne Zeitspanne.

**Nachher:** Aktueller Profilweg im Entra admin center und Übernahme/Abgleich von Endpunkt/App-ID; Include **und** Exclude bewahren. Explizite Trennung: Evaluation mit Microsoft-Codezustellung, separat Production-Providerzustellung und Test nach jeder Erhöhung. Integration/Providerkonto/Telefoniebetrug sowie separate Provider-/Azure-Kosten konkretisiert; Mehrregionen-/Zweitproviderbeispiele kein Failovernachweis. Der Absatz zur fehlenden Schweiz-/Tenant-/Anbieterprüfung bleibt sinngleich vollständig erhalten. Opt-out-Zeitspanne 01.09.2026–01.02.2027 und SSPR-Umfang ergänzt; Durchsetzung nicht verschoben. [1] [3] [14] [15] [16]

**Unverändert in diesem Abschnitt:** Entra-/MFA-Grunddefinition und Absatz zur automatischen Passkey-Aktivierung versus tatsächlicher Registrierung. Keine Graph-Anweisung hinzugefügt oder ausgeführt.

### Artikel: «Zuerst Inventar und Risiken, dann Technik erzwingen»

**Vorher im ersten Absatz:** «Benutzer mit aktiver SMS- oder Sprachmethode»; globale Administratoren und Gäste nur allgemein getrennt kennzeichnen.

**Nachher:** Für SMS-/Voice aktivierte Benutzer auswerten; Richtlinienzuordnung, Registrierung und Nutzung unterscheiden. Aktive GA, eligible PIM, weitere privilegierte Rollen und interne/externe Gäste getrennt zuordnen; individuelle Fristgruppen und SSPR erfassen. Temporär aktive Rolle kein belastbarer Aufschubgrund. Zitation [1] [3]. Alle weiteren Absätze einschliesslich Altanwendungen, Dienstleistungslinks und hypothetischem Beispiel unverändert.

### Artikel: «Passkey-Pilot: klein genug zum Lernen, breit genug für die Realität»

**Vorher:** Nach dem vorhandenen Pilotabsatz folgte direkt die fünfteilige Abnahmeliste; kein Absatz zur neuen Erst-MFA-Registrierung oder Passkey-Lizenzfreiheit.

**Nachher:** Genau ein Absatz davor ergänzt: Blog vom 06.11. bezeichnet Erstregistrierung als GA, Rollout aber bis Februar 2027; Detailanleitung verlangt noch vorherige MFA. Keine pauschale sofortige Verfügbarkeit, konkreter Pilot und geprüfter Bootstrap etwa TAP. Passkeys in Free ohne Zusatzlizenz, CA separat prüfen. [12] [17] [19] Pilotabsatz, fünf Fragen und gestufter Priorisierungsabsatz bleiben unverändert.

### Artikel: «Wiederherstellung vor der Durchsetzung planen»

**Vorher:** Allgemeiner Wiederherstellungsablauf, TAP-Grundabsatz und danach Notfallplanung/DSG-Hinweis; kein Gast-/Authenticator-Backupabsatz.

**Nachher:** Genau ein Absatz nach TAP ergänzt: interne Gäste gegenüber externen Gastkonten und Heimtenant-TAP unterscheiden; Authenticator-Kontonamenbackup nicht Passkey-Recovery; neue Androidmeldung erst Rollout ab Januar 2027/persönliche Profile, keine heutige Backupgarantie. [12] [17] [18] Allgemeiner Ablauf und TAP-Grundabsatz unverändert.

**Nur Prüfdatum im DSG-Absatz:** Vorher «am 1. November 2026», nachher «am 15. November 2026». Amtlicher Stand bleibt 7. Juli 2025 und der Original-Fachmarker bleibt wortgleich. Keine neue Rechtsaussage oder Fachfreigabe. [13] [21] [22]

### Artikel: «Quellen»

**Vorher:** 16 Definitionen, [16] alte `how-to-set-up-sms-voice-api`-Adresse mit altem Setup-Titel.

**Nachher:** [16] ausdrücklich verlinkte und geöffnete `choose-your-own-telephony-set-up`-Adresse mit aktuellem Admin-Center-Titel. Drei verwendete Quellen hinzugefügt: [17] Novemberblog, [18] Transferanleitung, [19] Passkeyaktivierung. Übrige Definitionen unverändert. Alte Adresse im Bericht als lesbar und ersetzt dokumentiert, nicht gelöscht aus der Nachvollziehbarkeit. Keine ungenutzten neuen Referenzen.

### Arbeitsmittel: Frontmatter und sichtbare Version

**Vorher:** Kein `stand`-Feld; `version: "Stand 1. November 2026"`, sichtbar «Version: 1. November 2026», gleiche alte 16/16-Prüfmetadaten wie Artikel.

**Nachher:** `stand: "15. November 2026"` ergänzt; Datumsversionskonvention beibehalten und materiell auf `version: "Stand 15. November 2026"` erhöht, sichtbar «Version: 15. November 2026». Quellenumfang/-status gleich konkret wie Artikel mit 19 Paarquellen und spezifischem Roadmapblocker. Die Version wurde wegen der materiellen Kontrollpunktänderungen erhöht, nicht allein wegen eines Prüfdatums.

### Arbeitsmittel: «Zweck»

**Vorher:** Public Cloud, pauschale GA-/Gastfristen, CYOT-GA seit 30.10., drei Anbieter und offene Schweiz-/Tenant-Eignung in einem Terminabsatz.

**Nachher:** Terminabsatz nennt GCC, aktive gegenüber eligible PIM-Rolle, interne Gäste ohne aktive GA im Februar, externe Benutzer im Juli, SSPR, zeitlich begrenzten Opt-out und genauen blockierenden Fall. TOTP-/Gastplanung als Grenzen ergänzt. Eigener CYOT-Absatz mit Unterlagenstand 11.11., Azure Function und Admin-Center-Profilweg; bisherige Schweiz-/Tenant-/Anbietergrenzen und vollständiger Original-Fachmarker bleiben. [1] [2] [8] [9] [10]

### Arbeitsmittel: «1. Ausgangslage und Entscheidungsrahmen»

**Vorher:** Kontrollpunkt «Privilegierte Rollen, IT-Provider, Finanz- und Personalrollen sowie interne und externe Gäste sind separat markiert.»

**Nachher:** «Aktive Global Administrators, nur eligible PIM-Zuweisungen, weitere privilegierte Rollen, IT-Provider, Finanz-/Personalrollen sowie interne und externe Gäste sind separat markiert und ihrer Februar- oder Juli-Frist zugeordnet. [2]»

**Neu eingefügt nach Benutzeridentifikation:** «SMS-/Voice-Richtlinienzuordnung, registrierte Methoden und tatsächliche Nutzung sind unterschieden; SSPR ist mit erfasst. [1] [2]» Alle übrigen Kontrollpunkte, Risiko-/Entscheidtabellen und leeren Felder unverändert.

### Arbeitsmittel: «2. Passkey-Design und Pilot»

**Vorher:** Kein Absatz über laufende Erst-MFA-GA und keine solche Testzeile.

**Nachher:** Ein Absatz nach Passkey-Grunderklärung zur Erstregistrierungsankündigung, noch älterer MFA-Voraussetzung, konkretem Bootstrap und separater Lizenzprüfung ergänzt. [6] [11] [13] Neue Zeile nach dem vorhandenen Registrierungstest: «Erstregistrierung ohne bisherige MFA, Gastunterstützung und ein geprüfter TAP-/Bootstrap-Ersatzweg sind konkret getestet; Rolloutankündigungen gelten nicht als Testnachweis. [2] [6] [11] [13]» Alle bisherigen Test-/Abnahmezeilen und Pilotgruppentabelle unverändert.

### Arbeitsmittel: «4. Wiederherstellung und Notfallzugang»

**Vorher:** TAP-Grunderklärung und bestehende Tabellen, ohne explizite Guest-/Backupgrenze oder permanent aktive Rollenzeile.

**Nachher:** Ein Absatz zur Gast-TAP-Grenze, Heimtenant-Vertrauen, Kontonamenübernahme versus Passkeys und nur angekündigtem Januar-/persönlichem Androidbackup ergänzt. [6] [11] [12] Neue Zeile nach Gerätewechseltest: «Interne und externe Gäste haben einen getrennt geprüften Recovery-Pfad; Authenticator-Backup und tatsächliche Passkey-Wiederherstellung sind nicht gleichgesetzt. [6] [12]» Neue Zeile nach Mindestzahl der Notfallkonten: «Notfallkonten haben eine permanent aktive, nicht nur eligible Global-Administrator-Rolle; Zugriff und Überwachung sind getestet. [14]» Die Vorlage bestätigt damit keine Durchführung: Alle Statusfelder bleiben leer beziehungsweise ☐. Alte Recovery-/CYOT-Ausfallzeilen und Testprotokoll unverändert.

### Arbeitsmittel: «5. Benutzerkommunikation und Support»

**Vorher:** Kein Kontrollpunkt zur Beendigung unnötiger Kampagnenaufforderungen nach Ersatzmethodentest.

**Nachher:** Neue Zeile nach Phishing-Warnung: «Nach Registrierung und erfolgreichem Ersatzmethodentest sind nicht mehr benötigte SMS-/Voice-Zuordnungen bereinigt, damit aufschiebbare Kampagnenaufforderungen nicht unnötig weiterlaufen. [2]» Kommunikationsabsatz, übrige Zeilen und Plan unverändert.

### Arbeitsmittel: «6. Rollout-Freigabe und Nachsteuerung»

**Vorher CYOT-Zeile:** «… dokumentiertem Evaluations- und Produktionstest mit stufenweiser Verkehrsverlagerung … bestehende SMS-/Voice-Zielgruppen … nicht unbeabsichtigt geändert.»

**Nachher:** Evaluation ausdrücklich mit weiterhin Microsoft-bereitgestellter Codezustellung; separater Produktionsnachweis der Providerzustellung; stufenweise Erhöhung und Test nach jeder Stufe; bestehende Include- und Exclude-Gruppen erhalten. [9] [10] Neue anschliessende CYOT-Zeile für Telefoniebetrug, getrennte Kosten, Erneuerung von Integrationsnachweisen, Support und Beispiel-Failovergrenze. [8] [9] Übrige Kriterien, Auswahlkästchen, Entscheid und Unterschriftsfeld unverändert und nicht ausgefüllt.

### Arbeitsmittel: «Grenzen» und «Quellen»

**Grenzen vorher/nachher:** Ausschliesslich Datum im DSG-Absatz von 1. auf 15. November 2026; Fassung 7. Juli 2025, Rechtsvorbehalt und Original-Fachmarker unverändert. [7]

**Quellen vorher:** 10 Definitionen, [10] alte Setup-Adresse.

**Nachher:** [10] aktuelle Herstelleradresse/Titel wie Artikel [16]; [11] Novemberblog, [12] Transferanleitung, [13] Passkeyaktivierung und [14] bereits im Artikel verwendete Notfallkontoquelle ergänzt. Alle vier sind zitiert; keine neuen ungenutzten Definitionen.

## Unveränderte Abschnitte, Metadaten und Paketziele

Im Artikel bleiben H1, vollständige Kurzantwort, «Warum MFA allein nicht genügt», «Conditional Access in Stufen einführen», «Kommunikation ist eine Sicherheitskontrolle», «Typische Fehler, die Aussperrungen oder Scheinsicherheit erzeugen», die vollständige Tabelle samt anschliessendem Absatz «Umstiegsplan bis Februar 2027» und «Nächster Schritt» wortgleich. In den geänderten Abschnitten bleiben alle nicht oben genannten Absätze, Listen, Tabellen und Beispiele erhalten. Die Tabelle nutzt weiterhin die nun aktuelle Definition [16], ohne dass ihr dokumentierter GA-/Eignungsscope materiell geändert werden musste.

Im Arbeitsmittel bleiben H1, Artikelbezug, Statuszeile und Marker, «Anwendung» mit Organisation-/Tenant-/Freigabefeldern, gesamter Abschnitt «3. Conditional Access kontrolliert einführen», alle bisherigen leeren Risiko-, Pilot-, Richtlinien-, Test-, Kommunikations- und Unterschriftstabellen sowie die nicht genannten bestehenden Kontrollpunkte erhalten. Keine Zeile wurde als erfolgreich erledigt markiert.

`meta_title`, `meta_description`, Slugs, Autor, Veröffentlichungsdatum **29.10.2026** und Statuswerte **Entwurf – nicht freigegeben** beziehungsweise **Arbeitsvorlage – nicht freigegeben** sind unverändert. Keine SEO-Vorschlagsfelder angelegt. Alle Originalmarker **[FACHPRÜFUNG ERFORDERLICH]** bleiben wortgleich: drei im Artikel und vier im Arbeitsmittel einschliesslich Frontmatter. Das vorhandene `fachprüfung_status` bleibt unverändert. `rechtsstand` und `fachlich_geprüft_am` beziehungsweise `fachlich_geprueft_am` waren in diesen Originalen nicht vorhanden und wurden nicht angelegt; heutiger Rechtsquellenabgleich ist ausdrücklich kein historisches oder neues Fachfreigabedatum.

Interne Links unverändert. Vorhandene Paket-Slugs zum Arbeitsmittel, zum Bezugsartikel, zu CEO-Betrug/BEC und Microsoft-365-Sicherheitskonfiguration wurden anhand der lokalen Slugzeilen lesend bestätigt. Bestehende Paket-Service-/Kontaktziele `/unsere-dienstleistungen/sicherheitsanalyse`, `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/notfallplanung` und `/kontakt` bleiben erhalten; keine neuen internen Ziele erfunden. **Keine öffentliche Erreichbarkeit oder CMS-Prüfung dieser Ziele in diesem Auftrag.** Historische 403-/404-Messungen aus dem Laufstatus werden nicht als heutige Messungen wiederholt.

## Offene konkrete Fachfragen und Quellenblocker

**Tenant/Rollen/Fristen:** Ist die konkrete Umgebung in der Public Cloud? Welche Benutzer haben aktive gegenüber nur eligible GA-Rollen, und wann ist eine Rolle wirksam? Welche Gäste sind intern oder extern? Welche Personen sind für SMS/Voice aktiviert, welche Methoden registriert und welche tatsächlich verwendet? Welche SSPR-Wege brauchen Ersatz? Diese Daten wurden nicht erhoben. PIM-Aktivierung ist keine empfohlene Umgehung des früheren Termins. [1] [3]

**Pilot/Lizenzen/Methoden:** Welche Geräte, Profile, Attestierungen und Apps unterstützen die gewählte Methode tatsächlich? Ist der neue Erstregistrierungspfad für die konkrete Person schon ausgerollt, trotz älterer MFA-Voraussetzung in der Detailanleitung? Ist Gast-Passkey-Unterstützung wirklich vorhanden? Sind P1/P2 und weitere benötigte Lizenzen belegt? Ist CA im Berichtsmodus mit realen Anmeldungspfaden geprüft? Keine Lizenz-, Geräte-, Rollen-, Policy- oder Anmeldeprüfung durchgeführt. [7] [8] [9] [17] [19]

**Recovery/Notfallkonten:** Sind Identitätsprüfung, TAP-Laufzeit/-Rollen und sichere Übermittlung festgelegt? Sind interne/externe Guestpfade, Heimtenant-Vertrauen, Geräteverlust/-wechsel und Notfallzugänge getestet? Welche Authenticator-/Passkeysicherungen funktionieren auf den tatsächlichen Geräteprofilen? Das Januar-Rolloutversprechen ersetzt keinen heutigen Backupnachweis. Keine Durchführung oder forensische Fallprüfung. [10] [12] [17] [18]

**CYOT Schweiz/Provider:** Workforce/global Azure ist nur dokumentierter Herstellerumfang. Tenantberechtigung, Security-Store-Angebot, regionale Schweiz-Zustellung, Senderregistrierung, Kosten, Vertrag, Datenschutz, regulatorische Anforderungen, Azure-Zahlungs-/Ressourcen-/Appvoraussetzungen, Betrugsschutz, Nachweiserneuerung, Monitoring und Support bleiben konkret offen. Kein Soprano-, Telesign- oder Infobip-Angebot gekauft, getestet, empfohlen oder freigegeben. Evaluation und Providerproduktion, unveränderte Zielgruppen, Migration bis zur relevanten Frist und Failover müssen tatsächlich nachgewiesen werden. [14] [15] [16]

**Rechts-/Fachstatus:** DSG Art. 8 wurde als amtlicher Wortlaut erneut gelesen, nicht auf konkrete Verfahren angewandt. Angemessenheit von Passkeys, Logging, Aufbewahrung, Recovery, Providerdatenflüssen oder branchenspezifischen Massnahmen bleibt fachlich und gegebenenfalls rechtlich offen. [13] [22]

**Quellenblocker 1 – Roadmap 568076:** Allgemeine Seite erreichbar, spezifischer Eintrag nicht auslesbar. Keine erfolgreiche Detailprüfung behauptet. Bloghinweis auf neue eigenständige Windows-Hello-/Platform-SSO-MFA bleibt eine offene Detail-/Bereitstellungsfrage; bestehende CA-Orientierung nicht pauschal umgeschrieben. [17] [24]

**Historischer Belegvorbehalt – FAQ-Datum:** Vorjournal 26.10. gegenüber Git-Patch-Altdatum 20.10.2026 nicht aufgelöst; kein vollständiger historischer Learn-Snapshot. Die konkreten Patches sind lesbar und belegen die PIM-/GCC-Änderungen, aber nicht jeden damaligen Seiteninhalt. Keine Wiederholungsschleife zur unbelegten Altversion. [26] [27]

**Veröffentlichung:** Der Artikel ist mit Termin 29.10.2026 bereits terminlich fällig, bleibt jedoch nicht freigegeben. Das Arbeitsmittel bleibt nicht freigegebene Arbeitsvorlage. Keine CMS-/Browseroperation, kein Zugangsdatenzugriff, keine Veröffentlichung, kein Import, keine Live-Synchronisierung und kein heutiger öffentlicher Linktest. Der Ablauf erzeugt ausschliesslich lokale redaktionelle Quellenpflege.

## Lokaler Abschlussnachweis

Die gezielte einmalige Inhaltsprüfung vom 15.11.2026, Rückgabe **09:11:25 CET**, zählte mit Whitespace-Trennung **2'883 Haupttextwörter im Artikel** und **2'308 im Arbeitsmittel**, jeweils vor dem Quellenabschnitt und ohne Frontmatter. Beide Volltexte liegen damit über 1'400 Wörtern. Gesamtdokumente einschliesslich Metadaten und Quellen: 3'302 beziehungsweise 2'664 Wörter. Es bestehen **19 Definitionen = 19 zitierte IDs** im Artikel und **14 Definitionen = 14 zitierte IDs** im Arbeitsmittel; keine undefinierten oder ungenutzten Zitate. Eindeutige externe Paarquellen: 19. Beide Frontmatter-Stände sind exakt **15. November 2026**; sichtbare Arbeitsmittelversion passt zur Datumsversionskonvention. Kein scharfes s in den zwei Inhaltsdateien. Dies ist eine Struktur-/Konsistenzprüfung nur dieser Inhalte, kein globaler QA-Validator oder Fachtest.

## References

[1]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement "Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication"
[2]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2 "Microsoft Learn – Passkeys FIDO2 authentication method"
[3]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq "Microsoft Learn – SMS and voice retirement FAQ, sichtbarer Stand 4. November 2026"
[4]: https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B – Authentication and Authenticator Management"
[5]: https://www.bacs.admin.ch/de/26w5-de "BACS – SharePoint-Phishing-Welle, 3. Februar 2026"
[6]: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf "CISA – Implementing Phishing-Resistant MFA, Oktober 2022"
[7]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths "Microsoft Learn – Conditional Access authentication strengths"
[8]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication "Microsoft Learn – Plan a phishing-resistant passwordless deployment"
[9]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access "Microsoft Learn – Plan a Conditional Access deployment"
[10]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts"
[11]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz für Unternehmen und Behörden"
[12]: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass "Microsoft Learn – Configure Temporary Access Pass"
[13]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz, Art. 8, Stand 7. Juli 2025"
[14]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers "Microsoft Learn – CYOT-Übersicht, Stand 11. November 2026"
[15]: https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq "Microsoft Learn – CYOT-FAQ, Stand 11. November 2026"
[16]: https://learn.microsoft.com/en-us/entra/identity/authentication/choose-your-own-telephony-set-up "Microsoft Learn – CYOT-Setup im Entra admin center, Stand 11. November 2026"
[17]: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-november-2026/4556457 "Microsoft Entra Blog – What’s new in Microsoft Entra: November 2026, 6. November 2026"
[18]: https://learn.microsoft.com/entra/identity/authentication/how-to-transfer-authenticator-new-phone "Microsoft Learn – Transfer Microsoft Authenticator account entries to a new phone"
[19]: https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2 "Microsoft Learn – Enable passkeys FIDO2 in Microsoft Entra ID"
[20]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api "Microsoft Learn – Bisherige Setup-URL, aktueller Admin-Center-Text lesbar"
[21]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG-Chronologie"
[22]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – Amtliche DSG-XML-Fassung, Stand 7. Juli 2025"
[23]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign "Microsoft Learn – Registration campaign"
[24]: https://www.microsoft.com/microsoft-365/roadmap?id=568076 "Microsoft Roadmap – Eintrag 568076 im Originalabruf nicht auslesbar"
[25]: https://api.github.com/repos/MicrosoftDocs/entra-docs/commits?path=docs/identity/authentication/concept-sms-voice-retirement-faq.yml&per_page=5 "MicrosoftDocs – Gezielte FAQ-Commitliste"
[26]: https://api.github.com/repos/MicrosoftDocs/entra-docs/commits/97f0076fa66905c007afed675278db5bae9e644d "MicrosoftDocs – PIM-Rollenpräzisierung, Commit 2. November 2026"
[27]: https://api.github.com/repos/MicrosoftDocs/entra-docs/commits/4484dcdec83741a2980f114f44f41bd76b41ea51 "MicrosoftDocs – GCC-Präzisierung, Commit 4. November 2026"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/05-microsoft-365-mfa-passkeys.md:** `/resources/05-passkey-rollout-checkliste` → `https://www.dkschv.ch/wissen/resources/05-passkey-rollout-checkliste.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 2 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/notfallplanung` → `https://www.dkschv.ch/notfallplanung.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
