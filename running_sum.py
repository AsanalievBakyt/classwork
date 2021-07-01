

l1 = [1,2,3,4]

# def runSum(nums):
#     l2 = []
#     for index in range(len(nums)):
#         if index == 0:
#             l2.append(nums[index])
#             continue
#         summ = sum(nums[:index + 1])
#         l2.append(summ)
#     return l2
#
#
#
# print(runSum(l1))


def runSum(nums):
    l2 = []
    summ = 0
    for index in range(len(nums)):
        summ += nums[index]
        l2.append(summ)
    return l2



print(runSum(l1))