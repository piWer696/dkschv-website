# DKSchV Schweiz // nDSG-Compliance-Paket für Schweizer KMU
**Dokumenten-Klassifikation:** Offizielles Vorlagenpaket  
**Geltungsbereich:** Neues Schweizer Datenschutzgesetz (nDSG) & Datenschutzverordnung (DSV)  
**Herausgeber:** DKSchV Datenschutz & IT-Sicherheit Schweiz (dkschv.ch)

---

## 1. VERZEICHNIS DER BEARBEITUNGSTÄTIGKEITEN (VdT) GEMÄSS ART. 12 nDSG

> [!NOTE]
> Schweizer KMU (unter 250 Mitarbeitende) sind nach Art. 24 DSV zwar von der VdT-Pflicht ausgenommen, **es sei denn**, sie bearbeiten besonders schützenswerte Personendaten in grossem Umfang oder führen ein Profiling mit hohem Risiko durch.  
> **Praxis-Empfehlung von DKSchV:** Jedes seriöse Schweizer KMU sollte dieses Verzeichnis führen, um bei Auskunftsbegehren (Art. 25 nDSG) und Haftungsfragen sofort rechenschaftsfähig zu sein.

### Muster-Eintragstabelle (Kernbereiche):

| Bereich / Prozess | Zweck der Datenbearbeitung | Kategorien von Personen | Kategorien bearbeiteter Daten | Empfänger / Auftragsbearbeiter | Aufbewahrungsfrist | Speicherort & Schutz |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Personalwesen / HR** | Arbeitsvertrag, Lohnabrechnung, Sozialversicherungen | Mitarbeitende, Bewerber | Stammdaten, AHV-Nr., Bankdaten, Lohndaten, Krankheitsmeldungen | Ausgleichskasse, Pensionskasse, Treuhänder, SUVA | 10 Jahre (OR 962) / Bewerber 3 Monate | HR-Server Schweiz, Zugriff nur GF/HR, 2FA |
| **Kundenverwaltung & CRM** | Angebotserstellung, Vertragsabwicklung, Support | B2B/B2C-Kunden, Ansprechpartner | Name, E-Mail, Telefon, Bestelldaten, Zahlungsinformationen | ERP/CRM-Provider, Zahlungsdienstleister (z.B. Stripe) | 10 Jahre (Handelsrechtliche Aufbewahrung) | Cloud-Hosting (CH/EU), Verschlüsselt |
| **Website & E-Commerce** | Bestellabwicklung, Web-Analytics, Kontaktformular | Website-Besucher, Shop-Käufer | IP-Adresse, Cookie-IDs, Lieferanschrift, Zahlungsstatus | Webhosting-Provider (CH), Stripe Payments | Sitzungsdauer bzw. Kaufbelege 10 Jahre | TLS 1.3, Cookie-Banner, Serverstandort CH |
| **Videoüberwachung / Zutritt** | Objektschutz, Diebstahlprävention | Besucher, Mitarbeitende | Videobildaufnahmen, Zutritts-Logs | Interner Sicherheitsverantwortlicher, ggf. Polizei | Automatische Löschung nach 72 Stunden | Lokaler NVR-Rekorder, gesicherter Serverraum |

---

## 2. KATALOG DER TECHNISCHEN & ORGANISATORISCHEN MASSNAHMEN (TOM)
*Erfüllung der Datensicherheitsanforderungen nach Art. 8 nDSG i.V.m. Art. 1–4 DSV*

### A. Vertraulichkeit (Zutritts-, Zugangs- und Zugriffskontrolle)
1. **Physische Sicherheit:** Serverraum alarmgesichert, Zutritt nur für autorisierte IT-Mitarbeiter per Badge/Schlüssel. Clean-Desk-Policy in allen Büros.
2. **Authentifizierung:**
   - [x] Obligatorische **Zwei-Faktor-Authentifizierung (2FA / MFA)** für alle Cloud-Dienste (M365, Mail, CRM, Admin-Panels).
   - [x] Mindestpasswortlänge: 14 Zeichen, Verwendung eines zentralen Passwort-Managers (z.B. Bitwarden/1Password).
3. **Rollen- & Rechtekonzept:** Least-Privilege-Prinzip. Mitarbeitende haben nur Zugriff auf Daten, die sie für ihre tägliche Arbeit zwingend benötigen. Keine dauerhaften Domain-Admin-Rechte auf Arbeitsplatz-PCs.

### B. Integrität (Weitergabe- und Eingabekontrolle)
1. **Verschlüsselung:**
   - **Data at Rest:** Vollverschlüsselung aller Laptops und Mobilgeräte (BitLocker / FileVault / LUKS). Datenbanken verschlüsselt (AES-256).
   - **Data in Transit:** Sämtlicher externer Datenverkehr über TLS 1.3 / HTTPS. Remote-Zugriff nur via verschlüsseltes VPN mit Zertifikaten und MFA.
2. **Protokollierung:** Automatisierte Erfassung von Login-Versuchen, Systemänderungen und Datei-Exporten (Syslog-Server).

