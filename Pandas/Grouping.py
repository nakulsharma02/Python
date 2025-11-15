import pandas as pd
data = pd.DataFrame({
    "Name" : ['Ram','Ram','Ghanshyam','Aditi','Raj'],
    "Age" : [28,28,28,30,30],
    "Salary" : [500000,600000,700000,400000,300000],
    "Performance Ratio" : [85,90,78,92,88]
})

# For Single Column
grouped = data.groupby("Age")["Salary"].sum()
print(grouped)

# For Multiple Column
grouped = data.groupby(["Age","Name"])["Salary"].sum()
print(grouped)