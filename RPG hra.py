import random
import time


class Bojovnik:
    def __init__(self, meno, zivoty=100, brnenie=5):
        self.meno = meno
        self.zivoty = zivoty
        self.max_zivoty = zivoty
        self.brnenie = brnenie

    def je_zivy(self):
        return self.zivoty > 0

    def zautoc(self, super):
        zakladny_utok = random.randint(15, 25)
        poskodenie = max(1, zakladny_utok - super.brnenie)
        
        super.zivoty -= poskodenie
        if super.zivoty < 0:
            super.zivoty = 0
            
        print(f"⚔️ {self.meno} utoci na {super.meno} a sposobuje {poskodenie} poskodenia! (Brnenie pohltilo {super.brnenie})")

    def vypis_status(self):
        print(f"❤️ {self.meno}: {self.zivoty}/{self.max_zivoty} HP")


def hraj_hru():
    print("=" * 45)
    print("      ⚔️ VITAJ V RPG ARENE (PvP) ⚔️")
    print("=" * 45)

    meno1 = input("Zadaj meno pre 1. Hraca: ") or "Hrac 1"
    meno2 = input("Zadaj meno pre 2. Hraca: ") or "Hrac 2"

    hrac1 = Bojovnik(meno1)
    hrac2 = Bojovnik(meno2)

    print("\n🔥 Suboj zicina! 🔥\n")
    hrac1.vypis_status()
    hrac2.vypis_status()
    print("-" * 45)

    kolo = 1

    while hrac1.je_zivy() and hrac2.je_zivy():
        print(f"\n--- KOLO {kolo} ---")
        
        if kolo % 2 != 0:
            utocnik = hrac1
            obranca = hrac2
        else:
            utocnik = hrac2
            obranca = hrac1

        print(f"🎯 Na tahu je: {utocnik.meno}")
        input("Stlac ENTER pre utok...")
        
        utocnik.zautoc(obranca)
        
        print("\nAktualny stav:")
        hrac1.vypis_status()
        hrac2.vypis_status()

        kolo += 1
        time.sleep(0.5)

    print("\n" + "=" * 45)
    print("🏆 KONIEC SUBOJA! 🏆")
    
    if hrac1.je_zivy():
        print(f"🎉 Vitazom sa stava {hrac1.meno}!")
    else:
        print(f"🎉 Vitazom sa stava {hrac2.meno}!")
    print("=" * 45)


if __name__ == "__main__":
    hraj_hru()
