import os
import sys
import logging
import logging.config
from dotenv import load_dotenv

log_directory = 'logs'
log_file = os.path.join(log_directory, 'app.log')
os.makedirs(log_directory, exist_ok=True)
if not os.path.exists(log_file):
    open(log_file, 'w').close()

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommmand
from app.history.clear_history import ClearHistory
from app.history.undo_history import UndoHistory
from app.history.load_history import LoadHistory
from app.history.save_history import SaveHistory

def load_environment():
    load_dotenv()

    db_user = os.getenv('DATABASE_USERNAME')
    env = os.getenv('ENVIRONMENT')
    secret_key = os.getenv('MY_SECRET_KEY')

    print(f"User: {db_user} | Environment: {env} | Secret key: {'*' * len(secret_key)}")
    logging.info("Environment variables loaded successfully. Database user and environment displayed.")
    logging.info("Secret key is also displayed but hidden using * for security.")


def main():
    logging.info("Calculator application started.")
    print("Welcome to Amy's Advanced Python Calculator ^.^!")
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
            "undohistory": UndoHistory(),
            "menu": MenuCommmand(),
        }

        if command in commands:
            try: 
                logging.info(f"Executing command: {command} with arguments: {args}")
                result = commands[command].execute(*args)
                if result is not None:
                    print(result)
                    logging.info(f"Command {command} executed successfully. Result: {result}")
            except TypeError as e:
                logging.error(f"Error executing {command} with arguments {args}: Missing or invalid arguments. Details: {e}")
                print(f"Error: Missing or invalid arguments for the command '{command}'. Type 'menu' to ensure proper arguments are provided.")
            except Exception as e:
                logging.error(f"Error executing command {command} with the arguments {args}: {e}")
                print(f"Error: {e}")
        elif command in {"exit"}:
            logging.info("Calculator application exited by user.")
            print("Exiting calculator... Goodbye!")
            sys.exit(0)
        else:
            logging.warning(f"Unknown command entered: {command}")
            print("Unknown command. Type 'menu' for the list of commands.")

if __name__ == "__main__":
    load_environment()
    main()
