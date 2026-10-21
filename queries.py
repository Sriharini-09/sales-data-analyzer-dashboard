
# Get all sales data
get_all_sales = """
SELECT * FROM sales_data
"""

# Get first 5 rows
get_sample_data = """
SELECT * FROM sales_data
LIMIT 5
"""

# Total sales
total_sales = """
SELECT SUM(Sales) AS total_sales
FROM sales_data
"""

# Sales by region
sales_by_region = """
SELECT Region, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Region
"""

# Top 5 products
top_products = """
SELECT `Product Name`, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 5
"""

# Sales by category
sales_by_category = """
SELECT Category, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Category
"""