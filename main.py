from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from foglalaskezelo import FoglalasKezelo
from datetime import datetime

def elozetes_jaratok(legitarsasag):
    # Alap járatok
    j1 = BelfoldiJarat("HUN101", "Budapest", 12000)
    j2 = BelfoldiJarat("HUN102", "Pér", 10000)
    j3 = BelfoldiJarat("HUN103", "Debrecen", 9000)
    j4 = NemzetkoziJarat("INT201", "Madrid", 50000)
    j5 = NemzetkoziJarat("INT202", "Dallas", 65000)
    j6 = NemzetkoziJarat("INT203", "London", 45000)
    j7 = NemzetkoziJarat("INT204", "Hawaii", 90000)

    legitarsasag.jarat_hozzaadas(j1)
    legitarsasag.jarat_hozzaadas(j2)
    legitarsasag.jarat_hozzaadas(j3)
    legitarsasag.jarat_hozzaadas(j4)
    legitarsasag.jarat_hozzaadas(j5)
    legitarsasag.jarat_hozzaadas(j6)
    legitarsasag.jarat_hozzaadas(j7)

    return [j1, j2, j3, j4, j5, j6, j7]

def menurendszer():
    legitarsasag = LegiTarsasag("SchubAIR")
    foglalaskezelo = FoglalasKezelo()
    jaratok = elozetes_jaratok(legitarsasag)

    # Foglalások betöltése fájlból
    foglalaskezelo.betoltes_fajlbol("foglalasok.txt", jaratok)

    while True:
        print("\n=== Repülőjegy Foglalási Rendszer ===")
        print("1 - Jegy foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Foglalások listázása")
        print("4 - Járatok listázása")
        print("0 - Mentés & Kilépés")

        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            utas = input("Add meg az utas nevét: ")
            legitarsasag.jaratok_listazasa()
            jaratszam = input("Add meg a járatszámot: ")
            idopont = input("Add meg a foglalás dátumát (pl. ÉÉÉÉ-HH-NN): ")

            # IDŐPONT VALIDÁCIÓ
            try:
                datum = datetime.strptime(idopont, "%Y-%m-%d")
                if datum < datetime.now():
                    print("Hiba: Nem lehet múltbeli időpontra foglalni.")
                    continue
            except ValueError:
                print("Hiba: Hibás dátumformátum! Használj ilyen formátumot: ÉÉÉÉ-HH-NN")
                continue

            # Járat megkeresése
            talalt_jarat = None
            for j in jaratok:
                if j.jaratszam == jaratszam:
                    talalt_jarat = j
                    break

            if talalt_jarat:
                foglalaskezelo.foglalas_hozzaadas(utas, talalt_jarat, idopont)
            else:
                print("Hiba: Nem létezik ilyen járatszám.")

        elif valasztas == "2":
            utas = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            foglalaskezelo.foglalas_lemondas(utas, jaratszam)

        elif valasztas == "3":
            foglalaskezelo.foglalasok_listazasa()

        elif valasztas == "4":
            legitarsasag.jaratok_listazasa()

        elif valasztas == "0":
            foglalaskezelo.mentes_fajlba("foglalasok.txt")
            print("Mentés & Kilépés...")
            break

        else:
            print("Hibás választás, próbáld újra!")

if __name__ == "__main__":
    menurendszer()
