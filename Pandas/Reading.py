import pandas as pd
# for CSV
print("Read CSV File : ")
df = pd.read_csv("Company.csv")
print(df)
# for Excel
print("Read Excel File : ")
df = pd.read_excel("Company.xlsx")
print(df)
# for Json
print("Read JSON File : ")
df = pd.read_json("Company.json")
print(df)