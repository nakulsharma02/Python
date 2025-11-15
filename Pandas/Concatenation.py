# Vertically (row - wise)
# Horizontally ( column - wise)
import pandas as pd
df_customer = pd.DataFrame({
     "CustomerId" : [1,2,3],
     "Name" : ["Ramesh","Suresh","Kalpesh"]
})
df_orders = pd.DataFrame({
    "CustomerId" : [1,2,4],
    "Order Amount" : [250,450,350]
})
# pd.concat([df1,df2],axis=0,ignore_index=True)
# axis - 0 for row-wise and 1 for column - wise
df_concat = pd.concat([df_customer,df_orders],axis=1,ignore_index=True)
print(df_concat)