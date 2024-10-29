'''Load history command file'''
import pandas as pd
import os
import logging

class LoadHistory:
    def __init__(self, historyFile="history.csv"):
        self.historyFile = historyFile
    
    def execute(self):
        if os.path.exists(self.historyFile):
            history_df = pd.read_csv(self.historyFile)
            if history_df.empty:
                print("History is empty.")
            else:
                print("Calculation History:")
                print(history_df.to_string(index=False))
            logging.info("History has loaded successfully.")
        else:
            logging.warning("No history file found to load.")
            print("No history file found.")
