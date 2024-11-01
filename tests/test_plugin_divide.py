import pytest
from app.plugins.divide import DivideCommand

def test_divide_command():
    command = DivideCommand()
    result = command.execute(10, 5)
    assert result == 2.0

def test_divide_command_with_negative_numbers():
    command = DivideCommand()
    result = command.execute(-12, 6)
    assert result == -2.0
