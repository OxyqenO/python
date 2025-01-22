liczba = int(input("Podaj liczbę: "))


#
# if liczba % 3 == 0 and liczba % 5 == 0:
#     print("Liczba jest podzielna przez 3 i 5.")
# else:
#     print("Liczba nie jest podzielna przez 3 i 5.")

# STRING
# first_name = "Marcin"
# food = "sushi"
# email = "wtf@fakeassbitch.com"
#
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is {email}")

# INTEGERES (int)
# age = 25
# quantity = 3
# num_of_students = 30
#
# print(f"Your are {age} years old")
# print(f"You've bought {quantity} apples")
# print(f"Ur class has {num_of_students} students")

# Float
# price = 10.99
# gpa = 3.2
# distance = 5.5
#
# print(f"The price is {price}$")
# print(f"Ur gpa is: {gpa}")
# print(f"U ran {distance}km")

# Boolean
# is_student = False
# for_sale = False
# is_online = False
#
# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is not available for sale")

# #Typecasting = the process of converting a variable form one data type to another
# #           str(), int(), float(), bool()
# name = "Nitt" #str()
# age = 19 #int()
# gpa = 3.0 #float()
# is_student = True #bool()

# input() = A function that prompts the user to enter data
#          returns the entered data as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# age = age + 1
#
# print(f"Hello {name}!")
# print("Happy Birthday")
# print(f"You are {age} years old")

# Ex.1 Rectangle Area Calc
# length = float(input("Enter the lenght: "))
# width = float(input("Enter the width: "))
# a = length * width
# print(f"{length} * {width} = ", a)

# Exercise 2 Shopping Cart Program

# item = input("What item would u like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would u like to buy?: "))
#
# total = price * quantity
# print(f"You have bought {quantity} {item}/s")
# print(f"Your total is: {total}")

# Augmented assignment operator
# friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2 #moduł(reszta z dzielenia)
# print(remainder)

# logical operators = evaluate multpile conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not Ture)
# temp = float(input("Podaj temperature: "))
# is_sunny = bool(input("Is it sunny? (True or False)"))
#
# if temp >= 28 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
#     print("It is Sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is Sunny")
# if temp >= 28 and not is_sunny:
#         print("It is hot outside")
#         print("It is cloudy")
# elif temp <= 0 and not is_sunny:
#         print("It is cold outside")
#         print("It is cloudy")
# elif 28 > temp > 0 and not is_sunny:
#         print("It is warm outside")
#         print("It is cloudy")

# while loop
# name = input("Podaj imie lambadziaro: ")
# while name == "":
#     print("NUH UH, NIC NIE PODAŁEŚ SCAMMERZE")
#     name = input("Podaj imie lambadziaro: ")
# else:
#     print(f"Hello {name}")
# age = int(input("Podaj swój wiek: "))
# while age < 0:
#     print("A TO NIE WIEK: ")
#     age = int(input("Podaj swój wiek: "))
#
# print(f"Jesteś tyle {age} lat stary. :) ")

# food = input("Wybierz żarcie mortadelko (kliknij q, by wyjsc)")
# while not food == "q":
#     print(f"Lubisz {food}")
#     food = input("Wybierz żarcie mortadelko (kliknij q, by wyjsc)")
# print("Bajo jajo")

# num = int(input("Wprowadź liczbę między 1 a 10:"))
#
# while num < 1 or num > 10:
#     print(f"{num} nie zawiera się w zbiorze ")
#     num = int(input("Wprowadź liczbę między 1 a 10:"))
#
# print(f"Twoja liczba {num} zawiera się w zbiorze")
# for x in reversed(range(1, 11)):
#     print(x)
# print("Szczęśliwego")


# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)


# for x in range(1, 21):
#     if x == 13:
#         break #continue = skipuje wyraz ale wymienia resztę liczb do końca
#     else:
#         print(x)

# function = a block of reuseable code
#           place a () after the function name to invoke it
# def happy_bday(name, age):
#     print(f"Happy Birthday to {name} you old hag")
#     print(f"You're {age} years old")
# happy_bday("Jon", 999999)
# happy_bday("909", 19)
# happy_bday("OwO", 20)

# def display_invoive(username, amount, due_date):
#     print(f"Hello {username}, you hoe!")
#     print(f"Your bill of {amount}$ is due: {due_date}")
#
# display_invoive("Jon", 1999, "28-11-1024")

