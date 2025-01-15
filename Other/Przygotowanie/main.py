#silnia
#def silnia_iteracyjnie(n):
   # wynik = 1
   # for i in range(1, n + 1):
       # wynik *= i
   # return wynik

#def silnia_rekurencyjnie(n):
    #if n == 0:
    #    return 1
    #else:
    #    return n * silnia_rekurencyjnie(n-1)



def zadanie1():

    #lista
    a = ["awdinbawdubwa", 1235, True, 'awidhaioufbhawioufgbwaiuotgbawuit']

    a[2]

    #krotka
    a = (1,2,3,4,5,6,7,8,9,10)

    print(a[7])

    #::-1 to wyświetlanie odwrotne
    #::-2 wyświetla parzyste
    print(a[::-2])


def zadanie2():

    a = [2,5,6,3,0,6,2,1]
    b = [10, 9, 8, 7, 6]

    def czy_posortowana(a):
        ostatni = a[0]
        for element in a:
            if element > ostatni:
                return False
            ostatni = element
        return True


    print(czy_posortowana(a))
    print(czy_posortowana(b))


def zadanie3():
    #dodawanie wektorów
    #(a,b)
    #(c,d)
    #(a+c,b+d)

    #len -> ilość elementów w...

    def suma_wektorow(a: list, b: list):
        if len(a)!= len(b):
            print("Nie można dodać")
        else:
            for i in range(len(a)):
                a[i] += b[i]
        print(a)
        return a

    suma_wektorow([1,10,20,36,24],[2,3,4,5,6])

def zadanie4():

    def func(lista:list, do_zamiany, zamien_na):

        for element in range(len(lista)):
            if lista[element] == do_zamiany:
                lista[element] = zamien_na
        return None
    print(func([10,9,7,6],7,2))

def zadanie5():
    import math

    a = [math.e**x for x in range(10)]
    print(a)


zadanie1()
zadanie2()
zadanie3()
zadanie4()
zadanie5()