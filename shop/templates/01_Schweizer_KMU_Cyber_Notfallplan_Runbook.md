# DKSchV Schweiz // Cyber-Security Notfall-Runbook & Incident-Response-Plan
**Dokumenten-Klassifikation:** Vertraulich / Intern  
**Zielgruppe:** Geschäftsleitung, IT-Verantwortliche, externe IT-Dienstleister von Schweizer KMU  
**Herausgeber:** DKSchV Cyber-Security Schweiz (dkschv.ch)  
**Rechtlicher Rahmen:** nDSG (Schweiz), BACS Meldewesen

---

## 1. SOFORTMASSNAHMEN (Die ersten 15 Minuten)

> [!CAUTION]
> **OBERSTE REGEL BEI RANSOMWARE / HACK:**  
> **GERÄTE NICHT NEUSTARTEN ODER AUSSCHALTEN!**  
> Beim Ausschalten geht der Arbeitsspeicher (RAM) mit flüchtigen Beweisen, Verschlüsselungs-Keys und laufenden Prozessen verloren.

### Checkliste Sofort-Isolierung:
1. **Netzwerk sofort physisch trennen:**
   - [ ] LAN-Kabel an betroffenen Servern, PCs und NAS sofort herausziehen.
   - [ ] WLAN an allen Geräten deaktivieren (Hardware-Schalter oder Flugmodus).
   - [ ] Hypervisor/Virtuelle Maschinen: Virtuelle Netzwerkkarten trennen (Disconnect vNIC), Maschinen **eingeschaltet lassen**.
2. **Backups sofort sichern:**
   - [ ] Alle physisch verbundenen Backup-Festplatten / USB-Laufwerke sofort abziehen.
   - [ ] Cloud-Backup-Zugänge (z.B. Immutable Backups, S3 Object Lock) prüfen und Schreibrechte temporär einfrieren.
3. **Zentrale Zugänge sperren:**
   - [ ] Microsoft 365 / Google Workspace Admin-Konsole aufrufen (von einem sauberen, separaten Gerät!).
   - [ ] Alle aktiven Benutzersitzungen widerrufen ("Revoke all sessions").
   - [ ] Passwörter für Domain-Admins, VPN-Gateways und Cloud-Admins sofort ändern.
   - [ ] VPN-Zugänge und RDP-Ports an der Firewall komplett deaktivieren.

---

## 2. NOTFALL-ORGANISATION & ESKALATIONSMATRIX

Im Ernstfall übernimmt der **Krisenstab** die alleinige Führung. 

| Rolle | Funktion im Notfall | Name / Stellvertreter | Telefon (privat/mobil) |
| :--- | :--- | :--- | :--- |
| **Krisenstabsleiter** | Geschäftsleitung (trifft Finanz- & Betriebsentscheide) | ____________________ | ____________________ |
| **Technischer Lead** | IT-Leiter / DKSchV Security-Experte | DKSchV Notfall-Hotline | +41 79 844 66 69 |
| **Recht & Compliance** | Datenschutzberater / Jurist (nDSG / Haftung) | ____________________ | ____________________ |
| **Kommunikation** | Einzige Person, die mit Kunden/Presse spricht | ____________________ | ____________________ |

---

## 3. SCHWEIZER MELDEPFLICHTEN & BEHÖRDEN-KONTAKTE

In der Schweiz gelten strenge rechtliche Meldefristen:

### A. Bundesamt für Cybersicherheit (BACS - ehemals NCSC)
* **Wann:** Bei jedem schwerwiegenden Cyber-Angriff (Ransomware, Erpressung, DDoS).
* **Meldeweg:** Meldeformular auf `https://www.bacs.admin.ch` oder via BACS-Notfallnummer.
* **Nutzen:** Das BACS liefert direkte Lageberichte, technische IoCs (Indicators of Compromise) und Hilfestellungen.

### B. Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)
* **Pflicht nach Art. 24 nDSG:** Verletzungen der Datensicherheit, die voraussichtlich zu einem hohen Risiko für die Persönlichkeit oder die Grundrechte der betroffenen Personen führen.
* **Frist:** **So rasch als möglich** (in der Praxis innert Stunden bis maximal 72 Stunden nach gesicherter Kenntnis).
* **Meldeweg:** Online-Meldeportal des EDÖB (`https://www.edoeb.admin.ch`).

### C. Kantonspolizei (Kantonales Cybercrime-Dezernat)
* **Kantonspolizei Wallis / Fachstelle Cybercrime:** Tel. 117 / Notruf oder lokale Dienststelle.
* **Hinweis für Strafanzeige:** Keine eigenmächtigen Löschungen vornehmen, damit digitale Spuren gerichtlich verwertbar bleiben.

