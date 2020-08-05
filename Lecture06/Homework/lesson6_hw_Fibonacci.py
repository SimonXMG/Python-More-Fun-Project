import turtle as t
t.speed(0)
def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-2)+f(n-1)
for i in range(1,31):
    print(f(i),end=',')
    t.circle(f(i)/1000,90)
