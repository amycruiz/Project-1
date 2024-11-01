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
        savedData = {"Expression": expression, 
                     "First number": num1, 
                     "Second number": num2, 
                     "Result": result}
        try:
            history_df = pd.read_csv(self.historyFile)
            
            if not any((history_df["Expression"] == expression) & (history_df["First number"] == num1) & (history_df["Second number"] == num2) & (history_df["Result"] == result)):
                history_df = pd.concat([history_df, pd.DataFrame([savedData])], ignore_index=True)
                history_df.to_csv(self.historyFile, index=False)
                logging.info(f"Calculation saved: {expression} {num1} {num2}= {result}")
                print(f"Saved history: {expression} {num1} {num2} = {result}")
            else:
                print("This calculation has already been saved.")

        except Exception as e:
            logging.error(f"Error saving history: {e}")
            print("Failed to save history.")