---

## 4. MUSTER-VORLAGEN FÜR DIE KRISENKOMMUNIKATION

### Vorlage 1: Interne Rundmail an alle Mitarbeitenden
> **Betreff:** DRINGEND: Sicherheitsvorfall – Verhaltensanweisungen für alle Mitarbeitenden  
> **Text:**  
> Sehr geehrte Kolleginnen und Kollegen,  
> unser Unternehmen verzeichnet aktuell eine technische Sicherheitsstörung unserer IT-Systeme. Unser internes IT-Team arbeitet gemeinsam mit externen Sicherheitsanalysten von DKSchV Schweiz mit Hochdruck an der Analyse und Isolierung des Vorfalls.  
>  
> **Ab sofort gelten folgende verbindliche Verhaltensregeln:**  
> 1. Schalten Sie Ihre Arbeitsstationen nicht aus, sondern ziehen Sie lediglich das Netzwerkkabel ab und deaktivieren Sie das WLAN.  
> 2. Versuchen Sie keinesfalls, verdächtige Dateien zu öffnen oder Systemänderungen vorzunehmen.  
> 3. Nutzen Sie für dringende Abstimmungen ausschließlich private Mobiltelefone / Messenger, nicht das Unternehmensnetzwerk.  
> 4. Jegliche Kommunikation nach außen (Kunden, Medien, Social Media) ist untersagt. Auskünfte erteilt ausschließlich die Geschäftsleitung.  
>  
> Wir informieren Sie regelmäßig über den Status der Wiederherstellung.  
> Mit freundlichen Grüßen,  
> Die Geschäftsleitung

---

### Vorlage 2: Transparente Kunden- & Partnerinformation
> **Betreff:** Wichtige Information zu vorübergehenden Störungen unserer IT-Erreichbarkeit  
> **Text:**  
> Sehr geehrte Damen und Herren,  
> Vertrauen und Transparenz sind das Fundament unserer Zusammenarbeit. Wir möchten Sie proaktiv darüber informieren, dass unsere IT-Infrastruktur Ziel eines Cyber-Angriffs wurde.  
>  
> Durch das sofortige Greifen unserer Notfallpläne konnten wir die betroffenen Systeme isolieren. Wir arbeiten eng mit spezialisierten Schweizer Cybersicherheits-Experten und den zuständigen Behörden zusammen.  
>  
> Aktuell prüfen wir mit höchster Priorität, ob und in welchem Umfang Daten betroffen sind. Unsere operativen Tätigkeiten führen wir über Ausweichkanäle bestmöglich fort. Wir halten Sie über alle weiteren Entwicklungen transparent auf dem Laufenden.  
>  
> Bei dringenden Rückfragen erreichen Sie unseren Krisenstab unter: [Telefonnummer / Notfall-E-Mail].

---

## 5. FORENSISCHE SICHERUNG & WIEDERHERSTELLUNG (Recovery)

```
[Isolierung] ---> [Forensisches Abbild] ---> [Root-Cause-Analyse] ---> [Härtung] ---> [Clean Recovery]
```

1. **Beweissicherung (Forensic Readiness):**
   - Vor jedem Wiederherstellungsversuch Speicherabbilder (RAM-Dumps) und Festplatten-Images (Bitstream-Images via `dd` oder FTK Imager) erstellen.
   - Firewall-Logs, DNS-Query-Logs, DHCP-Leases und Active Directory Event-Logs sichern und schreibgeschützt archivieren.
2. **Root-Cause Identifikation:**
   - Wie kam der Angreifer ins Netz? (Phishing-Mail, ungepatchte VPN-Schwachstelle, kompromittierte Zugangsdaten, offener RDP-Port).
   - Die gefundene Einbruchs-Schwachstelle muss behoben sein, **bevor** das erste Backup wieder ans Netz geht!
3. **Schrittweiser Wiederanlauf:**
   - 1. Core-Infrastruktur (Firewall, sauberes AD, DNS, NTP).
   - 2. Datenspeicher & Datenbanken aus verifiziertem, virenfreiem Backup.
   - 3. Kritische Kernapplikationen (ERP, Buchhaltung, Mail).
   - 4. Benutzer-Clients nach vollständigem Neuaufsetzen (Re-Imaging) freigeben.

---
*(c) DKSchV Schweiz – Dini Cyber-Security & Datenschutz Partner im Wallis*
