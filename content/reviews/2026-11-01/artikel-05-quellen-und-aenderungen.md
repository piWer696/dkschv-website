# Prüfbericht – Artikel 05: Microsoft 365 MFA und Passkeys

**Prüfdatum und Abrufzeit:** 1. November 2026, ISO-KW 44. Alle unten protokollierten Originalquellen wurden stateless am 1. November 2026 zwischen **09:05 und 09:09 CET, Europe/Zurich** abgerufen. Die Zeiten bezeichnen den tatsächlichen Abruf in diesem Prüfauftrag. Sie belegen weder einen historischen Wortlaut zu exakt 09:00 noch einen Tenant-Test.

**Geprüfte Dateien:**

- `blog-paket/articles/05-microsoft-365-mfa-passkeys.md`
- `blog-paket/resources/05-passkey-rollout-checkliste.md`

Der materielle neue Befund betrifft den zuvor nur angekündigten Telefonieanbieterweg: Microsoft dokumentiert «Choose Your Own Telephony Provider» (CYOT) seit dem 30. Oktober 2026 als allgemein verfügbar für **Microsoft Entra ID Workforce-Tenants in global Azure**. Die am selben Tag aktualisierte FAQ nennt Soprano, Telesign und Infobip und beschreibt Evaluations- sowie stufenweisen Produktivbetrieb. Das bestätigt die dokumentierte Produktbereitstellung im angegebenen Geltungsbereich. Es belegt **nicht**, dass ein bestimmter Tenant berechtigt ist, ein Anbieterangebot für die Schweiz verfügbar ist, regionale SMS-/Voice-Zustellung funktioniert oder die konkrete Azure-Integration produktiv arbeitet. [15] [16]

Alle 16 eindeutigen, nach der Aktualisierung in Artikel und Arbeitsmittel zitierten Quellenreferenzen wurden unmittelbar im Original gelesen. Die beiden vorhandenen Dateien enthalten damit 16/16 aktuell überprüfte externe Quellen. Zusätzlich geprüft wurden die amtliche Fedlex-Chronologie und XML-Fassung sowie zwei neue beziehungsweise vormerkte Originalquellen. Die Vollprüfung bezieht sich auf die tatsächlich in diesen zwei Dateien zitierten externen Quellen und die hier dokumentierten Zusatzquellen; sie ist keine Vollständigkeitszusage für nicht zitierte Hersteller-, Provider-, Rechts- oder Tenantinformationen.

## Quellenjournal: zitierte Originalquellen

1. **Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar, vollständiger relevanter Dokumentationsabschnitt lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 23.09.2026.  
   **Aussagegehalt:** Bestätigt die automatische Aktivierung von Passkeys für SMS-/Voice-aktivierte Benutzer ab 01.09.2026; den Rückzug der von Microsoft bereitgestellten SMS-/Voice-Übermittlung am 01.02.2027 für alle ausser Global Administrators und externen Benutzern; den 01.07.2027 für diese zwei Gruppen; interne Gäste verbleiben beim Februar-Termin. Nach den jeweiligen Terminen ist die Passkey-Aufforderung für Benutzer, deren einzige verfügbare MFA-Methode Microsoft-bereitgestelltes SMS oder Voice ist, blockierend. Ein temporärer Opt-out verzögert nur Aktivierung und Registrierungskampagne, nicht die Durchsetzung. [1]

2. **Microsoft Learn – Authentication methods in Microsoft Entra ID: passkeys FIDO2**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 06.04.2026.  
   **Aussagegehalt:** Bestätigt FIDO-basierte, herkunftsgebundene Public-Key-Kryptografie, lokale Entsperrung und die Unterscheidung von gerätegebundenen und synchronisierten Passkeys. Microsoft nennt Microsoft Authenticator und FIDO2-Sicherheitsschlüssel als gerätegebundene Beispiele. Synchronisierte Passkeys unterstützen keine Attestierung; bei erzwungener Attestierung sind nur gerätegebundene Passkeys zulässig. [2]

