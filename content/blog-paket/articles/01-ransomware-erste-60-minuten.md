---
status: "Entwurf – nicht freigegeben"
slug: "/wissen/ransomware-erste-60-minuten"
meta_title: "Ransomware im KMU: Erste Schritte im Vorfall | DKSchV"
meta_description: "Ransomware-Verdacht im Unternehmen: Ein Schweizer Leitfaden zu Eindämmung, Beweissicherung, Backups und der getrennten Prüfung möglicher Meldungen."
hauptkeyword: "Ransomware was tun KMU Schweiz"
suchintention: "Informational – Sofortmassnahmen bei Ransomware-Verdacht"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "01.10.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "14 von 14 externen Quellenreferenzen geprüft; BACS-, EDÖB- und Fedlex-Meldewege sowie einschlägige Originalmeldungen seit 18. Oktober 2026 geprüft"
quellenpruefung_status: "Vollständig für die Quellenreferenzen; Fedlex-Historie und amtliche XML-Fassungen zusätzlich geprüft; interne relative Ziele nicht live geprüft"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Ransomware im KMU: Die ersten 60 Minuten richtig handeln

**Kurzantwort:** Isolieren Sie bei einem Ransomware-Verdacht betroffene Geräte unverzüglich vom Netzwerk, ohne sie vorschnell neu zu starten. Übernehmen Sie die Führung, dokumentieren Sie Zeitpunkte und Entscheidungen und sichern Sie Logdateien sowie – falls erforderlich – forensisch verwertbare Spuren, bevor Reparaturversuche beginnen. Schützen Sie danach Backups und starten Sie keine Wiederherstellung in eine möglicherweise noch kompromittierte Umgebung. Prüfen Sie parallel getrennt, ob eine Meldung an das BACS, den EDÖB oder die Kantonspolizei angezeigt oder vorgeschrieben ist. Bei kritischen Infrastrukturen gilt für bestimmte Cyberangriffe eine BACS-Meldepflicht innert 24 Stunden. Bei Personendaten entscheidet das voraussichtlich hohe Risiko über eine EDÖB-Meldung. [1] [2] [3]

## Warum die erste Stunde über den weiteren Schaden entscheidet

**Ransomware** ist Schadsoftware, die Daten oder Systeme verschlüsseln und häufig zusätzlich mit einer Veröffentlichung erbeuteter Daten drohen kann. In der ersten Stunde geht es nicht darum, jedes technische Detail abschliessend zu verstehen. Vorrang haben drei Ziele: die Ausbreitung stoppen, entscheidungsrelevante Spuren bewahren und den Betrieb für eine kontrollierte Wiederherstellung vorbereiten. Das BACS empfiehlt, infizierte Systeme sofort vom Netz zu trennen, Logdateien zu sichern und vor weiteren Reparaturversuchen oder Neustarts über eine forensische Sicherung zu entscheiden. [1]

Die Geschäftsleitung sollte den Vorfall deshalb nicht als reine IT-Störung behandeln. Bestimmen Sie sofort eine Person als **Incident Lead**. Das ist die Person, die Lagebild, Prioritäten und Freigaben zusammenführt. Sie muss nicht jede technische Massnahme selbst ausführen. Sie sorgt aber dafür, dass IT, externe Dienstleister, Geschäftsleitung und gegebenenfalls Kommunikation mit demselben bestätigten Informationsstand arbeiten.

Nutzen Sie für die Abstimmung möglichst einen vom betroffenen Netz unabhängigen Kanal, etwa Telefon oder einen vorbereiteten Krisenkanal. Angreifer können kompromittierte Kommunikation beobachten. CISA empfiehlt deshalb eine koordinierte Isolierung und einen Kommunikationsweg ausserhalb der möglicherweise betroffenen Infrastruktur. [5]

## Minute 0–15: Führung übernehmen und Ausbreitung begrenzen

### 1. Vorfall erklären, Zeit festhalten, Verantwortliche bestimmen

Notieren Sie den Zeitpunkt der Entdeckung, die meldende Person, sichtbare Symptome und die bereits getroffenen Massnahmen. Benennen Sie Incident Lead, technische Einsatzleitung und eine Stellvertretung. Legen Sie eine Entscheidungslog an: Wer hat wann welches System isoliert, welche Konten gesperrt und welche Annahme lag zugrunde? Diese Chronologie hilft später bei Forensik, Meldungen und dem Wiederanlauf.

