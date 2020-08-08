from my_module import *
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Modulo")
print("6 - Divide exactly")
print("7 - Factorial")
print("8 - Lucky number")
print("9 - Prime")
print("0 - Quit")

choice = ''
while choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/0): ")
while choice != '0':
    if choice in ('7', '8', '9'):
        num = int(input("Enter number: "))
        if choice == '7':
            print(f'factorial of {num} is {factorial(num)}')
        elif choice == '8':
            print(f'lucky number of {num} is {lucky_number(num)}')
        elif choice == '9':
            print(f'the No.{num} prime number is {prime(num)}')
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", modulo(num1, num2))
        elif choice == '6':
            print(num1, "//", num2, "=", divide_exactly(num1, num2))
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/0): ")
