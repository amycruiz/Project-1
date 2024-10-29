'''Clear history command file'''
import pandas as pd
import os
import logging

class ClearHistory:
    def __init__(self, historyFile="history.csv"):
        self.historyFile = historyFile

    def execute(self):
        if os.path.exists(self.historyFile):
            pd.DataFrame().to_csv(self.historyFile, index=False)
            logging.info("History cleared.")
            print("History has been cleared.")
        else:
            logging.warning("No history to clear.")
            print("No history found to clear.")
