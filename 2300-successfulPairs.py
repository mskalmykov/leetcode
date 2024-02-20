from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        p = sorted(potions)
        lp = len(p)
        ans = [0] * len(spells)

        for idx, val in enumerate(spells):
            l, r = 0, lp - 1

            while l < r:
                mid = l + (r - l) // 2
                if p[mid] * val >= success:
                    r = mid
                else:
                    l = mid + 1
            
            if l == lp - 1 and p[l] * val < success:
                ans[idx] = 0
            else:
                ans[idx] = lp - l

        return ans
    
print(Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
print(Solution().successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))

