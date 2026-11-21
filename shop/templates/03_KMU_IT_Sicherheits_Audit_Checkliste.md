# DKSchV Schweiz // KMU IT-Sicherheits-Audit & Baseline-Prüfprotokoll
**Dokumenten-Klassifikation:** Prüf- und Auditvorlage  
**Prüfstandard:** BACS IT-Grundschutz Schweiz / CIS Critical Security Controls v8  
**Herausgeber:** DKSchV Cyber-Security Schweiz (dkschv.ch)

---

## 1. MANAGEMENT SUMMARY (Management-Zusammenfassung)

*Diese Übersicht dient der Geschäftsleitung als Entscheidungsgrundlage für IT-Budgets und Risikominimierung.*

* **Unternehmen:** __________________________________
* **Audit-Datum:** __________________________________
* **Prüfer / Auditor:** __________________________________
* **Gesamt-Sicherheitsbewertung:**
  - [ ] **GRÜN (Geringes Risiko):** Solide Sicherheitsstandards, Baseline erfüllt (>85% Konformität).
  - [ ] **GELB (Mittleres Risiko):** Sicherheitslücken vorhanden, sofortige Maßnahmen empfohlen (60-84%).
  - [ ] **ROT (Kritisches Risiko):** Akute Gefahr durch Ransomware/Einbruch (<60% Konformität).

---

## 2. AUDIT-PRÜFKATALOG (75+ KONTROLLPUNKTE)

### Modul 1: Identitäts- & Zugriffsmanagement (IAM)

| Nr. | Prüfkriterium | Soll-Zustand | Ist-Zustand | Status (OK / Mangel / Kritisch) | Handlungsbedarf / Notiz |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Multi-Faktor-Authentifizierung (MFA)** | Verpflichtend für alle Benutzer bei Cloud-Diensten, Mail & VPN | Aktiviert für alle / nur Admins / Keine | [ ] OK [ ] Mangel [ ] Kritisch | |
| **1.2** | **Passwort-Richtlinien** | Min. 14 Zeichen, keine schwachen Passwörter, Passwort-Manager | Mindestanforderung: | [ ] OK [ ] Mangel [ ] Kritisch | |
| **1.3** | **Privilegierte Konten (Admins)** | Strikte Trennung von Admin- und Standard-Benutzerkonten | Getrennte Konten vorhanden? | [ ] OK [ ] Mangel [ ] Kritisch | |
| **1.4** | **Offboarding-Prozess** | Sofortiger Entzug aller Berechtigungen bei Austritt innert 24h | Dokumentiert und eingehalten? | [ ] OK [ ] Mangel [ ] Kritisch | |
| **1.5** | **Inaktive Benutzerkonten** | Automatische Deaktivierung nach 60 Tagen Inaktivität | Bereinigung erfolgt regelmäßig? | [ ] OK [ ] Mangel [ ] Kritisch | |

---

### Modul 2: Netzwerk, Perimeter & Fernzugriff

| Nr. | Prüfkriterium | Soll-Zustand | Ist-Zustand | Status | Handlungsbedarf |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | **Offene Ports (Firewall)** | Keine ungesicherten Ports (RDP 3389, SMB 445) ins Internet | Port-Scan von extern durchgeführt? | [ ] OK [ ] Kritisch | |
| **2.2** | **Netzwerk-Segmentierung (VLANs)** | Trennung: Büro-PCs, Server, Gäste-WLAN, IoT/Kameras | Segmentierung vorhanden? | [ ] OK [ ] Mangel | |
| **2.3** | **VPN-Sicherheit** | Nur verschlüsseltes VPN (WireGuard/OpenVPN/IPsec) mit MFA | Remote-Zugriff geprüft? | [ ] OK [ ] Mangel | |
| **2.4** | **Gäste-Netzwerk** | Gäste-WLAN vollständig isoliert vom internen Firmennetz | Kein Zugriff auf Firmen-Ressourcen?| [ ] OK [ ] Mangel | |

---

### Modul 3: Endgeräte, Härtung & Patch-Management

