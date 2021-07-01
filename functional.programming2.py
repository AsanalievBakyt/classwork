import random

l1 =[random.randint(1,10000) for i in range(10000)]

def func1(obj):
    if obj > 9500:
        return obj
# print(list(filter(func1, l1)))

data = [
    {"2021-06-01":['john','sue','maksim','jyldyz','bill gates']},
    {"2021-06-02":['sue','maksim','bakyt']},
    {"2021-06-03":['boris the blade', 'john','sue','maksim','bakyt','jyldyz']},
    {"2021-06-04":['john','sue','maksim','jyldyz','bakyt']},
    {"2021-06-05":['john','sue','bakyt','jyldyz']}
]

def func2(obj):
    l1 = len(list(obj.values())[0])
    return l1
print(max(list(map(func2,data))))
