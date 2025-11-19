# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def percentage(value, percent):
    """Calculate percentage of a value"""
    return (value * percent) / 100

if __name__ == "__main__":
    print("Calculator loaded!")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 squared = {square(5)}")

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a**b

def square(a):
    """Return the square of a number"""
    return a ** 2