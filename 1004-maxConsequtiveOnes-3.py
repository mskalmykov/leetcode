from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = 0
        curOnes = 0
        zeroIds = []

        for i, v in enumerate(nums):
            if v == 1:
                curOnes += 1
            else:
                zeroIds.append(i)
                if len(zeroIds) > k:
                    maxOnes = max(maxOnes, curOnes)
                    curOnes = i - zeroIds.pop(0)
                else:
                    curOnes += 1

        return max(maxOnes, curOnes)


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(f'{nums}, {k} ->', Solution().longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(f'{nums}, {k} ->', Solution().longestOnes(nums, k))