### C. Verfügbarkeit & Belastbarkeit (Wiederherstellbarkeit)
1. **3-2-1-1-0 Backup-Regel:**
   - 3 Kopien aller kritischen Geschäftsdaten.
   - 2 unterschiedliche Medienarten (z.B. NAS + Cloud).
   - 1 Kopie an einem externen Schweizer Standort.
   - 1 Kopie **vollständig offline / air-gapped oder unlöschbar (Immutable Backup)** gegen Ransomware.
   - 0 Fehler: Vierteljährliche, dokumentierte Restore-Tests.
2. **USV (Unterbrechungsfreie Stromversorgung):** Pufferung für Server und Netzwerk-Switches bei Stromausfall.

---

## 3. MUSTER: AUFTRAGSBEARBEITUNGSVERTRAG (ADV) NACH ART. 9 nDSG

*(Dieser Vertrag wird zwischen Ihrem Unternehmen als Auftraggeber und externen Dienstleistern wie IT-Betreuern, Cloud-Providern oder Marketingagenturen geschlossen)*

**Vereinbarung über die Auftragsbearbeitung von Personendaten**

Zwischen  
**[Name Ihres Unternehmens, Adresse, Schweiz]** (nachfolgend „Auftraggeber“)  
und  
**[Name des Dienstleisters, Adresse]** (nachfolgend „Auftragsbearbeiter“)

### § 1 Gegenstand und Dauer
Der Auftragsbearbeiter erbringt für den Auftraggeber Dienstleistungen im Bereich [z.B. IT-Wartung / Webhosting / CRM]. Im Rahmen dieser Tätigkeit erhält der Auftragsbearbeiter Zugriff auf Personendaten des Auftraggebers.

### § 2 Pflichten des Auftragsbearbeiters (Art. 9 Abs. 1 nDSG)
1. Der Auftragsbearbeiter verpflichtet sich, Personendaten ausschließlich so zu bearbeiten, wie es der Auftraggeber selbst tun dürfte, und nur nach dokumentierter Weisung des Auftraggebers.
2. Eine Bearbeitung zu eigenen Zwecken oder Weitergabe an Dritte ist untersagt.
3. Der Auftragsbearbeiter garantiert die Einhaltung angemessener technischer und organisatorischer Massnahmen gemäss Art. 8 nDSG (Anhang 1 dieser Vereinbarung).

### § 3 Hinzuziehung von Unterauftragsbearbeitern (Subunternehmern)
Die Beauftragung von weiteren Dienstleistern ist nur mit vorheriger schriftlicher Genehmigung des Auftraggebers gestattet.

### § 4 Meldepflicht bei Sicherheitsverletzungen
Erlangt der Auftragsbearbeiter Kenntnis von einer Verletzung der Datensicherheit (z.B. Hackerangriff, Datenabfluss, Fehlversand), ist er verpflichtet, den Auftraggeber **unverzüglich, spätestens jedoch innert 24 Stunden**, schriftlich zu benachrichtigen.

### § 5 Löschung und Rückgabe nach Vertragsende
Nach Beendigung der vertraglichen Arbeiten hat der Auftragsbearbeiter sämtliche Personendaten nach Wahl des Auftraggebers entweder vollständig und datenschutzkonform zu vernichten oder an diesen zurückzugeben.

**Ort, Datum:** ________________________  
**Unterschrift Auftraggeber:** ________________________  
**Unterschrift Auftragsbearbeiter:** ________________________

---

## 4. MUSTER: ANTWORT AUF AUSKUNFTSBEGEHREN (Art. 25 nDSG)

> **Frist:** Das Auskunftsbegehren muss innert **30 Tagen** kostenlos beantwortet werden!  
> **Identitätsprüfung:** Vor Erteilung der Auskunft muss die Identität des Anfragenden (z.B. durch Kopie der ID/Pass) zweifelsfrei geprüft werden.

### Vorlage Antwortschreiben:
Sehr geehrte/r [Name],  
Bezug nehmend auf Ihr Auskunftsbegehren vom [Datum] teilen wir Ihnen hiermit gemäss Art. 25 des Bundesgesetzes über den Datenschutz (nDSG) mit:  
1. **Verarbeitete Personendaten:** Wir haben zu Ihrer Person folgende Stammdaten gespeichert: [Auflistung: Vorname, Name, Adresse, E-Mail, Bestellhistorie].
2. **Bearbeitungszweck:** Die Daten wurden ausschließlich zur Abwicklung unseres Kaufvertrags vom [Datum] erhoben und verwendet.
3. **Aufbewahrungsdauer:** Wir bewahren Ihre Rechnungsdaten gemäss den gesetzlichen handels- und steuerrechtlichen Pflichten (Art. 958f OR) für 10 Jahre auf.
4. **Empfänger:** Ihre Daten wurden ausschließlich an unseren Versanddienstleister [z.B. Schweizerische Post] zur Zustellung weitergegeben. Eine Übermittlung ins Ausland findet nicht statt.  

Mit freundlichen Grüßen,  
[Name / Datenschutzverantwortlicher]
