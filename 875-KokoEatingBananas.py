from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            eatHours = 0
            for v in piles:
                eatHours += ceil(v / mid)
            if eatHours > h:
                lo = mid + 1
            else:
                hi = mid

        return hi
    
print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))
print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6))