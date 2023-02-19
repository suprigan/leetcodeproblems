def searchInsert(nums, target):
    k = 0
    for i in range(len(nums)):
        if nums[i] < target:
            k += 1
    return k

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))
