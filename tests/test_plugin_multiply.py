import pytest
from app.plugins.multiply import MultiplyCommand

def test_multiply_command():
    command = MultiplyCommand()
    result = command.execute(5, 3)
    assert result == 15.0

def test_multiply_command_with_negative_numbers():
    command = MultiplyCommand()
    result = command.execute(-10, 6)
    assert result == -60.0
