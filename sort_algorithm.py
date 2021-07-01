
def bubbleSort(data):
    for i in range(len(data)- 1):
        for j in range(len(data)- 1):
            if data[j] > data[j +1]:
                data[j],data[j + 1] = data[j+1], data[j]
                j += 1
    return data
print(bubbleSort([3,1,4,5,2]))