3. **Microsoft Learn – Frequently asked questions about SMS and voice retirement**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 26.10.2026.  
   **Aussagegehalt:** Bestätigt Public Cloud als zeitlichen Geltungsbereich, Azure AD B2C ausserhalb des Umfangs und die angekündigte gesonderte spätere Behandlung von Entra External ID. Ergänzend erklärt die FAQ, dass externe MFA-Methoden nicht vom Rückzug betroffen sind, sofern die Benutzer nicht zugleich für SMS/Voice aktiviert sind, und dass Passkey-Unterstützung für B2B- und interne Gastbenutzer bis Ende 2026 geplant ist. Dies ist eine Herstellerplanung, keine Bestätigung für einen bestimmten Tenant. [3]

4. **NIST SP 800-63B – Digital Identity Guidelines: Authentication and Authenticator Management**  
   **URL:** https://pages.nist.gov/800-63-4/sp800-63b.html  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar, relevanter Abschnitt lesbar.  
   **Sichtbare Version:** kein seitenbezogenes Tages- oder Revisionsdatum im abgerufenen Abschnitt festgestellt.  
   **Aussagegehalt:** Definiert Phishing-Resistenz als Schutz vor Offenlegung von Geheimnissen oder gültigen Authenticator-Ausgaben an einen vorgetäuschten Verifier. Verfahren mit manueller Eingabe eines Authenticator-Outputs, darunter Out-of-Band- und OTP-Authenticators, gelten nicht als phishing-resistent, weil die Eingabe nicht an die konkrete Sitzung gebunden ist. [4]

5. **BACS – Woche 5: Weltweite SharePoint-Phishing-Welle**  
   **URL:** https://www.bacs.admin.ch/de/26w5-de  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
   **Sichtbare Version:** veröffentlicht am 03.02.2026.  
   **Aussagegehalt:** Das BACS schildert Real-Time-Phishing mit Echtzeit-Anmeldung im Microsoft-Konto und Weitergabe der Zweitfaktor-Abfrage an die Phishing-Seite. Es empfiehlt unter anderem, unklare Nachrichten über einen alternativen Kommunikationskanal zu verifizieren und Mitarbeitende fortlaufend zu informieren. Der Bericht belegt keinen Vorfall in einem konkreten Microsoft-365-Tenant. [5]

6. **CISA – Implementing Phishing-Resistant MFA**  
   **URL:** https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; offizielle PDF erreichbar und lesbar.  
   **Sichtbare Version:** Dokument Oktober 2022.  
   **Aussagegehalt:** Ordnet FIDO/WebAuthn als weithin verfügbaren phishing-resistenten Ansatz ein. Die PDF beschreibt SMS/Voice als gegenüber Phishing, SS7-Schwachstellen und SIM-Swaps verwundbar und empfiehlt, Systeme ohne MFA-Unterstützung zu identifizieren und verbleibende Risiken an die Leitung zu eskalieren. Die CISA ist keine Schweizer Rechts- oder Microsoft-Tenant-Freigabestelle. [6]

7. **Microsoft Learn – Conditional Access authentication strengths**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 24.10.2025.  
   **Aussagegehalt:** Bestätigt Microsoft Entra ID P1 als Voraussetzung für Conditional Access und die integrierte Stärke «Phishing-resistant MFA» mit Windows Hello for Business beziehungsweise Platform Credential, FIDO2-Sicherheitsschlüssel und multifaktorieller zertifikatsbasierter Authentisierung. Authentisierungsstärken werden erst nach der initialen Authentisierung ausgewertet. [7]

