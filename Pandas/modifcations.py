import pandas as pd
# Adding Columns
data = pd.DataFrame({
    "Id":[1,2,3,4,5,6,7,8,9],
    "Name":['SHERA','PATHAN','UJJWAL','ROHAN','MRIDUL','SONAM','NIKITA','ARYA','OP'],
    "Salary":[200000,888888,288883,3636553,525245,62626252,256622626,552667,365625]
})
data['Cashback'] = data['Salary']*0.0001
data['Username'] = ['shera.io','pathan.io','ujjwal.io','rohan.io','mridul.io','sonam.io','nikita.io','arya.io','op.io']
print(data)
# using insert()
# df.insert(location,"ColumnName",someData)
data.insert(1,"NickName",['sheru','petu','ujju','rohu','mridu','sona','niki','arya','op'])
print(data)

# Updating Values 
# loc[] --> method used for accessing cell or rows or set of rows  and modifying them.
# df.loc[row_index,"ColumnName",new_value]
data.loc[0,"Name"] = "SURAJ"
print(data)
data["Salary"] = data["Salary"]*0.1
print(data)

# Removing Columns
data.drop(columns=["NickName","Cashback"],inplace=True)
print(data)