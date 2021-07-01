
employees =[('john', 50000),('sue', 100000), ('wak', 78900)]
max_salary = 0
employee = None

for i in range(len(employees)):
    emp = employees[i]
    if emp[1] > max_salary:
        max_salary = emp[1]
        employee = emp

print(employee)








