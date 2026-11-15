---
arbeitsmittel: "Restore-Testprotokoll für Ransomware-Wiederherstellung"
passender_artikel: /wissen/backup-wiederherstellung-testen
version: "1.3"
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/07-restore-testprotokoll"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
stand: "15. November 2026"
quellenpruefung_umfang: "12 zitierte externe Originalquellen direkt geprüft; gemeinsames Quellenjournal mit 28 Originalabrufen, darunter Fedlex-Chronologie und vorhandene amtliche XML sowie 16 ergänzende Quellen. Abrufrückgaben am 15.11.2026, 09:06:11–09:08:59 CET Europe/Zurich, nach 09:00. BACS-Wordtemplate nach Base64-Rückgabe lokal dekodiert und gelesen. Interne Ziele nur lokal abgeglichen, keine Live-Prüfung."
quellenpruefung_status: "12/12 zitierte Quellen inhaltlich lesbar; 1 ergänzender Inhaltsblocker: Fedlex-Änderungsseite liefert nur Javascript-Hinweis, nicht erfolgreich verifiziert. DSG-Wortlaut separat per amtlicher XML bestätigt. Kein historischer 09:00-Wortlaut, keine tatsächliche Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt-, Veröffentlichungs- oder Nutzungsfreigabe."
---

# Restore-Testprotokoll für Ransomware-Wiederherstellung

**Version 1.3 · Quellenstand: 15. November 2026.** Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Nutzungsfreigabe. Die ergänzende Fedlex-Änderungsseite war nicht inhaltlich auslesbar; der amtliche DSG-XML-Wortlaut war lesbar.

> **[FACHPRÜFUNG ERFORDERLICH]** Die rechtlichen Hinweise und die organisationsspezifische Durchführung eines Wiederanlaufs müssen vor Verwendung durch zuständige Fachpersonen geprüft werden.

## Zweck

Dieses Protokoll hilft Schweizer KMU, einen Wiederherstellungstest als überprüfbaren Ablauf zu planen, durchzuführen und nachzubereiten. Es dokumentiert nicht nur, ob eine Sicherung technisch lesbar ist, sondern ob ein klar bestimmter kritischer Geschäftsprozess mit sauberen Systemen, einem ausreichenden Datenstand und innerhalb des vereinbarten Zeitrahmens wieder betrieben werden kann.

Die Vorlage stützt sich auf die BACS-Phasen Vorbereitung, Vorfallsbewältigung und Nachbearbeitung sowie auf die Empfehlung, Backups in einem Disaster-Recovery-Szenario auf Verfügbarkeit und Integrität zu testen.[1] [2] Sie ist kein Zertifikat und keine Garantie, dass eine Wiederherstellung in jedem Cybervorfall gelingt.

## Anwendung

Füllen Sie die Felder vor dem Test gemeinsam mit IT, Prozessverantwortung und der zuständigen Führungsperson aus. Führen Sie den Test nur in einer freigegebenen, vom angenommen kompromittierten Bereich getrennten Umgebung durch. Halten Sie Zeiten, Entscheidungen und Abweichungen unmittelbar fest. Schliessen Sie den Ablauf erst nach Debriefing, Massnahmenplanung und einem Nachtest kritischer Befunde ab.

**Wichtige Grenze:** Dieses Arbeitsmittel simuliert einen Vorfall. Es darf keine produktiven Daten verschlüsseln, keine Schadsoftware einsetzen und keine Wiederanlaufmassnahmen in der Produktivumgebung auslösen, wenn dies nicht ausdrücklich freigegeben und risikogerecht abgesichert ist.

---

## 1. Testauftrag und Freigabe

| Feld | Eintrag |
|---|---|
| Organisation / Bereich |  |
| Testbezeichnung / Version |  |
| Testdatum |  |
| Geplanter Zeitrahmen |  |
| Testleitung |  |
| Auftraggebende Führungsperson |  |
| Freigabe für Durchführung erteilt durch / Datum |  |
| Protokollführung |  |
| Testtyp | ☐ Tabletop ☐ Technischer Teiltest ☐ End-to-End-Restore-Test ☐ Nachtest |
| Testumgebung |  |
| Abbruchkriterien |  |
| Besonderer Schutzbedarf / Einschränkungen |  |

### Testszenario

