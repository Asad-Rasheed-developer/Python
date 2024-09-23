# Define the functions for the calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def get_user_choice():
    print("\nSelect an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power (Exponentiation)")
    print("6: Modulus")
    print("0: Exit")
    return input("Enter your choice: ")

def get_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def main():
    while True:
        choice = get_user_choice()

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            a, b = get_numbers()

            if choice == '1':
                print(f"The result of addition is: {add(a, b)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(a, b)}")
            elif choice == '3':
                print(f"The result of multiplication is: {multiply(a, b)}")
            elif choice == '4':
                print(f"The result of division is: {divide(a, b)}")
            elif choice == '5':
                print(f"The result of power is: {power(a, b)}")
            elif choice == '6':
                print(f"The result of modulus is: {modulus(a, b)}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
