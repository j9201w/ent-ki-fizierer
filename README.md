# ent-ki-fizierer (Claude Skill)

Ein spezialisierter Skill für Anthropic Claude, der KI-generierte, hölzerne deutsche Texte in lebendiges, natürliches und authentisches Deutsch verwandelt. Im Gegensatz zu englischen Standard-Tools bekämpft dieser Skill gezielt die typischen Muster des "LLM-Deutschs" (Nominalstil, Phrasendrescherei, künstliche Symmetrie) basierend auf den Beobachtungen des Wikipedia-AI-Cleanups.

## 🚀 Funktionsweise

Der Skill analysiert den eingegebenen Text auf typische KI-Indikatoren und schreibt ihn komplett neu. Dabei bleibt der Kerninhalt und die Kernaussage zu 100 % erhalten, während Stil, Rhythmus und Wortwahl radikal ent-ki-fiziert werden.

### Was der Skill korrigiert:
*   **Nominalstil-Konvertierung:** Macht aus starren Substantiv-Ketten (*"Die Durchführung der Optimierung..."*) aktive Verben (*"Wir optimieren..."*).
*   **Phrasen-Blacklist:** Eliminiert LLM-Floskeln wie *„Darüber hinaus“*, *„Des Weiteren“*, *„Es ist wichtig zu beachten“* oder *„Eintauchen“*.
*   **Rhythmus-Bruch:** Zerschlägt monotone Satzlängen und führt kurze, prägnante Sätze ein, um einen natürlichen Lesefluss zu erzeugen.
*   **Symmetrie-Stopp:** Verhindert, dass Listen und Absätze mathematisch perfekt und dadurch künstlich wirken.

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
*   `/entkifizieren --casual [Dein Text]` – Transformiert den Text in ein lockeres, nahbares "Du" (perfekt für Social Media, Blogs).
*   `/entkifizieren --formal [Dein Text]` – Transformiert den Text in ein seriöses, elegantes "Sie" (für Business, Behörden oder formelle E-Mails).

---

*Entwickelt für die linguistischen Besonderheiten der deutschen Sprache.*

---

## 📜 Versionshistorie (Changelog)

### v1.0.0 - *Initialer Release (Das Wikipedia-Fundament)*
*   **Neu:** Grundgerüst des Skills mit den Slash-Befehlen `/entkifizieren`, `--casual` und `--formal`.
*   **Neu:** Systematische Erkennung und Eliminierung von klassischen KI-Mustern basierend auf dem *Wikipedia-Projekt zur KI-Erkennung* (Zerschlagung von Nominalstil, Beendigung starrer Satz- und Listensymmetrien, Blacklist für Übergangswörter wie *Darüber hinaus* / *Des Weiteren*).
