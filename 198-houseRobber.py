from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
        elif l == 3:
            return max(nums[0] + nums[2], nums[1])
        
        a, b, c = nums[0], nums[1], max(nums[0] + nums[2], nums[1])

        for n in nums[3:]:
            d = max(a + n, b + n)
            a, b, c = b, c, d

        return max(b, c)

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
