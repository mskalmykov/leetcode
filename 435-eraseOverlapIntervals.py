from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        ints = sorted(intervals)
        prev = ints[0]

        for next in ints[1:]:
            if next[0] >= prev[1]:
                prev = next
            else:
                count += 1
                if next[1] < prev[1]:
                    prev = next

        return count

print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))
