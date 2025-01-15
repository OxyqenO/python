
# 1. Tworzenie klasy
# Aby stworzyć klasę, używamy słowa kluczowego 'class':

class MojaKlasa:
    pass

# 2. Konstruktor __init__
# Konstruktor to specjalna metoda, która jest wywoływana, gdy tworzysz nowy obiekt danej klasy. Inicjalizuje atrybuty obiektu.

class MojaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa  # Atrybut obiektu

# 3. Tworzenie obiektów
# Aby stworzyć obiekt, wywołujemy klasę jak funkcję:

obiekt = MojaKlasa("Przykład")

# 4. Metody instancji
# Metody instancji są funkcjami zdefiniowanymi w klasie, które operują na obiektach (instancjach) tej klasy.
# Pierwszym argumentem każdej metody instancji jest 'self', który odnosi się do konkretnego obiektu.

class MojaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    
    def wyswietl_nazwe(self):
        print(f"Nazwa: {self.nazwa}")

obiekt = MojaKlasa("Przykład")
obiekt.wyswietl_nazwe()  # Wypisze "Nazwa: Przykład"

# 5. Atrybuty obiektu
# Atrybuty obiektu są zmiennymi, które przechowują dane specyficzne dla danego obiektu:

class MojaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa  # Atrybut obiektu

# 6. Atrybuty klasy
# Atrybuty klasy są wspólne dla wszystkich obiektów tej samej klasy:

class MojaKlasa:
    atrybut_klasy = 42  # Atrybut klasy
    
    def __init__(self, nazwa):
        self.nazwa = nazwa

# 7. Dziedziczenie i funkcja super()
# Funkcja 'super()' służy do wywoływania metod klasy bazowej. Jest to przydatne, gdy chcemy rozszerzyć metodę klasy bazowej w klasie pochodnej.

class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek
    
    def daj_glos(self):
        print("Zwierzę wydaje dźwięk.")

class Pies(Zwierze):
    def __init__(self, gatunek, imie):
        super().__init__(gatunek)  # Wywołanie konstruktora klasy bazowej
        self.imie = imie

    def daj_glos(self):
        super().daj_glos()  # Wywołanie metody klasy bazowej
        print(f"{self.imie} szczeka!")

pies = Pies("Pies", "Reksio")
pies.daj_glos()  # Wypisze "Zwierzę wydaje dźwięk." i "Reksio szczeka!"
