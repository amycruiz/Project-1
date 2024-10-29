from app.commands.command_handler import Command
from app.calculator.operations import multiply

class MultiplyCommand(Command):
    def execute(self, a, b):
        return multiply(float(a), float(b))
