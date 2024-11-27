#1 - rekurencyjna
# 0 1 1 2 3 5 8 13
#def fibo(x):
#    a = 0
#    b = 1
#    if x == 0:
#        return 1
#    else:
#        a = a+b
#        b = a+b
#        return b + fibo(x -1)
       # return a + b + fibo(x-1)

def fibonacci(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))