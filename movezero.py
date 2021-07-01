
numbers = [0,0,0,1,2,3]
list_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        list_numbers.append(numbers[i])
for i in range(len(numbers)):
    if numbers[i] == 0:
        list_numbers.append(numbers[i])
print(list_numbers)



