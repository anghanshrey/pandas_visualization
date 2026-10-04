import pandas as pd

class handle_missing_value:

    def display_missing(self, data):
        print("Missing Values:")
        if data.isnull().sum().sum() == 0:
            print("No missing values found in the dataset.")
        else:
            print(data.isnull().sum())

    def fill_mean(self, data):

        if data.isnull().sum().sum() == 0:
            print("No missing values found in the dataset.")
            return
        for column in data.select_dtypes(include="number"):
            data[column] = data[column].fillna(data[column].mean())

        print("Missing numeric values filled with mean.")

    def drop_missing(self, data):
        if data.isnull().sum().sum() == 0:
            print("No missing values found in the dataset.")
            return
        data.dropna(inplace=True)
        print("Rows with missing values dropped.")

    def fill_missing(self, data):
        if data.isnull().sum().sum() == 0:
            print("No missing values found in the dataset.")
            return
        for column in data.columns:
            if data[column].isnull().any():

                if data[column].dtype == "object":
                    data[column] = data[column].fillna(data[column].mode()[0])
                else:
                    data[column] = data[column].fillna(data[column].mean())

        print("Missing values filled successfully.")