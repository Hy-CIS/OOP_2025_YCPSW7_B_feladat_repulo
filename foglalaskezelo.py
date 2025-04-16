from foglalas import JegyFoglalas

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas_hozzaadas(self, utas_nev, jarat, idopont):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat == jarat:
                print("Hiba: Ez az utas már foglalt erre a járatra.")
                return
        uj_foglalas = JegyFoglalas(utas_nev, jarat, idopont)
        self.foglalasok.append(uj_foglalas)
        print("Foglalás sikeresen rögzítve.")

    def foglalas_lemondas(self, utas_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                print("Foglalás lemondva.")
                return
        print("Hiba: Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            print("\nAktuális foglalások:")
            for f in self.foglalasok:
                print(f)

    def mentes_fajlba(self, fajlnev):
        with open(fajlnev, "w", encoding="utf-8") as f:
            for fgl in self.foglalasok:
                sor = f"{fgl.utas_nev};{fgl.jarat.jaratszam};{fgl.idopont}\n"
                f.write(sor)

    def betoltes_fajlbol(self, fajlnev, jaratok):
        try:
            with open(fajlnev, "r", encoding="utf-8") as f:
                for sor in f:
                    adatok = sor.strip().split(";")
                    if len(adatok) == 3:
                        utas_nev, jaratszam, idopont = adatok
                        jarat = next((j for j in jaratok if j.jaratszam == jaratszam), None)
                        if jarat:
                            self.foglalas_hozzaadas(utas_nev, jarat, idopont)
        except FileNotFoundError:
            pass
