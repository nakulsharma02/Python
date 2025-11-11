# Describe method provides the summary of descriptive statistics for numerical columns in your DataFrame
# step - 1 Sample data Frame
import pandas as pd
df = pd.read_csv("Company.csv")
print("Sample DataFrame : ")
print(df)
print("Descriptive Statistics")
print(df.describe())
