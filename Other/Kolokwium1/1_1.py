n = int(input("Liczba naturalna: "))

def zadanie1(n):
    a = 0
    for i in range(n+1):
        a += i**2
    return a

print(zadanie1(n))