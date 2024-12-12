#algorytm Euklidesa

x = int(input("Całkowita liczba A: "))
y = int(input("Całkowita liczba B: "))

def eukld(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(eukld(x,y))

a = 1
b = 2

p = a
q = b

while b:
    a, b = b, a%b
return a

#def dwa(a,b):
