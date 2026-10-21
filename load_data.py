import pandas as pd


# Load the dataset from data folder
df = pd.read_csv("../data/sales_data.csv")

# Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Show number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Show column names
print("\nColumns in dataset:")
print(df.columns)

# Show dataset information
print("\nDataset info:")
print(df.info())