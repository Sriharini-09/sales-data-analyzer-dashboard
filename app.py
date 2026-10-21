import streamlit as st
import pandas as pd
import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from encrypted.password_util import get_decrypted_password

# page title
st.title("Sales Data Dashboard")

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR PASSWORD",
    database="sales_project"
)


# Load data from MySQL
query = "SELECT * FROM sales_data"
df = pd.read_sql(query, conn)

# Close connection (data loaded into pandas)
conn.close()


# Fix Order Date format (day first)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)


# Show dataset
st.subheader("Sales Dataset")
st.dataframe(df)


# Total Revenue
total_revenue = df["Sales"].sum()
st.metric("Total Revenue", total_revenue)


# Top 5 Products by Sales
st.subheader("Top 5 Products by Sales")
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
st.table(top_products)


# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)


# Sales by Category
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)


# Trending Products (Month-over-Month Increase)
df["YearMonth"] = df["Order Date"].dt.to_period("M")

# Group by product and month
monthly_sales = df.groupby(["Product Name", "YearMonth"])["Sales"].sum().reset_index()

# Calculate month-over-month difference
monthly_sales["MoM_diff"] = monthly_sales.groupby("Product Name")["Sales"].diff()

# Get top trending products for latest month
latest_month = monthly_sales["YearMonth"].max()
trending_products = monthly_sales[monthly_sales["YearMonth"] == latest_month].sort_values("MoM_diff", ascending=False).head(5)

st.subheader(f"Trending Products for {latest_month}")
st.table(trending_products[["Product Name", "Sales", "MoM_diff"]])

