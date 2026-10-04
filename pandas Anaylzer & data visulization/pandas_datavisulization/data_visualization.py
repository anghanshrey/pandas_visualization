import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Data_Visualization:

    def bar_plot(self, data):

        X_axis = input("Enter the column name for X-axis: ")
        Y_axis = input("Enter the column name for Y-axis: ")

        if X_axis not in data.columns or Y_axis not in data.columns:
            print("Error: One or both column names are not present in the dataset.")
            return
        else:
            plt.bar(data[X_axis], data[Y_axis])
            plt.xlabel(X_axis)
            plt.ylabel(Y_axis)
            plt.title(f'Bar Plot of {Y_axis} vs {X_axis}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def line_plot(self, data):
        X_axis = input("Enter the column name for X-axis: ")
        Y_axis = input("Enter the column name for Y-axis: ")

        if X_axis not in data.columns or Y_axis not in data.columns:
            print("Error: One or both column names are not present in the dataset.")
            return
        else:
            plt.plot(data[X_axis], data[Y_axis])
            plt.xlabel(X_axis)
            plt.ylabel(Y_axis)
            plt.title(f'Line Plot of {Y_axis} vs {X_axis}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def scatter_plot(self, data):
        X_axis = input("Enter the column name for X-axis: ")
        Y_axis = input("Enter the column name for Y-axis: ")

        if X_axis not in data.columns or Y_axis not in data.columns:
            print("Error: One or both column names are not present in the dataset.")
            return
        else:
            plt.scatter(data[X_axis], data[Y_axis])
            plt.xlabel(X_axis)
            plt.ylabel(Y_axis)
            plt.title(f'Scatter Plot of {Y_axis} vs {X_axis}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def pie_chart(self, data):
        column = input("Enter the column name for Pie Chart: ")

        if column not in data.columns:
            print("Error: Column name is not present in the dataset.")
            return
        else:
            plt.pie(
                data[column].value_counts(),
                labels=data[column].value_counts().index,
                autopct='%1.1f%%',
                startangle=90
            )
            plt.title(f'Pie Chart of {column}')
            plt.ylabel('')
            plt.tight_layout()
            plt.show()

    def histogram(self, data):
        column = input("Enter the column name for Histogram: ")

        if column not in data.columns:
            print("Error: Column name is not present in the dataset.")
            return
        else:
            plt.hist(data[column], bins=10, edgecolor='black')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column}')
            plt.tight_layout()
            plt.show()

    def stack_plot(self, data):
        X_axis = input("Enter the column name for X-axis: ")
        Y_axis1 = input("Enter the first column name for Y-axis: ")
        Y_axis2 = input("Enter the second column name for Y-axis: ")

        if X_axis not in data.columns or Y_axis1 not in data.columns or Y_axis2 not in data.columns:
            print("Error: One or more column names are not present in the dataset.")
            return
        else:
            plt.stackplot(data[X_axis], data[Y_axis1], data[Y_axis2], labels=[Y_axis1, Y_axis2])
            plt.xlabel(X_axis)
            plt.ylabel('Values')
            plt.title(f'Stack Plot of {Y_axis1} and {Y_axis2} vs {X_axis}')
            plt.legend(loc='upper left')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def box_plot(self, data):
        column = input("Enter the column name for Box Plot: ")

        if column not in data.columns:
            print("Error: Column name is not present in the dataset.")
            return
        else:
            sns.boxplot(x=data[column],hue=data[column])
            plt.title(f'Box Plot of {column}')
            plt.tight_layout()
            plt.show()

    def heatmap(self, data):
        plt.figure(figsize=(10, 8))

        numeric_columns = data.select_dtypes(include=[np.number]).columns
        sns.heatmap(data[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Heatmap of Correlation Matrix')
        plt.tight_layout()
        plt.show()