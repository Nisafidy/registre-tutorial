import numpy as np
import pandas as pd
'''
Datas treatment with pandas.
'''


input_file ='ml-latest-small/movies.csv'

#registre movies dans DataFrame

df=pd.read_csv(input_file, header=0)
#colom selection and csv read

original_headers=list(df.columns.values)
#submit the column to DataFramework
df=df._get_numeric_data()
# delete no numeric data
numeric_headers=list(df.columns.values)
#resubmit to DataFramwork




numpy_array = df.to_numpy()

#
print(numpy_array)

