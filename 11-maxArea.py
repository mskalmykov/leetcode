from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result
    
height = [1,8,6,2,5,4,8,3,7]
print(height)
print(Solution().maxArea(height))

height = [2,1]
print(height)
print(Solution().maxArea(height))
