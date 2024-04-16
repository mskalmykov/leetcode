from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums) - 1:
            n = nums[i]
            
            if n == 0 and i < len(nums) - 1:
                return False
            if n + i >= len(nums) - 1:
                return True
            
            max_jump = i + 1
            max_idx = i + 1
            for j in range(1, n + 1):
                if nums[i + j] != 0 and i + j + nums[i + j] > max_jump:
                    max_jump = i + j + nums[i + j]
                    max_idx = i + j
            i = max_idx

        return True

print(Solution().canJump(nums = [2,3,1,1,4]))
print(Solution().canJump(nums = [3,2,1,0,4]))
print(Solution().canJump(nums = [2,5,0,0]))
print(Solution().canJump(nums = [1,1,2,2,0,1,1]))
