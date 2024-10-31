#b
a = int(input("Wprowadz liczbe:"))
if a > 0:
    print("|", a,"|=", a)
else:
    print("|", a, "|=", -a, sep="")