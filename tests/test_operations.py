import pytest
from calculator.operations import add, subtract, multiply, divide, power

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative_number():
    assert add(2, -3) == -1


def test_add_zero():
    assert add(2, 0) == 2

def test_add_decimals():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_positive_numbers():
    assert subtract(3, 2) == 1

def test_subtract_negative_numbers():
    assert subtract(-2, -3) == 1

def test_subtract_positive_and_negative_number():
    assert subtract(2, -3) == 5

def test_subtract_zero():
    assert subtract(2, 0) == 2

def test_subtract_decimals():
    assert subtract(0.3, 0.2) == pytest.approx(0.1)

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative_number():
    assert multiply(2, -3) == -6

def test_multiply_zero():
    assert multiply(2, 0) == 0

def test_multiply_decimals():
    assert multiply(0.5, 0.5) == 0.25

def test_divide_positive_numbers():
    assert divide(6, 3) == 2

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2

def test_divide_positive_and_negative_number():
    assert divide(6, -3) == -2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)

def test_divide_decimals():
    assert divide(0.5, 0.2) == 2.5

def test_power_positive_base_positive_exponent():
    assert power(2, 3) == 8

def test_power_negative_base_even_exponent():
    assert power(-2, 4) == 16

def test_power_negative_base_odd_exponent():
    assert power(-2, 3) == -8

def test_power_zero_base():
    assert power(0, 5) == 0

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_fractional_exponent():
    assert power(4, 0.5) == 2

def test_power_negative_base_fractional_exponent():
    with pytest.raises(ValueError):
        power(-4, 0.5)
