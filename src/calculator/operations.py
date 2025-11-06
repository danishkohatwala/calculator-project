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

def power(a: float, b: float) -> float:
    """Calculates the power of a number and returns the result."""
    if a < 0 and b % 1 != 0:
        raise ValueError("Cannot calculate the power of a negative number with a fractional exponent")
    return a ** b
