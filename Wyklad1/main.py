def main():
    n = int(input("Ilość liczb do wczytania: "))
    suma_odd = suma_ujem = 0
    for j in range(0,n):
        a = float(input("Podaj kolejną liczbęL "))
        if a > 0:
            suma_odd = suma_odd + a
        if a < 0:
            suma_ujem = suma_ujem + a

        print(f"Suma liczb dodatnich = {suma_odd}")