| Prüfpunkt | Eintrag |
|---|---|
| Angenommener Auslöser und Zeitpunkt |  |
| Als kompromittiert angenommene Systeme / Datenbereiche |  |
| Ausdrücklich nicht betroffene Systeme |  |
| Priorisierter Geschäftsprozess |  |
| Mindestfunktion nach Wiederanlauf |  |
| Zugelassene Behelfsprozesse |  |
| Angenommene Ausfälle von Zugängen, Lieferanten oder Schnittstellen |  |
| Wiederherstellungsquelle / Sicherungssatz |  |
| Referenzzeitpunkt für Datenstand |  |

---

## 2. Geschäftsprozess und Ziele

**Begriffshilfe:** Das **RTO** (Recovery Time Objective) ist die maximal akzeptierte Zeit bis zur vereinbarten Mindestfunktion des Geschäftsprozesses. Das **RPO** (Recovery Point Objective) ist der maximal vertretbare Datenverlust, als Zeitspanne gemessen. Ziele werden von der Organisation festgelegt; sie sind keine Eigenschaft eines Backup-Produkts.

| Prüfpunkt | Sollwert / Festlegung | Istwert / Ergebnis | Erfüllt? |
|---|---|---|---|
| Prozessverantwortliche Person |  |  | ☐ Ja ☐ Nein |
| RTO: Messstart |  |  | ☐ Ja ☐ Nein |
| RTO: Zielzeitpunkt / zulässige Dauer |  |  | ☐ Ja ☐ Nein |
| RTO: tatsächlicher Zeitpunkt fachlicher Abnahme |  |  | ☐ Ja ☐ Nein |
| RPO: maximal zulässige Datenlücke |  |  | ☐ Ja ☐ Nein |
| RPO: Zeitstempel wiederhergestellter Daten |  |  | ☐ Ja ☐ Nein |
| Fachliches Abnahmekriterium |  |  | ☐ Ja ☐ Nein |
| Notwendiger Behelfsprozess bis Wiederanlauf |  |  | ☐ Ja ☐ Nein |

### Abhängigkeiten und Wiederanlaufreihenfolge

| Nr. | Abhängigkeit / System / Dienstleister | Verantwortliche Person | Reihenfolge | Vorbedingung / Freigabe | Ergebnis |
|---:|---|---|---:|---|---|
| 1 |  |  |  |  | ☐ OK ☐ Abweichung |
| 2 |  |  |  |  | ☐ OK ☐ Abweichung |
| 3 |  |  |  |  | ☐ OK ☐ Abweichung |
| 4 |  |  |  |  | ☐ OK ☐ Abweichung |
| 5 |  |  |  |  | ☐ OK ☐ Abweichung |
| 6 |  |  |  |  | ☐ OK ☐ Abweichung |

---

## 3. Rollen, Kommunikation und Unterlagen

| Rolle | Name | Stellvertretung | Erreichbarkeit / Zugangsweg geprüft? | Ergebnis |
|---|---|---|---|---|
| Testleitung |  |  | ☐ Ja ☐ Nein |  |
| Wiederanlaufleitung |  |  | ☐ Ja ☐ Nein |  |
| Systemverantwortung |  |  | ☐ Ja ☐ Nein |  |
| Prozessverantwortung |  |  | ☐ Ja ☐ Nein |  |
| Sicherheits- / Forensikkoordination |  |  | ☐ Ja ☐ Nein |  |
| Lieferantenkoordination |  |  | ☐ Ja ☐ Nein |  |
| Protokollführung |  |  | ☐ Ja ☐ Nein |  |

### Kontrollpunkte vor dem Start

- [ ] Der Testauftrag, die Testumgebung und die Abbruchkriterien sind freigegeben.
- [ ] Die Testumgebung ist von der als kompromittiert angenommenen Umgebung getrennt.
- [ ] Notfallkontakte, Eskalationswege und Stellvertretungen sind über einen unabhängigen Zugang verfügbar.
- [ ] Zugänge zu Sicherungen, Systemvorlagen, Installationsmedien, Konfigurationsdokumentation und nötigen Lizenzen sind erreichbar.
- [ ] Der Sicherungssatz ist eindeutig bezeichnet; der erwartete Datenstand ist festgehalten.
- [ ] Die Prozessverantwortung kennt Testfall und Abnahmekriterium.
- [ ] Der Umgang mit Testdaten und Personendaten ist geklärt.
- [ ] Das Vorgehen gefährdet keine produktiven Systeme oder Daten.

---

## 4. Durchführungsprotokoll

> Erfassen Sie jede wesentliche Entscheidung und Übergabe mit Uhrzeit. Die RTO-Messung endet erst mit der fachlichen Abnahme der vereinbarten Mindestfunktion.

