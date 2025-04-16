class JegyFoglalas:
    def __init__(self, utas_nev, jarat, idopont):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.idopont = idopont  # Pl. "ÉÉÉÉ-HH-NN"

    def __str__(self):
        formatted_ar = f"{self.jarat.jegyar:,}".replace(",", " ")
        return f"Utas: {self.utas_nev} | {self.jarat.jarat_tipus()} - {self.jarat.jaratszam} -> {self.jarat.celallomas} ({formatted_ar} Ft) | Foglalás ideje: {self.idopont}"