| Nr. | Prüfkriterium | Soll-Zustand | Ist-Zustand | Status | Handlungsbedarf |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Laufwerksverschlüsselung** | 100% aller mobilen Geräte (Laptops) vollverschlüsselt | BitLocker / FileVault aktiv? | [ ] OK [ ] Kritisch | |
| **3.2** | **Endpoint Protection (EDR/AV)** | Zentral gemanagter Viren- & Ransomware-Schutz auf allen Clients | EDR-Lösung installiert und aktuell? | [ ] OK [ ] Kritisch | |
| **3.3** | **Betriebssystem-Updates** | Automatische Installation von Sicherheits-Patches innert 7 Tagen | Patch-Status überprüft? | [ ] OK [ ] Mangel | |
| **3.4** | **Lokale Administratorrechte** | Anwender haben **keine** lokalen Admin-Rechte auf ihren PCs | Rechte eingeschränkt? | [ ] OK [ ] Mangel | |
| **3.5** | **USB-Port-Sicherheit** | Richtlinie oder technische Sperre gegen unbefugte USB-Datenträger| Richtlinie kommuniziert? | [ ] OK [ ] Mangel | |

---

### Modul 4: Backup, Notfall-Wiederherstellung & Resilienz

| Nr. | Prüfkriterium | Soll-Zustand | Ist-Zustand | Status | Handlungsbedarf |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Unveränderbare Backups (Immutability)** | Backups können nicht durch Ransomware überschrieben/gelöscht werden| Immutable Storage / WORM aktiv? | [ ] OK [ ] Kritisch | |
| **4.2** | **Offline / Air-Gapped Kopie** | Mindestens 1 monatliche/wöchentliche Offline-Sicherung | Getrenntes Medium vorhanden? | [ ] OK [ ] Kritisch | |
| **4.3** | **Dokumentierter Restore-Test** | Mindestens halbjährlicher realer Wiederherstellungstest | Datum des letzten Tests: | [ ] OK [ ] Mangel | |
| **4.4** | **RPO / RTO definiert** | Maximaler tolerierbarer Datenverlust & Ausfallzeit festgelegt | RPO: _____ Std. / RTO: _____ Std. | [ ] OK [ ] Mangel | |

---

### Modul 5: Mensch, Phishing & Schulung (Awareness)

| Nr. | Prüfkriterium | Soll-Zustand | Ist-Zustand | Status | Handlungsbedarf |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5.1** | **Sicherheits-Schulung** | Jährliche Awareness-Schulung für alle Angestellten | Letzte Schulung: | [ ] OK [ ] Mangel | |
| **5.2** | **Phishing-Simulationen** | Regelmäßige simulierte Phishing-Tests zur Sensibilisierung | Werden Tests durchgeführt? | [ ] OK [ ] Mangel | |
| **5.3** | **Meldebutton / Meldeweg** | Einfacher Meldeweg für verdächtige Mails an IT/DKSchV | Wissen Mitarbeiter, wo melden? | [ ] OK [ ] Mangel | |
| **5.4** | **Vier-Augen-Prinzip Finanzen** | CEO-Fraud Schutz: Telefonische Verifikation bei Kontoänderungen | Prozess verbindlich etabliert? | [ ] OK [ ] Kritisch | |

---

## 3. MASSNAHMENPLAN & PRIORITÄTEN (Roadmap)

| Priorität | Maßnahme | Verantwortlich | Frist | Budget / Aufwand |
| :--- | :--- | :--- | :--- | :--- |
| **Prio 1 (Sofort)** | 2FA für alle M365-Konten erzwingen | IT-Lead / DKSchV | 48 Stunden | Gering |
| **Prio 1 (Sofort)** | Lokale Admin-Rechte der Mitarbeiter entziehen | IT-Lead | 5 Tage | Gering |
| **Prio 2 (30 Tage)** | Immutable Cloud-Backup (S3 WORM) einrichten | IT-Lead | 3 Wochen | Mittel |
| **Prio 3 (90 Tage)** | Phishing-Awareness Schulung & Notfallübung | GF / DKSchV | 8 Wochen | Mittel |

---
*(c) DKSchV Schweiz – Dini Cyber-Security & Datenschutz Partner im Wallis*