| Uhrzeit | Schritt / Entscheidung | Verantwortliche Person | Nachweis / Ergebnis | Abweichung oder Risiko |
|---|---|---|---|---|
|  | Alarmzeitpunkt gemäss Szenario / RTO-Messung gestartet |  |  |  |
|  | Testlage bestätigt und Grenze der Testumgebung geprüft |  |  |  |
|  | Wiederanlaufumgebung vorbereitet |  |  |  |
|  | Vertrauenswürdige Systemvorlage / Installationsquelle geprüft |  |  |  |
|  | Identität, Netzwerk und weitere Grundkomponenten bereitgestellt |  |  |  |
|  | Anwendung wiederhergestellt |  |  |  |
|  | Daten wiederhergestellt |  |  |  |
|  | Datenstand gegen RPO geprüft |  |  |  |
|  | Berechtigungen und Sicherheitskonfiguration geprüft |  |  |  |
|  | Fachlicher Test durchgeführt |  |  |  |
|  | Mindestfunktion durch Prozessverantwortung abgenommen |  |  |  |
|  | Freigabe / kontrollierter Abschluss des Tests |  |  |  |

### Technische Kontrollpunkte

| Kontrollpunkt | Ergebnis / Nachweis | Erfüllt? |
|---|---|---|
| Wiederherstellungsquelle verfügbar und eindeutig identifiziert |  | ☐ Ja ☐ Nein |
| Zugang zur Sicherung unabhängig von der Test-Schadensannahme möglich |  | ☐ Ja ☐ Nein |
| Wiederanlaufumgebung sauber und getrennt bereitgestellt |  | ☐ Ja ☐ Nein |
| System aus vertrauenswürdiger Quelle bereitgestellt bzw. neu installiert |  | ☐ Ja ☐ Nein |
| Administrations- und Dienstkonten nur im benötigten Umfang aktiviert |  | ☐ Ja ☐ Nein |
| Wiederhergestellte Daten lesbar und dem erwarteten Sicherungsstand entsprechend |  | ☐ Ja ☐ Nein |
| Anwendungs-, Netzwerk- und Schnittstellenfunktion geprüft |  | ☐ Ja ☐ Nein |
| Protokollierung und Überwachung nach Wiederanlauf aktiv |  | ☐ Ja ☐ Nein |
| Rückfall- oder Abbruchweg verfügbar |  | ☐ Ja ☐ Nein |
| Verwendete Komponenten, Produkt- oder Paketversionen sowie zuständige Betreiberin oder zuständiger Betreiber dokumentiert |  | ☐ Ja ☐ Nein |
| Fixstand der verwendeten Komponenten durch laufende korrigierte Version oder Anbieterbestätigung nachgewiesen |  | ☐ Ja ☐ Nein |

**Abgrenzung zum Vorfallsbefund:** Die beiden letzten Kontrollpunkte dokumentieren nur die Komponenten und Fixnachweise der für diesen Test bereitgestellten Wiederanlaufumgebung. Die BACS-Warnung zu PHP empfiehlt bei integrierten und extern betriebenen Komponenten die Kontrolle der tatsächlich laufenden korrigierten Version oder eines vom Anbieter als behoben bestätigten Pakets; ein Update beseitigt jedoch keine bereits erfolgte Kompromittierung.[6] Dieses Protokoll beurteilt deshalb weder einen früheren Daten- oder Kontenkompromiss noch dessen Umfang, Zeitpunkt oder Folgen. Beweise, Logs und betroffene produktive Systeme gehören in einem tatsächlichen Vorfall in eine gesonderte, fachlich gesteuerte Incident-Response- und Forensikbehandlung.

### Rückfall und Beweissicherungsübergabe

Die aktuell angebotene BACS-KMU-Vorlage verlangt eine durch Experten bestätigte Beseitigung der Gefahr vor dem Wiederanlauf betroffener Systeme und Dienste.[8] Im Test wird dieser Freigabepunkt nur simuliert. Protokollieren Sie Kriterien, benannte Rolle, Entscheid und offene Befunde; damit wird keine echte Umgebung zur Wiederverbindung freigegeben.