# return = statement used to end a function
#         and send a result back to the caller
# def dodawanie(x, y):
#     z = x+ y
#     return z
# def odejmowanie(x, y):
#     z = x - y
#     return z
# def mnożenie(x, y):
#     z = x * y
#     return z
# def dzielenie(x, y):
#     z = x / y
#     return z
#
# print(mnożenie(7,9))


# *args     =allows you to pass multiple non-key arguments
# *kwargs   =allows you to pass multiple keyword arguments

# def dodawanie(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total
# print(dodawanie(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr", "Spongebob", "Harold","Squarepants", "III")

# n = 5
# s = 1
# for i in range(1,n + 1):
#     s*=i
# print(s)

# a = 1
# c = 0
# while (a < 3):
#     for b in range(1,3):
#         c += a + b + 1
#         c += 8
#         a += 1
# print(c)

# x = int(input("Podaj rozmiar trojkota: "))
#
# for i in range(x + 1):
#
#
#     print(str(i) * (i), ' ')

# x = int(input("Podaj rozmiar trojkota: "))
#
# for i in range(x + 1):
#     print("*" * (i), ' ')
# x = int(input("Podaj rozmiar trojkota: "))
#
# for i in range(1, x + 1):
#     for h in range(1, i+1):
#         print(h, end=" ")
#     print()


# def czy_liczba_pierwsza(n):
#     if n <= 1:
#         return 0  # Liczby mniejsze lub równe 1 nie są pierwsze
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return 0  # Znaleziono dzielnik, liczba nie jest pierwsza
#     return 1  # Liczba jest pierwsza
# def main():
#     try:
#         liczba = int(input("Podaj liczbę całkowitą: "))
#         if czy_liczba_pierwsza(liczba):
#             print(f"Liczba {liczba} jest liczbą pierwszą.")
#         else:
#             print(f"Liczba {liczba} nie jest liczbą pierwszą.")
#     except ValueError:
#         print("Wprowadzono niepoprawną liczbę. Spróbuj ponownie.")
# if __name__ == "__main__":
#     main()

# def liczby_catalana(*args):
#     parzyste = 0
#     nieparzyste = 0
#
#     # Przechodzenie przez liczby Catalana przekazane jako args
#     print("Liczby Catalana mniejsze od miliona:")
#     for liczba in args:
#         print(liczba, end=", ")  # Wypisz każdą liczbę
#         if liczba % 2 == 0:
#             parzyste += 1
#         else:
#             nieparzyste += 1
#     print("\n")  # Nowa linia po wypisaniu liczb
#
#     # Wypisz statystyki
#     print(f"Liczb parzystych: {parzyste}")
#     print(f"Liczb nieparzystych: {nieparzyste}")
#
#
# # Generowanie liczb Catalana i przekazanie ich jako argumenty
# catalan_numbers = []
# n = 0
# catalan = 1  # C_0 = 1
#
# while catalan < 1_000_000:
#     catalan_numbers.append(catalan)
#     n += 1
#     catalan = catalan * (2 * (2 * n - 1)) // (n + 1)
#
# # Przekazanie wygenerowanych liczb jako argumenty
# liczby_catalana(*catalan_numbers)

def temp(*args):
    if args[1] == "F":
        print((args[0] - 32) / 1.8)

    elif args[1] == "C":
        print((args[0] * 1.8) + 32)


temp(float(input("Wprowadź temperaturę: ")), input("Wprowadź jednostkę w jakiej podajesz temperaturę: "))


def gmean(*args):
    w = len(args)
    wynik = 1
    for i in range(w):
        wynik = wynik * args[i]
    wynik = wynik ** (1 / w)
    print(wynik)


gmean(3, 9, 27)

i = ''
sumcia = 0
while i != 'x':
    i = input('proszę podać literkę: ')
    sumcia += 1
print('udało Ci się zgadnąć, oto twoja ilość nietrafień', sumcia)
w = int(input(""""podaj liczbę: """))
while not 1 <= w <= 10:
    print(w * 2)
    w = int(input('podaj INNĄ liczbę: '))
print(w * 2)

w = int(input(""""podaj liczbę: """))
while 1 <= w <= 10:
    w = int(input('podaj INNĄ liczbę: '))
print(w * 2)