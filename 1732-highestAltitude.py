from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestAlt = 0
        currentAlt = 0

        for g in gain:
            currentAlt += g
            highestAlt = max(highestAlt, currentAlt)

        return highestAlt
    
print(Solution().largestAltitude([-5,1,5,0,-7]))
print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
