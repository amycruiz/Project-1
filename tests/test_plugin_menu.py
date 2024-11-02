'''Menu plugin test file'''
from app.plugins.menu import MenuCommmand

def menu_command_test ():
    '''Tests menu command plugin'''
    return MenuCommmand()

def returns_expected_menu_test(menu_command):
    '''Tests if menu command execution is done as expected'''
    expected_output = (
        "Available commands:\n"
        "add [num1] [num2] - Add two numbers\n"
        "subtract [num1] [num2] - Subtract two numbers\n"
        "multiply [num1] [num2] - Multiply two numbers\n"
        "divide [num1] [num2] - Divide two numbers\n"
        "savehistory [expression] [num1] [num2] [result] - Save a specific calculation to history\n"
        "loadhistory - Load saved calculation history\n"
        "clearhistory - Clear all saved calculation history\n"
        "undohistory - Undo your last saved calculation history entry\n"
        "menu - Show a menu of all available commands\n"
        "exit - Exit the calculator"
    )
    assert menu_command.execute() == expected_output
