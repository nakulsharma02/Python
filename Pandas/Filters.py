'''
1 - Select Specific Columns.
2 - Filter Rows
3 - Combine Multiple Conditions.
'''
'''
1 - Square Brackets 
2 - Boolean Conditions
'''
'''
Boolean Indexing 
'''
# For Selecting a column
import pandas as pd
df = pd.read_csv("Company.csv")
column = df['Name']
print(column)

# For Selecting Multiple Columns
columns = df[['Name','Age']]
print(columns)
print("Filtering Of Rows :")
# For filtering the rows
'''
Based on a Single Condition.
'''
Filtered_row = df[df['Age']<30]
print(Filtered_row)
print("")

'''
Based on Multiple Conditions.
'''
Filtered_rows = df[(df['Age']>30)&(df['Salaries']>50000)]
print(Filtered_rows)