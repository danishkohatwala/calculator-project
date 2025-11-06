def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divides two numbers and returns the result."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
