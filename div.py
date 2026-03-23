def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Example usage
num1 = 10
num2 = 2
result = divide(num1, num2)
print(f"{num1} / {num2} = {result}")