Melden Sie intern nur die bestätigten Fakten: etwa verschlüsselte Dateien, eine Lösegeldnotiz, ungewöhnliche Anmeldeereignisse oder nicht erreichbare Freigaben. Vermeiden Sie Schuldzuweisungen und spekulative Erklärungen. Ein frühes, nüchternes Lagebild ist wertvoller als eine scheinbar vollständige, aber ungesicherte Diagnose.

Ein einzelnes unspezifisches Anzeichen wie ein deutlich langsamer Computer belegt noch keine Infektion. Treten mehrere ungewöhnliche Beobachtungen auf oder warnt ein Sicherheitsprogramm, lassen Sie den Verdacht technisch untersuchen und informieren Sie bei Geschäftsgeräten die zuständige IT. [10]

### 2. Betroffene Systeme isolieren – nicht reflexartig ausschalten

Trennen Sie sichtbar betroffene Endgeräte und Server unverzüglich vom Netzwerk: Netzwerkkabel ziehen, WLAN deaktivieren oder das Gerät in eine vorgesehene Quarantäne überführen. Bei mehreren betroffenen Systemen oder Subnetzen kann es notwendig sein, die Verbindung auf Switch-Ebene zu unterbrechen. Priorisieren Sie Systeme, deren weiterer Betrieb die Verschlüsselung von Freigaben, Backups oder kritischen Prozessen fördern könnte. [1] [5]

**Nicht neu starten und nicht bereinigen**, solange die Entscheidung über eine forensische Untersuchung offen ist. Ein Neustart oder Reparaturversuch kann flüchtige Spuren im Arbeitsspeicher und weitere Beweismittel beseitigen. Ausschalten ist ein Notbehelf, wenn sich ein Gerät nicht anders vom Netz trennen lässt und eine weitere Ausbreitung droht; auch dann geht möglicherweise flüchtige Evidenz verloren. [1] [5]

Sperren Sie keinen ganzen Betrieb unkoordiniert. Halten Sie fest, welche Fernzugänge, Administrationskonten oder Freigaben technisch betroffen sein könnten, und lassen Sie die technische Einsatzleitung über gezielte Schutzmassnahmen entscheiden. Unkontrollierte globale Passwortwechsel oder Änderungen an zentralen Diensten können die Analyse und den Betrieb zusätzlich erschweren.

### 3. Menschen und Geschäftsprozesse schützen

Informieren Sie Prozessverantwortliche über konkrete betriebliche Einschränkungen: beispielsweise, dass keine Dokumente auf einem bestimmten Laufwerk geöffnet oder keine Lieferdaten aus einem betroffenen System verwendet werden dürfen. Für kritische Leistungen sind vorab definierte manuelle Ersatzprozesse oft sicherer als improvisierte Systemeingriffe. Das BACS ordnet klare Verantwortlichkeiten, Notfallkontakte und Krisenkommunikation ausdrücklich als Bestandteile eines Notfallkonzepts ein. [6]

## Minute 15–30: Betroffene Systeme erfassen und Beweise sichern

### 4. Lagebild aufbauen statt nur Dateien zu zählen

Erstellen Sie eine erste Liste: Geräte- und Servername, Benutzerkonto, Standort, Netzwerksegment, Zeitpunkt der Beobachtung, Symptome, letzter bekannter funktionierender Zustand und geschäftliche Abhängigkeiten. Kennzeichnen Sie klar, was bestätigt, vermutet oder noch unbekannt ist. Fotografieren oder dokumentieren Sie Lösegeldnotizen, Fehlermeldungen und auffällige Dateiendungen, ohne die betroffenen Dateien zu verändern.

Sichern Sie verfügbare **Logdateien**. Das sind automatisch aufgezeichnete Ereignisprotokolle von beispielsweise Firewall, E-Mail-Gateway, VPN, Identitätsdienst, Endpoint-Schutz und Servern. Sie können zeigen, welche Konten und Systeme betroffen sind und ob verdächtige Verbindungen bestanden. Das BACS nennt insbesondere Protokolle von E-Mail-Server, Proxy, Firewall und weiterer Sicherheitssoftware als wichtige Grundlage, um Ausmass, URLs und IP-Adressen zu ermitteln. [1]

Bewahren Sie die Originale nachvollziehbar auf und arbeiten Sie, wenn möglich, mit Kopien. Notieren Sie Quelle, Zeitraum, Exportzeitpunkt und verantwortliche Person. Löschen Sie keine verdächtigen E-Mails, Dateien oder Alarmmeldungen. Die technische Einsatzleitung kann bekannte schädliche URLs oder IP-Adressen an Proxy und Firewall blockieren, wenn dies anhand belastbarer Informationen geschieht. [1]

