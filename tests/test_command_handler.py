import pytest
from app.commands.command_handler import CommandHandler, Command

class FakeCommand(Command):
    def execute(self, *args):
        return sum(args)

class FailingCommand(Command):
    def execute(self, *args):
        raise ValueError("Intentional failure.")

def test_register_command():
    handler = CommandHandler()
    fake_command = FakeCommand()
    handler.registerCommand("fake", fake_command)
    assert "fake" in handler.commands

def test_execute_nonexistent_command():
    handler = CommandHandler()
    result = handler.executeCommand("nonexistent")
    assert "Oops! The command 'nonexistent' is not recognized." in result
