import pandas as pd
import psycopg2

conn = psycopg2.connect(
  host = 'localhost',
    database = 'train',
    user = 'postgres',
    password = '192837465',
    port = '5433'
)
cur = conn.cursor()

df = pd.DataFrame({
    'Імʼя':['John', 'Mary', 'Oleg'],
    'Вік': [29, 34, 22],
    'Місто': ['Lutsk', 'Kyiv', 'Odesa']
    })

df.to_csv('New_users.csv', mode='w')

df.to_excel('New_users.xlsx', index=False)

cur.execute('INSERT INTO public.products (name, price) VALUES (%s, %s)',
    ('phone', 2933))

cur.execute('Delete from public.products where name = %s',
    ('John',))
            
conn.commit()

cur.close()
conn.close()