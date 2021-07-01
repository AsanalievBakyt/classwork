
def binarySearch(data,x):
    L = 0
    R = len(data) - 1
    found = 0
    while L <= R and not found:
        mid = (L+R) // 2
        if data[mid] == x:
            found = 1
        else:
            if data[mid] < x:
                L = mid + 1
            else:
                R = mid - 1
    return found

print(binarySearch([1,2,3,4,5,6], 4))