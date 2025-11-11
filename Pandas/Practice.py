import pandas as pd
data = {
    "Name" : ['Ram','Shyam','Ghanshyam','Aditi','Raj'],
    "Age" : [28,34,22,30,29],
    "Salary" : [500000,600000,700000,400000,300000],
    "Performance Ratio" : [85,90,78,92,88]
}
df = pd.DataFrame(data)
# Display the data 
print("Sample Data :")
print(df)
print("Names(Single column return series)")
print(df['Name'])
# Selecting Multiple Columns
subset = df[['Name','Age']]
print(subset)
# Filtering of Rows
high_salary = df[df['Salary']>400000]
print('Employees with Salary > 400000')
print(high_salary)
# Filterzing Rows with multiple conditions 
filtered = df[(df['Age']<30)&(df['Salary']>=500000)]
print(f'Employees list Age < 30 + Salary >400000')
print(filtered)
# Using OR Condition 
filtered_or = df[(df['Age']>28)|(df['Performance Ratio']>=85)]
print(filtered_or)