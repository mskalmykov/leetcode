from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = {0}
        l = len(nums)

        for i in range(l):
            if i not in reachable:
                return False
            
            n = nums[i]
            if i + n >= l - 1:
                return True
            
            for j in range(1, n + 1):
                reachable.add(i + j)

        return True

print(Solution().canJump(nums = [2,3,1,1,4]))
print(Solution().canJump(nums = [3,2,1,0,4]))
print(Solution().canJump(nums = [2,5,0,0]))
print(Solution().canJump(nums = [1,1,2,2,0,1,1]))
