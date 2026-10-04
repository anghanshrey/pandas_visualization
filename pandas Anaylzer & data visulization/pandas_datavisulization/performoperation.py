import pandas as pd
import numpy as np

class mathematical_operations:

    def math_operations(self, data):
        print("========================== Mathematical Operations ==========================")

        print(
            f"Total Sales       : {np.sum(data['Sales'])}"
            f"\nAverage Sales     : {np.mean(data['Sales'])}"
            f"\nMaximum Sales     : {np.max(data['Sales'])}"
            f"\nMinimum Sales     : {np.min(data['Sales'])}"
        )

    def combine_dataframes(self, data1, data2):
        print("========================== Combine DataFrames ==========================")

        combined_data = pd.concat([data1, data2], ignore_index=True)
        print("Combined DataFrame:\n", combined_data)

    def split_data(self, data):

        print("========================== Split DataFrame ==========================")

        high_sales = data[data['Sales'] > 50000]
        low_sales = data[data['Sales'] <= 50000]

        print("High Sales :\n", high_sales)
        print("Low Sales :\n", low_sales)

    def search_data(self, data):

        print("========================== Search Data ==========================")

        search_term = input("Enter Product name : ")

        search_results = data[data['Product'] == search_term]

        if search_results.empty:
            print(f"No results found for '{search_term}'.")
        else:
            print(f"Search Results for '{search_term}':\n", search_results)

    def sort_data(self, data):

        print("========================== Sort Data ==========================")

        while True:
            print(
                f"1. Sort by Sales (Descending)\n"
                f"2. Sort by Sales (Ascending)\n"
                f"3. Back to DataFrame Operations Menu"
            )

            try:
                choice_sort = int(input("Enter Your Choice (1-3): "))
            except EOFError as e:
                print("Error :", e)
                return
            except ValueError as e:
                print("Error :", e)
                return

            match choice_sort:
                case 1:
                    sorted_data = data.sort_values(by='Sales', ascending=False)
                    print("Data sorted by Sales (Descending):\n", sorted_data)
                case 2:
                    sorted_data = data.sort_values(by='Sales', ascending=True)
                    print("Data sorted by Sales (Ascending):\n", sorted_data)
                case 3:
                    print("Returning to DataFrame Operations Menu...")
                    break

    def filter_data(self, data):
        print("========================== Filter Data ==========================")

        min_sales = int(input("Enter minimum sales value: "))

        print("Filtered Data:\n")

        filtered_data = data[data['Sales'] >= min_sales]

        if filtered_data.empty:
            print(f"No data found with Sales greater than or equal to {min_sales}.")
        else:
            print(filtered_data)

    def aggregate_data(self, data):
        print("========================== Aggregate Data ==========================")

        total_sales = np.sum(data['Sales'])
        average_sales = np.mean(data['Sales'])
        count_sales = len(data['Sales'])
        max_sales = np.max(data['Sales'])
        min_sales = np.min(data['Sales'])

        print(
            f"Total Sales       : {total_sales}"
            f"\nAverage Sales     : {average_sales}"
            f"\nCount of Sales     : {count_sales}"
            f"\nMaximum Sales     : {max_sales}"
            f"\nMinimum Sales     : {min_sales}"
        )
