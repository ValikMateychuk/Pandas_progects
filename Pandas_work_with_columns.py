import pandas as pd

data = {
    'Name':['John', 'Mary', 'Paul', 'Anna', 'Kate', 'Tom'],
    'Age': [29, 34, None, 45, 17, 28],
    'City': ['Lutsk', 'Kyiv', 'Odesa', None, 'Lviv', 'Dnipro']}

df = pd.DataFrame(data)
for i in df.index:
    if df.at[i,'Age'] > 30:
        df.at[i, 'Class_groupe'] = 32
    else: df.at[i, 'Class_groupe'] = 31

df = df.rename(columns={'Class_groupe': 'Groupe_number'})
sorted_df = df.sort_values(by='Groupe_number', ascending=False)
sorted_df['Older_groupe_number'] = df['Groupe_number'] + 10
print(df.index)
print(sorted_df)