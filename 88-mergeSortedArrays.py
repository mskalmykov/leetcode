from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j1 = m - 1
        j2 = n - 1
        i = n + m - 1
        while i >= 0 and j2 >= 0:
            if j1 >= 0 and nums1[j1] > nums2[j2]:
                nums1[i] = nums1[j1]
                j1 -= 1
            else:
                nums1[i] = nums2[j2]
                j2 -= 1
            i -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0

Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

Solution().merge(nums1, m, nums2, n)
print(nums1)