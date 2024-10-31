#1 - rekurencyjna

def fibo(x):
    if x == 0:
        return 1
    else:
        return x - fibo(x-1)


print(fibo(1))