8. **Microsoft Learn – Plan a phishing-resistant passwordless authentication deployment**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; relevant vollständige Abschnitte lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 26.03.2026.  
   **Aussagegehalt:** Empfiehlt einen personenbasierten Ansatz, repräsentative Test- und Pilotbenutzer statt nur Administratoren, eine Entra-Gruppe für den Piloten, den Authentication Methods Activity Report für Registrierung und Nutzung sowie Auswertung von Feedback und Helpdesk-Volumen. Genannte Betriebssystem-Mindeststände sind Orientierung, nicht für den konkreten Tenant oder jedes verwendete Gerät verifiziert. [8]

9. **Microsoft Learn – Plan a Conditional Access deployment**  
   **URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access  
   **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; relevante vollständige Abschnitte lesbar.  
   **Sichtbare Version:** zuletzt aktualisiert am 01.06.2026.  
   **Aussagegehalt:** Bestätigt das Vorgehen mit Test-/Pilotgruppe, Berichtsmodus, Anmeldeprotokollen und Kommunikation. Vor breiter Durchsetzung nennt Microsoft registrierte erforderliche Methoden, ausgenommene Notfallzugänge und Kommunikation als Voraussetzungen. Der Tipp nennt mindestens eine Woche Berichtsmodus vor Durchsetzung; die passende Dauer bleibt eine konkrete Fachentscheidung. [9]

10. **Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; relevante vollständige Abschnitte lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 05.06.2026.  
    **Aussagegehalt:** Bestätigt zwei oder mehr cloud-only Notfallzugangskonten auf `.onmicrosoft.com`, permanente aktive Global-Administrator-Zuweisung, eine zum regulären Adminweg unabhängige phishing-resistente Methode, sichere getrennte Aufbewahrung, Ausschluss von blockierenden oder einschränkenden Conditional-Access-Regeln sowie Monitoring und regelmässige Tests. Für die konkrete Policy-Ausnahme, Verwahrung und Überwachung ist kein Tenant-Test erfolgt. [10]

11. **BACS – Grundschutz: Schützen Sie Ihr Unternehmen und Ihre Behörde**  
    **URL:** https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
    **Sichtbare Version:** kein sichtbares Veröffentlichungs- oder Änderungsdatum im abgerufenen Inhalt.  
    **Aussagegehalt:** Das BACS verlangt ein Zusammenspiel technischer und organisatorischer Massnahmen und bezeichnet Cybersicherheit als Leitungsaufgabe. MFA ist als organisatorische Grundschutzmassnahme aufgeführt. Die Seite setzt keine spezifische Microsoft-Konfiguration oder gesetzliche Einzelfallpflicht fest. [11]

12. **Microsoft Learn – Configure Temporary Access Pass to register passwordless authentication methods**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; relevante vollständige Abschnitte lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 04.03.2026.  
    **Aussagegehalt:** Beschreibt TAP als zeitlich begrenzten, einmalig oder mehrfach nutzbaren Passcode für die Einrichtung passwortloser Methoden und die Wiederherstellung nach Verlust oder Vergessen einer starken Methode. Nur im Richtlinienumfang befindliche Benutzer können einen TAP verwenden. Der tatsächliche Wert ist nach dem Schliessen der Anzeige nicht erneut einsehbar. Rollen, Laufzeit, Identitätsprüfung und sichere Übermittlung bleiben Tenant-spezifisch zu prüfen. [12]

13. **Fedlex – Bundesgesetz über den Datenschutz, DSG, Art. 8**  
    **URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar, Art. 8 im stateless Abruf lesbar.  
    **Sichtbare Fassung:** durch die unten separat geprüfte amtliche Chronologie und XML-Fassung als Fassung mit Stand 07.07.2025 bestätigt.  
    **Aussagegehalt:** Art. 8 Abs. 1 verlangt von Verantwortlichem und Auftragsbearbeiter geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit; Abs. 2 verlangt, dass die Massnahmen Verletzungen der Datensicherheit vermeiden können. Daraus folgt keine automatische Angemessenheit einer Passkey-, TAP- oder CYOT-Konfiguration. [13] [17] [18]

