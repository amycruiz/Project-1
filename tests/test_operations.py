from app.calculator.operations import add, subtract, multiply, divide

def addition_test():
    assert add(3,4) == 7
    assert add(-5,6) == 1

def subtraction_test():
    assert subtract(5,4) == 1
    assert subtract(4,8) == -4

def multiplication_test():
    assert multiply(3,5) == 15
    assert multiply(-2, 4) == -8

def division_test():
    assert divide(10,5) == 2
    assert divide(-15,3) == -5
