import pandas as pd
data = {
    'Name': ['Amit', 'Priya', 'Raj', 'Sneha', 'Vikram', 'Anjali', 'Rohit', 'Neha'],
    'Age': [22, 21, 23, 20, 24, 22, 21, 23],
    'Marks': [85, 92, 78, 88, 65, 90, 72, 95],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
}
print(f"Students with marks greater than 80:\n{pd.DataFrame(data)[pd.DataFrame(data)['Marks']>80]}")
print(f"\nStudents from Delhi:\n{pd.DataFrame(data)[pd.DataFrame(data)['City']=='Delhi']}")
print(f"\nStudents aged minimum 22 and marks minimum 85:\n{pd.DataFrame(data)[(pd.DataFrame(data)['Age']>=22) & (pd.DataFrame(data)['Marks']>=85)]}")
print(f"\nStudents from Mumbai or Bangalore:\n{pd.DataFrame(data)[(pd.DataFrame(data)['City']=='Mumbai') | (pd.DataFrame(data)['City']=='Bangalore')]}")
print(f"\nStudents with marks less than 75:\n{pd.DataFrame(data)[pd.DataFrame(data)['Marks']<75]}")
print(f"\nStudents aged 21 and from Mumbai:\n{pd.DataFrame(data)[(pd.DataFrame(data)['Age']==21) & (pd.DataFrame(data)['City']=='Mumbai')]}")
print(f"\nStudent with highest marks:\n{pd.DataFrame(data)[pd.DataFrame(data)['Marks']==pd.DataFrame(data)['Marks'].max()]}")
