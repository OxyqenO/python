
def zadanie6(*args):
    x = 1
    for i in args:
        x = x * (i**2)
    return x

print(zadanie6(1,2,3,4,5,6))


