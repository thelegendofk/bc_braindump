# KI-Kostenmodell im Angebot, Entscheidung und Platzierung

Diese Datei entscheidet zwei Dinge für ein Angebot mit KI-gestützter Entwicklung: wie
Werkzeug-, Modell- und Tokenkosten in den Preis kommen, und wo die Erfassungslogik im
Dokument steht. Den Wortlaut der Klauseln trägt die Datei
`textbausteine-ki-verrechnung.md` im Skill `tender-document-library`. Diese Datei trägt die Wahl, jene den Text.

Grundlage: Weisung Arbeitszeiterfassung in KI-SWE-Projekten, Version 1.1, Abschnitt 9. Die
Weisung verlangt, dass die Projektleitung pro Angebot genau eine der drei Varianten wählt und
die Wahl vor Projektstart dokumentiert.

Der Grund, warum es diese Entscheidung überhaupt gibt: weil wir unbetreute Laufzeit nicht als
Arbeitszeit verrechnen, fehlt den Modell- und Tokenkosten der Weg über die Stunden. Sie sind
echte Projektkosten und brauchen einen eigenen, offen deklarierten Weg in die Offerte.

## Die Entscheidung in vier Fragen

Der Reihe nach durchgehen, die erste zutreffende Antwort gewinnt.

1. **Ist der Scope abgrenzbar, sind die Anforderungen belastbar, und gibt es einen
   definierten Änderungsprozess?**
   Ja: Variante 2, Festpreis pro Ergebnis. Es ist die stärkste Variante, weil sie die
   Diskussion über Zeit und Laufzeiten ganz beendet. Nein bei einem der drei Punkte: weiter.

2. **Ist der Kunde kostensensitiv, öffentlich, oder verlangt er eine nachvollziehbare
   Positionsliste?**
   Ja: Variante 3, separate Position. Höchste Transparenz, und sie ist die einzige Variante,
   die unbeaufsichtigte Läufe ausdrücklich abdeckt. Preis: die Position wird zum
   Verhandlungspunkt.

3. **Sind unbetreute Läufe ein wesentlicher Kostenblock?**
   Typisch bei Migrationen, Massenanalysen, Nacht- und Batchläufen. Ja: Variante 3, auch wenn
   Frage 2 mit nein beantwortet wurde. Begründung unten, Abschnitt Deckungsprobe.

4. **Sonst**: Variante 1, KI-Premium-Stundensatz. Das ist der Standardfall bei laufenden
   T&M-Mandaten: eine Zahl, keine Zusatzposition, keine Nachweispflicht.

## Die drei Varianten im Vergleich

| | 1, Premium-Stundensatz | 2, Festpreis pro Ergebnis | 3, Separate Position |
|---|---|---|---|
| Umsetzung | Standardsatz plus 10 bis 20 Prozent | Preis pro Ergebnis, Kosten in der Kalkulation | Eigene Position, Pauschale, 3 bis 8 Prozent oder durchgereicht |
| Was der Kunde sieht | Einen höheren Satz | Einen Preis | Eine zusätzliche Zeile |
| Eignung | Laufende T&M-Mandate | Abgrenzbarer Scope | Kostensensitive und öffentliche Kunden |
| Deckt unbetreute Läufe | Nur indirekt über die Stunden | Ja, über die Kalkulation | Ja, ausdrücklich |
| Nachweispflicht | Keine | Keine | Bei Durchreichung ja, monatlich |
| Verhandlungsangriff | "Warum ein höherer Satz?" | "Warum dieser Preis?" | "Streichen wir die Position" |
| Grösstes Risiko | Zuschlag deckt die Kosten nicht mehr, wenn die Stunden sinken | Scope ohne Änderungsprozess | Position wird herausverhandelt, Kosten bleiben |

## Die Deckungsprobe für Variante 1

Variante 1 hat einen eingebauten Widerspruch, der in der Weisung nicht steht und der bei
stark KI-getriebenen Projekten zuschlägt: der Zuschlag skaliert mit den verrechneten Stunden,
die Tokenkosten skalieren mit der Anzahl und Länge der Läufe. Je besser die KI wirkt, desto
weniger Stunden und desto mehr Läufe. Der Zuschlag trägt also genau dann am wenigsten, wenn
er am meisten gebraucht wird.

Vor der Wahl von Variante 1 einmal rechnen:

```
erwartete Modell- und Tokenkosten pro Monat
--------------------------------------------  =  nötiger Zuschlag pro Stunde
erwartete verrechnete Stunden pro Monat
```

Liegt das Ergebnis über 20 Prozent des Standardsatzes, trägt Variante 1 nicht. Dann Variante
3 wählen, oder Variante 2 mit dem Kostenblock in der Kalkulation. Die Zahl gehört in die
interne Kalkulation, nicht ins Angebot.

## Wo es im Angebot steht

Die Erfassungslogik ist kein eigenes Kapitel. Sie wird an drei Stellen sichtbar, jede mit
einer anderen Funktion.

