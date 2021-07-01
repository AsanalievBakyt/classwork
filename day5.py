from math import inf
import datetime


emp_names = ['boris the blade', 'john','sue','maksim','bakyt','jyldyz']
data = [
    {"2021-06-01":['john','sue','maksim','jyldyz','bill gates']},
    {"2021-06-02":['sue','maksim','bakyt']},
    {"2021-06-03":['boris the blade', 'john','sue','maksim','bakyt','jyldyz']},
    {"2021-06-04":['john','sue','maksim','jyldyz','bakyt']},
    {"2021-06-05":['john','sue','bakyt','jyldyz']}
]

emp_come = {}
best_day = {}
for name in emp_names:
    count = 0
    for day in data:
        for key, value in day.items():
            if name in value:
                count += 1
        emp_come[name] = count

min = inf
emp_name = None
for i in emp_come:
    if emp_come[i] < min:
        min = emp_come[i]
        emp_name = i
print(emp_name,':', min,'посещение')

max_val = 0

for day in data:
    count = 0
    for key,values in day.items():
        for i in values:
            count += 1
        if count > max_val:
            max_val = count
            best_day = day
print(best_day,max_val)



