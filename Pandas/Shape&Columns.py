'''
1. How big is your dataset ?
2. What are the names of the columns ?
'''
'''
There are attributes in pandas like .shape and .columns which helps in viewing of data shape and columns.
'''
import pandas as pd
df = pd.read_excel("Company.xlsx")
print(f'shape   :   {df.shape}')
print(f'Column Names :   {df.columns}')