

def fact(number):
    a = 1
    for i in range(1, number + 1):
        a *= i
    return a

print(fact(5))