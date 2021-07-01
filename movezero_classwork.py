
data =[3,0,1,0,2,0]
i = 0
for num in data:
    if num != 0:
        data[i] = num
        i += 1
for j in range(i,len(data)):
    data[j] = 0
print(data)
