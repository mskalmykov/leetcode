from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shots = len(points)

        points.sort()

        prev = points[0]

        for p in points[1:]:
            if p[0] > prev[1]:
                prev = p
            else:
                prev = [p[0], min(prev[1], p[1])]
                shots -= 1

        return shots

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
