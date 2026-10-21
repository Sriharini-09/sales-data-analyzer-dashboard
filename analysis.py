import pandas as pd
import mysql.connector
import queries



conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR PASSWORD",
    database="sales_project"
)

# run query from queries.py
df = pd.read_sql(queries.get_sample_data, conn)

# display result
print("First 5 rows from sales_data table:")
print(df)

# total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# close connection
conn.close()
