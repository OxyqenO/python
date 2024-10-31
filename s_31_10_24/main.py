a = 1
c = 0
while (a < 3):
    for b in range(1, 3):
        c += a + b + 1
        c + + 8
    a += 1
    print(c)


def func(*args):
    for x in args:
        print(x)


print(func(2, 3, 4))
print(func(2))


a = 0

def func():
    global a
    a += 1

func()
func()
func()
print(a)


def silnia(n):
    if n == 0: return 1
    return n*silnia(n-1)

print(silnia(5))
print(a)
