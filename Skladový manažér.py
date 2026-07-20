import json

try:
    with open("sklad.json", "r") as subor:
        sklad = json.load(subor)
except FileNotFoundError:
    sklad = {"notebook": 999, "mobil": 1200, "slúchadlá":295}
    
while True:
    print("--MENU SKLADU ---")
    volba = input("Vyber si akciu (1 - Zobraziť sklad, 2 - Pridať tovar, 3 - Odobrať tovar, 0 - Koniec):")
    
    if volba == "1":
        print("Aktuálny stav skladu:")
        for tovar, cena in sklad.items():
            print("-", tovar.capitalize(), ":", cena, "€")

    elif volba == "2":
        novy_tovar = input("Zadaj názov nového tovaru: ").lower()
        nova_cena = int(input("Zadaj cenu pre tento tovar (€): "))
        
        sklad[novy_tovar] = nova_cena

        with open("sklad.json", "w") as subor:
            json.dump(sklad, subor)
            
        print("Tovar bol úspešne pridaný a uložený na disk")
        
    elif volba == "3":
        tovar_na_mazanie = input("Zadaj názov tovaru, ktorý chceš vymazať: ").lower()

        if tovar_na_mazanie in sklad:
            del sklad[tovar_na_mazanie]
            with open("sklad.json", "w") as subor:
                json.dump(sklad, subor)
                
            print("Tovar bol úspešne odobraný zo skladu")
        else:
            print("Tento tovar sa v sklade nenachádza!")
            
    elif volba == "0":
        print("Program sa zatvára...")
        break
        
    else:
        print("Neplatná voľba, skús to znova.")
        
