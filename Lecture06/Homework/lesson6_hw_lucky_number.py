def lucky_number1(n):
    i = 0
    ln = 0
    while True:
        d = n // 10**i
        ln = ln + d % 10
        i = i + 1
        if d < 10:
            break
    return ln

def lucky_number2(n):
    i = 0
    ln = 0
    while n // 10**i >= 1:
        ln = ln + n // 10**i % 10
        i = i + 1
    return ln

def lucky_number3(n):
    ln = 0
    for d in str(n):
        ln = ln + int(d)
    return ln    

bd = input('What day is your birthday? ')
while not(bd.isdigit()):
    bd = input('What day is your birthday? ')
b1 = b2 = b3 = int(bd)
while b1 > 9:
    b1 = lucky_number1(b1)
while b2 > 9:
    b2 = lucky_number1(b2)
while b3 > 9:
    b3 = lucky_number1(b3)
print ('Your lucky number is:',b1)
print ('Your lucky number is:',b2)
print ('Your lucky number is:',b3)
