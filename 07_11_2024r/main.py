rows = int(input())

def silnia(a):
    if a == 0:
        return 1
    else:
        return a * silnia(a-1)


def wynik(a, b):

    return silnia(a) // (silnia((a - b)) * silnia(b))



def pascal(rows):
    for i in range(rows):
        for j in range(rows-i+1):

            # for left spacing
            print(end=" ")

        for j in range(i+1):

            # nCr = n!/((n-r)!*r!)
            print(wynik(i,j), end=" ")

        # for new line
        print()


pascal(rows)