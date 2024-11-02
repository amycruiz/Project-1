'''Multiplication plugin test file'''
from app.plugins.multiply import MultiplyCommand

def test_multiply_command():
    '''Tests multiplication plugin command'''
    command = MultiplyCommand()
    result = command.execute(5, 3)
    assert result == 15.0

def test_multiply_command_with_negative_numbers():
    '''Tests multiplication plugin command with negative numbers'''
    command = MultiplyCommand()
    result = command.execute(-10, 6)
    assert result == -60.0

def test_multiply_command_zero():
    '''Tests multiplication plugin command with 0'''
    command = MultiplyCommand()
    result = command.execute(0, 5)
    assert result == 0.0

def test_multiply_command_with_floats():
    '''Tests multiplication plugin command with floats'''
    command = MultiplyCommand()
    result = command.execute(2.5, 4.0)
    assert result == 10.0
