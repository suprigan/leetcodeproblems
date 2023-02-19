def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k, nums

# Press the green button in the gutter to run the script.
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))