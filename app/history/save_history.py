import pandas as pd
import os
import logging
import logging.config
logging.config.fileConfig('logging.conf')

class SaveHistory:
    def __init__(self, historyFile="data/history_file.csv"):
        os.makedirs("data", exist_ok=True)
        self.historyFile = historyFile
        
        if not os.path.exists(self.historyFile):
            pd.DataFrame(columns=["Expression", "First number", "Second number", "Result"]).to_csv(self.historyFile, index=False)

    def execute(self, expression, num1, num2, result):
        savedData = {"Expression": expression.strip(), 
                     "First number": num1, 
                     "Second number": num2, 
                     "Result": result}
        try:
            history_df = pd.read_csv(self.historyFile)

            history_df["Expression"] = history_df["Expression"].str.strip()
            history_df["First number"] = history_df["First number"].astype(type(num1))
            history_df["Second number"] = history_df["Second number"].astype(type(num2))
            history_df["Result"] = history_df["Result"].astype(type(result))

            duplicate = history_df.loc[
                (history_df["Expression"] == savedData["Expression"]) &
                (history_df["First number"] == savedData["First number"]) &
                (history_df["Second number"] == savedData["Second number"]) &
                (history_df["Result"] == savedData["Result"])
                ]
            
            if duplicate.empty:
                history_df = pd.concat([history_df, pd.DataFrame([savedData])], ignore_index=True)
                history_df.to_csv(self.historyFile, index=False)
                logging.info(f"Calculation saved: {expression} {num1} {num2} = {result}")
                return f"Saved history: {expression} {num1} {num2} = {result}"
            else:
                logging.info(f"Calculation {expression} {num1} {num2} {result} has already been saved in history file.")
                return "This calculation has already been saved."

        except Exception as e:
            logging.error(f"Error saving history: {e}")
            return "Failed to save history."
