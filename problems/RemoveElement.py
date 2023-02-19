def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1





    return k, nums

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
