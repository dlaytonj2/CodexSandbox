def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation: ").strip()
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if op not in operations:
        print("Invalid operation.")
        return

    try:
        result = operations[op](a, b)
        print(f"Result: {result}")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