| Prüfpunkt | Festlegung vor Test / Ergebnis / verantwortliche Person |
|---|---|
| Simulierter Sicherheitsentscheid vor Wiederanlauf: Kriterien, Rolle, Uhrzeit und Nachweis |  |
| Nicht nutzbarer Sicherungssatz: zulässige Alternative und zusätzlicher Datenverlust |  |
| RPO verfehlt oder Fachtest gescheitert: Abbruchentscheid, Behelfsprozess und Nachtest |  |
| Verdächtiger Zugriff nach Start: Stoppbefugnis, sichere Trennung und Eskalationsweg |  |
| Rückfall durchgeführt: Auslöser, Zeitpunkt, Ergebnis und erneute Abnahme |  |
| Log-Erhalt und Beweissicherungsübergabe: betroffene Quellen, zuständige Fachstelle, Entscheid vor veränderndem Eingriff |  |
| Zugelassene Homeoffice-/Heimnetzabhängigkeit: Betreiber, Exposition, Geräte-/Dienststand und Zugangsweg |  |
| Prozessrelevante OT-/Kühlsteuerung: Betreiber, Sollwerte, Alarme und sichere Betriebsabnahme |  |

Die Rückfallszenarien konkretisieren die bisherigen Test-, Abbruch- und Freigabefelder, sie sind keine neu eingeführte allgemeine Behördenpflicht. BACS und CISA betonen den Erhalt relevanter Logs und flüchtiger Beweise.[3] [2] Die Zeile zur Beweissicherungsübergabe hält nur Planung, Zuständigkeit und Entscheid fest; sie ist keine forensische Sicherung oder Bestätigung einer Beweiskette. Bei einem tatsächlichen Vorfall bestimmt die zuständige Fachstelle das risikogerechte Vorgehen. Der Rückfall darf nicht in die als kompromittiert angenommene Produktion führen.

Die BACS-Meldung vom 3. November 2026 verlangt im Heimnetzkontext aktuelle Geräte und Dienste und empfiehlt getrennte Segmente, VPN sowie wenn möglich einen zweiten Faktor.[7] Die Zeile gilt nur für tatsächlich zugelassene Geschäftsprozessabhängigkeiten; sie erlaubt keine Auslagerung auf private Geräte und bestätigt keine Heimnetzsicherheit. Die BACS-Warnung vom 10. November 2026 zu Kühlsteuerungen begründet den OT-Prüfpunkt, sofern solche Anlagen zum Prozess gehören.[9] Sollwerte, Alarme und sichere Schalthandlungen sind durch zuständige Betriebsfachpersonen zu bestimmen, nicht durch dieses Protokoll.

Eine KEV-Aufnahme ist kein Kompromittierungsbefund und kein Restoreentscheid.[10] CISA-BOD-Fristen gelten im dort definierten US-Behördenumfang, nicht automatisch für Schweizer KMU.[11] Update, Anbieterbestätigung und Funktionstest ersetzen keinen gesonderten Sicherheitsentscheid.

### Fachliche Abnahme

| Testfall für Mindestfunktion | Erwartetes Ergebnis | Tatsächliches Ergebnis | Abnahme durch / Uhrzeit |
|---|---|---|---|
| Anmeldung mit vorgesehener Rolle |  |  |  |
| Kerntransaktion erfassen oder bearbeiten |  |  |  |
| Relevante Daten finden und prüfen |  |  |  |
| Erforderliche Ausgabe oder Schnittstelle prüfen |  |  |  |
| Behelfsprozess beenden / Übergabe dokumentieren |  |  |  |

**Abnahmeentscheid:** ☐ Mindestfunktion erreicht ☐ Mit Einschränkungen erreicht ☐ Nicht erreicht  
**Begründung / Einschränkungen:**

................................................................................................................................................

---

## 5. Messung und Ergebnis

| Kennzahl | Soll | Ist | Differenz | Bewertung |
|---|---|---|---|---|
| RTO: Zeit bis zur fachlichen Abnahme |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |
| RPO: Datenlücke zum Referenzzeitpunkt |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |
| Vollständigkeit der Abhängigkeiten |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |
| Fachliche Mindestfunktion |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |
| Rollen und Kommunikation |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |
| Sicherheit der Wiederanlaufumgebung |  |  |  | ☐ Erfüllt ☐ Nicht erfüllt |

**Gesamtergebnis:** ☐ Bestanden ☐ Bestanden mit Auflagen ☐ Nicht bestanden ☐ Abgebrochen  
**Entscheid durch / Datum:**

................................................................................................................................................

---

## 6. Debriefing und Massnahmen

Das BACS empfiehlt ein strukturiertes Debriefing, um aus der Bewältigung zu lernen und Vorfall-, Notfall- und Krisenplanung fortlaufend zu verbessern.[1] Führen Sie das Debriefing zeitnah durch und konzentrieren Sie sich auf beobachtbare Fakten.