### 5. Früh über Forensik und Strafanzeige entscheiden

**Forensik** bedeutet die fachgerechte Sicherung und Untersuchung digitaler Spuren mit dem Ziel, Ursache, Umfang und mögliche Beweise nachvollziehbar zu klären. Entscheiden Sie früh, ob eine spezialisierte Fachperson beigezogen werden soll. Das ist besonders wichtig, wenn eine Strafanzeige erwogen wird oder ein Datenabfluss nicht ausgeschlossen werden kann. Das BACS empfiehlt, Strafverfolgungsbehörden in diesem Fall früh zu informieren und Sicherungen von Arbeitsspeicher und Festplatten vor Neustarts oder Reparaturversuchen durch fachkundige Personen vorzunehmen. [1]

**[FACHPRÜFUNG ERFORDERLICH]** Lassen Sie Umfang und Vorgehen durch eine qualifizierte Incident-Response- oder Forensik-Fachperson beurteilen, wenn die eigene Organisation diese Kompetenz nicht hat. Auch CISA empfiehlt, besonders flüchtige oder nur kurz gespeicherte Beweise wie Arbeitsspeicher und Logpuffer früh zu sichern. [5]

## Minute 30–45: Backups schützen, Wiederanlauf noch nicht starten

### 6. Backup-Umgebung vom Vorfall abgrenzen

Ein Backup hilft nur, wenn es lesbar, vollständig und vom Angreifer nicht ebenfalls verändert oder gelöscht wurde. Beenden oder unterbrechen Sie daher nach fachlicher Abklärung automatisierte Backup- und Synchronisationsläufe, die verschlüsselte Daten in Sicherungen übernehmen könnten. Trennen Sie die Backup-Verwaltung und vorhandene Sicherungsmedien vom betroffenen Produktionsnetz, soweit dies ohne Verlust vorhandener Sicherungen möglich ist. Verwenden Sie für die Prüfung keine Zugangsdaten, die vermutlich auf kompromittierten Systemen hinterlegt waren.

Dokumentieren Sie für jede relevante Sicherung den letzten erfolgreichen Lauf, das enthaltene Datum, Aufbewahrungsort, Administrationsweg und den Status der Unveränderbarkeit oder Offline-Lagerung. Halten Sie zusätzlich fest, ob ein Test der Wiederherstellbarkeit vor dem Vorfall vorliegt. CISA empfiehlt offline gehaltene, verschlüsselte Backups sowie regelmässig getestete Verfügbarkeit und Integrität. [5]

Starten Sie jetzt **keine** Wiederherstellung in die bisherige Umgebung. Das BACS stellt die Neuinstallation betroffener Systeme vor die Wiederherstellung von Daten; CISA warnt ebenfalls davor, saubere Systeme während der Wiederherstellung erneut zu infizieren. Der Wiederanlauf gehört auf eine bereinigte, kontrollierte Grundlage und folgt einer priorisierten Liste kritischer Dienste. [1] [5]

Für die anschliessende Architekturprüfung sind die Themen [ransomware-resistente Backups](/wissen/ransomware-resistente-backups) und [Backup-Wiederherstellung realistisch testen](/wissen/backup-wiederherstellung-testen) relevant. In der Akutphase genügt zunächst die klare Antwort auf zwei Fragen: Welche Sicherungen sind vom Produktionsnetz getrennt, und welcher Datenstand ist nachweisbar verfügbar?

## Minute 45–60: BACS, Polizei und EDÖB richtig einordnen

Meldungen verfolgen unterschiedliche Zwecke. Sie ersetzen einander nicht. Prüfen Sie sie parallel und dokumentieren Sie die Beurteilung.

### BACS: Pflicht für bestimmte kritische Infrastrukturen, freiwillige Meldung für andere

Für **nicht jedes KMU** besteht allein wegen eines Ransomware-Vorfalls eine allgemeine gesetzliche BACS-Meldepflicht. Meldepflichtig sind die im Informationssicherheitsgesetz und in der Cybersicherheitsverordnung erfassten Behörden und Organisationen kritischer Infrastrukturen, etwa in Energie- oder Trinkwasserversorgung, Transport sowie kantonalen und kommunalen Verwaltungen. Die genaue Einordnung und allfällige Ausnahme müssen im konkreten Fall geprüft werden. [2] [8]

