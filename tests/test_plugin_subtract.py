'''Subtraction plugin test file'''
from app.plugins.subtract import SubtractCommand

def test_subtract_command():
    '''Tests subtraction plugin command'''
    command = SubtractCommand()
    result = command.execute(15, 10)
    assert result == 5.0

def test_subtract_command_with_negative_numbers():
    '''Tests subtraction plugin command with negative numbers'''
    command = SubtractCommand()
    result = command.execute(-25, 5)
    assert result == -30.0
