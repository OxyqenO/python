import math
from contextlib import nullcontext


#1
def gmean(*args):
    a = 0
    c = 1
    for x in args:
        a += 1
        c = c * x

    y = c**(1/len(args))
    return y

print(gmean(2,2,5,7))

#2
def pyramid(*args):
    for x in args:
        for y in range(x):
            print(y+1, end="")
        print()


pyramid(1,2,3,4)

#3
def pyramid_2(*args):
    for x in args:
        for y in range(x):
            print(x, end="")
        print()

pyramid_2(1,2,3,4)


