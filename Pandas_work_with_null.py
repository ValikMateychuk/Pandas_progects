import pandas as pd

data = {
    'Імʼя':['John', 'Mary', 'Paul', 'Anna', 'Kate', 'Tom'],
    'Вік': [29, 34, None, 45, 17, 28],
    'Місто': ['Lutsk', 'Kyiv', 'Odesa', None, 'Lviv', 'Dnipro']}

df = pd.DataFrame(data)
df.isnull()
# df = df.dropna()
# df = df.dropna(subset=['Місто'])
df['Вік'] = df['Вік'].fillna(df['Вік'].mean())
df['Місто'] = df['Місто'].fillna('Unknown')
print(df)
null_sum = df.isnull().sum()
print(null_sum)
