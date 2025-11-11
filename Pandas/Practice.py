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