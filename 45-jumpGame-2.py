
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0

        while i < len(nums) - 1:
            n = nums[i]
            jumps += 1
            
            if n + i >= len(nums) - 1:
                break
            
            max_jump = i + 1
            max_idx = i + 1
            for j in range(1, n + 1):
                if nums[i + j] != 0 and i + j + nums[i + j] > max_jump:
                    max_jump = i + j + nums[i + j]
                    max_idx = i + j
            i = max_idx

        return jumps

print(Solution().jump(nums = [2,3,1,1,4]))
print(Solution().jump(nums = [2,3,0,1,4]))