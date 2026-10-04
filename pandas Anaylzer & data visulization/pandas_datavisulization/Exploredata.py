import pandas as pd

class Exploredata:
    def display_first_rows(self, data):
        print("First 5 Rows:")
        print(data.head())

    def display_last_rows(self, data):
        print("Last 5 Rows:")
        print(data.tail())

    def display_column_names(self, data):
        print("Column Names:")
        print(data.columns)

    def display_data_types(self, data):

        print("Data Types:")
        print(data.dtypes)

    def display_basic_info(self, data):
        print("Basic Information:")
        print(data.info())

    def display_shape(self, data):
        print("Dataset Shape:")
        print(data.shape)

    def display_statistical_summary(self, data):
        print("Statistical Summary:")
        print(data.describe())
