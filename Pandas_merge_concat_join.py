import pandas as pd 

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['John', 'Mary', 'Alex']
    })

df2 = pd.DataFrame({
    'id': [1, 2, 4, 5],
    'name': [5000, 6000, 5500, 7000],
    })

merged = pd.merge(df1, df2, on='id', how='outer', suffixes=('_left', '_right'))
concated = pd.concat([df1, df2], axis=1, ignore_index=True)
print(concated)
print(merged)

df3 = pd.DataFrame({
    'name': ['John', 'Mary', 'Alex']
    })

df4 = pd.DataFrame({
    'name': ['Valik', 'Roma', 'Alex']
    })

result = df3.join(df4, how='left', lsuffix='_left', rsuffix='_right')
print(result)