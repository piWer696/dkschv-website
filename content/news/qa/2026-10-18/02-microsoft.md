# Microsoft Identitaetssicherheit – Quellenotizen

- **Newsfenster:** 11.10.2026 09:00 bis 18.10.2026 09:00 Europe/Zurich.
- **Tatsaechliche Abrufe:** 18.10.2026 ab 09:04 Europe/Zurich (Tool-Logs). Bei nicht versionierten Seiten kein minutengenauer historischer Wortlaut garantiert.
- **Vorwochenausgabe abgegrenzt:** 2026-10-11_DKSchV_Branchennews.md behandelte FortiMail, NetScaler, BACS und Oversharing; Microsoft war dort nur als geprueftes Umfeld ohne belastbare neue Wochenmeldung genannt.

## Belegte neue Meldung

### 1. Oktober 2026 Security Update (MSRC)
- URL: https://www.microsoft.com/en-us/msrc/blog/2026/10/202610-security-update
- Titel: 2026 年 10 月のセキュリティ更新プログラム (月例)
- Seitentext datiert 12.10.2026; Release der Updates: 13.10.2026 US-Zeit.
- MSRC/Japan Security Team nennt als vorab aktiv ausgenutzt bestaetigte Luecke ausschliesslich CVE-2026-96951 (Windows Shell Security Feature Bypass). Nicht als bloss moegliche Schwachstelle formulieren.
- Betroffene Produktfamilien laut Bulletin: Windows 11, Windows Server 2025/2022/2019/2016, Office, SharePoint, Exchange Server, SQL Server, .NET, Visual Studio, Dynamics, Azure und System Center. Maximalfolgen reichen je Produkt von RCE (u.a. Windows/Office/SharePoint/Exchange/.NET/Visual Studio) bis wichtige Einstufungen; konkrete KBs fuer Windows: 5127648/5127646/5126653, Server 2025 5126646, Server 2022 5126655, Server 2019 5126651, Server 2016 5126868. Exchange-Guidance ist separat verlinkt.
- Zwei bestehende CVE-Eintraege (CVE-2026-69896, CVE-2026-62737) wurden nur um Danksagungen aktualisiert. Neue Advisory ADV260001 betrifft ReFS-Hardening auf Wechseldatentraegern; ab Updates ab 13.10.2026 eingefuehrt, aber bis 2027 standardmaessig nicht aktiviert. Naechster Patch-Tuesday laut Quelle: 10.11.2026 US-Zeit.
- Geltungsbereich: Hersteller-Update-/Advisory-Information; konkrete Betroffenheit haengt von Produkt, Version, Rolle und Deployment ab. Keine Schweizer Rechtsfrist.

## Abgrenzung / keine neue Meldung im Fenster

- Microsoft Security Blog: https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/ – Titel/Datum 13.07.2026, daher Vorfenster. Bestaetigt wurden nur die bereits bekannten Termine: Passkey-Autoenablement 01.09.2026, Provider-Konfiguration ab 30.10.2026, Microsoft-SMS/Voice-Ruhestand 01.02.2027; Public Cloud only. Nicht als neue Wochenmeldung ausgeben.
- Microsoft Learn: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement – Last updated 23.09.2026, daher Vorfenster. Verifiziert: 01.09.2026 automatische Passkey-Aktivierung fuer SMS/Voice-Nutzer; 30.10.2026 Providerwahl im Microsoft Security Store; 01.02.2027 Ruhestand fuer alle ausser Global Administrators/externe Nutzer (interne Gaeste eingeschlossen); 01.07.2027 fuer Global Administrators und externe Nutzer. Initiale Provider Soprano/Telesign Private Preview; Anbieter-/Telephony-Funktion nicht als Lizenzfreiheit behaupten. Temporarer Opt-out nur fuer automatische Aktivierung (Graph beta Policy.ReadWrite.AuthenticationMethod, passkeyDynamicMigration=true), kein Opt-out der spaeteren Durchsetzung. Tenant-Konfiguration und Nutzerpopulation entscheiden.
- Microsoft Learn Entra releases: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new – abgerufene Seite zeigte als aktuellste Sektionen Juni bis Januar 2026, keine belegte Meldung datiert 11.–18.10.2026; enthaltene Connect-/Preview-/Lizenzhinweise sind daher nicht als neue Fenster-Meldung aufgenommen.
- MSRC Risk Cohorts: https://www.microsoft.com/en-us/msrc/blog/2026/10/using-risk-cohorts-to-prioritize-security-updates – 13.10.2026. Neue explorative Triage-Methode, aber keine Fix-/Produktänderung: provisorisch, keine offiziellen Microsoft-Kategorien, ersetzt keine CVE-Einzelprüfung und aendert keine Update-Guidance. Nicht als substanzielle Identitaetsfixmeldung aufgenommen; kann als Kontext erwaehnt werden.

## Recherchegrenze

Nur maximal eine substanzielle neue Microsoft-Meldung aufgenommen. Keine Vollstaendigkeitszusage fuer alle Microsoft-Portale, Tenants oder nicht indexierte Release Notes. Lizenz-/Preview-/Tenant-Aussagen nur dort, wo die jeweilige Originalquelle sie explizit nennt.
