zmienna = str("W roku Panskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20%ej zniżce podatków!")

def zadanie3(a):
    b = a.split()
    for i in range(len(b)):
        if b[i].isdigit():
            b[i].replace(str(i),'')
           # b -= i
    return b


print(zadanie3(zmienna))