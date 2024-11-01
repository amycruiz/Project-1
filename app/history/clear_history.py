'''Clear history command file'''
import pandas as pd
import os
import logging
import logging.config
logging.config.fileConfig('logging.conf')

class ClearHistory:
    def __init__(self, historyFile="data/history_file.csv"):
        os.makedirs("data", exist_ok=True)
        self.historyFile = historyFile

    def execute(self):
        try:
            empty_df = pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"])
            empty_df.to_csv(self.historyFile, index=False)

            logging.info("History cleared sucessfully, headers retained.")
            print("History cleared successfully, only headers remain.")
        
        except Exception as e:
            logging.error(f"Error clearing history: {e}")
            print("Failed to clear history.")
