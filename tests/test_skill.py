import os
import re
import sys
import anthropic

# 1. API-Key laden
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ Fehler: ANTHROPIC_API_KEY fehlt!")
    sys.exit(1)

client = anthropic.Anthropic(api_key=api_key)

# 2. SKILL.md einlesen
try:
    with open("SKILL.md", "r", encoding="utf-8") as f:
        system_prompt = f.read()
except FileNotFoundError:
    print("❌ Fehler: SKILL.md wurde nicht gefunden.")
    sys.exit(1)

# 3. Alle 22 Testfälle voll integriert
test_cases = [
    {
        "name": "Hohle Marketing-Superlative",
        "input": "Unsere bahnbrechende und revolutionäre Plattform bietet Ihnen die Möglichkeit, eine nahtlose Integration zu gewährleisten.",
        "forbidden": ["bahnbrechende", "revolutionäre", "nahtlose", "gewährleisten", "Möglichkeit"]
    },
    {
        "name": "Typische Übersetzungs-Floskeln (Anglizismen)",
        "input": "Am Ende des Tages müssen wir einsehen, dass diese Strategie absolut keinen Sinn macht.",
        "forbidden": ["Am Ende des Tages", "Sinn macht", "Sinn machen"]
    },
    {
        "name": "KI-Einstiegsfloskeln & Phrasen-Brei",
        "input": "Kennst du das auch? In der heutigen schnelllebigen Welt ist Effizienz von entscheidender Bedeutung.",
        "forbidden": ["Kennst du das auch", "In der heutigen", "schnelllebigen Welt", "von entscheidender Bedeutung"]
    },
    {
        "name": "Falsche englische Typografie & Zahlenformate",
        "input": "In 2024 konnten wir das System optimieren. Die Erfolgsquote stieg signifikant um 23.5 % — ein Meilenstein.",
        "forbidden": ["In 2024", "23.5", "—"] 
    },
    {
        "name": "Nominalstil (Substantivitis)",
        "input": "Die Durchführung der Optimierung des Prozesses führt zur Erreichung einer massiven Effizienzsteigerung.",
        "forbidden": ["Durchführung der", "Erreichung einer"] 
    },
    {
        "name": "LinkedIn Emoji-Spam & Phrasen",
        "input": "🚀 Erfolg ist kein Zufall! 🔥 Hier sind 3 zukunftsweisende Tipps für dein Business: 🎯 Fokus, 📈 Skalierung und Durchhaltevermögen.",
        "forbidden": ["🚀", "🔥", "🎯", "📈", "Erfolg ist kein Zufall", "zukunftsweisende"]
    },
    {
        "name": "Schlechte Überleitungen & Fazit-Zusammenfassung",
        "input": "Darüber hinaus lässt sich sagen, dass das Tool hilft. Zusammenfassend lässt sich sagen: Die Zukunft wird großartig. Ich hoffe, das hilft!",
        "forbidden": ["Darüber hinaus lässt sich sagen", "Zusammenfassend lässt sich sagen", "Ich hoffe, das hilft"]
    },
    {
        "name": "Synonym-Cycling (Elegante Variation)",
        "input": "Der Protagonist verlässt die Stadt. Die Hauptfigur erreicht den Wald. Der besagte Held trifft einen Fremden. Die zentrale Gestalt der Erzählung kehrt schließlich heim.",
        "forbidden": ["Die zentrale Gestalt der Erzählung", "Der besagte Held"]
    },
    {
        "name": "Scheinanalysen mit Partizip I",
        "input": "Die Fassade kombiniert Blau, Grün und Gold, was die Verbundenheit der Gemeinde mit der Landschaft widerspiegelt und ihre kulturelle Tiefe unterstreicht.",
        "forbidden": ["was die Verbundenheit der Gemeinde", "kulturelle Tiefe unterstreicht"]
    },
    {
        "name": "Schein-Spektren (unechte von-bis-Reihen)",
        "input": "Unsere Reise reicht von der Idee bis zur Umsetzung, von der ersten Skizze bis zum fertigen Produkt.",
        "forbidden": ["von der Idee bis zur Umsetzung", "von der ersten Skizze bis zum"]
    },
    {
        "name": "Pseudo-Tiefe & Autoritäts-Floskeln",
        "input": "Im Kern geht es nicht um Technik. Die eigentliche Frage ist, ob das Team bereit ist. Letztlich geht es um die richtige Haltung.",
        "forbidden": ["Die eigentliche Frage ist", "Im Kern", "Letztlich geht es um"]
    },
    {
        "name": "Fragment-Header (Aufwärm-Satz nach Überschrift)",
        "input": """## Performance

Geschwindigkeit ist wichtig.

Wenn eine Seite zu langsam lädt, springen Nutzer ab und kommen nicht wieder.""",
        "forbidden": ["Geschwindigkeit ist wichtig"]
    },
    {
        "name": "Copula-Vermeidung (kein schlichtes ist/sind)",
        "input": "Die Galerie fungiert als zentrale Ausstellungsfläche und zählt mit über 300 Quadratmetern zu den größten Räumen des Vereins.",
        "forbidden": ["fungiert als", "zählt mit über"]
    },
    {
        "name": "Erzwungene Dreierfiguren (Rule of Three)",
        "input": "Unser Ansatz steht für Effizienz, Exzellenz und Empowerment. Wir liefern Lösungen, die begeistern, überzeugen und bestehen.",
        "forbidden": ["Effizienz, Exzellenz und Empowerment", "begeistern, überzeugen und bestehen"]
    },
    {
        "name": "Vage Quellen- und Autoritäts-Zuschreibung",
        "input": "Experten sind sich einig, dass dieser Ansatz die Zukunft ist. Studien zeigen, dass Nutzer ihn klar bevorzugen.",
        "forbidden": ["Experten sind sich einig", "Studien zeigen"]
    },
    {
        "name": "Storytelling-Floskeln & theatralische Haken (Muster 13)",
        "input": "Tauchen wir ein in die Welt der Datenanalyse. Ehrlich gesagt? Sie ist ziemlich wichtig.",
        "forbidden": ["Tauchen wir ein in", "Ehrlich gesagt?"]
    },
    {
        "name": "Abgenutzte Metaphern (Muster 17)",
        "input": "Klare Kommunikation ist der Schlüssel zum Erfolg und das Herzstück jedes guten Teams.",
        "forbidden": ["Schlüssel zum Erfolg", "Herzstück"]
    },
    {
        "name": "Hedging / Weichspüler (Muster 18)",
        "input": "Möglicherweise könnte man unter Umständen annehmen, dass die Maßnahme in der Regel wirkt.",
        "forbidden": ["Möglicherweise könnte man", "unter Umständen", "in der Regel"]
    },
    {
        "name": "Pleonasmus & Redundanz (Muster 19)",
        "input": "Unsere gemeinsame Zusammenarbeit schafft eine grundlegende Basis für zukunftsorientierte Innovationen.",
        "forbidden": ["gemeinsame Zusammenarbeit", "grundlegende Basis"]
    },
    {
        "name": "Englische/gerade Anführungszeichen (Muster 23)",
        "input": "Er nannte es einen \"vollen Erfolg\" und blieb fest dabei.",
        "forbidden": ["\"vollen Erfolg\""]
    },
    {
        "name": "Modalpartikeln im Casual-Modus (Muster 6)",
        "command": "/entkifizieren --casual",
        "input": "Das ist nicht einfach, aber es funktioniert trotzdem zuverlässig.",
        "required_any": ["ja", "doch", "halt", "eben", "schon", "wohl", "mal"]
    },
    {
        "name": "Präteritum→Perfekt im Casual-Modus (Muster 7)",
        "command": "/entkifizieren --casual",
        "input": "Ich ging gestern ins Büro und sah, dass niemand da war.",
        "forbidden": ["Ich ging", "und sah"],
        "required_any": ["gegangen", "gesehen"]
    }
]

