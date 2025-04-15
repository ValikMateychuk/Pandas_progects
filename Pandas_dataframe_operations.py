import pandas as pd

data = {
    'Імʼя':['John', 'Mary', 'Paul', 'Anna', 'Kate', 'Tom'],
    'Вік': [29, 34, 22, 45, 17, 28],
    'Місто': ['Lutsk', 'Kyiv', 'Odesa', 'Kharkiv', 'Lviv', 'Dnipro']}

df = pd.DataFrame(data)

df.head(2)
df.tail(2)
print(df.info())
