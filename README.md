# ent-ki-fizierer (Claude Skill)

Ein spezialisierter Skill für Anthropic Claude, der KI-generierte, hölzerne deutsche Texte in lebendiges, natürliches und authentisches Deutsch verwandelt. 

Im Gegensatz zu englischen Standard-Tools bekämpft dieser Skill gezielt die spezifischen Muster des "LLM-Deutschs". Das Fundament bilden die empirischen Beobachtungen des deutschen Wikipedia-AI-Cleanups, kombiniert mit professionellen Copywriting- und SEO-Lektorats-Standards (z. B. Wortliga).

## 🚀 Funktionsweise

Der Skill analysiert den eingegebenen Text auf typische KI-Indikatoren, filtert hohle Phrasen heraus und schreibt den Text komplett neu. Dabei bleibt der Kerninhalt zu 100 % erhalten, während Stil, Rhythmus und Wortwahl radikal ent-ki-fiziert werden.

### Was der Skill korrigiert:
*   **Nominalstil-Konvertierung:** Macht aus starren Substantiv-Ketten (*"Die Durchführung der Optimierung..."*) aktive Verben (*"Wir optimieren..."*).
*   **Phrasen- & Metaphern-Blacklist:** Eliminiert LLM-Floskeln (*„Darüber hinaus“*, *„Des Weiteren“*) sowie abgenutzte KI-Sprachbilder (*„Der Schlüssel zum Erfolg“*, *„Das Fundament legen“*).
*   **Hohle Superlative:** Streicht inhaltsleere Buzzwords wie *bahnbrechend*, *revolutionär* oder *nahtlos* und zwingt Claude zu konkreten Fakten.
*   **Rhythmus-Bruch:** Zerschlägt monotone Satzlängen und sorgt für einen dynamischen, menschlichen Lesefluss.
*   **Fehlübersetzungen (False Friends):** Korrigiert typische, aus dem Englischen übernommene KI-Muster wie *„Am Ende des Tages“* oder *„Sinn machen“*.
*   **Aktivierung:** Transformiert passive Distanzformulierungen und das unpersönliche Pronomen "man" in direkte Aktivsätze.

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
*   `/entkifizieren --casual [Dein Text]` – Transformiert den Text in ein lockeres, nahbares "Du" (perfekt für Blogs und moderne Texte).
*   `/entkifizieren --formal [Dein Text]` – Transformiert den Text in ein seriöses, elegantes "Sie" (für Business, Behörden oder formelle E-Mails).

---

## 📜 Versionshistorie (Changelog)

### v1.1.0 (Aktuelle Version) - *Copywriting & Marketing Extension*
*   **Neu:** Integration professioneller Lektorats-Standards (basierend auf Wortliga & SEO-Copywriting-Leitfänden).
*   **Neu:** Filter gegen hohle Marketing-Superlative (*bahnbrechend*, *revolutionär*).
*   **Neu:** Korrektur von typischen Übersetzungsfehlern aus dem Englischen (*"Am Ende des Tages"*, *"Sinn machen"*).
*   **Neu:** Harte Transformation von passiven Distanzformulierungen und dem unpersönlichen "man" in direkte Aktivsätze.

### v1.0.0 - *Initialer Release (Das Wikipedia-Fundament)*
*   **Neu:** Grundgerüst des Skills mit den Slash-Befehlen `/entkifizieren`, `--casual` und `--formal`.
*   **Neu:** Systematische Erkennung und Eliminierung von klassischen KI-Mustern basierend auf dem *Wikipedia-Projekt zur KI-Erkennung* (Zerschlagung von Nominalstil, Beendigung starrer Satz- und Listensymmetrien, Blacklist für Übergangswörter wie *Darüber hinaus* / *Des Weiteren*).
