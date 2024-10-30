import os
import sys
import logging
import logging.config
logging.config.fileConfig('logging.conf')

from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommmand
from app.history.clear_history import ClearHistory
from app.history.delete_history import DeleteHistory
from app.history.load_history import LoadHistory
from app.history.save_history import SaveHistory

def main():
    logging.info("Calculator application started.")
    print("Welcome to Amy's Simple Python Calculator!")
    print("Type 'menu' to see all available commands.")

    while True:
        userInput = input("Enter command: ").strip().split()
        command = userInput[0].lower()
        args = userInput[1:]

        commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
            "savehistory": SaveHistory(),
            "loadhistory": LoadHistory(),
            "clearhistory": ClearHistory(),
            "deletehistory": DeleteHistory(),
            "menu": MenuCommmand(),
        }

        if command in commands:
            try: 
                logging.info(f"Executing command: {command} with arguments: {args}")
                result = commands[command].execute(*args)
                if result is not None:
                    print(result)
                    logging.info(f"Command {command} executed successfully. Result: {result}")
            except Exception as e:
                logging.error(f"Error executing command {command} with arguments {args}: {e}")
                print(f"Error: {e}")
        elif command in {"exit"}:
            logging.info("Calculator application exited by user.")
            print("Exiting calculator... Goodbye!")
            sys.exit(0)
        else:
            logging.warning(f"Unknown command entered: {command}")
            print("Unknown command. Type 'menu' for the list of commands.")

if __name__ == "__main__":
    main()
