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

def test_multiply_command_zero():
    command = MultiplyCommand()
    result = command.execute(0, 5)
    assert result == 0.0

def test_multiply_command_with_floats():
    command = MultiplyCommand()
    result = command.execute(2.5, 4.0)
    assert result == 10.0
