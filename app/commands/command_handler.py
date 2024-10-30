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
            logging.info(f"Executing command: {commandName} with arguments: {args}")
            self.commands[commandName].execute(*args)
        except KeyError: 
            logging.error(f"Command '{commandName}' not found.")
            return f"Command '{commandName}' not found."
        except Exception as e:
            logging.error(f"Error executing command '{commandName}': {e}")
            return f"Error executing command '{commandName}': {e}"