14. **Microsoft Learn – Choose a telephony provider for SMS and voice authentication**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 23.09.2026.  
    **Aussagegehalt:** Die ältere Übersichtsseite beschreibt den damaligen privaten Vorschauzustand mit Soprano und Telesign und kündigt die Konfiguration ab 30.10.2026 an. Sie erklärt, dass das Unternehmen regionale Abdeckung, Vertragsbedingungen, Beschaffung, Datenschutz, regulatorische Anforderungen, Konfiguration und Serviceüberwachung verantwortet. Weil diese Seite vor der späteren GA-Dokumentation datiert, ist sie nicht allein als aktueller Verfügbarkeitsnachweis geeignet. [14]

15. **Microsoft Learn – Frequently asked questions about Choose Your Own Telephony Provider**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und vollständig lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 30.10.2026.  
    **Aussagegehalt:** Dokumentiert CYOT als allgemein verfügbar ab 30.10.2026 für Microsoft Entra ID Workforce-Tenants in global Azure. Die FAQ nennt Soprano, Telesign und Infobip. Sie beschreibt die Provider- und Azure-Kosten, Evaluationsmodus, stufenweise Verkehrsverlagerung, mögliche Verzögerung von Richtlinienänderungen bis etwa eine Stunde sowie die Verantwortungsaufteilung zwischen Microsoft, dem Unternehmen und dem Telekommunikationsanbieter. Die FAQ belegt keine Schweizer Providerabdeckung, kein Angebot für einen bestimmten Kunden und keinen erfolgreichen Produkttest. [15]

16. **Microsoft Learn – Set up SMS and voice with Choose Your Own Telephony Provider**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:06 CET; erreichbar und vollständig lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 30.10.2026.  
    **Aussagegehalt:** Beschreibt eine CYOT-Integration mit Azure Function in der Azure-Subscription des Unternehmens. Als Voraussetzungen nennt Microsoft einen Entra-Workforce-Tenant, Azure-Subscription mit gültiger Zahlungsmethode und Testbenutzer mit hinterlegter Nummer. Die Anleitung verlangt je nach Schritt spezifische Entra- und Azure-Berechtigungen, den Bezug eines Anbieterangebots, das Bereitstellen der Integration, Anbieterregistrierung, Policy-Update und Tests. Evaluation und anschliessende Produktion sollen mit niedrigem `migrationPercentage` beginnen; bestehende `includeTargets` sollen im Produktionstenant erhalten bleiben. Diese Anleitung wurde nur gelesen, nicht ausgeführt. [16]

## Zusätzlich geprüfte Originalquellen und Reichweite

17. **Fedlex – Chronologie zum DSG**  
    **URL:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/history  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und lesbar.  
    **Sichtbare Fassung:** Jüngster Chronologieeintrag: Berichtigung der Bundeskanzlei, Beschluss 02.07.2025, Inkrafttreten 07.07.2025, AS 2025 444.  
    **Aussagegehalt:** Die Chronologie verlinkt für diese Fassung ausdrücklich HTML, PDF, DOC und XML. Der bei eingeschränktem technischer Zugriff mögliche JavaScript-Hinweis ist daher kein Nachweis einer fehlenden Rechtsfassung. [17]

18. **Fedlex – amtliche XML-Fassung des DSG, Stand 07.07.2025**  
    **URL:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:05 CET; erreichbar und lesbar.  
    **Sichtbare Fassung:** 07.07.2025.  
    **Aussagegehalt:** Bestätigt den abgerufenen Wortlaut von Art. 8 Abs. 1–3. Die technische XML-Prüfung ersetzt keine Rechtsberatung und keine Prüfung, ob konkrete organisatorische oder technische Massnahmen angemessen sind. [18]

