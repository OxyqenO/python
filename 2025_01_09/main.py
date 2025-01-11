import random


def zadanie_1():
    class Postac:
        def __init__(self, imie, zywotnosc, punkty_taktyki):
            self.imie = imie
            self.zywotnosc = max(0, min(100, zywotnosc))
            self.punkty_taktyki = punkty_taktyki

        def zmiana_punktow_zycia(self, zmiana):
            self.zywotnosc = max(0, min(100, self.zywotnosc + zmiana))

    class Lucznik(Postac):
        def __init__(self, imie, zywotnosc, zrecznosc, punkty_taktyki):
            super().__init__(imie, zywotnosc, punkty_taktyki)
            self.zrecznosc = zrecznosc

        def moc_ataku(self):
            return self.zrecznosc * self.punkty_taktyki * (self.zywotnosc / 100)

    class Wojownik(Postac):
        def __init__(self, imie, zywotnosc, sila, punkty_taktyki):
            super().__init__(imie, zywotnosc, punkty_taktyki)
            self.sila = sila

        def moc_ataku(self):
            return self.sila * self.punkty_taktyki * (self.zywotnosc / 100)

    # Test
    lucznik = Lucznik("Robin", 80, 15, 10)
    wojownik = Wojownik("Conan", 50, 20, 8)

    print(f"Moc ataku łucznika: {lucznik.moc_ataku()}")
    print(f"Moc ataku wojownika: {wojownik.moc_ataku()}")

    # Test zmiany punktów życia
    lucznik.zmiana_punktow_zycia(-30)
    wojownik.zmiana_punktow_zycia(20)
    print(f"Żywotność łucznika po zmianie: {lucznik.zywotnosc}")
    print(f"Żywotność wojownika po zmianie: {wojownik.zywotnosc}")


def zadanie_2():
    # (a) Generowanie liczb losowych i zapis do plików
    liczby = [random.randint(-100, 100) for _ in range(100)]

    with open("dodatnie.txt", "w") as dodatnie, open("ujemne.txt", "w") as ujemne:
        for liczba in liczby:
            if liczba >= 0:
                dodatnie.write(f"{liczba}\n")
            else:
                ujemne.write(f"{liczba}\n")

    # (b) Obliczanie średniej z poprzednich plików
    def srednia_z_pliku(nazwa_pliku):
        with open(nazwa_pliku, "r") as plik:
            liczby = [int(linia.strip()) for linia in plik]
            return sum(liczby) / len(liczby) if liczby else 0

    srednia_dodatnich = srednia_z_pliku("dodatnie.txt")
    srednia_ujemnych = srednia_z_pliku("ujemne.txt")

    print(f"Średnia dodatnich: {srednia_dodatnich}")
    print(f"Średnia ujemnych: {srednia_ujemnych}")


def zadanie_3():
    # Wczytanie pliku DNA
    plik_dna = "DNA.txt"
    with open(plik_dna, "r") as plik:
        dna = plik.read().strip()

    # (b) Zliczanie zasad azotowych
    zasady = {"A": 0, "C": 0, "G": 0, "T": 0}
    for znak in dna:
        if znak in zasady:
            zasady[znak] += 1

    print("Zliczanie zasad azotowych:", zasady)

    # (c) Usuwanie błędów typu N
    dna_czyste = dna.replace("N", "")
    print("Długość DNA po usunięciu N:", len(dna_czyste))

    # (d) Zliczanie wystąpień sekwencji GAGA
    wystapienia_gaga = dna.count("GAGA")
    print("Wystąpienia GAGA:", wystapienia_gaga)

    # (e) Znalezienie indeksu 7 guanin z rzędu
    indeks_7g = dna.find("G" * 7)
    print("Indeks 7 guanin z rzędu:", indeks_7g)

    # (f) Znalezienie 6 cytozyn z rzędu
    indeks_6c = dna.find("C" * 6)
    print("Indeks 6 cytozyn z rzędu:", indeks_6c)

    # (g) Liczba sekwencji CTGAAA
    liczba_ctgaaa = dna.count("CTGAAA")
    print("Liczba CTGAAA:", liczba_ctgaaa)

    # (h) Mutacje w CTGAAA (zmiana ostatniej litery)
    if dna.endswith("CTGAAA"):
        print("Sekwencja kończy się na CTGAAA, może być mutacja.")

    # (i) Tworzenie RNA
    rna = dna_czyste.replace("T", "U")
    with open("RNA.txt", "w") as plik:
        plik.write(rna)
    print("RNA zapisane do RNA.txt")


# Wykonanie zadań
zadanie_1()
zadanie_2()
zadanie_3()
