from app.commands.command_handler import Command
from app.calculator.operations import divide

class DivideCommand(Command):
    def execute(self, a, b):
        return divide(float(a), float(b))