19. **Microsoft Learn – Run a registration campaign to set up a passkey or Microsoft Authenticator**  
    **URL:** https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:06 CET; Version gegen 09:09 CET erneut abgerufen; erreichbar und relevante Abschnitte lesbar.  
    **Sichtbare Version:** zuletzt aktualisiert am 12.10.2026.  
    **Aussagegehalt:** Bestätigt, dass eine Registrierungskampagne bei interaktiver MFA-Anmeldung zur Einrichtung auffordern kann. Für Passkey-Kampagnen müssen Passkey FIDO2 in der Authentication Methods Policy und «Allow self-service setup» aktiviert sein. Im Microsoft-managed Zustand sind Passkey-Nudges standardmässig unbegrenzt aufschiebbar. Die Quelle stützt die bereits vorhandene Unterscheidung zwischen aktivierter Methode, Aufforderung und tatsächlicher Registrierung; sie erforderte keine Textkorrektur. [19]

20. **BACS – Woche 42: Hotelbuchungs-Phishing zielt auf TWINT-Konten**  
    **URL:** https://www.bacs.admin.ch/de/26w42-de  
    **Abruf/Erreichbarkeit:** 01.11.2026, 09:07 CET; erreichbar und vollständig lesbar.  
    **Sichtbare Version:** veröffentlicht am 20.10.2026.  
    **Aussagegehalt:** Die vorgemerkte Meldung beschreibt kontextbezogenes E-Banking-/TWINT-Phishing, bei dem Opfer zur Preisgabe beziehungsweise Freigabe des zweiten Faktors verleitet werden. Sie stützt keine Entra-, Microsoft-365-, Passkey- oder Telefonieanbieter-spezifische Produktbehauptung. Es wurde deshalb keine künstliche Wochennews- oder CVE-Ergänzung im Evergreen-Text vorgenommen. [20]

**Erreichbarkeitsbilanz:** Alle 20 in diesem Bericht geführten Original-URLs lieferten beim Abruf verwertbaren Inhalt; es gab keine HTTP-Fehler. Die angegebene sichtbare Version ist die auf der jeweiligen Seite beziehungsweise im PDF tatsächlich festgestellte Datumsangabe. Fehlt eine solche Angabe, ist dies ausdrücklich vermerkt und nicht geschätzt.

## Materiell geänderte Passagen

### Artikel `05-microsoft-365-mfa-passkeys.md`

- **Frontmatter, Quellenstand:** Vorher «stand: 18. Oktober 2026» sowie ein Quellenumfang von 14 eindeutigen Referenzen. Nachher «stand: 1. November 2026», 16/16 zitierte Referenzen, die zusätzlich amtlich geprüfte Fedlex-Chronologie/XML und eine genaue Abgrenzung von dokumentierter CYOT-GA gegenüber fehlender Tenant-, Lizenz-, Provider- und Produktfreigabe.  
  **Grund:** Zwei am 30.10.2026 aktualisierte Microsoft-Originalquellen erweitern den belastbaren aktuellen Anbieterbefund. [15] [16]

- **Kurzantwort und sichtbarer Produktstandhinweis:** Vorher endete die Kurzantwort beim Passkey-Rollout und verlangte allgemein eine Prüfung von Herstellerterminen, Geltungsbereich, Lizenzen und Tenant-Einstellungen. Nachher enthält sie die enge Aussage «seit 30. Oktober 2026 allgemein verfügbar für Workforce-Tenants in global Azure» und stellt unmittelbar klar, dass Schweiz-, Provider- und Tenant-Eignung vor Einsatz nicht bewiesen ist. Der sichtbare Stand lautet nun 1. November 2026 und nennt zusätzlich konkrete CYOT-Providerabdeckung als Fachprüfungspunkt.  
  **Grund:** Der bisherige Hinweis «Konfiguration ab 30.10.2026» war nach Erreichen des Datums ohne weitere Prüfung nicht als tatsächliche Bereitstellung verwendbar. Nun stützt ihn die am 30.10. aktualisierte Microsoft-FAQ, aber nur im dokumentierten Scope. [15]

