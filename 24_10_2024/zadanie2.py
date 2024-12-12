import tempfile
def dziel(a,b):
    if b != 0:
        print(a/b)
    else:
        print("Nie dziel #### przez 0!")
dziel(5.0,2)

dziel(3,0)

#konwerter temperatur

numtemp = float(input("Podaj temperaturę: "))
temp = input("F czy C:")
finaltemp = 0
def temperatura(num,stopn,fintemp):
    if stopn == "f" or stopn == "F":
        finaltemp = (num - 32) * (5/9)
        print("Temperatura ", num, "F w Celsjuszach wynosi", finaltemp)
    elif stopn == "c" or stopn == "C":
        finaltemp = (num * (9/5)) + 32
        print("Temperatura ",num,"C w Fahrenheit wynosi", finaltemp)
    else:
        print("Nie potrafię tego przekonwetować ;-;")

temperatura(numtemp,temp,finaltemp)