import logging
import logging.config
logging.config.fileConfig('logging.conf')

from app.commands.command_handler import Command

class MenuCommmand(Command):
    def execute(self, *args):
        logging.info("Displaying menu to user")
        return (
                "Available commands:\n"
                "add [num1] [num2] - Add two numbers\n"
                "subtract [num1] [num2] - Subtract two numbers\n"
                "multiply [num1] [num2] - Multiply two numbers\n"
                "divide [num1] [num2] - Divide two numbers\n"
                "savehistory [expression] [result] - Save a specific calculation to history\n"
                "loadhistory - Load saved calculation history\n"
                "clearhistory - Clear all saved calculation history\n"
                "deletehistory - Delete/undo your last saved calculation history entry\n"
                "menu - Show a menu of all available commands\n"
                "exit - Exit the calculator"
                )
