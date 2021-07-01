
data = ['1000', 'spam', 3000, 25.5, 'spam', ['spam'], {'a':'spam'}, 10000, '20000']

def func1(obj):
    if isinstance(obj,(int, float)):
        return obj
    elif isinstance(obj,str):
        if obj.isdigit():
            return int(obj)
        else:
            return 0
    else:
        return 0
print(list(map(func1, data)))