from app.commands.command_handler import Command
from app.calculator.operations import subtract

class SubtractCommand(Command):
    def execute(self, a, b):
        return subtract(float(a), float(b))