- **Abschnitt «Die Termine»:** Vorher: «Unternehmen ... können ab 30. Oktober 2026 einen unterstützten Telekommunikationsanbieter ... auswählen und konfigurieren. Am 18. Oktober 2026 ist diese Konfigurationsfunktion ... noch nicht verfügbar; in der privaten Vorschau nennt Microsoft Soprano und Telesign.» Nachher: Die ältere Übersicht wird ausdrücklich als vorheriger Vorschauzustand eingeordnet. Der neue Text nennt CYOT-GA für Workforce-Tenants in global Azure, die drei in der aktuellen FAQ genannten Anbieter sowie den konkreten Integrationsweg mit Anbieterangebot, Azure Function, Azure-Subscription, Evaluation und schrittweiser Produktionsumleitung.  
  **Grund:** Microsoft hat am 30.10. eine neuere FAQ und eine vollständige Setup-Anleitung veröffentlicht. Das ist eine materielle Produktstatusänderung gegenüber dem Stand 18.10.; keine Aussage über individuelle Implementierbarkeit. [14] [15] [16]

- **Tabelle «Umstiegsplan bis Februar 2027»:** Vorher: Die Providerkonfiguration «wird laut Microsoft erst ab 30. Oktober 2026 verfügbar». Nachher: CYOT ist «seit 30. Oktober 2026» im genannten Scope dokumentiert allgemein verfügbar, aber Anbieterangebot, regionale Abdeckung einschliesslich Schweiz, Azure-Voraussetzungen sowie Evaluations- und Produktionstest müssen vor Nutzung belegt werden.  
  **Grund:** Der Arbeitsplan darf aus einem verstrichenen Termin keine pauschale Betriebsbereitschaft ableiten. [15] [16]

- **Fedlex-Hinweis im Wiederherstellungsabschnitt:** Nur das Abrufdatum wechselte von 18. Oktober auf 1. November 2026; die verifizierte Fassung bleibt 7. Juli 2025.  
  **Grund:** Chronologie und amtliche XML-Fassung wurden am heutigen Datum erneut abgeglichen. [17] [18]

### Arbeitsmittel `05-passkey-rollout-checkliste.md`

- **Frontmatter und sichtbare Arbeitsmittelversion:** Vorher «Stand 18. Oktober 2026». Nachher einheitlich «Stand 1. November 2026» mit dem gleichen 16/16-Quellenumfang und Quellenstatus wie der Artikel.  
  **Grund:** Arbeitsmittel und Artikel sollen beim dokumentierten Informationsstand konsistent sein.

- **Abschnitt «Zweck»:** Vorher beschrieb die Checkliste den angekündigten Konfigurationsstart und die am 18.10. noch fehlende Funktion. Nachher beschreibt sie die dokumentierte GA ab 30.10. für Workforce-Tenants in global Azure, die drei genannten Anbieter sowie die harten Abgrenzungen: keine Bestätigung für Schweizer regionale Zustellung, konkretes Angebot, Tenant-Berechtigung, Lizenz oder Integration.  
  **Grund:** Gleicher materieller CYOT-Statuswechsel wie im Artikel. [15] [16]

- **Neue Kontrollpunkte in «Ausgangslage und Entscheidungsrahmen»:** Ergänzt wurden der Nachweis, warum bei SMS-/Voice-Ausnahme keine phishing-resistente Methode genügt, sowie die fachliche Prüfung von Workforce-Tenant/global Azure, Angebot, regionaler Abdeckung einschliesslich Schweiz, Vertrag, Kosten, Datenschutz und Azure-Subscription.  
  **Grund:** Microsoft weist diese Verantwortlichkeiten dem Unternehmen zu. Der Kontrollpunkt ersetzt keine Beschaffungs-, Datenschutz- oder Fachfreigabe. [14] [15] [16]

