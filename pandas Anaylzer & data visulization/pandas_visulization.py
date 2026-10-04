from pandas_datavisulization import load_Dataset
from pandas_datavisulization import Exploredata
from pandas_datavisulization import mathematical_operations
from pandas_datavisulization import handle_missing_value
from pandas_datavisulization import Data_Visualization
import matplotlib.pyplot as plt
import numpy as np

class Visualization:

    def __init__(self):
        self.load_dataset = load_Dataset()
        self.explore_data = Exploredata()
        self.per_option = mathematical_operations()
        self.missing_Value = handle_missing_value()
        self.visu_data = Data_Visualization()
        self.data = None

    def Load_datset(self):
        print("========================== Load Dataset ==========================")

        data = input("Enter the path of the dataset (CSV File): ")

        self.data = self.load_dataset.load_Dataset(data)


    def Explore_data(self):
        print("========================== Explore Data ==========================")
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        if len(self.data) < 0:
            print("Dataset is empty. Please load a valid dataset.")
            return
            
        while True:
            print(
                f"1. Display the first 5 Rows\n"
                f"2. Display the last 5 Rows\n"
                f"3. Display column names\n"
                f"4. Display data types\n"
                f"5. Display basic information\n"
                f"6. Display datset shape\n"
                f"7. Display statistical summary\n"
                f"8. Back to Main Menu"
            )

            try:
                choice = int(input("Enter YOur Choice (1-8): "))
            except EOFError as e:
                print("Error :",e)
                return
            except ValueError as e:
                print("Error :",e)
                return

            match choice:
                case 1:
                    self.explore_data.display_first_rows(self.data)
                case 2:
                    self.explore_data.display_last_rows(self.data)
                case 3:
                    self.explore_data.display_column_names(self.data)
                case 4:
                    self.explore_data.display_data_types(self.data)
                case 5:
                    self.explore_data.display_basic_info(self.data)
                case 6:
                    self.explore_data.display_shape(self.data)
                case 7:
                    self.explore_data.display_statistical_summary(self.data)
                case 8:
                    print("Returning to Main Menu...")
                    break

    def DataFrame_operations(self):
        print("========================== DataFrame Operations ==========================")
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        if len(self.data) < 0:
            print("Dataset is empty. Please load a valid dataset.")
            return
        while True:
            print(
                f"1. Mathematical Operations\n"
                f"2. Combine DataFrames\n"
                f"3. Split DataFrame\n"
                f"4. Search Data\n"
                f"5. Sort Data\n"
                f"6. Filter Data\n"
                f"7. Aggregate Data\n"
                f"8. Back to Main Menu"
            )

            try:
                choice_math = int(input("Enter YOur Choice (1-8): "))
            except EOFError as e:
                print("Error :",e)
                return
            except ValueError as e:
                print("Error :",e)
                return

            match choice_math:
                case 1:
                    self.per_option.math_operations(self.data)
                case 2:
                    file_path = input("Enter second CSV file path: ")

                    data2 = self.load_dataset.load_Dataset(file_path)

                    if data2 is not None:
                        self.per_option.combine_dataframes(self.data, data2)
                case 3:
                    self.per_option.split_data(self.data)
                case 4:
                    self.per_option.search_data(self.data)
                case 5:
                    self.per_option.sort_data(self.data)
                case 6:
                    self.per_option.filter_data(self.data)
                case 7:
                    self.per_option.aggregate_data(self.data)
                case 8:
                    print("Returning to Main Menu...")
                    break

    def Handle_missing_data(self):
        print("========================== Handle Missing Data ==========================")
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return
        if len(self.data) < 0:
            print("Dataset is empty. Please load a valid dataset.")
            return
        while True:
            print(
                f"1. Display rows with missing values\n"
                f"2. Fill missing values with mean\n"
                f"3. Drop rows with missing values\n"
                f"4. Replace missing values with a specific value\n"
                f"5. Back to Main Menu"
            )

            try:
                choice_missing = int(input("Enter YOur Choice (1-5): "))
            except EOFError as e:
                print("Error :",e)
                return
            except ValueError as e:
                print("Error :",e)
                return

            match choice_missing:
                case 1:
                    self.missing_Value.display_missing(self.data)
                case 2:
                    self.missing_Value.fill_mean(self.data)
                case 3:
                    self.missing_Value.drop_missing(self.data)
                case 4:
                    self.missing_Value.fill_missing(self.data)
                case 5:
                    print("Returning to Main Menu...")
                    break

    def Generate_descriptive_statistics(self):
        print("========================== Generate Descriptive Statistics ==========================")

        print("Sales Statistics:\n")

        print("Total Sales:", self.data['Sales'].sum())
        print("Mean Sales:", self.data['Sales'].mean())
        print("Median Sales:", self.data['Sales'].median())
        print("Standard Deviation of Sales:", round(self.data['Sales'].std(),2))
        print("Variance of Sales:", round(self.data['Sales'].var(),2))
        print("Minimum Sales:", self.data['Sales'].min())
        print("Maximum Sales:", self.data['Sales'].max())

        print("Percentiles:\n")
        print("25th Percentile of Sales:", self.data['Sales'].quantile(0.25))
        print("50th Percentile of Sales:", self.data['Sales'].quantile(0.50))
        print("75th Percentile of Sales:", self.data['Sales'].quantile(0.75))

        print("NumPy Statistics:\n")

        print("Sales Array:\n")

        sales_array = np.array(self.data['Sales'])

        print(sales_array)

        print("Sum :", np.sum(sales_array))
        print("Mean :", round(np.mean(sales_array),2))
        print("Median :", round(np.median(sales_array),2))
        print("Standard Deviation :", round(np.std(sales_array),2))
        print("Variance :", round(np.var(sales_array),2))
        print("Minimum :", np.min(sales_array))
        print("Maximum :", np.max(sales_array))

    def Data_visualization(self):
        print("========================== Data Visualization ==========================")
        while True:
            print(
                f"1. Bar Plot\n"
                f"2. Line Plot\n"
                f"3. Scatter Plot\n"
                f"4. Pie Chart\n"
                f"5. Histogram\n"
                f"6. Stack Plot\n"
                f"7. Seaborn Box Plot\n"
                f"8. Seaborn Heatmap\n"
                f"9. Back to Main Menu"
            )

            try:
                choice_visual = int(input("Enter YOur Choice (1-9): "))
            except EOFError as e:
                print("Error :",e)
                return
            except ValueError as e:
                print("Error :",e)
                return

            match choice_visual:
                case 1:
                    self.visu_data.bar_plot(self.data)
                case 2:
                    self.visu_data.line_plot(self.data)
                case 3:
                    self.visu_data.scatter_plot(self.data)
                case 4:
                    self.visu_data.pie_chart(self.data)
                case 5:
                    self.visu_data.histogram(self.data)
                case 6:
                    self.visu_data.stack_plot(self.data)
                case 7:
                    self.visu_data.box_plot(self.data)
                case 8:
                    self.visu_data.heatmap(self.data)
                case 9:
                    print("Returning to Main Menu...")
                    break

    def Save_visualization(self):

        print("========================== Save Visualization ==========================")

        filename = input("Enter file name: ")

        if not filename.endswith(".png"):
            filename = filename + ".png"
            
        plt.savefig(filename)

        print(f"Visualization saved as {filename} successfully!")

    def run(self):
        print("========================================================")
        print("      Sales Data Analysis & Visualization Program ")
        print("========================================================")

        while True:
            print("\nPlease select an option:")
            print(
                f"1. Load Dataset\n"
                f"2. Explore Data\n"
                f"3. Perform DataFrame Operations\n"
                f"4. Handle Missing Data\n"
                f"5. Generate Descriptive Statistics\n"
                f"6. Data Visualization\n"
                f"7. Save Visualization\n"
                f"8. Exit"
            )

            try:
                choice = int(input("Enter Your Choice (1-8): "))
            except EOFError as e:
                print("Error :",e)
                return
            except ValueError as e:
                print("Error :",e)
                return

            match choice:
                case 1:
                    self.Load_datset()
                case 2:
                    self.Explore_data()
                case 3:
                    self.DataFrame_operations()
                case 4:
                    self.Handle_missing_data()
                case 5:
                    self.Generate_descriptive_statistics()
                case 6:
                    self.Data_visualization()
                case 7:
                    self.Save_visualization()
                case 8:
                    print("========================================================")
                    print("Exiting the program. Goodbye!")
                    print("========================================================")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    visualization = Visualization()
    visualization.run()