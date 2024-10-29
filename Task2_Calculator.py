import sys
def display_menu():

    print("\nMENU:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")
    option_no = 0

    while option_no not in [1, 2, 3, 4, 5]:
        option_no = int(input("Please enter the option number(1/2/3/4/5): "))

    if option_no == 5:
        sys.exit()

    num1 = input("Enter number1: ")
    num2 = input("Enter number2: ")

    while not (num1.isdigit() and num2.isdigit()):
        print("Invalid input, only numbers are accepted. Please try again")
        num1 = input("Enter number1: ")
        num2 = input("Enter number2: ")

    num1, num2 = int(num1), int(num2)

    if option_no == 1:
        addition(num1, num2)
    elif option_no == 2:
        subtraction(num1, num2)
    elif option_no == 3:
        multiplication(num1, num2)
    elif option_no == 4:
        division(num1, num2)


def addition(num1, num2):
    print(f"Addition of {num1} and {num2} is: {num1 + num2}")
    display_menu()


def subtraction(num1, num2):
    print(f"Subtraction of {num1} and {num2} is: {num1 - num2}")
    display_menu()


def multiplication(num1, num2):
    print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    display_menu()


def division(num1, num2):
    print(f"Division of {num1} and {num2} is: {num1 / num2}")
    display_menu()



display_menu()

