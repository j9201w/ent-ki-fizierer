# ent-ki-fizierer (Claude Skill)

Ein spezialisierter Skill für Anthropic Claude, der KI-generierte, hölzerne deutsche Texte in lebendiges, natürliches und authentisches Deutsch verwandelt. 

Im Gegensatz zu englischen Standard-Tools bekämpft dieser Skill gezielt die spezifischen Muster des "LLM-Deutschs". Das Fundament bilden die empirischen Beobachtungen des deutschen Wikipedia-AI-Cleanups, kombiniert mit professionellen Copywriting-, SEO- und Stilistik-Standards (z. B. Wortliga, Duden-Stilkritik).

## 🚀 Funktionsweise

Der Skill analysiert den eingegebenen Text auf typische KI-Indikatoren, filtert hohle Phrasen heraus und formuliert ihn neu. Dabei bleibt der Kerninhalt zu 100 % erhalten und die Absatzstruktur des Originals gewahrt (fünf Absätze rein, fünf Absätze raus), während Stil, Rhythmus und Wortwahl gründlich ent-ki-fiziert werden.

Seit Version 2.0.0 ist der Skill als modularer Muster-Katalog aufgebaut (nummerierte Einträge im Schema „Worauf achten / Problem / Vorher / Nachher") und arbeitet transparent: Er gibt erst einen Entwurf aus, prüft ihn dann in einem kurzen Selbst-Audit auf verbliebene KI-Muster, liefert anschließend den finalen Text und eine knappe Änderungsliste.

### Was der Skill korrigiert:
*   **Nominalstil-Konvertierung:** Macht aus starren Substantiv-Ketten (*"Die Durchführung der Optimierung..."*) aktive Verben (*"Wir optimieren..."*).
*   **Phrasen- & Metaphern-Blacklist:** Eliminiert LLM-Floskeln (*„Darüber hinaus“*) sowie abgenutzte KI-Sprachbilder (*„Der Schlüssel zum Erfolg“*).
*   **Hohle Superlative & Bürokratie-Verben:** Streicht inhaltsleere Buzzwords (*bahnbrechend*, *nahtlos*) und ersetzt steife Verben (*gewährleisten*, *vorantreiben*) durch echte Aktion.
*   **Rhythmus-Bruch & Modalpartikeln:** Zerschlägt monotone Satzlängen und streut organisch deutsche Modalpartikeln (*ja*, *doch*, *mal*) ein, um den Text menschlich klingen zu lassen.
*   **Fehlübersetzungen (False Friends):** Korrigiert typische, aus dem Englischen übernommene KI-Muster wie *„Am Ende des Tages“* oder *„Sinn machen“*.
*   **Weichspüler- & Redundanz-Filter:** Eliminiert unsicheres "Hedging" (*oftmals*, *möglicherweise*) sowie statistische Dopplungen (*echte Fakten*, *gemeinsame Zusammenarbeit*).
*   **Komposita- & Gender-Korrektur:** Entwirrt unleserliche Bindestrich-Monster-Wörter und erzwingt ein konsistentes, fehlerfreies Gendersystem ohne stilistische Brüche.
*   **Social-Media-Optimierung:** Verhindert nervige, formelhafte KI-Einstiegsfragen (*„Kennst du das auch?“*) und stoppt die typische Emoji-Inkontinenz (symmetrische Emoji-Listen).
*   **Synonym-Cycling, Scheinanalysen & Schein-Tiefe:** Stoppt das nervöse Umbenennen derselben Sache, entfernt nachgestellte Partizip-I-Floskeln (*widerspiegelnd*, *unterstreichend*) und entlarvt Pseudo-Tiefe-Gesten (*„im Kern“*) sowie unechte „von … bis“-Spektren.

> **Zusätzlich (nur bei lockeren Texten):** Über das Modul „Persönlichkeit & Seele" spritzt der Skill auf Wunsch echte menschliche Stimme ein (Haltung, Rhythmus-Wechsel, Ich-Perspektive), statt nur Floskeln zu entfernen. Dieses Modul ist an den `--casual`-Modus gekoppelt und bleibt bei sachlichen, technischen oder formellen Texten bewusst inaktiv.

---

## 🛠️ Installation & Anwendung

Du kannst diesen Skill auf zwei Arten in Claude nutzen:

### Option A: In Claude "Projects" (Empfohlen)
1. Erstelle ein neues **Project** in Claude Pro.
2. Kopiere den gesamten Inhalt der `SKILL.md` in die **Custom Instructions** des Projects.
3. Füge optional diese `README.md` zu den Project-Dateien hinzu, damit Claude den Kontext versteht.

### Option B: Direkt im Chat (Prompt-Form)
Kopiere den Inhalt der `SKILL.md` und füge ihn vor deinem eigentlichen Text mit folgendem Befehl ein:
> *"Friere folgende Instruktionen als dein System-Framework ein: [Inhalt der SKILL.md]... Ent-ki-fiziere nun folgenden Text: [Dein Text]"*

---

## 📝 Befehle im Chat

Sobald der Skill aktiv ist, kannst du ihn mit einfachen Befehlen steuern:

*   `/entkifizieren [Dein Text]` – Transformiert den Text standardmäßig in ein natürliches, professionelles Deutsch (im passenden Du/Sie-Format des Ausgangstextes).
*   `/entkifizieren --casual [Dein Text]` – Transformiert den Text in ein lockeres, nahbares "Du" (perfekt für LinkedIn, Blogs und Social Media). Aktiviert zusätzlich das Seele-Modul, Modalpartikeln und die Perfekt-Vergangenheit.
*   `/entkifizieren --formal [Dein Text]` – Transformiert den Text in ein seriöses, elegantes "Sie" (für Business, Behörden oder formelle E-Mails).

---

## 📜 Versionshistorie (Changelog)

### v2.2.0 (Aktuelle Version) - *Das Pattern-Parity-Update*
*   **Neu (5 Muster, von 23 auf 28):** Der Katalog schließt zu den sprachunabhängigen KI-Tells auf, die bislang fehlten, einsortiert in ihre Kategorien (A/B/D):
    *   **Elegante Variation / Synonym-Cycling** (Muster 8): das krampfhafte Umbenennen derselben Entität über Synonym-Ketten (*Protagonist … Hauptfigur … Held*).
    *   **Scheinanalysen mit Partizip I** (Muster 9): nachgestellte „-end“-Phrasen, die Tiefe simulieren (das deutsche Pendant zum englischen „-ing“-Muster).
    *   **Schein-Spektren** (Muster 18): unechte „von … bis“-Reihen ohne echte Skala, mit Schutz für echte Bereiche.
    *   **Pseudo-Tiefe & Autoritäts-Floskeln** (Muster 19): „im Kern“, „die eigentliche Frage ist“ als vorgetäuschte Bedeutsamkeit (abgegrenzt vom Hedging).
    *   **Fragment-Header** (Muster 28): der generische Aufwärm-Satz direkt nach einer Überschrift.
*   **Geändert (Nummerierung):** Der Katalog ist vollständig durchnummeriert (1 bis 28); interne Querverweise wurden angepasst (Dash-Sperre jetzt Muster 22).

### v2.1.0 - *Das Grammatik- & Rechtschreib-Update*
*   **Neu (Harte Regel):** Der finale Text folgt jetzt ausdrücklich durchgehend der amtlichen deutschen Rechtschreibung und Grammatik nach Duden (Groß-/Kleinschreibung, Kommasetzung, Kasus/Kongruenz, das/dass, ss/ß, Apostrophe). Bislang ergab sich Korrektheit nur implizit aus dem Modell; sie ist nun als nicht verhandelbare Vorgabe verankert.
*   **Neu (Final-Pass-Check):** Vor der Ausgabe scannt der Skill zweifach – auf Em-/En-Dashes (wie bisher) und neu auf Grammatik-/Rechtschreibfehler, besonders an umgebauten Sätzen und aufgelösten Gedankenstrichen.
*   **Klarstellung (`--casual`):** Umgangssprachliche Verkürzungen (*hab*, *gibt's*, *geht's*) gelten als gewolltes Register und nicht als Fehler.

### v2.0.0 - *Das Blader-Format & Transparenz-Update*
*   **Umbau (Architektur):** Die linguistischen Regeln (vormals Abschnitt 3) sind in einen modularen Muster-Katalog mit 23 nummerierten Einträgen überführt. Jeder Eintrag folgt dem Schema *Worauf achten / Problem / Vorher / Nachher* (angelehnt an das englische "humanizer"-Format). Inhaltlich bleibt jede Regel vollständig erhalten.
*   **Neu (Transparente Ausgabe):** Statt nur des fertigen Textes gibt der Skill jetzt vier Teile aus: Entwurf (Draft), ein kurzes Selbst-Audit (*„Was klingt hier noch nach KI?“*), den finalen Text und eine knappe Änderungsliste.
*   **Neu (Persönlichkeit & Seele):** Konditionales Modul, das lebendige menschliche Stimme einspritzt (Haltung, Rhythmus, Ich-Perspektive). Greift nur bei Blog-, Essay- und lockeren Texten und ist an den `--casual`-Modus gekoppelt; bei sachlichen, technischen oder juristischen Texten bleibt der Ton neutral.
*   **Geändert (Strukturtreue):** Standardmäßig bleibt die Absatzstruktur des Originals erhalten (*fünf Absätze rein, fünf Absätze raus*). Der absolute Informationserhalt (Zahlen, Eigennamen, Keywords) bleibt die harte Grenze.
*   **Neu (Tooling):** Frontmatter mit `allowed-tools` (Read/Write/Edit/Grep/Glob), damit der Skill optional auch direkt über Dateien laufen kann statt nur über eingefügten Text.

### v1.5.1 - *Das Konsistenz- & Typografie-Fix*
*   **Fix (Few-Shot-Beispiele):** Die Ausgaben im Bereich der Few-Shot-Beispiele (Abschnitt 6) wurden korrigiert. Die restriktive Gedankenstrich-Sperre wird nun auch in den menschlichen Beispiel-Outputs fehlerfrei eingehalten.
*   **Fix (Nomenklatur):** Die Bezeichnungen der einzelnen Phasen innerhalb der gesamten Systemarchitektur wurden im gesamten Dokument vollständig auf eine einheitliche vierteilige Kette synchronisiert (*Kalibrierungs-, Draft-, Audit- und Final-Pass*).

### v1.5.0 - *Architektur- & Kalibrierungs-Update*
*   **Neu (Architektur):** Integration der "Voice Calibration" – Ermöglicht es dem Nutzer, eine eigene Schreibprobe einzureichen, deren Rhythmus, Wortwahl und Tonalität der Skill adaptiert.
*   **Neu (Qualitätssicherung):** Einführung des "Draft-Audit-Final"-Loops. Der Skill prüft den ersten Entwurf intern auf verbliebene KI-Muster, bevor das finale Ergebnis ausgegeben wird.
*   **Neu (Schutzmechanismen):** "Anti-False-Positive"-Leitfaden – Verhindert, dass fachlich präzise oder seriöse Texte fälschlicherweise als "KI-Floskeln" entwertet werden.
*   **Neu (Muster-Erkennung):** Erweiterung um fortgeschrittene strukturelle Indikatoren wie Scheinkorrelationen, Aphorismus-Formeln und staccatoartiges Drama.

### v1.4.1 - *Few-Shot-Erweiterung für Fachdaten*
*   **Neu:** Drittes Few-Shot-Beispiel für komplexe SEO- und Fachtexte hinzugefügt. Es trainiert Claude gezielt darin, harte Daten (Zahlen, Prozentwerte) und Fachbegriffe bei gleichzeitig korrekter deutscher Typografie (`.` zu `,`) verlustfrei zu erhalten.

### v1.4.0 - *Informationsschutz- & Typografie-Update*
*   **Neu:** Faktischer Informationserhalt – Verhindert Inhalts- und Detailverluste bei radikalen Umformulierungen (essenziell für SEO-, Fach- und Businesstexte).
*   **Neu:** Deutsche Typografie-Erzwingung – Korrigiert englische Anführungszeichen (`""` zu `„“`) und korrigiert Dezimaltrennzeichen (`.` zu `,`) im deutschen Fließtext.

### v1.3.0 - *Präzisions- & Stilistik-Update*
*   **Neu:** Weichspüler-Filter gegen "Hedging" – eliminiert unentschlossene KI-Absicherungen (*oftmals*, *möglicherweise*).
*   **Neu:** Pleonasmus- und Redundanz-Schutz nach Duden-Standard (*echte Fakten*, *zukunftsorientierte Innovationen*).
*   **Neu:** Entwirrung von Monster-Komposita und Bindestrich-Ketten für flüssigere Lesbarkeit.
*   **Neu:** Durchsetzung einer konsistenten, fehlerfreien Gender-Stilistik über den gesamten Text.

### v1.2.0 - *Linguistisches & Social-Media-Update*
*   **Neu:** Integration von deutschen Modalpartikeln (`ja`, `doch`, `mal`), um Texten eine authentische menschliche Färbung zu geben (Linguistik-Standard).
*   **Neu:** Anti-Emoji-Spam-Filter für sauberere Social-Media- und LinkedIn-Beiträge.
*   **Neu:** Verbot von formelhaften KI-Einstiegsfragen (*"Kennst du das auch?"*).
*   **Neu:** Bereinigung des bürokratischen "Corporate-Verb-Karussells" (*gewährleisten*, *vorantreiben*).

### v1.1.0 - *Copywriting & Marketing Extension*
*   **Neu:** Integration professioneller Lektorats-Standards (basierend auf Wortliga & SEO-Copywriting-Leitfäden).
*   **Neu:** Filter gegen hohle Marketing-Superlative (*bahnbrechend*, *revolutionär*).
*   **Neu:** Korrektur von typischen Übersetzungsfehlern aus dem Englischen (*"Am Ende des Tages"*, *"Sinn machen"*).
*   **Neu:** Harte Transformation von passiven Distanzformulierungen und dem unpersönlichen "man" in direkte Aktivsätze.

### v1.0.0 - *Initialer Release (Das Wikipedia-Fundament)*
*   **Neu:** Grundgerüst des Skills mit den Slash-Befehlen `/entkifizieren`, `--casual` und `--formal`.
*   **Neu:** Systematische Erkennung und Eliminierung von klassischen KI-Mustern basierend auf dem *Wikipedia-Projekt zur KI-Erkennung* (Zerschlagung von Nominalstil, Beendigung starrer Satz- und Listensymmetrien, Blacklist für Übergangswörter wie *Darüber hinaus* / *Des Weiteren*).
