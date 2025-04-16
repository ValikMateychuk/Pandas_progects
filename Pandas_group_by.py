import pandas as pd

data = {
    'Name':['John', 'Mary', 'Zina', 'Alex', 'Lina', 'Oleg'],
    'Department':['IT', 'HR', 'IT', 'HR', 'IT', 'IT'],
    'Salary':[50000, 60000, 70000, 80000, 90000, 5000],
}

df = pd.DataFrame(data)
department_all_salary = df.groupby('Department')['Salary'].sum().reset_index()
print(department_all_salary)

department_average_salary = df.groupby('Department')['Salary'].mean().reset_index()
print(department_average_salary)

department_workers_amount = df.groupby('Department')['Name'].count().reset_index()
print(department_workers_amount)

department_all_data = df.groupby('Department').agg(
    Salary_sum=('Salary', 'sum'),
    Salary_average=('Salary', 'mean'),
    Workers_amount=('Name', 'count')
).reset_index()

print(department_all_data)