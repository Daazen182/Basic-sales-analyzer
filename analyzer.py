import pandas as pd 
#Load Csv
df = pd.read_csv('mysales.csv')
#Calculate total per row
df['Total'] = df['Quantity'] * df['Price']
#Total sales per product
sales_per_product = df.groupby('Product')['Total'].sum()
print("Total Sales Per Product:\n",sales_per_product)
#Top-selling product
top_product = sales_per_product.idxmax()
top_sales = sales_per_product.max()
print(f"\nTop-Selling-Product:{top_product} (${top_sales})")
#DAily Revenue
daily_revenue = df.groupby('Date')['Total'].sum()
print("\nDaily Revenue :\n", daily_revenue)
