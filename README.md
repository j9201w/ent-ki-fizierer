# ent-ki-fizierer (Claude Skill)

Ein spezialisierter Skill für Anthropic Claude, der KI-generierte, hölzerne deutsche Texte in lebendiges, natürliches und authentisches Deutsch verwandelt. 

Im Gegensatz zu englischen Standard-Tools bekämpft dieser Skill gezielt die spezifischen Muster des "LLM-Deutschs". Das Fundament bilden die empirischen Beobachtungen des deutschen Wikipedia-AI-Cleanups, kombiniert mit professionellen Copywriting-, SEO- und Stilistik-Standards (z. B. Wortliga, Duden-Stilkritik).

## 🚀 Funktionsweise

Der Skill analysiert den eingegebenen Text auf typische KI-Indikatoren, filtert hohle Phrasen heraus und schreibt den Text komplett neu. Dabei bleibt der Kerninhalt zu 100 % erhalten, während Stil, Rhythmus und Wortwahl radikal ent-ki-fiziert werden.

### Was der Skill korrigiert:
*   **Nominalstil-Konvertierung:** Macht aus starren Substantiv-Ketten (*"Die Durchführung der Optimierung..."*) aktive Verben (*"Wir optimieren..."*).
*   **Phrasen- & Metaphern-Blacklist:** Eliminiert LLM-Floskeln (*„Darüber hinaus“*) sowie abgenutzte KI-Sprachbilder (*„Der Schlüssel zum Erfolg“*).
*   **Hohle Superlative & Bürokratie-Verben:** Streicht inhaltsleere Buzzwords (*bahnbrechend*, *nahtlos*) und ersetzt steife Verben (*gewährleisten*, *vorantreiben*) durch echte Aktion.
*   **Rhythmus-Bruch & Modalpartikeln:** Zerschlägt monotone Satzlängen und streut organisch deutsche Modalpartikeln (*ja*, *doch*, *mal*) ein, um den Text menschlich klingen zu lassen.
*   **Fehlübersetzungen (False Friends):** Korrigiert typische, aus dem Englischen übernommene KI-Muster wie *„Am Ende des Tages“* oder *„Sinn machen“*.
*   **Weichspüler- & Redundanz-Filter:** Eliminiert unsicheres "Hedging" (*oftmals*, *möglicherweise*) sowie statistische Dopplungen (*echte Fakten*, *gemeinsame Zusammenarbeit*).
*   **Komposita- & Gender-Korrektur:** Entwirrt unleserliche Bindestrich-Monster-Wörter und erzwingt ein konsistentes, fehlerfreies Gendersystem ohne stilistische Brüche.
*   **Social-Media-Optimierung:** Verhindert nervige, formelhafte KI-Einstiegsfragen (*„Kennst du das auch?“*) und stoppt die typische Emoji-Inkontinenz (symmetrische Emoji-Listen).

---

## 🛠️ Installation & Anwendung

Du kannst diesen Skill auf zwei Arten in Claude nutzen:

### Option A: In Claude "Projects" (Empfohlen)
1. Erstelle ein neues **Project** in Claude Pro.
2. Kopiere den gesamten Inhalt der `SKILLS.md` in die **Custom Instructions** des Projects.
3. Füge optional diese `README.md` zu den Project-Dateien hinzu, damit Claude den Kontext versteht.

### Option B: Direkt im Chat (Prompt-Form)
Kopiere den Inhalt der `SKILLS.md` und füge ihn vor deinem eigentlichen Text mit folgendem Befehl ein:
> *"Friere folgende Instruktionen als dein System-Framework ein: [Inhalt der SKILLS.md]... Ent-ki-fiziere nun folgenden Text: [Dein Text]"*

---

## 📝 Befehle im Chat

Sobald der Skill aktiv ist, kannst du ihn mit einfachen Befehlen steuern:

*   `/entkifizieren [Dein Text]` – Transformiert den Text standardmäßig in ein natürliches, professionelles Deutsch (im passenden Du/Sie-Format des Ausgangstextes).
*   `/entkifizieren --casual [Dein Text]` – Transformiert den Text in ein lockeres, nahbares "Du" (perfekt für LinkedIn, Blogs und Social Media).
*   `/entkifizieren --formal [Dein Text]` – Transformiert den Text in ein seriöses, elegantes "Sie" (für Business, Behörden oder formelle E-Mails).

---

## 📜 Versionshistorie (Changelog)

### v1.3.0 (Aktuelle Version) - *Präzisions- & Stilistik-Update*
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
