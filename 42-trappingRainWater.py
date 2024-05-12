from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            if not stack or height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                h = -1
                while len(stack) > 0 and height[i] > height[stack[-1]]:
                    if h >= 0:
                        water += (min(height[i], height[stack[-1]]) - h) * (i - stack[-1] - 1)
                    h = height[stack.pop()]
                if stack:
                    water += (min(height[i], height[stack[-1]]) - h) * (i - stack[-1] - 1)
                stack.append(i)

        return water
    
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))
