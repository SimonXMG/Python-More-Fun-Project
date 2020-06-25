calc_on = 1

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function modulos two numbers
def modulo(x, y):
    return x % y

def count_to_ten():
    for number in range(1, 11):
	    print(number)  

def quit():
    global calc_on
    calc_on = 0          

print("Select operation.")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Modulo")
print("6 - Count to Ten")
print("q - Quit")

while calc_on == 1:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/q): ")

    if choice == 'q':
        quit()

    if choice == '6':
        count_to_ten()

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
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
        
    if choice not in ('1', '2', '3', '4', '5', '6', 'q'):
        print("Invalid Input")