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
This code defines a function `divide` that takes two arguments, `a` and `b`, and returns the result of dividing `a` by `b`. It also includes error handling for division by zero. The example usage demonstrates how to use the function with two numbers.