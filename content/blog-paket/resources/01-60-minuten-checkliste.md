---
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/01-60-minuten-checkliste"
titel: "60-Minuten-Checkliste bei Ransomware-Verdacht"
meta_title: "60-Minuten-Checkliste bei Ransomware-Verdacht | DKSchV"
meta_description: "Druckbare Arbeitsvorlage für die erste Stunde nach einem Ransomware-Verdacht: Eindämmung, Beweissicherung, Backups und Meldeprüfung."
suchintention: "Arbeitsmittel – Ransomware-Erstreaktion dokumentieren"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
version: "Stand 1. November 2026"
quellenpruefung_umfang: "11 von 11 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft"
quellenpruefung_status: "Vollständig für die Quellenreferenzen; Fedlex-Historie und amtliche XML-Fassungen zusätzlich geprüft; interne relative Ziele nicht live geprüft"
bezug: "/wissen/ransomware-erste-60-minuten"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# 60-Minuten-Checkliste bei Ransomware-Verdacht

## Zweck

Diese Checkliste unterstützt Geschäftsleitung und IT dabei, in der ersten Stunde nach einem Ransomware-Verdacht strukturiert zu handeln. Sie hilft, Eindämmung, Beweissicherung, Backup-Schutz und die erste Einordnung von BACS-, Polizei- und EDÖB-Meldungen zu dokumentieren. Sie ist für den Ausdruck und die handschriftliche Verwendung gedacht.

Sie ersetzt weder eine forensische Untersuchung noch einen organisationsspezifischen Notfallplan. Eine korrekte Abarbeitung verhindert nicht automatisch Datenverlust, Betriebsunterbruch, Datenabfluss oder rechtliche Folgen.

## Anwendung

1. Tragen Sie zuerst Zeit, Incident Lead und sichere Kontaktwege ein.
2. Arbeiten Sie die Zeitfenster in der vorgegebenen Reihenfolge ab. Markieren Sie nur erledigte oder bewusst nicht anwendbare Punkte.
3. Halten Sie bei jeder wesentlichen Massnahme Zeitpunkt, Person und Grund fest.
4. Erweitern Sie den Entscheidungslog sofort, wenn neue Fakten vorliegen.
5. Übergeben Sie das Blatt bei Schichtwechsel oder Übergabe an die nächste verantwortliche Person.

> **Wichtig:** Das BACS empfiehlt, infizierte Systeme umgehend vom Netz zu trennen. Vor Reparaturversuchen oder Neustarts ist früh über eine fachkundige forensische Sicherung zu entscheiden. [1] Ausschalten ist nur ein Notbehelf, wenn eine Netztrennung nicht möglich ist und die Ausbreitung sonst nicht gestoppt werden kann; dabei können flüchtige Beweise verloren gehen. [2]

---

## A. Start- und Kontaktfelder

| Feld | Eintrag |
|---|---|
| Organisation / Standort |  |
| Datum |  |
| Entdeckt am, Uhrzeit |  |
| Meldende Person / erreichbar unter |  |
| Incident Lead / erreichbar unter |  |
| Technische Einsatzleitung / Stellvertretung |  |
| Geschäftsleitungs-Freigabe / erreichbar unter |  |
| Sicherer Kommunikationskanal ausserhalb des betroffenen Netzes |  |
| Externe IT-/Incident-Response-Fachperson |  |
| Versicherer / Policen- oder Schadenfallnummer, falls vorhanden |  |
| Kantonspolizei / weitere vorab definierte Kontakte |  |

## B. Minute 0–15: Eindämmung und Führung

**Zeitfenster begonnen um:** __________  **abgeschlossen um:** __________

- [ ] Ransomware-Verdacht als Incident deklariert; Incident Lead benannt.
- [ ] Uhrzeit, meldende Person und sichtbare Symptome im Entscheidungslog erfasst.
- [ ] Sicheren Kommunikationsweg ausserhalb der möglicherweise betroffenen Infrastruktur genutzt.
- [ ] Betroffene Geräte, Server oder Freigaben unmittelbar identifiziert und vom Netzwerk getrennt.
- [ ] Bei Geräten: Netzwerkkabel entfernt und WLAN deaktiviert oder technisch gleichwertig isoliert.
- [ ] Bei mehreren betroffenen Systemen: Notwendigkeit einer Netzwerkisolation auf Switch-/Segmentebene durch technische Einsatzleitung beurteilt.
- [ ] Betroffene Systeme nicht neu gestartet und nicht mit Bereinigungstools verändert.
- [ ] Falls Ausschalten unvermeidbar war: Grund und Zeitpunkt dokumentiert.
- [ ] Kritische Prozessverantwortliche über bestätigte Einschränkungen informiert.

