a,b,fib=0,1,[]
fib.append(a)
fib.append(b)
def f(n):
    if n==2:
        return
    global a,b
    a,b=b,a+b
    fib.append(b)
    f(n-1)
f(500)
print(fib)
