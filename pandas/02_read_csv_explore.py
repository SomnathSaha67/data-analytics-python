# Download this CSV:  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
# Save it in the same folder as your script
import pandas as pd
contents_titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(f"First 10 rows: \n{contents_titanic.head(10)}")
print(f"Last 5 rows: \n{contents_titanic.tail(5)}")
print(f"Shape of the DataFrame: {contents_titanic.shape}")
print(f"Column names: {contents_titanic.columns}")
print(f"Data types and info: \n{contents_titanic.info()}")
print(f"Statistical summary: \n{contents_titanic.describe()}")
print(f"Missing values in each column: \n{contents_titanic.isnull().sum()}")