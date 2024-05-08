from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = result[-1]

            if cur[0] > prev[1]:
                result.append(cur)
            else:
                result[-1][1] = max(prev[1], cur[1])

        return result

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))