### Leitfragen

- Was hat den Wiederanlauf beschleunigt oder verzögert?
- Welche Abhängigkeit, Information, Berechtigung oder Freigabe war nicht vollständig bekannt?
- War die Wiederherstellungsreihenfolge für den Geschäftsprozess richtig?
- Konnten RTO und RPO nachweisbar erreicht werden?
- War die Datenqualität für die vereinbarte Mindestfunktion ausreichend?
- Welche Rolle, Stellvertretung oder Lieferantenleistung war unklar oder nicht erreichbar?
- Welche Massnahme verhindert eine Wiederholung der kritischen Abweichung?

| Nr. | Befund / Ursache | Risiko / Auswirkung | Massnahme | Verantwortliche Person | Termin | Nachtest nötig? |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  | ☐ Ja ☐ Nein |
| 2 |  |  |  |  |  | ☐ Ja ☐ Nein |
| 3 |  |  |  |  |  | ☐ Ja ☐ Nein |
| 4 |  |  |  |  |  | ☐ Ja ☐ Nein |
| 5 |  |  |  |  |  | ☐ Ja ☐ Nein |

### Nachtest und Dokumentenpflege

| Prüfpunkt | Eintrag |
|---|---|
| Kritischer Befund, der nachgetestet wird |  |
| Nachtestziel / Abnahmekriterium |  |
| Termin Nachtest |  |
| Verantwortliche Person |  |
| Aktualisierte Dokumente (Notfallplan, Runbook, Kontaktliste, Risikoregister) |  |
| Abgenommen und geschlossen durch / Datum |  |

---

## Grenzen und Eskalation

Dieses Protokoll ersetzt keine forensische Untersuchung, keine Incident Response und keine fachjuristische Beratung. In einem tatsächlichen Ransomware-Vorfall empfiehlt das BACS, den Infektionsweg zu ermitteln, Neuinfektionen zu verhindern, betroffene Systeme vor der Datenwiederherstellung neu aufzusetzen und allfällige forensische Sicherungen vor Reparaturversuchen oder Neustarts frühzeitig durch Fachpersonen zu beurteilen.[3]

Ein einzelnes Anzeichen beweist keine Malware-Infektion. Mehrere ungewöhnliche Beobachtungen rechtfertigen laut BACS jedoch eine genauere Untersuchung; bei einer bestätigten Infektion empfiehlt das BACS ein Neuaufsetzen und anschliessende Passwortänderungen.[5]

Ein Restore- oder Patch-Ergebnis ersetzt auch die gesonderte Beurteilung der Betroffeneninformation nicht. Die EDÖB-Mitteilung vom 6. November 2026 zum konkreten Fall SkySale hält fest, dass nachträgliche technische Massnahmen die bestätigte Informationspflicht nicht beseitigten.[12] Art. 24 Abs. 4 DSG und die konkrete Schutzbedürftigkeit sind getrennt zu beurteilen; daraus wird keine allgemeine Pflicht zur öffentlichen Bekanntmachung abgeleitet.[4]

**[FACHPRÜFUNG ERFORDERLICH]** Ergibt ein Test Hinweise auf eine reale Kompromittierung oder einen Datenabfluss, stoppen Sie den Test nach dem definierten Sicherheitsverfahren. Melde- und Informationspflichten sind anhand des konkreten Sachverhalts durch Datenschutz- und Rechtsfachpersonen zu beurteilen. Art. 24 DSG verlangt eine Meldung an den EDÖB so rasch als möglich, wenn eine Datensicherheitsverletzung voraussichtlich zu einem hohen Risiko für Persönlichkeit oder Grundrechte führt.[4]

## Quellen

[1]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[2]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide"
[3]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Art. 24"
[5]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[6]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
[7]: https://www.bacs.admin.ch/de/26w44-de "BACS – Woche 44: Wenn das Heimnetzwerk zum Einfallstor für Cyberkriminelle wird, 3. November 2026"
[8]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS – Template IT-Notfall- und Krisenplan für KMU, Download-Datum 11. November 2026"
[9]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen, 10. November 2026"
[10]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – Known Exploited Vulnerabilities Catalog, abgerufen am 15. November 2026"
[11]: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk "CISA – BOD 26-04: Prioritizing Security Updates Based on Risk, US-Geltungsbereich"
[12]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB – Bundesverwaltungsgericht bestätigt Informationspflicht der Onlineshop-Betreiberin, 6. November 2026"
