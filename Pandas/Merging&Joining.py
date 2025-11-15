# pd.merge(df1,df2,on="ColumnName",how="Type of join")
import pandas as pd
# Customer dataframe
df_customer = pd.DataFrame({
     "CustomerId" : [1,2,3],
     "Name" : ["Ramesh","Suresh","Kalpesh"]
})
df_orders = pd.DataFrame({
    "CustomerId" : [1,2,4],
    "Order Amount" : [250,450,350]
})
df_merged = pd.merge(df_customer,df_orders,on="CustomerId",how="left")
print("Left Joint : ")
print(df_merged)