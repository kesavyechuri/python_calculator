import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulus(x, y):
    return x % y
def square(x):
    return x ** 2
def square_root(x):
    return math.sqrt(x)
while True:
    print("\nSELECT OPERATOR:")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.MODULUS")
    print("6.SQUARE")
    print("7.SQUARE_ROOT")
    print("8.EXIT")
    try:
        choice = int(input("Enter your choice: "))
        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 4:
                print(num1, "/", num2, "=", divide(num1, num2))
            elif choice == 5:
                print(num1, "%", num2, "=", modulus(num1, num2))
        elif choice == 6:
            num = float(input("Enter number: "))
            print(num, "^2 =", square(num))
        elif choice == 7:
            num = float(input("Enter number: "))
            print(num, "square root =", square_root(num))
        elif choice == 8:
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number.")
