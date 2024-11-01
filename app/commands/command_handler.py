'''Registering and executing commands file'''
import logging
import logging.config
logging.config.fileConfig('logging.conf')

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def registerCommand(self, commandName: str, command: Command):
        '''Register a new command to the handler.'''
        self.commands[commandName] = command
        logging.info(f"Registered command: {commandName}")
    
    def executeCommand(self, commandName: str, *args):
        '''Execute a command by name, with optional arguments.'''
        try:
            logging.info(f"Executing command: {commandName} with the arguments: {args}")
            self.commands[commandName].execute(*args)
        except KeyError: 
            logging.error(f"The command '{commandName}' was not found.")
            return f"Oops! The command '{commandName}' is not recognized. Please type 'menu' to see a list of available commands."
        except Exception as e:
            logging.error(f"Error executing command '{commandName}': {e}")
            return f"An error occured while trying to execute command '{commandName}'. Please check your input and try again. Error details: {e}"
