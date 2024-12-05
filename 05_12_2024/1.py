
#a
lista = ["elo", 2, 0, 'Cheri Cheri Lady', 2.01, 2137, "91", "dziewięćdziesiąt jeden", "Living in devotion", "lista"]

print(lista[8])

for i,j in enumerate(lista[::-1]):
    if (i % 2) == 0:
        print(j)

#b
def is_sorted(x):
    indx = 0
    for i in x:
        indx += 1
        if x[indx] > x[indx+1]:
            return False
        else:
            return True
        indx += 1
print(is_sorted([1,2,3,4,5,6,7,8,9,9]))

