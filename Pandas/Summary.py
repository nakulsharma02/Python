# Summary -> Aggregation 
import pandas as pd
data = pd.DataFrame({
    "Name" : ['Ram','Shyam','Ghanshyam','Aditi','Raj'],
    "Age" : [28,34,22,30,29],
    "Salary" : [500000,600000,700000,400000,300000],
    "Performance Ratio" : [85,90,78,92,88]
})
print(data["Age"].mean())
print(data["Age"].min())
print(data["Age"].max())
print(data["Age"].std())
print(data["Age"].sum())
