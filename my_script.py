from my_lambdata.new_col import col_adder
from my_lambdata.date_split import date_splitter
import pandas as pd

print('Testing col adder')

data_list = [0,42,-5,3]
col = pd.Series(data_list)
df = pd.DataFrame({'1':[21,2,32,48], '2':[49,65,6,27]})

print('\nbefore')
print(df)

df = col_adder(df, data_list)
print('\nafter')
print(df)


print('\n\nTesting date splitter')
df2 = pd.DataFrame({'Name':['Fred', 'Vicky', 'Bunny'], \
    'Birthday':['01/30/2004', '02/29/2008', '10/31/2016']} )
print('\nbefore')
print(df2)

df2 = date_splitter(df2, 'Birthday')
print('\nafter')
print(df2)