| Ort im Angebot | Baustein | Funktion |
|---|---|---|
| Vorgehen oder Qualitätssicherung | TB-5 | Wir setzen KI ein, wir prüfen jedes Ergebnis, wir stehen für die Qualität ein. Das ist ein Argument, kein Kleingedrucktes |
| Kommerzielles Angebot, bei den Sätzen | TB-1, plus TB-2, TB-3 oder TB-4 je Variante | Was verrechnet wird und was nicht, plus der Weg der Werkzeugkosten |
| Annahmen und Rahmenbedingungen | eigener Satz, siehe unten | Was wir voraussetzen, damit die Erfassung so funktioniert |

Für die Annahmen genügt ein Satz, zum Beispiel: "Die Angaben zum Aufwand setzen voraus, dass
Umgebungen und Zugänge zu Projektbeginn bereitstehen und Rückmeldungen zu Ergebnissen
innerhalb von zwei Arbeitstagen erfolgen."

Reihenfolge im kommerziellen Kapitel: erst der Preis, dann die Erfassungsklausel. Die Klausel
begründet den Preis, sie geht ihm nicht voraus.

## Die Argumentation, je Variante zwei Sätze

Variante 1, der höhere Satz ist der schwierigste Verkauf und braucht die Rechnung, nicht die
Haltung:

> Wir verrechnen für dasselbe Ergebnis weniger Stunden als ohne KI-Unterstützung. Der Satz
> für KI-gestützte Entwicklung liegt X Prozent über dem Standardsatz und enthält alle
> Werkzeug- und Modellkosten, unter dem Strich zahlen Sie für dieses Arbeitspaket weniger.

Wenn möglich mit einer Zahl aus einem vergleichbaren Paket. Ohne Vergleichszahl wirkt der
Satz wie eine Preiserhöhung mit neuer Begründung.

Variante 2:

> Sie kaufen das Ergebnis, nicht den Aufwand. Werkzeug- und Modellkosten sind Teil unserer
> Kalkulation, Sie tragen kein Risiko für Laufzeiten und Wiederholungen.

Variante 3:

> Die Werkzeug- und Modellkosten stehen als eigene Position, damit Sie sehen, was davon
> Arbeitszeit ist und was Infrastruktur. Diese Position deckt auch die Läufe, die wir Ihnen
> nicht als Arbeitszeit verrechnen.

Der zweite Satz ist der wichtige. Er macht aus einer zusätzlichen Zeile eine Gegenleistung
für einen Verzicht.

## Einwände und Antworten

| Einwand | Antwort |
|---|---|
| "Mit KI sollte es doch günstiger werden, nicht teurer" | Es wird günstiger, über die Stunden. Der Satz steigt, die Anzahl Stunden sinkt stärker. Mit Zahl aus einem vergleichbaren Paket belegen |
| "Wir zahlen doch nicht für Ihre Werkzeuge" | Sie zahlen für das Ergebnis. Wenn Ihnen eine eigene Position lieber ist als ein höherer Satz, machen wir das, aber nicht beides |
| "Streichen wir die KI-Position" | Dann geht sie in den Stundensatz, der Preis bleibt derselbe. Die Wahl ist die Darstellung, nicht die Höhe |
| "Wie belegen Sie diese Kosten?" | Bei Durchreichung monatlich mit Nachweis. Bei Pauschale und Prozentanteil nicht, dafür mit Kostensicherheit für Sie |
| "Warum verrechnen Sie Wartezeit gar nicht?" | Weil wir in dieser Zeit nicht an Ihrer Lösung arbeiten. Das ist die Zusage, die den Rest glaubwürdig macht |

## Was nicht gemacht wird

- Nie zwei Varianten für dieselbe Leistung. Premium-Satz und Tokenposition zusammen ist
  doppelte Verrechnung derselben Kosten (Weisung Abschnitt 9).
- Nie eine Variante in ein laufendes Mandat nachschieben. Einführung nur mit Verlängerung
  oder neuem Projekt, geführt von Account und Projektleitung.
- Nie den Effizienzgewinn über die Stundenlogik zurückholen. Wenn Stunden das Ergebnis nicht
  mehr abbilden, ist das der Anlass für Variante 2, nicht für längere Buchungen.
- Nie Modellnamen, Prompts oder interne Werkzeuge offenlegen, um den Preis zu begründen. Das
  ist unser Know-how. Für Fragen zu Datenverarbeitung und Personendaten
  `isms-proposal-assurance` verwenden.
- Keine Zahl in das Angebot schreiben, die aus dieser Datei stammt. Zuschlag, Pauschale und
  Prozentanteil sind Richtwerte für die Kalkulation, der Wert im Angebot kommt aus der
  Kalkulation des Mandats.

## Übergabe

Die gewählte Variante, die Zahl und die Begründung gehören in die `AGENTS.md` des Mandats,
Abschnitt Entscheidungen, mit Datum. Damit ist die Anforderung der Weisung erfüllt, die Wahl
vor Projektstart zu dokumentieren, und die Erfassung im Projekt kann sich darauf berufen
(siehe Skill `ai-time-tracking`).
