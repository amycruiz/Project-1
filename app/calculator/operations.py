import logging

def add(a, b):
    result = a + b
    logging.info(f"The addition of {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"The subtraction of {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"The multiplication of {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logging.info(f"The division of {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted division by zero.")
        return "Error: Division by zero is not allowed, since it is undefined."
