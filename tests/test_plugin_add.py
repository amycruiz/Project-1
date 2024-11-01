import pytest
from app.plugins.add import AddCommand

def test_add_command():
    command = AddCommand()
    result = command.execute(3, 4)
    assert result == 7.0

def test_add_command_with_negative_numbers():
    command = AddCommand()
    result = command.execute(-5, 6)
    assert result == 1.0
