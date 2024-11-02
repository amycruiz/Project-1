# Project one: Amy's Advanced Calculator Application

Welcome to my Python-based calculator that supports  basic arithmetic operations (add, subtract, multiply, divide) and advanced history management (savehistory, loadhistory, undohistory, clearhistory) functionalities using a command-line interface!

---

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Project Overview](#project-overview)
- [Usage Examples](#usage-examples)
- [Development Process](#development-process)
- [Design Patterns, Architechture, & Logging](#design-patterns-and-architechture)

---

## Setup Instructions
1. **Making the directory and setting up your Virtual Environment + git**
Assuming you have linux or ubuntu running, type in the following commands:
- mkdir (folder name)
- cd (folder name made from the above command)
From completing these commands you have created your folder and should be currently inside of it. Now you need to set up your virtual environment and iniitialize git. In order to do so you must type in the following commands:
- ```bash
  git init 
  virtualenv -p python3 my_env
  source my_env/bin/activate
These commands should have intialized git on your folder and also activated your virtual environment called 'my_env'.

2. **Clone the Repository**:
Once you've set up the basics you can now clone my repository. This can be done with the command below:
- ```bash
  git clone https://github.com/amycruiz/Project-1.git

3. **Install Dependencies**:
Once you've cloned my repository you must now ensure you have all the dependencies downloaded. You can do so by running the following command:
- ```bash
  pip install -r requirements.txt

# Project Overview
My command-line interface application is designed to be user-friendly focusing on:
1. Basic Operations: Add, Subtract, Multiply, Divide
2. History Management: Command patterns for saving, loading, clearing, and undoing history.
3. Design Patterns: Implementation using plugins and command handler classes.
4. Logging and Error Handling: Centralized logging configuration to track activities without cluttering the terminal.

# Usage Examples
To start the application (assuming you have completed the previous steps successfully) enter the command: 
- ```bash 
  python main.py

To use the basic operations of the application you can type:
- ```bash
  add 3 5 | add [num1] [num2] | to add two numbers
  subtract 8 3 | subtract [num1] [num2] | to subtract two numbers
  multiply 4 7 | multiply [num1] [num2] | to multiply two numbers
  divide 9 3 | divide [num1] [num2] to divide two numbers

In order to use the history management features you can type:
- ```bash
  savehistory [expression] [num1] [num2] [result] | to save a specific calculation to history
  loadhistory | to load any saved calculation history
  clearhistory | to clear all saved calculation history  
  undohistory | to undo your last saved calculation history entry  

To simply see a list of all the avaliable commands you can type the command:
- ```bash
  menu

To exit the application entirely you can type the command: 
- ```bash
  exit

Check out this [video recording](amys_calculator.mp4) where I walk through my application and its features!

# Development Process
**Initial Setup**
1. Created the primary structure with an app folder, organizing it for functionality with subdirectories as required by the CLI application.

**Adding Core Functionality**
2. Implemented basic operations (Add, Subtract, Multiply, Divide) with initial logging configurations for each operation.

**Command Registration and Execution**
3. Added Command and CommandHandler classes to enable registration and management of calculator commands.

**Menu and History Commands**
4. Created a history folder with files for each history command (Save, Load, Clear, Undo). Added a Menu plugin listing available commands and logging its display.

**Plugin Development and Enhanced Logging**
5. Integrated logging with each command and incorporated user input for command executions, refining the main command menu.

**History Management Features**
6. Added detailed logging configurations across files, refined the save_history.py file for correct functionality, and ensured that history commands were correctly invoked by the main command line interface.

**Test Coverage and Duplicate Check**
7. Replaced all print statements with return statements, facilitating more testable functions, and added unit tests for each history functionality.

**Error Handling and Environment Variable Integration**
8.  Updated error messages for better user experience and added an environment variable loader to integrate variables into the terminal session.

**Final Test and Coverage Assurance**
9. Made final adjustments to meet test coverage requirements (90%+), ensuring robust functionality and passing all test cases.

# Design Patterns, Architechture, & Logging
**Command Pattern**
In my application, I've used the Command Pattern to haandle command registration and execution. This approach has kept my code organized, making it easier to add new features or modify exisiting ones without any hassle.

**Logging Strategy**
Moreover, I've set up a centralized logging system that captures important application events without cluttering the terminal with messages. Instead, all logs are saved in an app.log file located in a logs folder that can only be seen by me. Each function records key activities---like user commands, errors, and menu interactions---so you can track what's happening behind the scenes. Ultimately, making it more user-friendly.

**Singleton Pattern for Configuration**
Additionally, to manage my environment variables effectively, I used the Singleton Pattern ensuring that there are consistent values throughout my application, allowing it to all run smoothly.

Thank you for using my application and reading through my process!
