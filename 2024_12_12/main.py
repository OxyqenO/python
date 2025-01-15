# Ćwiczenie 1 (Zbiory):

# Część (a): Zbiór z nazwami państw
panstwa = {"Polska", "Niemcy", "Francja", "Hiszpania", "Włochy"}

# Dodawanie istniejącego elementu do zbioru
panstwa.add("Polska")  # Nie zmieni zbioru, bo element już istnieje

# Sprawdzenie, czy "Polska" jest w zbiorze
print("Polska" in panstwa)  # Wynik: True

# Usuwanie istniejącego elementu
panstwa.discard("Hiszpania")  # Bezpieczne usunięcie, nie rzuca błędu
print(panstwa)

# Część (b): Dwa zbiory z nazwami miast
miasta_a = {"Warszawa", "Kraków", "Gdańsk", "Wrocław"}
miasta_b = {"Gdańsk", "Wrocław", "Poznań", "Łódź"}

# Miasta, które są w przynajmniej jednym ze zbiorów (suma zbiorów)
suma_miast = miasta_a | miasta_b
print("Suma zbiorów:", suma_miast)

# Miasta, które są jednocześnie w obu zbiorach (część wspólna)
wspolne_miasta = miasta_a & miasta_b
print("Część wspólna:", wspolne_miasta)

# Miasta, które są w pierwszym zbiorze, ale nie w drugim (różnica zbiorów)
roznica_miast = miasta_a - miasta_b
print("Różnica zbiorów:", roznica_miast)

# Sprawdzenie, czy zbiór x jest podzbiorem zbioru y
print("Czy miasta_a jest podzbiorem miasta_b?", miasta_a.issubset(miasta_b))

# Ćwiczenie 2 (Słowniki):

# Część (a): Tworzenie słownika i operacje
phone_numbers = {
    "Jan Kowalski": "123-456-789",
    "Anna Nowak": "987-654-321",
    "Piotr Wiśniewski": "456-789-123"
}

# Wypisanie na konsoli wszystkich danych
for name, phone in phone_numbers.items():
    print(f"{name} ma numer {phone}.")

# Część (b): Funkcje operujące na słowniku

# 1. Tłumaczenie dni tygodnia
def tlumacz_dni(lista_dni):
    translator = {
        "Monday": "Poniedziałek",
        "Tuesday": "Wtorek",
        "Wednesday": "Środa",
        "Thursday": "Czwartek",
        "Friday": "Piątek",
        "Saturday": "Sobota",
        "Sunday": "Niedziela"
    }
    return [translator[day] for day in lista_dni]

dni_angielskie = ["Monday", "Tuesday", "Friday"]
print(tlumacz_dni(dni_angielskie))

# 2. Sortowanie miesięcy według nazw
def sortuj_miesiace(miesiace):
    return dict(sorted(miesiace.items()))

miesiace = {
    "Styczeń": 1,
    "Marzec": 3,
    "Luty": 2
}
print(sortuj_miesiace(miesiace))

# 3. Konwersja liczb rzymskich na arabskie
def roman_to_int(roman):
    roman_values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

print(roman_to_int("XIV"))  # Wynik: 14

# 4. Konwersja liczb arabskich na rzymskie
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]
    return roman

print(int_to_roman(14))  # Wynik: XIV
