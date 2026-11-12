def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not possible"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

op = input("Enter your choice: ")

if op == "+":
    print("Result:", addition(a, b))
elif op == "-":
    print("Result:", subtraction(a, b))
elif op == "*":
    print("Result:", multiplication(a, b))
elif op == "/":
    print("Result:", division(a, b))
else:
    print("Invalid operation")