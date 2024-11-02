'''Add plugin test file'''
from app.plugins.add import AddCommand

def test_add_command():
    '''Tests the add plugin command'''
    command = AddCommand()
    result = command.execute(3, 4)
    assert result == 7.0

def test_add_command_with_negative_numbers():
    '''Tests the add plugin command with negative numbers'''
    command = AddCommand()
    result = command.execute(-5, 6)
    assert result == 1.0
