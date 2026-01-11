import pandas as pd 
data = {
    'Book': ['Python Crash Course', 'Clean Code', 'Design Patterns', 'Algorithms', 'Data Science'],
    'Author': ['Eric Matthes', 'Robert Martin', 'Gang of Four', 'Cormen', 'Jake VanderPlas'],
    'Pages': [544, 464, 395, 1312, 541],
    'Price': [2500, 3200, 2800, 5500, 3000],
    'Year': [2019, 2008, 1994, 2009, 2016]
}
print(f"First row using iloc:\n{pd.DataFrame(data).iloc[0]}")
print(f"Last row using iloc:\n{pd.DataFrame(data).iloc[-1]}")
print(f"\nFirst three rows using iloc:\n{pd.DataFrame(data).iloc[0:3]}")
print(f"\nRows from 2 to 4 using iloc:\n{pd.DataFrame(data).iloc[1:4]}")
print(f"\n2ndcolumn of 3rd row using iloc:\n{pd.DataFrame(data).iloc[2,1]}")
print(f"All rows with first 2 columns: \n{pd.DataFrame(data).iloc[:,2]}")
print(f"\nFirst row using loc:\n{pd.DataFrame(data).loc[0]}")
print(f"Last row using loc:\n{pd.DataFrame(data).loc[len(data['Book'])-1]}")
print(f"\nFirst three rows using loc:\n{pd.DataFrame(data).loc[0:2]}")
print(f"\nRows from 2 to 4 using loc:\n{pd.DataFrame(data).loc[1:3]}")
print(f"\n2nd column of 3rd row using loc:\n{pd.DataFrame(data).loc[2,'Author']}")
print(f"\nBooks and Price for all rows using loc:\n{pd.DataFrame(data).loc[:,['Book','Price']]}")
print(f"\nAuthor and Year for first 3 rows using loc:\n{pd.DataFrame(data).loc[0:2,['Author','Year']]}")