**Betroffene oder verdächtige Systeme / Freigaben:**

| System, Dienst oder Freigabe | Benutzer / Standort | Symptom | Isoliert um | Durch |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Kurzlage (nur bestätigte Fakten):**

____________________________________________________________________________

____________________________________________________________________________

Ein einzelnes unspezifisches Zeichen wie ein langsames Gerät ist noch kein Infektionsbeweis. Dokumentieren Sie mehrere ungewöhnliche Beobachtungen oder Sicherheitswarnungen für die technische Untersuchung und informieren Sie bei Geschäftsgeräten die zuständige IT. [8]

## C. Minute 15–30: Lagebild und Beweissicherung

**Zeitfenster begonnen um:** __________  **abgeschlossen um:** __________

- [ ] Liste der betroffenen, verdächtigen und nach aktuellem Stand nicht betroffenen Systeme angelegt.
- [ ] Lösegeldnotiz, Fehlermeldungen und auffällige Dateiendungen dokumentiert, ohne Originale zu verändern.
- [ ] Verfügbare Logs gesichert: Firewall, E-Mail-Gateway, VPN, Identitätsdienst, Endpoint-Schutz und relevante Server.
- [ ] Für jeden Logexport Quelle, Zeitraum, Exportzeit, Speicherort und verantwortliche Person notiert.
- [ ] Verdächtige E-Mails, Dateien, Alarmmeldungen und technische Beobachtungen nicht gelöscht.
- [ ] Frühe Entscheidung über Forensik getroffen; bei Bedarf qualifizierte Fachperson kontaktiert.
- [ ] Bei erwogener Strafanzeige: Beweissicherung und Kontakt zur Kantonspolizei vorbereitet.
- [ ] Nur belastbar identifizierte schädliche URLs oder IP-Adressen zur technischen Blockierung an die Einsatzleitung übergeben.

Das BACS nennt Logdateien und insbesondere Protokolle von E-Mail-Servern, Proxy, Firewall und weiterer Sicherheitssoftware als wichtige Grundlage zur Feststellung von Ausmass und Angriffsinfrastruktur. [1]

**Gesicherte Unterlagen und Spuren:**

| Objekt / Quelle | Zeitraum oder Zeitpunkt | Speicherort / Referenz | Gesichert durch |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**Forensik-Entscheid:**

- [ ] Fachperson beauftragt: ______________________________
- [ ] Nicht beauftragt; Grund / Freigabe: __________________________________________
- [ ] Noch offen; Entscheidung bis: ______________________________

## D. Minute 30–45: Backups sichern, Wiederherstellung vorbereiten

**Zeitfenster begonnen um:** __________  **abgeschlossen um:** __________

- [ ] Automatische Backup- oder Synchronisationsläufe auf Risiko der Übernahme verschlüsselter Daten geprüft.
- [ ] Backup-Verwaltung und Sicherungsmedien soweit sicher möglich vom betroffenen Produktionsnetz abgegrenzt.
- [ ] Keine Wiederherstellung in die möglicherweise kompromittierte Umgebung gestartet.
- [ ] Letzten erfolgreichen Lauf und enthaltenen Datenstand je kritischer Sicherung dokumentiert.
- [ ] Aufbewahrungsort, Administrationsweg und Status als offline oder unveränderbar je Sicherung erfasst.
- [ ] Verfügbarkeit eines früheren Wiederherstellungstests vermerkt.
- [ ] Wiederanlaufprioritäten der kritischen Geschäftsprozesse bereitgelegt oder bestimmt.

CISA empfiehlt, Daten von offline gehaltenen, verschlüsselten Backups wiederherzustellen und dabei eine erneute Infektion sauberer Systeme zu verhindern. [2]

| Kritische Sicherung | Letzter erfolgreicher Lauf | Datenstand | Getrennt / geschützt? | Wiederherstellungstest bekannt? |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## E. Minute 45–60: Meldungen und nächste Entscheidung

**Zeitfenster begonnen um:** __________  **abgeschlossen um:** __________

