
#
# data = {'name': 'john'}
# print(data['name'])
# data = dict(name= 'bakyt')
# print(data)
# data['car'] = '123'

from math import inf


data = [{'name':'bakyt','dep':'devopment','salary':300000},
    {'name':'maksim','dep':'manager','salary':230000},
    {'name':'john','dep':'security','salary':inf},
    {'name':'jaime','dep':'friend','salary':1000000}]
max_salary = 0
emp_name = None
emp_dep = None
for emp in data:
    emp_sal = emp.get('salary')
    if max_salary < emp_sal:
        max_salary = emp_sal
        emp_name = emp.get('name')
        emp_dep = emp.get('dep')
print(emp_name, emp_dep,max_salary)





