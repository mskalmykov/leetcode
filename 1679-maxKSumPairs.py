from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sNums = sorted(nums)
        left = 0
        right = len(sNums) - 1
        opCount = 0

        while right > 0 and sNums[right] >= k:
            right -= 1

        while left < right:
            t = sNums[left] + sNums[right]
            if t > k:
                right -= 1
            elif t < k:
                left += 1
            else:
                opCount += 1
                left += 1
                right -= 1
        
        return opCount
        



nums = [1,2,3,4]
k = 5
print(nums, k, Solution().maxOperations(nums, k))

nums = [3,1,3,4,3]
k = 6
print(nums, k, Solution().maxOperations(nums, k))
