'''History classes test file'''
import os
import pytest
import pandas as pd
from app.history.clear_history import ClearHistory
from app.history.load_history import LoadHistory
from app.history.save_history import SaveHistory
from app.history.undo_history import UndoHistory

TEST_HISTORY_FILE = "data/TEST_HISTORY_FILE.csv"

@pytest.fixture
def clear_history_instance():
    '''Fixture for creating a ClearHistory instance and cleaning up the test file after use.'''
    instance = ClearHistory(historyFile=TEST_HISTORY_FILE)
    yield instance
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)

@pytest.fixture
def load_history_instance():
    '''Fixture for creating a LoadHistory instance and cleaning up the test file after use.'''
    instance = LoadHistory(historyFile=TEST_HISTORY_FILE)
    yield instance
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)

@pytest.fixture
def save_history_instance():
    '''Fixture for creating a SaveHistory instance and cleaning up the test file after use.'''
    instance = SaveHistory(historyFile=TEST_HISTORY_FILE)
    yield instance
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)

@pytest.fixture
def undo_history_instance():
    '''Fixture for creating a UndoHistory instance and cleaning up the test file after use.'''
    instance = UndoHistory(historyFile=TEST_HISTORY_FILE)
    yield instance
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)

# Clear history file test
def test_clear_history_successful(clear_history_instance):
    '''Tests if the clear history command is successful upon execution.'''
    pd.DataFrame({
        "Expression": ["add 2 2"],
        "First number": [2],
        "Second number": [2],
        "Result": [4.0]
    }).to_csv(TEST_HISTORY_FILE, index=False)

    result = clear_history_instance.execute()
    assert result == "History cleared successfully, only headers remain."

    cleared_df = pd.read_csv(TEST_HISTORY_FILE)
    assert cleared_df.empty
    assert list(cleared_df.columns) == ["Expression", "First number", "Second number", "Result"]

# Load history file test
def test_load_history_with_data(load_history_instance):
    '''Tests if load history command with data is successful upon execution.'''
    test_data = pd.DataFrame({
        "Expression": ["add", "subtract"],
        "First number": [2, 5],
        "Second number": [2, 3],
        "Result": [4.0, 2.0]
    })
    test_data.to_csv(TEST_HISTORY_FILE, index=False)

    result = load_history_instance.execute()
    expected_output = "Calculation History:\nExpression,First number,Second number,Result\nadd,2,2,4.0\nsubtract,5,3,2.0\n"
    assert result == expected_output

def test_load_history_empty_file(load_history_instance):
    '''Tests if the load history command is successful when the file is empty.'''
    empty_data = pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"])
    empty_data.to_csv(TEST_HISTORY_FILE, index=False)
    result = load_history_instance.execute()
    assert result == "History is empty."

def test_load_history_file_not_found(load_history_instance):
    '''Tests what happens when a file is not found'''
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)

    result = load_history_instance.execute()
    assert result == "No history file found to load."

# Save history file test
def test_save_history_successful(save_history_instance):
    '''Tests if save history command is successful upon execution.'''
    result = save_history_instance.execute("add", 2, 2, 4.0)
    assert result == "Saved history: add 2 2 = 4.0"

    saved_df = pd.read_csv(TEST_HISTORY_FILE)
    assert not saved_df.empty
    assert len(saved_df) == 1
    assert saved_df.iloc[0]["Expression"] == "add"
    assert saved_df.iloc[0]["First number"] == 2
    assert saved_df.iloc[0]["Second number"] == 2
    assert saved_df.iloc[0]["Result"] == 4.0

def test_save_duplicate_history_entry(save_history_instance):
    '''Tests if the duplication code correctly recognizes a duplicate and states that it has been saved.'''
    save_history_instance.execute("add", 2, 2, 4.0)
    result = save_history_instance.execute("add", 2, 2, 4.0)
    assert result == "This calculation has already been saved."

    saved_df = pd.read_csv(TEST_HISTORY_FILE)
    assert len(saved_df) == 1

def test_save_history_empty_file_error():
    '''Tests what happens when there is an empty file.'''
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)
    instance = SaveHistory(historyFile=TEST_HISTORY_FILE)
    result = instance.execute("add", 2, 2, 4.0)
    assert result == "Saved history: add 2 2 = 4.0"

    history_df = pd.read_csv(TEST_HISTORY_FILE)
    assert not history_df.empty
    assert len(history_df) == 1

# Undo history file test

def test_undo_sucessful(undo_history_instance):
    '''Tests if the undo history command is successful upon execution.'''
    test_data = pd.DataFrame({
        "Expression": ["add"],
        "First number": [2],
        "Second number": [2],
        "Result": [4.0]
    })
    test_data.to_csv(TEST_HISTORY_FILE, index=False)

    result = undo_history_instance.execute()
    assert result == "Last calculation undone."

    history_df = pd.read_csv(TEST_HISTORY_FILE)
    assert history_df.empty

def test_undo_empty_history(undo_history_instance):
    '''Tests what happens when there is an empty history and the undo command is executed.'''
    empty_data = pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"])
    empty_data.to_csv(TEST_HISTORY_FILE, index=False)

    result = undo_history_instance.execute()
    assert result == "No entries in history to delete."

def test_undo_history_file_not_found():
    '''Tests what happens when there is no file for the undo history command to delete from'''
    instance = UndoHistory(historyFile="data/non_existent_history_file.csv")
    result = instance.execute()
    assert result == "No history file found to delete from."

def cleaup():
    '''Ensures that the file created through these tests are deleted.'''
    yield
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)
