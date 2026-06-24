import os
import sys
import anthropic

# 1. API-Key aus den sicheren GitHub-Umgebungsvariablen laden
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ Fehler: ANTHROPIC_API_KEY fehlt!")
    sys.exit(1)

client = anthropic.Anthropic(api_key=api_key)

# 2. Deine SKILL.md einlesen
try:
    with open("SKILL.md", "r", encoding="utf-8") as f:
        system_prompt = f.read()
except FileNotFoundError:
    print("❌ Fehler: SKILL.md wurde im Hauptverzeichnis nicht gefunden.")
    sys.exit(1)

# 3. Testfälle definieren: Input -> Was darf auf KEINEN Fall im Output landen?
# Hier kannst du beliebig viele Testfälle hinzufügen!
test_cases = [
    {
        "name": "Standard KI-Marketingfloskeln",
        "input": "Unsere bahnbrechende Plattform bietet Ihnen die Möglichkeit, nahtlose Prozesse zu gewährleisten.",
        "forbidden": ["bahnbrechende", "nahtlose", "gewährleisten", "Möglichkeit"]
    },
    {
        "name": "Gedankenstriche & Fazit-Phrasen",
        "input": "Eine signifikante Zeitersparnis — oftmals der Schlüssel zum Erfolg — spielt eine große Rolle. Zusammenfassend lässt sich sagen: Die Zukunft wird großartig.",
        "forbidden": ["—", "Zusammenfassend lässt sich sagen", "spielt eine große Rolle"]
    }
]

failed = False

# 4. Testschleife starten
print("🚀 Starte automatisierte Prompt-Tests für den Ent-KI-fizierer...\n")

for test in test_cases:
    print(f"Prüfe Testfall: '{test['name']}'...")
    try:
        # Anfrage an Claude senden
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Nutzt das aktuelle Claude 3.5 Sonnet
            max_tokens=1000,
            system=system_prompt,  # Hier füttern wir deinen Skill rein
            messages=[{"role": "user", "content": test["input"]}]
        )
        output = message.content[0].text
        
        # Output auf verbotene Wörter analysieren (case-insensitive)
        found_forbidden = [word for word in test["forbidden"] if word.lower() in output.lower()]
        
        if found_forbidden:
            print(f"❌ FEHLGESCHLAGEN!")
            print(f"   -> Input:  {test['input']}")
            print(f"   -> Output: {output}")
            print(f"   -> Fehler: Folgende KI-Muster wurden NICHT entfernt: {found_forbidden}\n")
            failed = True
        else:
            print(f"✅ ERFOLGREICH! Text wurde sauber ent-ki-fiziert.\n")
            
    except Exception as e:
        print(f"❌ API-Fehler bei Test '{test['name']}': {e}\n")
        failed = True

# 5. Ergebnis an GitHub zurückmelden
if failed:
    print("💥 Einige Tests sind fehlgeschlagen. Bitte überprüfe deine SKILL.md!")
    sys.exit(1)  # Signalisiert GitHub: Der Test war ROT
else:
    print("🎉 Alle Tests erfolgreich bestanden! Dein Skill ist stabil.")
    sys.exit(0)  # Signalisiert GitHub: Der Test war GRÜN
