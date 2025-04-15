import pandas as pd
import csv

# Дані для запису
data = [
    ['Імʼя', 'Вік', 'Місто'],
    ['Оля', 25, 'Луцьк'],
    ['Іван', 30, 'Київ']
]

# # Створення CSV-файлу
with open('users.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

data1 = [1, 2, 3, 4, 5]
s = pd.Series(data1, index=['a', 'b', 'c', 'd', 'e'])
print(s)


data2 = {'name':['alex', 'bob', 'fill'], 'age':[23, 27, 21]}
b = pd.DataFrame(data2, index=['student1', 'student2', 'student3'])
print(b)