liczbaA = float(input())
liczbaB = float(input())


def absolute(x):
    if x < 0:
        x = x*-1
    return x

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

print(maximum(liczbaA,liczbaB))
