
cvs = [{'name': 'maksim', 'personal_info': {'name':'KSTU','spec':'Information Security','exp':2.5,},
        'waited_salary':100000,},
        {'name': 'bakyt', 'personal_info': {'name':'MIT','spec':'Finance','exp':12.5},
        'waited_salary':900000,},
        {'name': 'robert', 'personal_info': {'name':'Stanford','spec':'MBA','exp':9,},
        'waited_salary':789000,}
       ]
max_exp = 0
emp_name = None
emp_salary = 0

for cv in cvs:
        cur_exp = cv.get('personal_info').get('exp')
        if max_exp < cur_exp:
                max_exp = cur_exp
                emp_name = cv.get('name')
                emp_salary = cv.get('waited_salary')
print(emp_name, emp_salary, max_exp)
