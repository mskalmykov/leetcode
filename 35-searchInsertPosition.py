from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1

        if target < nums[m]:
            return m
        else:
            return m + 1

print(Solution().searchInsert(nums = [1,3,5,6], target = 5))
print(Solution().searchInsert(nums = [1,3,5,6], target = 2))
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))
print(Solution().searchInsert(nums = [1,3,5,6], target = 0))
