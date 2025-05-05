def compute(a,b,operator):

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operator")
def main():
    print("Welcome to the calculator program!")
    print("You can perform the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")

    try:
        result = compute(a, b, operator)
        print(f"The result of {a} {operator} {b} is: {result}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()