Ist Ihr Unternehmen erfasst und gefährdet der Angriff die Funktionsfähigkeit, führt er zu Manipulation oder Informationsabfluss, blieb er länger unentdeckt oder ist er mit Erpressung, Drohung oder Nötigung verbunden, muss die Meldung innert 24 Stunden nach Entdeckung an das BACS erfolgen. Unbekannte Angaben dürfen die Erstmeldung nicht verzögern; der Gesetzestext verlangt die Ergänzung, sobald neue Informationen vorliegen. [8]

Für die elektronische Übermittlung stellt das BACS ein sicheres System bereit. Die aktuelle BACS-Meldeoberfläche nennt ausserdem `incidents@ncsc.ch` als alternative Übermittlung und ordnet eine solche E-Mail ausdrücklich als fristwahrende Erstmeldung ein. Auf derselben Oberfläche bezeichnet das BACS die Schlussmeldung innert 14 Tagen als nächsten Schritt. Dieser praktische Meldeweg und seine Anforderungen sind im konkreten Fall unmittelbar vor der Übermittlung zu prüfen; sie ändern weder die gesetzliche Einzelfallprüfung noch den Wortlaut von Art. 74e ISG. [2] [8] [11]

Auch Organisationen ohne gesetzliche Pflicht können Cybervorfälle dem BACS freiwillig melden. [11] Für akute Gefährdungen oder eine Strafanzeige gelten die zuständigen polizeilichen Kontaktwege. [9]

### Polizei: Strafanzeige früh mit Beweissicherung abstimmen

Eine Strafanzeige erstatten Sie bei der Kantonspolizei am Geschäftssitz. Das BACS rät bei erwogener Lösegeldzahlung ausdrücklich, das Vorgehen mit der Kantonspolizei zu besprechen. Für nicht über den Online-Polizeiposten erfassbare Delikte ist eine Polizeistelle zuständig. [1] [9]

Übergeben Sie keine vorschnell bearbeiteten Systeme. Stellen Sie stattdessen das Ereignisprotokoll, gesicherte Logs, Lösegeldforderung, betroffene Systemliste und vorhandene technische Beobachtungen bereit. Die Polizei oder eine beigezogene Forensik-Fachperson bestimmt, welche weiteren Spuren gesichert werden sollen.

### EDÖB: Personendaten und hohes Risiko beurteilen

Ransomware kann eine **Verletzung der Datensicherheit** nach Datenschutzgesetz sein, wenn Personendaten unbeabsichtigt oder widerrechtlich verloren gehen, verändert werden oder Unbefugten offengelegt beziehungsweise zugänglich gemacht werden. Allein die technische Bezeichnung «Ransomware» entscheidet aber nicht automatisch über eine Meldung. [4]

Der Verantwortliche muss den EDÖB nach Art. 24 DSG **so rasch als möglich** informieren, wenn die Verletzung voraussichtlich zu einem hohen Risiko für Persönlichkeit oder Grundrechte natürlicher Personen führt. Die Meldung muss mindestens Art der Verletzung, Folgen sowie ergriffene oder vorgesehene Massnahmen nennen. Betroffene Personen sind zu informieren, wenn dies zu ihrem Schutz erforderlich ist oder der EDÖB es verlangt. [3]

Der EDÖB stellt Verantwortlichen für diese Meldung ein sicheres Online-Formular zur Verfügung; es ist nicht das Kontaktformular für betroffene Personen. Art. 15 DSV konkretisiert die zu erfassenden Angaben: soweit möglich Zeitpunkt und Dauer, Kategorien und ungefähre Anzahl betroffener Daten und Personen, Folgen und Risiken, getroffene oder vorgesehene Massnahmen sowie eine Ansprechperson. Fehlende Angaben sind so rasch als möglich nachzureichen; der Verantwortliche muss die Verletzung mit Tatsachen, Auswirkungen und Massnahmen dokumentieren. [13] [14]

Prüfen Sie diese Schwelle nicht erst nach Abschluss der Technikarbeiten. Der EDÖB weist darauf hin, dass bei Zweifeln, welche ein hohes Risiko nicht mit hinreichender Wahrscheinlichkeit ausschliessen, nicht zugewartet werden darf. Besonders schützenswerte Daten, identifizierende Unterlagen, mögliche Veröffentlichung oder ein nicht ausschliessbarer Abfluss können die Bewertung beeinflussen. **[FACHPRÜFUNG ERFORDERLICH]** Die konkrete Risiko- und Meldebeurteilung sowie Meldetexte brauchen eine Datenschutz- oder Rechtsfachperson; dieser Artikel ersetzt keine individuelle Rechtsberatung. [4]

