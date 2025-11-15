# Sorting Data
''' A B C D '''
# sort_values(by = "ColumnName" , ascending = True/False , inplace = True)
import pandas as pd
data = pd.DataFrame({
    "Name" : ['Ram','Shyam','Ghanshyam','Aditi','Raj'],
    "Age" : [28,34,22,30,29],
    "Salary" : [500000,600000,700000,400000,300000],
    "Performance Ratio" : [85,90,78,92,88]
})

# For Single Columns
data.sort_values(by = "Name" , ascending = True , inplace = True )
print(data)

# For Multiple Columns
data.sort_values(by = ["Name","Age"],ascending = [False,True] , inplace = True)
print(data)
