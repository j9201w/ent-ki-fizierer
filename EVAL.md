# EVAL.md – So sind die Beispiele zu lesen und zu prüfen

Diese Datei erklärt den Ordner `examples/`. Sie richtet sich an Nutzer und Mitentwickler, nicht an den Skill selbst: Der Skill kennt diese Dateien nicht und braucht sie nicht. Sie dienen der Dokumentation und als Prüf-/Regressionsset.

## Was im Ordner liegt

`examples/` ist nach **Textsorte** gegliedert, nicht nach Version. Der aktuelle Stand passt immer zur aktuellen `SKILL.md`; ältere Stände stehen im Git-Verlauf bzw. unter dem jeweiligen Release-Tag.

```
examples/
├── academic_education/
├── corporate_business/
├── creative_prose/
├── daily_casual/
├── marketing_social/
├── press_journalism/
├── seo_tech/
└── support_service/
```

Pro Fall gibt es zwei Dateien:

- `NN_input.txt` – ein typischer KI-/LLM-Deutsch-Text (der Input).
- `NN_expected.txt` – wie das ent-ki-fizierte Ergebnis ungefähr aussehen soll (das Referenzziel).

## Das Wichtigste zuerst: Referenzziele, keine Soll-Strings

Die `expected`-Dateien sind **Referenzziele**, keine zeichengenau einzuhaltenden Vorgaben. Stil-Umschreibungen haben viele gleich gute Lösungen. Eine Ausgabe ist also nicht „falsch", nur weil sie anders formuliert ist als das Expected.

**Nicht** per Exact-Match (`output == expected`) vergleichen. Stattdessen **nach Kriterien** bewerten (siehe Prüfliste unten) oder per LLM-Grader, der fragt: „Erfüllt die Ausgabe dieselben Kriterien wie die Referenz und transportiert sie denselben Inhalt?"

## Nur den „Final"-Block vergleichen

Seit v2.0.0 gibt der Skill **vier Teile** aus: Draft, ein kurzes Audit („Was klingt hier noch nach KI?"), den finalen Text und eine Änderungsliste. Die `expected`-Dateien enthalten nur den **finalen Text**.

Vor dem Vergleich also erst den Final-Block aus der Ausgabe herausziehen. Draft, Audit und Änderungsliste sind von Lauf zu Lauf variabel und gehören nicht in den Vergleich.

```python
import re

def extract_final(output: str) -> str:
    """Zieht den Text zwischen '**Final:**' und '**Änderungen:**' aus der 2.0.0-Ausgabe."""
    m = re.search(r"\*\*Final:\*\*\s*(.+?)(?:\n\s*\*\*Änderungen:\*\*|\Z)", output, re.S)
    return (m.group(1).strip() if m else output.strip())
```

## Prüfliste „bestanden / nicht bestanden"

Diese Kriterien folgen direkt aus den Regeln der `SKILL.md`. Ein guter Final-Text erfüllt sie alle:

- [ ] **Keine Em-/En-Dashes** (`—`, `–`) im Text.
- [ ] **Deutsches Zahlenformat:** Dezimalkomma (`12,4 %`, `1,5 Sekunden`, `24,95 €`), und `2024` statt `In 2024`.
- [ ] **Deutsche Anführungszeichen** `„…"` statt `"…"`.
- [ ] **Keine Standard-Floskeln** (z. B. *Darüber hinaus, Des Weiteren, Es ist wichtig zu beachten, Zusammenfassend lässt sich sagen, Abschließend bleibt festzuhalten*).
- [ ] **Kein „man", kein Passiv-Cluster, kein Nominalstil-Cluster.**
- [ ] **Keine hohlen Buzzwords** (*bahnbrechend, nahtlos, ganzheitlich, revolutionär, Game-Changer, maximieren* …).
- [ ] **Inhalt erhalten:** alle Fakten, Zahlen, Eigennamen und wörtlichen Zitate stehen unverändert drin.
- [ ] **Struktur erhalten:** ungefähr gleiche Absatz-/Satzanzahl, keine erfundenen Zusätze (z. B. keine Anrede, die im Input nicht stand).
- [ ] **Register stimmt:** Du/Sie wie im Input.
- [ ] **Bei `--casual`:** Modalpartikeln (*ja, doch, mal, nämlich* …) und Perfekt vorhanden, Emoji-/Hashtag-Flut reduziert.
- [ ] **Kein Chatbot-Rahmen** (*Hier ist dein Text, Ich hoffe, das hilft, Gerne!*).

Ein paar dieser Punkte lassen sich automatisch prüfen (Dashes, Zahlenformat, Anführungszeichen, Floskel-Blacklist per Regex/grep); der Rest ist eine inhaltlich-stilistische Bewertung.

## Welche Fälle sind „kontaminiert"?

Beispiele, die als Few-Shots **in der `SKILL.md`** stehen, hat das Modell beim Transformieren bereits gesehen. Sie taugen daher zur *Steuerung*, aber nicht als *unabhängiger* Test. Halte solche Fälle aus der Messung heraus (held-out).

**Aktueller Stand:** Keiner der Fälle aus `examples/` ist in der `SKILL.md` eingebettet (die Vorher/Nachher-Paare und das Vollbeispiel dort sind eigenständige, generische Texte). Damit sind derzeit **alle** Fälle in `examples/` saubere, unabhängige Testfälle.

**Wenn du später Few-Shots aus diesem Set in die `SKILL.md` hochziehst,** trage sie hier ein und schließe sie vom unabhängigen Test aus, z. B.:

| Fall | als Few-Shot in SKILL.md | nur Doku / held-out |
| --- | --- | --- |
| `seo_tech/05` | – | held-out |
| … | … | … |

## Welche Eval-Version gehört zu welcher Skill-Version?

Es gibt **keine** Versionsordner. Der Ordnerinhalt entspricht immer der aktuellen `SKILL.md`. Die Zuordnung „dieser Eval-Stand gehört zu Skill vX.Y.Z" steht im Changelog der `README.md` und in den Git-Tags. Den Stand zu einem früheren Release bekommst du über `git checkout <tag>`.

## Kurz: der Prüfablauf in fünf Schritten

1. `NN_input.txt` durch den Skill schicken (passender Modus, z. B. `--casual` für `daily_casual`).
2. Aus der Ausgabe den **Final-Block** extrahieren.
3. Final gegen `NN_expected.txt` halten – **als Referenz**, nicht als Pflichtwortlaut.
4. Prüfliste oben durchgehen (teils automatisch, teils inhaltlich).
5. Abweichungen notieren und ggf. die Regeln in der `SKILL.md` schärfen, nicht die Expecteds an die Ausgabe anpassen.