- **Neue Kontrollpunkte in «Wiederherstellung» und «Rollout-Freigabe»:** Ergänzt wurden der Umgang mit CYOT-Zustellungsausfall im Wiederherstellungsablauf sowie die Anforderung an dokumentierten Evaluations- und Produktionstest mit stufenweiser Verkehrsverlagerung bei unveränderten SMS-/Voice-Zielgruppen.  
  **Grund:** Die neue Setup-Anleitung empfiehlt Evaluation, schrittweise Migration und das Bewahren bestehender `includeTargets` in Produktion. [16]

- **Fedlex-Hinweis unter «Grenzen»:** Nur das Abrufdatum wechselte auf 1. November 2026. Die ausgewiesene Fassung von Art. 8 DSG bleibt Stand 7. Juli 2025. [17] [18]

## Unveränderte Metadaten, Schutzmarker und Struktur

Die SEO-Importfelder wurden nicht geändert. Im Artikel bleiben `meta_title` und `meta_description` unverändert. Im Arbeitsmittel bleiben ebenfalls `meta_title` und `meta_description` unverändert. Es wurden keine Felder `meta_title_vorschlag` oder `meta_description_vorschlag` angelegt, weil keine konkret belegte SEO-Korrektur vorlag.

Unverändert bleiben ferner die Slugs `/wissen/microsoft-365-mfa-passkeys` und `/resources/05-passkey-rollout-checkliste`, das ursprüngliche Veröffentlichungsdatum des Artikels `29.10.2026`, die Statuswerte «Entwurf – nicht freigegeben» beziehungsweise «Arbeitsvorlage – nicht freigegeben», die internen relativen Verweise und das Feld `fachprüfung_status`.

Alle bestehenden **[FACHPRÜFUNG ERFORDERLICH]**-Marker bleiben erhalten: drei im Artikel und vier im Arbeitsmittel, jeweils einschliesslich der Frontmatter-Marker. Kein `fachlich_geprueft_am` und kein `rechtsstand` wurden angelegt. Die nun dokumentierte Fedlex-Fassung 07.07.2025 betrifft nur den amtlich gelesenen Gesetzeswortlaut und ist keine Individual- oder Rechtsfreigabe.

## Verbleibende genaue Blocker

1. **Tenant- und Lizenznachweis fehlt:** Es wurde kein Microsoft-Entra-Tenant geöffnet, keine Benutzerklassifikation geprüft und keine Lizenz, Conditional-Access-Policy, Passkey-Profil-, TAP- oder Emergency-Access-Einstellung getestet. Insbesondere bleiben die konkrete Rolle interner gegenüber externer Gastbenutzer, die Public-Cloud-Anwendbarkeit und die wirksamen Authentisierungsmethoden offen.

2. **CYOT-Eignung für die konkrete Organisation ist offen:** Die Microsoft-Dokumentation bestätigt nur Workforce-Tenants in global Azure. Nicht geprüft wurden Berechtigung und technische Voraussetzungen eines bestimmten Tenants, die Azure-Subscription mit Zahlungsmittel, erforderliche Entra-/Azure-Berechtigungen, Security-Store-Angebot, Vertrags- und Kostenlage, Schweizer regionale SMS-/Voice-Abdeckung, Senderregistrierung, Datenschutz- und regulatorische Anforderungen, Provider-Fraud-Controls, Hochverfügbarkeit, Serviceüberwachung und Failover. Weder Soprano, Telesign noch Infobip wird für die Schweiz, einen Tenant oder einen Anwendungsfall empfohlen oder freigegeben.

3. **Kein Produktiv- oder Evaluationstest:** Die in der Quelle beschriebenen Azure-Function-, Policy-, Evaluation- und Produktionstests wurden nicht durchgeführt. Es gibt keinen Nachweis über Codezustellung, Protokolle, `CyotEvaluation` oder `Cyot`, Rückfall, Wiederherstellung oder schrittweise Verkehrsverlagerung. Eine dokumentierte allgemeine Verfügbarkeit darf nicht mit einer erfolgreich eingerichteten Konfiguration gleichgesetzt werden.

