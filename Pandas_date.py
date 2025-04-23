import pandas as pd

df = pd.DataFrame({
    'name': ['Ivan', 'Ola', 'Max'],
    'date': ['1990-01-01', '1985-05-15', '1992-08-20']
    })

df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.day_name()

df = df[df['date'] > '1989-01-01']

pd.Timestamp.now()

print(df)