Der vertiefende Entscheidungsweg folgt im Beitrag [Datenpanne in der Schweiz: EDÖB oder BACS?](/wissen/datenpanne-melden-schweiz).

## Hypothetisches Praxisbeispiel: Produktion und Dateiablage betroffen

> **Hypothetisches Beispiel, kein Kundenfall:** Um 08.12 Uhr meldet ein Mitarbeiter einer Maschinenbau-KMU, dass Dateien auf einer Projektfreigabe nicht mehr geöffnet werden können. Die IT sieht eine Lösegeldnotiz und trennt den betroffenen Arbeitsplatz sowie die Freigabe vom Netz. Die Geschäftsleitung setzt die IT-Leitung als Incident Lead ein und informiert Produktion und Disposition telefonisch über den Ausfall.
>
> Bis 08.30 Uhr liegen eine Systemliste, Screenshots der Forderung und Exporte der Firewall-, VPN- und Identitätsprotokolle vor. Da die Projektfreigabe Personendaten enthalten kann und ein Datenabfluss nicht ausgeschlossen ist, wird eine Fachperson zur forensischen und datenschutzrechtlichen Beurteilung beigezogen. Bis 08.45 Uhr wird die Backup-Verwaltung vom Produktionsnetz abgegrenzt; eine Wiederherstellung wird noch nicht ausgelöst. Bis 09.12 Uhr prüft das Team die BACS-Relevanz, bereitet eine Strafanzeige vor und hält die EDÖB-Risikobeurteilung im Entscheidungslog fest. Erst danach beginnt die vertiefte Untersuchung.

Das Beispiel zeigt keinen Erfolgsablauf und keine Garantie. Es veranschaulicht nur die Reihenfolge: eindämmen, belegen, Sicherungen schützen, Pflichten klären.

## Lösegeld ist keine verlässliche Wiederherstellungsstrategie

Das BACS rät von Lösegeldzahlungen ab. Eine Zahlung garantiert weder Entschlüsselung noch Nichtveröffentlichung oder Nichtweitergabe der Daten. Sie kann den Angriff zudem wirtschaftlich fördern. Wird eine Zahlung dennoch erwogen, empfiehlt das BACS ausdrücklich die Abstimmung mit der Kantonspolizei. [1]

Die Geschäftsleitung sollte daher nicht unter Zeitdruck allein über eine Zahlungsforderung entscheiden. Klären Sie zuerst, welche Systeme betroffen sind, ob Daten abgeflossen sein könnten, welche Backups vorhanden sind, welche Meldepflichten bestehen und welche Ermittlungs- oder Versicherungsprozesse einzubeziehen sind. Vertrags- und sanktionsrechtliche Fragen gehören zur fachlichen Prüfung durch dafür zuständige Stellen.

## Typische Fehler in der Akutphase

Der häufigste Fehler ist der vorschnelle Neustart eines Geräts. Er kann eine Ausbreitung zwar in Einzelfällen unterbrechen, vernichtet aber möglicherweise flüchtige Spuren. Besser ist die sofortige Netztrennung; ausschalten bleibt die Ausnahme, wenn keine andere Eindämmung möglich ist. [1] [5]

Ebenso riskant ist es, verschlüsselte Daten aus laufender Synchronisation in Sicherungen zu übernehmen oder Backups ohne Prüfung in die kompromittierte Umgebung zurückzuspielen. Wiederherstellung ist kein erster Schritt, sondern Teil einer kontrollierten Bereinigung. [1] [5]

Ein dritter Fehler ist, Meldungen als reine Formalität zu behandeln. Die BACS-Meldepflicht, eine Strafanzeige und die EDÖB-Beurteilung haben unterschiedliche Auslöser. Wer den Entscheid, die zugrunde liegenden Fakten und den Zeitpunkt nicht dokumentiert, erschwert spätere Nachweise und Korrekturen. Das aktuelle BACS-Notfallkonzept ordnet daher Rollen, Meldung, Vorfallsbewältigung und Nachbearbeitung als zusammenhängende Phasen ein. [6]

## Nach der ersten Stunde: kontrolliert bereinigen und lernen

