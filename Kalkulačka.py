import math

def spcitaj(a, b):
    return a + b

def odcitaj(a, b):
    return a - b

def nasob(a, b):
    return a * b

def vydel(a, b):
    if b == 0:
        return "Chyba: Delenie nulou nie je povolené!"
    return a / b

def mocnina(a, b):
    return a ** b

def kalkulacka():
    while True:
        print("\n" + "=" * 35)
        print("--- PYTHON KALKULAČKA ---")
        print("=" * 35)
        print("1. Sčítanie (+)")
        print("2. Odčítanie (-)")
        print("3. Násobenie (*)")
        print("4. Delenie (/)")
        print("5. Umocňovanie (^)")
        print("6. Koniec")
        print("-" * 35)

        volba = input("Vyber možnosť (1-6): ")

        if volba == "6":
            print("Kalkulačka sa zatvára. Prajem pekný deň!")
            break

        if volba in ["1", "2", "3", "4", "5"]:
            try:
                cislo1 = float(input("Zadaj 1. číslo: "))
                cislo2 = float(input("Zadaj 2. číslo: "))
            except ValueError:
                print("❌ Chyba: Musíš zadať platné číslo!")
                continue

            if volba == "1":
                vysledok = spcitaj(cislo1, cislo2)
                op = "+"
            elif volba == "2":
                vysledok = odcitaj(cislo1, cislo2)
                op = "-"
            elif volba == "3":
                vysledok = nasob(cislo1, cislo2)
                op = "*"
            elif volba == "4":
                vysledok = vydel(cislo1, cislo2)
                op = "/"
            elif volba == "5":
                vysledok = mocnina(cislo1, cislo2)
                op = "^"

            print(f"Výsledok: {cislo1} {op} {cislo2} = {vysledok}")
        else:
            print("Neplatná voľba, skús znova!")

if __name__ == "__main__":
    kalkulacka()
