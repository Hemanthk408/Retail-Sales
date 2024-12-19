# Importing necessary libraries
import pandas as pd

# Load the dataset (ensure the correct file path is provided)
file_path = '/mnt/data/retail_sales_dataset.csv'
data = pd.read_csv(file_path)

# Preview the first few rows of the dataset
print("Preview of the dataset:")
print(data.head())

# Display the structure and summary information about the dataset
print("\nDataset Info:")
data.info()

# Example of additional insights: Summarizing data
print("\nSummary Statistics:")
print(data.describe())

# Example of checking unique values in a column
print("\nUnique Product Categories:")
print(data['Product Category'].unique())