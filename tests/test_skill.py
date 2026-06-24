import os
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

# 3. Alle Testfälle voll integriert
test_cases = [
    {
        "name": "Hohle Marketing-Superlative",
        "input": "Unsere bahnbrechende und revolutionäre Plattform bietet Ihnen die Möglichkeit, eine nahtlose Integration zu gewährleisten.",
        "forbidden": ["bahnbrechende", "revolutionäre", "nahtlose", "gewährleisten", "die Möglichkeit,"]
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
    }
]

failed = False
print("🚀 Starte kombinierten Struktur- und Inhaltstest für den Ent-KI-fizierer...\n")

for test in test_cases:
    print(f"Prüfe Testfall: '{test['name']}'...")
    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1200,
            system=system_prompt,
            messages=[{"role": "user", "content": test["input"]}]
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
        found_forbidden = [word for word in test["forbidden"] if word.lower() in final_part.lower()]
        
        if found_forbidden:
            print(f"❌ FEHLGESCHLAGEN!")
            print(f"   -> Finaler Text: {final_part.strip()}")
            print(f"   -> Fehler: Folgende KI-Muster wurden im FINALE nicht entfernt: {found_forbidden}\n")
            failed = True
        else:
            print(f"✅ ERFOLGREICH! Struktur eingehalten und Finale ist absolut sauber.\n")
            
    except Exception as e:
        print(f"❌ API-Fehler bei Test '{test['name']}': {e}\n")
        failed = True

if failed:
    print("💥 Einige Tests sind fehlgeschlagen. Bitte überprüfe deine SKILL.md!")
    sys.exit(1)
else:
    print(f"🎉 Perfekt! Alle {len(test_cases)} Tests bestanden. Struktur steht und das Finale ist KI-frei.")
    sys.exit(0)
