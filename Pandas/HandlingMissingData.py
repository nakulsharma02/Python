'''
Handling Missing Data 
NaN (Not a Number)
None (for Object data types)
'''
# isnull()-->True (NaN or any data is missing)
# False --> Value is present
import pandas as pd
data = pd.DataFrame({
    "Name" : ['SHERA','PATHAN','UJJWAL','ROHAN','MRIDUL','SONAM','NIKITA','ARYA','OP'],
    "Age":[22,33,None,55,21,23,34,23,45],
    "Salary" : [200000,888888,None,3636553,525245,62626252,256622626,552667,None],
})
print(data)
print(data.isnull())
print(data.isnull().sum())
# Returns the count of null values in each column.

'''Handle'''
# dropna() --> drop rows with missing values 
# dropna(axis = 0 ,inplace = True) axis0[drop rows],axis1[drop columns]
"""data.dropna(inplace=True)
print(data)
"""
# fillna() --> used to fill values on the default places
data['Age'] = data['Age'].fillna(data['Age'].mean())
print(data)
data.fillna({'Salary': data['Salary'].mean()}, inplace=True)
print(data)
