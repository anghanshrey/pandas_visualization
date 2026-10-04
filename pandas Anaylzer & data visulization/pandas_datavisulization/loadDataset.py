import pandas as pd

class load_Dataset:

    def load_Dataset(self, file_path):
        try:
            data = pd.read_csv(file_path)
            print("Dataset loaded successfully.")
            return data
        except FileNotFoundError as e:
            print("Error: File not found.", e)
        except pd.errors.EmptyDataError as e:
            print("Error: No data found in the file.", e)
        except OSError as e:
            print("Error: OS error occurred while reading the file.", e)
            return None