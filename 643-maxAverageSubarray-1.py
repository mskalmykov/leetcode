from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSub = 0
        
        for i in range(k):
            curSub += nums[i]

        maxSub = curSub
        i += 1
        
        while i < len(nums):
            curSub += nums[i]
            curSub -= nums[i-k]
            maxSub = max(maxSub, curSub)
            i += 1

        return maxSub / k
    
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverage([5], 1))

