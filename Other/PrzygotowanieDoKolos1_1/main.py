#zadanie 1
def zadanie1():
    n = int(input())

    b = 0

    for a in range(n+1):
        a = float(a)
        b = b + a**2
        print(b)
    return b
#print(zadanie1())

#zadanie 2
def zadanie2():
    b = int(input())
    a = 1
    while b < 0:
        b = int(input())
        a *= b
    return a
#print(zadanie2())

#zadanie 3
def zadanie3():
    a = str('W Roku Panskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalil dekret o 20%ej zniżce podatkwo!')
    w = ""
    for i in str(a):
        #jeśli != liczba to and, jeśli != litera to or
        if i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '0' and i != '%' and i != ' ' and i != ',' and i != '.' and i != '!':
            w += i
    print(w[::-3])
#zadanie3()

def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + shift)
    return encrypted_text

# Example usage
text_to_encrypt = "Hello, World!"
shift_value = 3
encrypted = encrypt_text(text_to_encrypt, shift_value)
print(f"Original text: {text_to_encrypt}")
print(f"Encrypted text: {encrypted}")

def zadanie5():
    a = float(input())
    b = float(input())
    def absMaximum(a,b):
        if a < 0:
            a = -a
        else:
            a = a
        if b < 0:
            b = -b
        else:
            b = b

        if a >= b:
            return a
        if b > a:
            return b
    print(absMaximum(a,b))
#zadanie5()

#zadanie6
def zadanie6():
    def funkcjaArgs(*args):
        a = 1
        for i in args:
            a *= i**2
        print(a)
    funkcjaArgs(5,-1,7)
#zadanie6()

#zadanie 7
def zadanie7():
    def sum_of_digits(number):
        total = 0
        while number != 0:
            total += number % 10  # Dodaj ostatnią cyfrę
            number //= 10  # Usuń ostatnią cyfrę
        return total
    print(sum_of_digits(112))
#zadanie7()

#zadanie 8
def zadanie8():
    def func():
        a = float(input())
        b = float(input())
        c = float(input())

        while a < 0 or b < 0 or c < 0:
            a = float(input())
            b = float(input())
            c = float(input())
        else:
            if a > (b+c):
                return True
            elif b > (a+c):
                return True
            elif c > (a+b):
                return True
            else:
                return False
    print(func())
zadanie8()
