# Challenge:4
# Reading from a CSV file and printing all columns as rows.


import pandas as pd

pd_data = pd.read_csv("test.csv")
for col in pd_data.columns:
    print(pd_data[col].values)