Nach der Stabilisierung folgen Ursachenanalyse, Bereinigung, Neuaufbau und priorisierte Wiederherstellung. Prüfen Sie auch den ursprünglichen Zugang: kompromittierte Konten, Fernzugänge, Schwachstellen oder missbrauchte Administrationswege können sonst den erneuten Zugriff ermöglichen. CISA empfiehlt, nach vollständiger Bereinigung betroffene Passwörter zurückzusetzen, Persistenzmechanismen zu entfernen und Systeme auf einer sauberen Grundlage wieder aufzubauen. [5]

Ein nachträglich eingespieltes Sicherheitsupdate schliesst eine bekannte Schwachstelle, ist aber kein Nachweis dafür, dass davor keine Kompromittierung erfolgt ist. Das BACS weist in seiner aktuellen Warnung zu kritischen PHP-Schwachstellen ausdrücklich darauf hin, dass ein Update eine bereits erfolgte Kompromittierung nicht beseitigt. Diese allgemeine Abgrenzung enthält weder eine Aussage über ein bestimmtes Produkt noch eine organisationsspezifische Forensikanweisung. [12]

Dokumentieren Sie Befunde, Entscheidungen, Auswirkungen, Meldewege und offene Risiken in einem Debriefing. NIST empfiehlt, Incident Response in das laufende Cyberrisikomanagement einzubetten, damit Vorbereitung, Erkennung, Reaktion und Wiederherstellung messbar verbessert werden. [7] Eine [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) kann technische Schwachstellen und blinde Flecken sichtbar machen. Im [Risikomanagement](/unsere-dienstleistungen/risikomanagement) lassen sich geschäftliche Auswirkungen, Eigentümer und Restrisiken verbindlich steuern. Die allgemeinen [Kontaktdaten](/kontakt) gehören zusammen mit Polizei, Versicherer, IT-Provider und Fachpersonen in die offline verfügbare Notfallmappe.

## Nächster Schritt

Nutzen Sie die [60-Minuten-Checkliste](/resources/01-60-minuten-checkliste), um Rollen, Zeitpunkte und offene Entscheide zu dokumentieren. Wenn Sie Unterstützung bei der Vorbereitung Ihres Notfallplans wünschen, können Sie eine [DKSchV-Notfallplanungsleistung](/unsere-dienstleistungen/notfallplanung) anfragen. Umfang und Ergebnis hängen von der vereinbarten Leistung und Ihrer Ausgangslage ab.

## Grenzen dieses Sofortleitfadens

Diese Anleitung ist eine allgemeine operative Orientierung für Schweizer KMU auf dem Stand der Quellenprüfung vom 1. November 2026; dieser Stand ist keine Fachfreigabe. Sie ersetzt weder eine technische Forensik noch eine individuelle rechtliche, datenschutzrechtliche, strafrechtliche, versicherungs- oder sanktionsrechtliche Beratung. **[FACHPRÜFUNG ERFORDERLICH]** Lassen Sie insbesondere die Einstufung als kritische Infrastruktur, die BACS-Meldepflicht, das hohe Risiko nach Art. 24 DSG, Meldetexte und den Umgang mit Lösegeld durch qualifizierte Fachpersonen prüfen. Halten Sie dafür die 60-Minuten-Checkliste und Ihren Entscheidungslog bereit.

## Quellen

[1]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[2]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Art. 24 Meldung von Verletzungen der Datensicherheit"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information Betroffener nach Art. 24 DSG"
[5]: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware "CISA – I've Been Hit By Ransomware! Response Checklist"
[6]: https://www.bacs.admin.ch/de/notfallkonzept "BACS – Das Notfallkonzept als Schlüssel zur Cyberresilienz"
[7]: https://csrc.nist.gov/pubs/sp/800/61/r3/final "NIST SP 800-61 Rev. 3 – Incident Response Recommendations and Considerations for Cybersecurity Risk Management"
[8]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Bundesgesetz über die Informationssicherheit, Art. 74a–74h Cyberangriffe auf kritische Infrastrukturen"
[9]: https://www.suisse-epolice.ch/cybercrime-case "Suisse ePolice – Cyberkriminalität anzeigen"
[10]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 6. Oktober 2026"
[11]: https://www.report.ncsc.admin.ch/de/chat?path=406%3E407%3E1 "BACS – Freiwillige Meldung eines Cybervorfalls"
[12]: https://www.bacs.admin.ch/de/warnung-php-de "BACS – Kritische Schwachstellen in PHP: Sicherheitsupdates sofort einspielen, 21. Oktober 2026"
[13]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach: Meldung von Datensicherheitsverletzungen durch Verantwortliche"
[14]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz, Art. 15 Meldung von Verletzungen der Datensicherheit"
