import pytest
import os
import pandas as pd
from app.history.clear_history import ClearHistory
from app.history.load_history import LoadHistory
from app.history.save_history import SaveHistory
from app.history.undo_history import UndoHistory

test_history_file = "data/test_history_file.csv"

@pytest.fixture
def clear_history_instance():
    instance = ClearHistory(historyFile=test_history_file)
    yield instance
    if os.path.exists(test_history_file):
        os.remove(test_history_file)

@pytest.fixture
def load_history_instance():
    instance = LoadHistory(historyFile=test_history_file)
    yield instance
    if os.path.exists(test_history_file):
        os.remove(test_history_file)

@pytest.fixture
def save_history_instance():
    instance = SaveHistory(historyFile=test_history_file)
    yield instance
    if os.path.exists(test_history_file):
        os.remove(test_history_file)

@pytest.fixture
def undo_history_instance():
    instance = UndoHistory(historyFile=test_history_file)
    yield instance
    if os.path.exists(test_history_file):
        os.remove(test_history_file)

'''Clear history file test'''

def test_clear_history_successful(clear_history_instance):
    pd.DataFrame({
        "Expression": ["add 2 2"],
        "First number": [2],
        "Second number": [2],
        "Result": [4.0]
    }).to_csv(test_history_file, index=False)

    result = clear_history_instance.execute()
    assert result == "History cleared successfully, only headers remain."

    cleared_df = pd.read_csv(test_history_file)
    assert cleared_df.empty
    assert list(cleared_df.columns) == ["Expression", "First number", "Second number", "Result"]

'''Load history file test'''

def test_load_history_with_data(load_history_instance):
    test_data = pd.DataFrame({
        "Expression": ["add", "subtract"],
        "First number": [2, 5],
        "Second number": [2, 3],
        "Result": [4.0, 2.0]
    })
    test_data.to_csv(test_history_file, index=False)

    print("Contents of the history file after saving:")
    with open(test_history_file, 'r') as f:
        print(f.read())
        
    result = load_history_instance.execute()
    expected_output = "Calculation History:\nExpression,First number,Second number,Result\nadd,2,2,4.0\nsubtract,5,3,2.0\n"
    assert result == expected_output

def test_load_history_empty_file(load_history_instance):
    empty_data = pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"])
    empty_data.to_csv(test_history_file, index=False)
    result = load_history_instance.execute()
    assert result == "History is empty."

def test_load_history_file_not_found(load_history_instance):
    if os.path.exists(test_history_file):
        os.remove(test_history_file)

    result = load_history_instance.execute()
    assert result == "No history file found to load."

'''Save history file test'''

def test_save_history_successful(save_history_instance):
    result = save_history_instance.execute("add", 2, 2, 4.0)
    assert result == "Saved history: add 2 2 = 4.0"

    saved_df = pd.read_csv(test_history_file)
    assert not saved_df.empty
    assert len(saved_df) == 1
    assert saved_df.iloc[0]["Expression"] == "add"
    assert saved_df.iloc[0]["First number"] == 2
    assert saved_df.iloc[0]["Second number"] == 2
    assert saved_df.iloc[0]["Result"] == 4.0

def test_save_duplicate_history_entry(save_history_instance):
    save_history_instance.execute("add", 2, 2, 4.0)
    result = save_history_instance.execute("add", 2, 2, 4.0)
    assert result == "This calculation has already been saved."

    saved_df = pd.read_csv(test_history_file)
    assert len(saved_df) == 1

def test_save_history_empty_file_error():
    if os.path.exists(test_history_file):
        os.remove(test_history_file)
    instance = SaveHistory(historyFile=test_history_file)
    result = instance.execute("add", 2, 2, 4.0) # add 2 2
    assert result == "Saved history: add 2 2 = 4.0"

    history_df = pd.read_csv(test_history_file)
    assert not history_df.empty
    assert len(history_df) == 1

'''Undo history file test'''

def test_undo_sucessful(undo_history_instance):
    test_data = pd.DataFrame({
        "Expression": ["add"],
        "First number": [2],
        "Second number": [2],
        "Result": [4.0]
    })
    test_data.to_csv(test_history_file, index=False)

    result = undo_history_instance.execute()
    assert result == "Last calculation undone."

    history_df = pd.read_csv(test_history_file)
    assert history_df.empty

def test_undo_empty_history(undo_history_instance):
    empty_data = pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"])
    empty_data.to_csv(test_history_file, index=False)

    result = undo_history_instance.execute()
    assert result == "No entries in history to delete."

def test_undo_history_file_not_found():
    instance = UndoHistory(historyFile="data/non_existent_history_file.csv")
    result = instance.execute()
    assert result == "No history file found to delete from."

def cleaup():
    yield
    if os.path.exists(test_history_file):
        os.remove(test_history_file)
