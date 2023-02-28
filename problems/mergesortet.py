def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    k = m + n - 1
    while n > 0 and m > 0:
        print(n,m)
        if nums1[m-1] > nums2[n-1]:
            nums1[k] = nums1[m-1]
            m -= 1
        else:
            nums1[k] = nums2[n-1]
            n -= 1
        k -= 1
    while n > 0:
        nums1[k] = nums2[n-1]
        n -= 1
        k -= 1
    return (nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))