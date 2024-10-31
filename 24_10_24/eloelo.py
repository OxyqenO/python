import mathxa = 0xb = 0
a = int(input("liczba a:"))
b = int(input("liczba b:"))
c = int(input("liczba c:"))
delta = b ** 2 - (4 * a * c)


def main(a1, b1, c1, delt, pierwszyX, drugiX):
    if a1 == 0: print("nope")
    elif (a1 ** 2) + b1 + c1 == 0: print("równanie zespolone")
    else:
        pierwszyX = (-b1 - math.sqrt(delt)) / 2 * a1
        drugiX = (-b1 + math.sqrt(delt)) / 2 * a1
print("x1 =", pierwszyX)
print("x2 =", drugiX)
main(a, b, c, delta, xa, xb)
