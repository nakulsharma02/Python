import pandas as pd
data = {
    "Name" : ['Ram','Shyam','Ghanshyam','Mohan','Rohan','Atul','Suraj','Vishal'],
    "Age" : [25,56,30,40,24,60,34,22],
    "Salaries" : [35000,100000,30000,40000,400000,200000,25000,50000],
    "City" : ['Delhi','Mumbai','Nagpur','Meerut','Noida','Ghaziabad','Dehradun','Gudgaon']
}
df = pd.DataFrame(data)
print(df)
df.to_csv("Company.csv",index = False)
df.to_excel("Company.xlsx",index = False)
df.to_json("Company.json",index = False)