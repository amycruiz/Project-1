'''Undo history command file'''
import pandas as pd
import os
import logging
import logging.config
logging.config.fileConfig('logging.conf')

class UndoHistory:
    def __init__(self, historyFile="data/history_file.csv"):
        os.makedirs("data", exist_ok=True)
        self.historyFile = historyFile

    def execute(self):
        try:
            if os.path.exists(self.historyFile):
                history_df = pd.read_csv(self.historyFile)
                if not history_df.empty:
                    history_df = history_df[:-1]
                    history_df.to_csv(self.historyFile, index=False)
                    logging.info("Last entry deleted from history.")
                    return "Last calculation undone."
                else:
                    logging.warning("No entries to delete in history.")
                    return "No entries in history to delete."
            else:
                logging.warning("No history file to delete from.")
                return "No history file found to delete from."
        
        except Exception as e:
            logging.error(f"Error deleting history: {e}")
            return "Failed to delete history."
