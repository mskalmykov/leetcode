from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            cur = nums[i]

            while 0 < cur < n+1 and nums[cur - 1] != cur:
                prev = nums[cur - 1]
                nums[cur - 1] = cur
                cur = prev

        i = 0
        while i < n and nums[i] == i + 1:
            i += 1
        
        return i + 1

print(Solution().firstMissingPositive([2]))
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))

        