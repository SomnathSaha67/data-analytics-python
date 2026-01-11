import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [45000, 500, 1500, 12000, 2500],
    'Stock': [15, 150, 80, 25, 60],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'Rating': [4.5, 4.2, 4.0, 4.7, 4.3]
}
df=pd.DataFrame(data)
print(f"Product and Price details:\n{df[['Product', 'Price']]}")
print(f"\nContents of Products:\n{pd.Series(df['Product'])}")
print(f"\nPrice details as DataFrame:\n{df[['Price']]}")
print(f"\nProduct, Stock and Rating details:\n{df[['Product', 'Stock', 'Rating']]}")
print(f"\nAll columns except Category:\n{df.drop(columns=['Category'])}")