import random

historia = []

while True:
    hrac = input("Vyber si: (kameň, papier, nožnice) alebo napíš 'koniec': ").lower()
    if hrac == "koniec":
        print("Ďakujem za hru! Aplikácia sa zatvára.")
        print(f"Tvoja história hier: {historia}")
        break
    
    pocitac = random.choice(["kameň", "papier", "nožnice"])
    print(f"Počítač si vybral: {pocitac}")
    
    if hrac == pocitac:
        print("Je to remiza")
        historia.append("Remíza")
    elif (hrac == "kameň" and pocitac == "nožnice") or\
         (hrac == "papier" and pocitac == "kameň") or\
         (hrac == "nožnice" and pocitac == "papier"):
        print ("Vyhral si!")
        historia.append("Výhra")
    else:
        print("Počítač vyhráva alebo si nezadal správnu možnosť!")
        historia.append("Prehra")
