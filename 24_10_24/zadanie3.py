import math

a = int(input("Podaj liczbę całkowitą:"))
b = 0
def main(liczba, wynik):
    wynik = math.log(liczba, 10) + 1

    print(int(wynik))

main(a,b)


n = int(input("Podaj liczbę:"))
def pierwsza(liczba):
    for i in range(2,liczba):
        if liczba % i == 0:
            return 0
    return 1

print(pierwsza(n))
