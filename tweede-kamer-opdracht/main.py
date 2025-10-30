import requests
import json

url = "https://voteflow.api.nos.nl/TK25/index.json"
r = requests.get(url)
data = r.json()

partijen = data["landelijke_uitslag"]["partijen"]
geselecteerde_partijen = []

def toon_partijen():
    print("\nBeschikbare partijen:")
    for i, item in enumerate(partijen, 1):
        naam = item["partij"]["short_name"]
        zetels = item["huidig"]["zetels"]
        status = "✓" if naam in geselecteerde_partijen else " "
        print(f"{i}. [{status}] {naam}: {zetels} zetels")

def bereken_totaal_zetels():
    totaal = 0
    for item in partijen:
        if item["partij"]["short_name"] in geselecteerde_partijen:
            totaal += item["huidig"]["zetels"]
    return totaal

def toggle_partij(index):
    if 1 <= index <= len(partijen):
        naam = partijen[index-1]["partij"]["short_name"]
        if naam in geselecteerde_partijen:
            geselecteerde_partijen.remove(naam)
            print(f"{naam} gedeselecteerd")
        else:
            geselecteerde_partijen.append(naam)
            print(f"{naam} geselecteerd")
    else:
        print("Ongeldige keuze!")

def reset_selectie():
    geselecteerde_partijen.clear()
    print("Alle partijen gedeselecteerd. Zetels: 0")

while True:
    toon_partijen()
    print(f"\nTotaal zetels geselecteerd: {bereken_totaal_zetels()}")
    print("\nOpties:")
    print("- Voer een nummer in om een partij te selecteren/deselecteren")
    print("- Voer 'r' in voor reset")
    print("- Voer 'q' in om te stoppen")
    
    keuze = input("\nJouw keuze: ").strip().lower()
    
    if keuze == 'q':
        print("Programma afgesloten.")
        break
    elif keuze == 'r':
        reset_selectie()
    elif keuze.isdigit():
        toggle_partij(int(keuze))
    else:
        print("Ongeldige invoer!")