failed = False
print("🚀 Starte kombinierten Struktur- und Inhaltstest für den Ent-KI-fizierer...\n")

for test in test_cases:
    print(f"Prüfe Testfall: '{test['name']}'...")
    try:
        # Optionaler Slash-Befehl (z. B. --casual) wird dem Text vorangestellt
        if test.get("command"):
            user_content = test["command"] + "\n\n" + test["input"]
        else:
            user_content = test["input"]
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1200,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}]
        )
        output = message.content[0].text
        
        # --- STRUKTUR-TEST (Loop-Überwachung) ---
        has_draft = "**Draft:**" in output or "Draft:" in output
        has_final = "**Final:**" in output or "Final:" in output
        
        if not (has_draft and has_final):
            print(f"❌ FEHLGESCHLAGEN! Claude hat den Draft-Audit-Loop ignoriert.")
            print(f"   -> Output entsprach nicht dem vorgegebenen Format.\n")
            failed = True
            continue
            
        # --- EXTRAKTION (Wir isolieren den finalen Part) ---
        if "**Final:**" in output:
            final_part = output.split("**Final:**")[1]
        else:
            final_part = output.split("Final:")[1]
            
        # Falls danach noch die Änderungsliste kommt, schneiden wir sie ab
        if "**Änderungen:**" in final_part:
            final_part = final_part.split("**Änderungen:**")[0]
        elif "Änderungen:" in final_part:
            final_part = final_part.split("Änderungen:")[0]

        # --- INHALTS-TEST (Nur auf das saubere Finale!) ---
        # a) Verbotene Muster dürfen NICHT im Finale stehen (Teilstring-Prüfung)
        found_forbidden = [word for word in test.get("forbidden", []) if word.lower() in final_part.lower()]

        # b) Bei Transform-/Hinzufüge-Mustern muss MINDESTENS eines der erwarteten
        #    Wörter auftauchen. Wortgrenzen-Prüfung (\b) verhindert Fehltreffer
        #    wie "ja" in "Januar" oder "mal" in "normal".
        required_any = test.get("required_any", [])
        required_ok = True
        if required_any:
            required_ok = any(
                re.search(r"\b" + re.escape(word) + r"\b", final_part, re.IGNORECASE)
                for word in required_any
            )

        if found_forbidden or not required_ok:
            print(f"❌ FEHLGESCHLAGEN!")
            print(f"   -> Finaler Text: {final_part.strip()}")
            if found_forbidden:
                print(f"   -> Nicht entfernt: {found_forbidden}")
            if not required_ok:
                print(f"   -> Kein erwartetes Muster gefunden (mind. eines nötig): {required_any}")
            print()
            failed = True
        else:
            print(f"✅ ERFOLGREICH! Struktur eingehalten und Finale ist sauber.\n")
            
    except Exception as e:
        print(f"❌ API-Fehler bei Test '{test['name']}': {e}\n")
        failed = True

if failed:
    print("💥 Einige Tests sind fehlgeschlagen. Bitte überprüfe deine SKILL.md!")
    sys.exit(1)
else:
    print("🎉 Perfekt! Alle 22 Tests bestanden. Struktur steht und das Finale ist KI-frei.")
    sys.exit(0)
