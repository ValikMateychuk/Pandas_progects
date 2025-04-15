import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'train',
    user = 'postgres',
    password = '192837465',
    port = '5433'
)

cur = conn.cursor()
# Вказуємо схему 'public' явно в запиті
queries = ['DROP DATABASE IF EXISTS train']

for query in queries:
    cur.execute(query)


#colums = [desc[0] for desc in cur.description]
#print(colums)


#result = cur.fetchall()  # Отримуємо всі результати 
#for row in result:
 #   print(row)

# Закриваємо курсор та з’єднання
cur.close()
conn.close()