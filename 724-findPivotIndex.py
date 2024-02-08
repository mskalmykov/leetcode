from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = [0 for _ in range(len(nums))]

        for i in range(-2, -len(nums)-1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        leftSum = 0
        for i in range(len(nums)):
            if leftSum == rightSum[i]:
                return i
            else:
                leftSum += nums[i]

        return -1
        
print(Solution().pivotIndex([-1,-1,0,1,1,0]))
print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([2,1,-1]))
