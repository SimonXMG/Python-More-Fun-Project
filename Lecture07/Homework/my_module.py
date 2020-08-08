def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulo(x, y):
    return x % y
def divide_exactly(x, y):
    return x // y
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
def lucky_number(n):
    ln = 0
    while n >= 1:
        ln = ln + n % 10
        n = n // 10
    return ln
def prime(x):
    c = n = 1
    while c <= x:
        i = 2
        n = n+1
        while (n % i !=0) and (i <= int(n/2)):
            i = i + 1
        if i > int(n/2):
            c = c + 1
    return n
