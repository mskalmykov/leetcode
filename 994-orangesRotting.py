from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = set()
        rotten = set()
        q = deque()
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
                
        for r in rotten:
            q.appendleft(r)

        while q:
            if fresh:
                minutes += 1
            else:
                break

            for _ in range(len(q)):
                a, b = q.pop()
                rotten.add((a, b))

                for i, j in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                    if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                        continue
                    if (i, j) in rotten:
                        continue
                    if (i, j) in fresh:
                        fresh.remove((i, j))
                        rotten.add((i, j))
                        q.appendleft((i, j))

        if fresh:
            return -1
        else:
            return minutes

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[0,2]]))