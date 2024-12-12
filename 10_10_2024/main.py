#ćw 3
#a
age = int(input("Wprowadz swoj wiek: "))
if 18 <= age <= 100:
    print("Autoryzacja uzyskana")
else:
    print("Odmowa")

#b
a = int(input("Wprowadz liczbe:"))
if a > 0:
    print("|", a,"|=", a)
else:
    print("|", a, "|=", -a, sep="")

#c
a = 50
b = 10

if a > b:
    print("Hello World")

#d
a = int(input("Wprowadz liczbe:"))

if a % 2 == 0:
    print("Liczba", a, "jest parzysta")
else:
    print("Liczba", a, "jest nieparzysta")

#e
a = float(input("Wprowadz pierwsza liczbe:"))
b = float(input("Wprowadz druga liczbe:"))

if a == b:
    print(a, "i", b, "sa sobie rowne")

if a > 0 or b > 0:
    if (a - b) > 0:
        print(a, "Jest większe od", b)
    elif (b - a) > 0:
        print(b, "Jest większe od", a)
elif b < 0 and a < 0:
    if (-b - -a) < 0:
        print(b, "Jest większe od", a)
    elif (-a - -b) < 0:
        print(a, "Jest większe od", b)

#f
a = int(input("Wprowadz liczbe:"))

if a >= 1 and a <= 10:
    print(a, "nalezy do przedzialu [1,10]")
elif a >= 17 and a <= 21:
    print(a, "nalezy do przedzialu [17,21]")
else:
    print(a, "nie nalezy do danych dzialow")

#g
a = int(input("Wprowadz liczbe:"))

if a % 3 == 0 and a % 5 == 0:
    print(a, "jest podzielne przez 3 i 5")

elif a % 3 != 0 and a % 5 != 0:
    print(a, "NIE jest podzielne przez 3 i 5")

elif a % 3 != 0:
    print(a, "NIE jest podzielne przez 3 i jest podzielne przez 5")
else:
    print(a, "jest podzielne przez 3 i NIE podzielne przez 5")


#h
a = int(input("Calc1:"))
b = int(input("Calc2:"))
c = input("+, -, * albo :")


if c == "+":
    d = a + b
    print(a, c, b, "=", d)
elif c == "-":
    d = a - b
    print(a, c, b, "=", d)
elif c == "*":
    d = a * b
    print(a, c, b, "=", d)
elif c == "/":
    d = a / b
    print(a, c, b, "=", d)
else:
    print("Nie poprawne dzialanie matematyczne")

#i
a = int(input("Temperatura:"))
b = input("C czy F:")

if b == "C" or b =="c":
    print(a, "W Fahrenheitach wynosi:", a * 33.8, "F")
elif b == "F" or b =="f":
    print(a, "W Celsjuszach wynosi:", a / 33.8, "C")
else:
    print("Nie poprawna temperatura")

#j
a = int(input("Dlugosc boku a:"))
b = int(input("Dlugosc boku b:"))
c = int(input("Dlugosc boku c:"))

if (a**2) + (b**2) == (c**2):
    print("Liczby stanowią trojkę pitagorejska.")
elif (c**2) + (b**2) == (a**2):
    print("Liczby stanowią trojkę pitagorejska.")
elif (a**2) + (c**2) == (b**2):
    print("Liczby stanowią trojkę pitagorejska.")
else:
    print("To nie jest trojka pitagorejska.")