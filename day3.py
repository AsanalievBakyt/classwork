

numbers = [10,100,30,-1,8,-13]
max_num,min_num,max_index,min_index = 0,0,0,0


for i in range(len(numbers)):
    num = numbers[i]
    if num > max_num:
        max_num = num
        max_index = i
    if num < min_num:
        min_num = num
        min_index = i
numbers[max_index], numbers[min_index] = min_num, max_num


print(numbers)








