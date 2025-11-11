'''
Problems covered by Info method
1 - Columns , rows ?
2 - What types of ?
3 - Missing Data ?
'''
'''
info() -> Method which gives concise summary.
1 - Numbers of rows and Columns
2 - Column name
3 - int64, float64, Object
4 - non null counts
5 - memory usage of the DataFrame.
'''
import pandas as pd
df = pd.read_json("Company.json")
print("Displaying the information of data set")
print(df.info())

data = {
    "Name" : ['Ram','Shyam'],
    "Age" : [20,25],
    "City" : ['Nagpur','Mumbai']
}
df = pd.DataFrame(data)
print('Displaying the info of the data set')
print(df.info())