import pytest
from app.calculator.operations import add, subtract, multiply, divide

def addition_test():
    assert add(3,4) == 7.0
    assert add(-5,6) == 1.0
    assert add(0, 5) == 5.0
    assert add(1.5, 2.5) == 4.0

def test_add_large_numbers():
    assert add(1e10,1e10) == 2e10

def subtraction_test():
    assert subtract(5,4) == 1.0
    assert subtract(4,8) == -4.0
    assert subtract(3,3) == 0.0
    assert subtract(-3,-2) == -1.0

def test_subtract_with_zero():
    assert subtract(5, 0) == 5.0
    assert subtract(0, 5) == -5.0

def test_subtract_large_numbers():
    assert subtract(1e10, 1e9) == 9e9

def test_subtract_negative_numbers():
    assert subtract(5, -3) == 8.0
    assert subtract(-5, 3) == -8.0

def test_subtract_large_negative_numbers():
    assert subtract(-1e10, -1e9) == -9e9

def multiplication_test():
    assert multiply(3,5) == 15.0
    assert multiply(-2, 4) == -8.0
    assert multiply(1,7) == 7.0

def test_multiply_large_numbers():
    assert multiply(1e10, 1e10) == 1e20
    assert multiply(-1e10, -1e10) == 1e20

def test_multiply_by_zero():
    assert multiply(100,0) == 0.0
    assert multiply(0,5) ==0.0

def test_multiply_negative_numbers():
    assert multiply(-2,-3) == 6

def division_test():
    assert divide(10,5) == 2.0
    assert divide(-15,3) == -5.0

def test_divide_float_result():
    assert divide(7,4) == 1.75

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5.0
    assert divide(-10, 2) == -5.0

def test_divide_small_numbers():
    assert divide(1e-10, 1e-10) == 1.0

def test_divide_precise_float():
    assert divide(0.1, 0.2) == 0.5

def test_operations():
    assert add(1, 1) == 2.0
    assert subtract (10, 5) == 5.0
    assert multiply(2, 3) == 6.0
    assert divide(6, 2) == 3.0