4. **Fach- und Rechtsfragen offen:** Die Angemessenheit konkreter Passkey-, Notfallzugangs-, Recovery-, Logging-, Aufbewahrungs-, Provider- und Datenschutzmassnahmen nach DSG Art. 8 ist für keinen Bearbeitungskontext bewertet. Bestehende [FACHPRÜFUNG ERFORDERLICH]-Marker sind keine Formalität, sondern vor einer produktiven Umsetzung durch fachlich zuständige Personen zu behandeln. Die Quellenpflege ersetzt keine Rechts-, Sicherheits-, Beschaffungs-, Datenschutz- oder Tenantfreigabe.

5. **Keine öffentliche oder Live-Prüfung:** Es wurde weder ein CMS geöffnet noch ein CMS-Login, eine Webador- oder sonstige Live-Änderung vorgenommen. Die öffentlichen Ziel-URLs interner relativer Slugs wurden in diesem Auftrag nicht geprüft; sie bleiben Planungswerte für die übergeordnete Prüfung. Es gibt keine neue Live-URL, keinen Veröffentlichungszeitpunkt und keine behauptete Live-Synchronisierung.

## Abschlussstatus

Die lokale Quellenpflege ist auf **1. November 2026** aktualisiert. Der Artikel umfasst nach der Änderung 2'710 Wörter und bleibt damit deutlich über der Mindestvorgabe von 1'400 Wörtern. Die abschliessende Strukturprüfung fand 16 definierte und 16 verwendete Quellen im Artikel sowie 10 definierte und 10 verwendete Quellen im Arbeitsmittel; es bestehen keine undefinierten oder ungenutzten Zitationen. Geändert wurden ausschliesslich die zwei zugewiesenen Inhaltsdateien und dieser Prüfbericht. Globale Manifeste, QA-Skripte und CMS-Inhalte blieben unangetastet.

**References**

[1]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement "Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication"
[2]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2 "Microsoft Learn – Authentication methods in Microsoft Entra ID: passkeys FIDO2"
[3]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq "Microsoft Learn – Frequently asked questions about SMS and voice retirement"
[4]: https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B – Digital Identity Guidelines: Authentication and Authenticator Management"
[5]: https://www.bacs.admin.ch/de/26w5-de "BACS – Woche 5: Weltweite SharePoint-Phishing-Welle"
[6]: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf "CISA – Implementing Phishing-Resistant MFA"
[7]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths "Microsoft Learn – Conditional Access authentication strengths"
[8]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication "Microsoft Learn – Plan a phishing-resistant passwordless authentication deployment"
[9]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access "Microsoft Learn – Plan a Conditional Access deployment"
[10]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID"
[11]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz: Schützen Sie Ihr Unternehmen und Ihre Behörde"
[12]: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass "Microsoft Learn – Configure Temporary Access Pass to register passwordless authentication methods"
[13]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Art. 8"
[14]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers "Microsoft Learn – Choose a telephony provider for SMS and voice authentication"
[15]: https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq "Microsoft Learn – Frequently asked questions about Choose Your Own Telephony Provider"
[16]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api "Microsoft Learn – Set up SMS and voice with Choose Your Own Telephony Provider"
[17]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – Chronologie zum Datenschutzgesetz"
[18]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – Amtliche XML-Fassung DSG, Stand 7. Juli 2025"
[19]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign "Microsoft Learn – Run a registration campaign to set up a passkey or Microsoft Authenticator"
[20]: https://www.bacs.admin.ch/de/26w42-de "BACS – Woche 42: Hotelbuchungs-Phishing zielt auf TWINT-Konten"
