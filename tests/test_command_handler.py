'''Command Handler test file'''
from app.commands.command_handler import CommandHandler, Command

class FakeCommand(Command):
    '''Creates a fake command'''
    def execute(self, *args):
        return sum(args)

class FailingCommand(Command):
    '''Creates a failing command'''
    def execute(self, *args):
        raise ValueError("Intentional failure.")

def test_register_command():
    '''Tests the registration of a fake command'''
    handler = CommandHandler()
    fake_command = FakeCommand()
    handler.registerCommand("fake", fake_command)
    assert "fake" in handler.commands

def test_execute_nonexistent_command():
    '''Tests for what happens after a nonexistent command is executed'''
    handler = CommandHandler()
    result = handler.executeCommand("nonexistent")
    assert "Oops! The command 'nonexistent' is not recognized." in result
