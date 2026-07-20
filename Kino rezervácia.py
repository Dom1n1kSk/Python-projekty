filmy = ["Spiderman", "Avatar", "Matrix"]
volne_miesta = 100
for cislo, nazov in enumerate(filmy, start=1):
    print(cislo, nazov)
    
volba = int(input("Vyber si číslo filmu (1-3): "))
if volba >= 1 and volba <= 3:
    vybrany_film = filmy[volba - 1]
    print(f"Skvelá voľba! Tvoj film je: {vybrany_film}")
    
    cena_listka = 8
    pocet_listkov = int(input("Kolko lístkov si chceš kúpiť?"))
    
    if pocet_listkov <= volne_miesta:
        cena_listka = 8
        celkova_cena_listka = pocet_listkov * cena_listka
        volne_miesta = volne_miesta - pocet_listkov
        print(f"Lístky úspešne rezervované! Zostáva voľných miest: {volne_miesta}")
        print(f"Rezervoval si si {pocet_listkov} lístkov na film {vybrany_film}.")
        print(f"Celková cena je: {celkova_cena_listka} €")

        print("--- PONUKA OBČERSTVENIA ---")
        print("1. Žiadne menu (0€)")
        print("2. Popcorn (3.50€) ")
        print("3. Výhodné menu: Popcorn + nápoj (4.50€) ")

        menu_volba = int(input("Vyber si občerstvenie (1-3): "))

        nazov_obcerstvenia = "Žiadne"
        cena_obcerstvenia = 0
        
        if menu_volba == 2:
            nazov_obcerstvenia = "Popcorn"
            cena_obcerstvenia = 3.5
        elif menu_volba == 3:
            nazov_obcerstvenia = "Výhodné menu (Popcorn + nápoj)"
            cena_obcerstvenia = 4.5
            
        konecna_suma = celkova_cena_listka + cena_obcerstvenia
        
        print("\n" + "="*40)
        print("         POTVRDENIE REZERVÁCIE        ")
        print("="*40)
        print(f" Film:         {vybrany_film}")
        print(f" Počet miest:  {pocet_listkov} lístkov")
        print(f" Občerstvenie: {nazov_obcerstvenia}")
        print("-" * 40)
        print(f" CELKOVÁ SUMA: {konecna_suma} €")
        print("="*40)
        print(" Užite si predstavenie!")
        
    else:
        print(f"Bohužiaľ, nemáme dostatok miest! K dispozícii je len {volne_miesta}")

    

else:
    print("Neplatná voľba! Zadaj číslo od 1 do 3.")
    

    
