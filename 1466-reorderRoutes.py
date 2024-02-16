from typing import List
from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cities = {}
        stack = deque()
        seen = {0}
        reorderCount = 0

        for c_from, c_to in connections:
            if c_from in cities:
                cities[c_from].append((c_to, True))
            else:
                cities[c_from] = [(c_to, True)]

            if c_to in cities:
                cities[c_to].append((c_from, False))
            else:
                cities[c_to] = [(c_from, False)]

        stack.append(0)

        while stack:
            c = stack.pop()
            for neighbor, needReverse in cities[c]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    reorderCount += int(needReverse)
                    seen.add(neighbor)

        return reorderCount
    
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(Solution().minReorder(3, [[1,0],[2,0]]))
