'''Save history command file'''
import pandas as pd
import logging
import os

class SaveHistory:
    def __init__(self, historyFile="history.csv"):
        self.historyFile = historyFile

    def execute(self, expression, result):
        newEntry = {"Expression": expression, "Result": result}

        if os.path.exists(self.historyFile):
            history_df = pd.read_csv(self.historyFile)
        else:
            history_df = pd.DataFrame(columns=["Expression", "Result"])
        
        history_df = history_df.append(newEntry, ignore_index=True)
        history_df.to_csv(self.historyFile, index=False)
        logging.info(f"Saved new history entry: {expression} = {result}")
        print("Calculation saved to history.")
