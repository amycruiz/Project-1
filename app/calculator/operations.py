'''Operations file'''
import logging
import logging.config
logging.config.fileConfig('logging.conf')

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
    if b == 0:
        logging.error("Attempted division by zero.")
        raise ZeroDivisionError("Division by zero is not allowed, since it is undefined.")
    result = a / b
    logging.info(f"The division of {a} / {b} = {result}")
    return result
