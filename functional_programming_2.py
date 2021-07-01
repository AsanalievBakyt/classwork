

def twoSum(nums, target):
    for index in range(len(nums)):
        current = nums[index]
        next_list = nums[index + 1:]
        for j in range(len(next_list)):
            num = next_list[j]
            if current + num == target:
                return index, nums.index(num, index+1)



print(twoSum([2,7,11,15],9))


