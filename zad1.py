class Klasa:
    def __init__(self, imie, zywotnosc, sila, zrecznosc, punkty_taktyki):
        self.imie = imie
        self.zywotnosc = f"{zywotnosc/100:.0%}"
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.punkty_taktyki = punkty_taktyki

wojownik = Klasa("Wojownik", 100, 50, 2, 25)
lucznik = Klasa("Lucznik", 100, 4, 48, 29)