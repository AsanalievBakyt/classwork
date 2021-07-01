list_num = []
ranges = [[1,2,4], [2,3,100],[7,8,20]]
for i in range(len(ranges)):
    max_num = 0
    min_num = 10000000
    elem = ranges[i]
    for num in elem:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    list_num.append([min_num, max_num])
print(list_num)