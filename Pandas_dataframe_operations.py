import pandas as pd

data = {
    'Імʼя':['John', 'Mary', 'Paul', 'Anna', 'Kate', 'Tom'],
    'Вік': [29, 34, 22, 45, 17, 28],
    'Місто': ['Lutsk', 'Kyiv', 'Odesa', 'Kharkiv', 'Lviv', 'Dnipro']}

df = pd.DataFrame(data)

df.head(2)
df.tail(2)
# df.info()
df.shape
df.columns
young = df[(df['Вік']<30) & ((df['Місто'] == 'Lviv') | (df['Місто'] == 'Lutsk') | (df['Місто'] == 'Odesa'))]
sorted_df = df.sort_values(by='Вік', ascending=True)
print(sorted_df)
