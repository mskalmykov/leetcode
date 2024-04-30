from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minL = len(nums) + 1
        subS = nums[0]

        while True:
            if subS < target:
                r += 1
                if r == len(nums):
                    break
                else:
                    subS += nums[r]
            else:
                minL = min(minL, r-l+1)
                if l < r:
                    subS -= nums[l]
                    l += 1
                else:
                    return 1

        if minL == len(nums) + 1:
            return 0
        else:
            return minL

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(target = 4, nums = [1,4,4]))
print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))