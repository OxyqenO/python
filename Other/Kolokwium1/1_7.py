a = input("Liczba: ")

def suma(a):
    x = int(0)
    for i in range(len(a)):
        x += a[i-1]
    return x


print(suma(a))