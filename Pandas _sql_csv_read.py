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


some_query = """INSERT INTO products (name, price) 
VALUES ('Фен для волосся 2200 Вт', 740), 
('Подовжувач на 3 розетки з вимикачем', 230),
('Настільна лампа LED з USB', 520),
('Розумна розетка Wi-Fi', 690),
('Пральна машина автоматична', 11990),
('Холодильник двокамерний', 15400),
('Пилосос циклонний', 2450),
('Сушарка для взуття електрична', 350),
('Тепловентилятор настільний', 630),
('Обігрівач масляний 9 секцій', 2850),
('Мікрохвильова піч 20 л', 2200),
('Плитка електрична настільна', 780),
('Зарядний пристрій для телефону', 280),
('Світильник нічний сенсорний', 210),
('Радіо-будильник з цифровим дисплеєм', 430),
('Розетка з таймером механічна', 160),
('Блок живлення для ноутбука', 450),
('Зволожувач повітря ультразвуковий', 960),
('Мережевий фільтр 5 розеток', 290)"""
cur.execute(some_query)
conn.commit()

data = pd.read_csv('users.csv', sep=',', header=0, index_col=1)
print(data)

data1 = pd.read_excel('family.xlsx')
print(data1)

select_query = 'SELECT * FROM products'

data2 = pd.read_sql_query(select_query, conn)
print(data2)
cur.close()
conn.close()