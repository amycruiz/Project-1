'''Delete history command file'''
import pandas as pd
import logging
import os

class DeleteHistory:
    def __init__(self, historyFile="history.csv"):
        self.historyFile = historyFile

    def execute(self, index):
        if os.path.exists(self.historyFile):
            try:
                history_df = pd.read_csv(self.historyFile)
                if index < 0 or index >= len(history_df):
                    raise IndexError("Index provided is out of range.")
                
                history_df = history_df.drop(index)
                history_df.to_csv(self.historyFile, index=False)
                logging.info(f"Deleted history entry at index {index}.")
                print(f"Deleted history entry at index {index}.")

            except IndexError:
                logging.error("Index is out of range for the delete operation.")
                print("Error: Index is out of range.")
        else:
            logging.warning("There is no history to delete from.")
            print("No history file found.")
