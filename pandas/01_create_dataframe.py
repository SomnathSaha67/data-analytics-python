import pandas as pd 
data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Roll Number": [101, 102, 103, 104, 105],
        "Branch": ["CSE", "ECE", "ME", "CE", "EE"],
        "Semester": [5, 6, 5, 7, 6],
        "CGPA": [8.5, 7.8, 9.0, 8.2, 7.5]}
df = pd.DataFrame(data)
print("\nDataFrame of Students:")
print(df)
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))
print("\nLast 3 rows of the DataFrame:")
print(df.tail(3))
print(f"\nShape of the DataFrame: {df.shape}")
print(f"\nColumn names of the DataFrame: {df.columns}")
print(f"\nData types of all columns: {df.dtypes}")