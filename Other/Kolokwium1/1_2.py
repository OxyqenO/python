
x = 1

def zadanie2(x):
    c = float(input("Liczba całkowita: "))
    if c < 0:
        x += x * c
        return x
    elif c > 0:
        x += x * c
        return x
    else:
        x += c
    return x

print(zadanie2(x))