- [ ] BACS-Relevanz geprüft: Ist die Organisation als kritische Infrastruktur erfasst oder besteht eine freiwillige Meldemöglichkeit?
- [ ] Bei möglicher BACS-Pflicht: Frist von 24 Stunden ab Entdeckung festgehalten und Erstmeldung vorbereitet.
- [ ] Polizei: Strafanzeige oder frühzeitige Abstimmung zur Beweissicherung beurteilt.
- [ ] EDÖB-Risikobeurteilung begonnen: Sind Personendaten betroffen, und ist ein voraussichtlich hohes Risiko für Persönlichkeit oder Grundrechte möglich?
- [ ] Für EDÖB-/BACS-Beurteilung zuständige Datenschutz-, Rechts- oder Fachperson benannt.
- [ ] Bei möglicher EDÖB-Meldung: soweit verfügbare Angaben zu Art, Zeitpunkt, Dauer, betroffenen Daten und Personen, Folgen, Massnahmen sowie Ansprechperson für die fachliche Prüfung zusammengestellt.
- [ ] Betroffene Personen nicht vorschnell informiert; Informationsbedarf fachlich geprüft.
- [ ] Lageupdate für Geschäftsleitung mit bestätigten Fakten, Geschäftsauswirkung und offenen Entscheiden erstellt.
- [ ] Nächster Entscheid, verantwortliche Person und Zeitpunkt verbindlich festgelegt.

Für Betreiber kritischer Infrastrukturen gilt bei meldepflichtigen Cyberangriffen eine Meldung an das BACS innert 24 Stunden nach Entdeckung. Die Voraussetzungen ergeben sich aus dem Informationssicherheitsgesetz und der Cybersicherheitsverordnung; die konkrete Einordnung ist fachlich zu prüfen. [3] [4]

Nach Art. 24 DSG meldet der Verantwortliche dem EDÖB eine Datensicherheitsverletzung so rasch als möglich, wenn sie voraussichtlich zu einem hohen Risiko für Persönlichkeit oder Grundrechte natürlicher Personen führt. **Dies ist keine individuelle Rechtsberatung; lassen Sie die konkrete Bewertung durch eine Datenschutz- oder Rechtsfachperson prüfen.** [5] [6]

Der EDÖB stellt für Meldungen von Verantwortlichen ein sicheres Online-Formular bereit. Art. 15 DSV nennt die Angaben, die soweit möglich in der Meldung stehen müssen, und verlangt, fehlende Angaben so rasch als möglich nachzureichen. Er verlangt zudem eine Dokumentation der Tatsachen, Auswirkungen und Massnahmen. [10] [11]

| Entscheidung / Meldung | Pflicht oder Option nach Prüfung | Verantwortlich | Frist / nächster Termin | Status |
|---|---|---|---|---|
| BACS |  |  |  |  |
| Kantonspolizei |  |  |  |  |
| EDÖB |  |  |  |  |
| Versicherer / Vertragspartner |  |  |  |  |
| Interne Kommunikation |  |  |  |  |

## F. Entscheidungslog und Übergabe

| Uhrzeit | Neue Tatsache oder Massnahme | Entscheidung / Begründung | Verantwortlich | Offener Punkt / Termin |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Lage bei Ablauf der ersten 60 Minuten:**

____________________________________________________________________________

____________________________________________________________________________

**Nächste verbindliche Entscheidung um:** __________  **durch:** ______________________________

## Grenzen und fachliche Prüfung

Diese Checkliste ist ein allgemeines Arbeitsmittel für die erste Reaktion auf dem Stand der Quellenprüfung vom 1. November 2026; dieser Stand ist keine Fachfreigabe. Sie ersetzt keine organisationsspezifische Notfallplanung, technische Forensik, Meldung oder Rechtsberatung. Sie erlaubt keine Aussage darüber, ob Systeme frei von Angreifern sind, ob ein Backup sicher wiederherstellbar ist oder ob keine Daten abgeflossen sind. Ein nachträglich eingespieltes Sicherheitsupdate beseitigt keine bereits erfolgte Kompromittierung. [9] Bei möglicher Personendatenverletzung, kritischer Infrastruktur, Strafanzeige, Lösegeldforderung oder grossem Betriebsunterbruch ist **[FACHPRÜFUNG ERFORDERLICH]**; ziehen Sie unverzüglich eine geeignete Fachperson bei.

Das BACS beschreibt Notfallkonzepte als Zusammenspiel von Vorbereitung, Eintritt des Vorfalls, Vorfallsbewältigung und Nachbearbeitung. Pflegen und testen Sie Rollen, Kontakte, Backup-Wiederherstellung und Entscheidungswege daher ausserhalb des akuten Vorfalls. [7]

## Quellen

[1]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[2]: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware "CISA – I've Been Hit By Ransomware! Response Checklist"
[3]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Bundesgesetz über die Informationssicherheit, Art. 74a–74h Cyberangriffe auf kritische Infrastrukturen"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Art. 24 Meldung von Verletzungen der Datensicherheit"
[6]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information Betroffener nach Art. 24 DSG"
[7]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[8]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[9]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
[10]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach: Meldung von Datensicherheitsverletzungen durch Verantwortliche"
[11]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz, Art. 15 Meldung von Verletzungen der Datensicherheit"
