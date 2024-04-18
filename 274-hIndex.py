from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for idx, val in enumerate(sorted(citations, reverse=True)):
            if idx < val:
                h += 1
            else:
                break
        return h


print(Solution().hIndex([3,0,6,1,5]))
print(Solution().hIndex([1,3,1]))
print(Solution().hIndex([1]))
