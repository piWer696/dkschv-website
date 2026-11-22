# VEREINBARUNG ÜBER DIE DURCHFÜHRUNG EINES PENETRATIONSTESTS
## (Rules of Engagement – RoE & Rechtliche Ermächtigung)

**Zwischen:**

**Auftraggeber (Kunde):**  
Firma: _________________________________________________________________  
Strasse / Nr.: _________________________________________________________  
PLZ / Ort: _____________________________________________________________  
Vertretungsberechtigte Person: _________________________________________  
Funktion: ______________________________________________________________  
(nachfolgend *„Auftraggeber“* genannt)

**und**

**Auftragnehmer (Prüfer):**  
**DKSchV Dini**  
Inhaber: Andreas Dini  
Bammattenweg 19, CH-3904 Naters (Wallis)  
E-Mail: info@dkschv.ch · Tel: +41 79 844 66 69  
(nachfolgend *„DKSchV“* genannt)

---

### Präambel
Der Auftraggeber beabsichtigt, die Sicherheit seiner informationstechnischen Systeme und Netzwerke durch eine kontrollierte, simulierte Cyber-Angriffsanalyse (Penetrationstest) überprüfen zu lassen. Ziel ist das Aufdecken von Schwachstellen vor böswilligen Dritten.

### 1. Ausdrückliche Ermächtigung & Straffreiheit (Art. 143 & 143bis StGB)
1. Der Auftraggeber bestätigt, uneingeschränkter Eigentümer, Betreiber oder hierzu vollumfänglich bevollmächtigter Nutzungsberechtigter der in Abschnitt 2 definierten Zielsysteme (Scope) zu sein.
2. Der Auftraggeber ermächtigt DKSchV hiermit ausdrücklich, im definierten Zeitraum und Rahmen die vereinbarten Systeme anzugreifen, Sicherheitsbarrieren zu analysieren und Schwachstellen im Sinne einer kontrollierten Prüfung aufzudecken.
3. Diese schriftliche Vollmacht stellt die erforderliche Einwilligung dar, sodass Handlungen im Rahmen dieser Vereinbarung **nicht** den Straftatbeständen von Art. 143 StGB (Unbefugte Datenbeschaffung) oder Art. 143bis StGB (Unbefugtes Eindringen in ein Datenverarbeitungssystem) unterliegen.

---

### 2. Zieldefinition & Testumfang (Scope)

Folgende Systeme sind **ausdrücklich freigegeben (In-Scope)**:

| Nr. | Externe IP-Adresse / IP-Bereich | Domain / URL / Hostname | Beschreibung des Systems |
| :--- | :--- | :--- | :--- |
| 1 | `_______________________` | `___________________________` | Haupt-Firewall / Gateway |
| 2 | `_______________________` | `___________________________` | Firmen-Website / Webportal |
| 3 | `_______________________` | `___________________________` | VPN-Zugang / Mailserver |
| 4 | `_______________________` | `___________________________` | Cloud-Dienst / Testsystem |

**Ausdrücklich ausgeschlossen (Out of Scope):**
* Reine Denial-of-Service-Angriffe (DoS/DDoS), die auf die dauerhafte Lahmlegung der Bandbreite oder Systemressourcen abzielen.
* Systeme, Netze oder Schnittstellen Dritter (z. B. Hoster, Rechenzentren, externe SaaS-Provider), für die keine schriftliche Freigabe vorliegt.
* Physische Einbruchsversuche in Gebäude oder Social-Engineering-Angriffe auf Personal, sofern nicht gesondert vereinbart.

---

### 3. Testmethodik & Vorgehensweise
* [ ] **Externer Perimeter-Test (Blackbox):** Prüfung der öffentlich über das Internet erreichbaren Systeme ohne Vorabwissen oder Vorabzugangsdaten.
* [ ] **Web-Applikations-Test:** Detaillierte Prüfung auf Schwachstellen nach OWASP Top 10 (z. B. SQL-Injection, Cross-Site Scripting, Authentifizierungs-Bypässe).
* [ ] **Greybox-Test:** Prüfung unter Nutzung eines bereitgestellten Standard-Benutzerkontos.

DKSchV verpflichtet sich, den Test mit grösster Sorgfalt und unter Einsatz branchenüblicher Standards (z. B. PTES, OWASP) durchzuführen. Entdeckte Schwachstellen werden ausschliesslich durch schonende Machbarkeitsnachweise (Proof of Concept) belegt; ein destruktives Ausnutzen oder Verändern von Produktivdaten unterbleibt.

---

### 4. Zeitfenster & Notfall-Eskalation

* **Testzeitraum:** Von ______________________ bis ______________________
* **Erlaubte Testzeiten:**  
  [ ] Rund um die Uhr (24/7)  
  [ ] Nur ausserhalb der regulären Bürozeiten (z. B. 19:00 bis 06:00 Uhr)  
  [ ] Nach individueller Absprache

**Notfallkontakte bei Störungen / Sofortiger Abbruch (Emergency Stop):**

* **Notfallkontakt Auftraggeber:**  
  Name: _______________________________________ Mobil (24/7): _______________________  
* **Notfallkontakt DKSchV (Andreas Dini):**  
  Mobil: +41 79 844 66 69 · E-Mail: info@dkschv.ch
* **Abbruch-Passwort / Codewort:** `________________________________________________`  
  *(Wird dieses Codewort vom Auftraggeber genannt, stellt DKSchV sämtliche Aktivitäten unverzüglich ein.)*

---

### 5. Vertraulichkeit (NDA) & Datenschutz (revDSG)
1. DKSchV verpflichtet sich zu absoluter Verschwiegenheit über alle im Rahmen der Prüfung erlangten Informationen, Geschäftsgeheimnisse und festgestellten Schwachstellen.
2. Sämtliche im Test erfassten Daten, Logfiles und Testberichte werden verschlüsselt gespeichert und nach Ablauf der Aufbewahrungsfrist oder auf schriftliches Verlangen des Auftraggebers unwiderruflich gelöscht.
3. Der Ergebnisbericht wird ausschliesslich der in dieser Vereinbarung genannten Ansprechperson des Auftraggebers übermittelt.

---

### 6. Haftungsbegrenzung & Gewährleistung
1. DKSchV führt die Tests mit professioneller Sorgfalt durch. Dennoch kann trotz schonender Methodik nicht völlig ausgeschlossen werden, dass fehlerhafte Zielsysteme instabil werden oder Dienste neu starten.
2. Die Haftung von DKSchV für leichte Fahrlässigkeit, mittelbare Schäden, Folgeschäden und entgangenen Gewinn wird – soweit gesetzlich zulässig (Art. 100 OR) – ausgeschlossen.
3. Der Auftraggeber stellt sicher, dass vor Beginn der Testaktivitäten **ein vollständiges, aktuelles und wiederherstellbares Daten-Backup** aller betroffenen Systeme vorliegt.

---

### 7. Schlussbestimmungen
Änderungen dieser Vereinbarung bedürfen der Schriftform. Es gilt ausschliesslich **Schweizer Recht**. Ausschliesslicher Gerichtsstand für allfällige Streitigkeiten ist **Brig / Naters (Kanton Wallis)**.

---

**Ort, Datum:** ________________________________________________________

**Für den Auftraggeber:**  
*(Rechtsgültige Unterschrift & Firmenstempel)*

_________________________________________________________________________  
Name & Funktion in Druckbuchstaben: _____________________________________

**Für den Auftragnehmer (DKSchV Dini):**

_________________________________________________________________________  
Andreas Dini, Inhaber DKSchV Dini
