from my_lambdata.new_col import col_adder
import pandas as pd

data_list = [1,2,3,4]

col = pd.Series(data_list)

df = pd.DataFrame({'A':[1,2,3,4], 'B':[4,5,6,7]})

print('before\n')
print(df)

df = col_adder(df, data_list)
print('after\n')
print(df)