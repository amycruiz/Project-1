from app.commands.command_handler import Command
from app.calculator.operations import add

class AddCommand(Command):
    def execute(self, a, b):
        return add(float(a), float(b))
