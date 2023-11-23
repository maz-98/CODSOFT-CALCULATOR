# First we define all the operation with the help of def:
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# observer view :
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")

    # Get user input
    choice = input("Enter operation first letter (A/S/M/D): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation based on user choice
    if choice == 'A':
        result = add(num1, num2)
        operation = '+'
        answer = "successfully Add"
    elif choice == 'S':
        result = subtract(num1, num2)
        operation = '-'
        answer = "successfully Subtract"
    elif choice == 'M':
        result = multiply(num1, num2)
        operation = '*'
        answer = "successfully Multiply"
    elif choice == 'D':
        result = divide(num1, num2)
        operation = '/'
        answer = "successfully Divide"
    else:
        print("Invalid input. Please enter a valid operation number.")
        return

    # Display the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result} {answer}")

# Run the calculator
calculator()