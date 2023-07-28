def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def display_choices():
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

print("Simple Calculator")
display_choices()

while True:
    try:
        choice = int(input("Enter your choice (1/2/3/4/5): "))
    except ValueError:
        print("Invalid choice. Please enter a valid option.")
        continue

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in (1, 2, 3, 4):
        print("Invalid choice. Please enter a valid option.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    else:
        try:
            result = divide(num1, num2)
            operation = "Division"
        except ValueError as e:
            print(e)
            continue

    print(f"\nResult of {operation}: {result}\n\n")
    display_choices()
