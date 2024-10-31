#Ćwiczenie 1

#a)
i = 2
d = 0
for i in range(100):
    if (i % 2) == 0:
        d += i
    i += 1
if i == 100:
    print("a) Suma liczb parzystych od 2 do 100 wynosi :",d)

#b)
num1 = int(input("Wprowadz liczbe 1:"))
num2 = int(input("Wprowadz liczbe 2:"))
num3 = int(input("Wprowadz liczbe 3:"))
num4 = int(input("Wprowadz liczbe 4:"))
num5 = int(input("Wprowadz liczbe 5:"))
totalNumbersEven = 0

if (num1 % 2) == 0:
    totalNumbersEven += 1
if (num2 % 2) == 0:
    totalNumbersEven += 1
if (num3 % 2) == 0:
    totalNumbersEven += 1
if (num4 % 2) == 0:
    totalNumbersEven += 1
if (num5 % 2) == 0:
    totalNumbersEven += 1

print("b) Łącznie parzystych liczb jest :",totalNumbersEven)

#c)
a = 1
b = 0
for a in range(100):
    b += a**2
    a += 1
if a == 100:
    print("c) Suma kwadratów wszystkich liczb od 1 do 100 wynosi :", b)

#d)
liczba1 = 2
potega = 1
sumapoteg = 0
while potega in range (63):
    sumapoteg += liczba1 ** potega
    potega += 1
if potega == 63:
    print("d) Suma potęg liczby 2 dla wykładników od 1 do 63 wynosi :", sumapoteg)

#e)
liczbaA = int(input("Podaj liczbę A :"))
liczbaB = int(input("Podaj liczbę B :"))

sumaLiczbNieParz = 0

if liczbaA > liczbaB:
    print("e) Wynik:", sumaLiczbNieParz)
else:
    for liczbaA in range(liczbaB):
        if (liczbaA % 2) == 1:
            sumaLiczbNieParz += liczbaA
        liczbaA += 1
print("e) Wynik:", sumaLiczbNieParz)

#f)
aa = int(input("Wprowadź liczbę całkowitą dodatnią:"))
ab = 1
for ab in range(aa):
    print(ab + "" + ab+1) * ab
