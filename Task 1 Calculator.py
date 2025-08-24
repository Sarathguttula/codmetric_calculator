def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Welcome to Codmetric Calculator!")
print("Available operations: +, -, *, /")
print("Type 'exit' anytime to quit.\n")

while True:
    try:
        num1 = input("Enter the first number (or 'exit' to quit): ")
        if num1.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break
        num1 = float(num1)

        operation = input("Enter operation (+, -, *, /): ")
        if operation.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        num2 = input("Enter the second number: ")
        if num2.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break
        num2 = float(num2)

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please use +, -, *, /.")
            continue

        print(f"Result: {num1} {operation} {num2} = {result}\n")

    except ValueError:
        print("Invalid input! Please enter numeric values only.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
