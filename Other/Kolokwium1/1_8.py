
def zadanie8():
    a = int(input("Liczba a: "))
    b = int(input("Liczba b: "))
    c = int(input("Liczba c: "))

    if a < 0 or b < 0 or c < 0:
        return zadanie8()
    else:
        if a < (b+c) and b <(a+c) and c <(b+c):
            return True
        else:
            return False

print(zadanie8())
