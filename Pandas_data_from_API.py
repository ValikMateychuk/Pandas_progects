import pandas as pd
import requests
import json
import psycopg2


# url = 'https://api.exchangerate.host/latest?base=USD'
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Error:", response.status_code)

conn = psycopg2.connect(
    host = 'localhost',
    database = 'train',
    user = 'postgres',
    password = '192837465',
    port = '5433'
)
cur = conn.cursor()

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = response.json()

cur.execute('CREATE TABLE IF NOT EXISTS public.api_data (userId INT, id INT, title VARCHAR(500), body VARCHAR(500))')

for post in data:
    cur.execute('INSERT INTO public.api_data (userId, id, title, body) VALUES (%s, %s, %s, %s)',
        (post['userId'], post['id'], post['title'], post['body']))

conn.commit()
cur.close()
conn.close()
