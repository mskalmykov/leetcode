from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = 0
        zeroes = 0
        for n in nums:
            zeroes = zeroes + 1 - n
            if zeroes > 1:
                zeroes = zeroes - (1 - nums[j])
                j += 1
        return len(nums) - j - 1

print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))


