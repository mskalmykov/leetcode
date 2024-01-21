from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = {}
        rows = {}
        pairs = 0

        for col in grid:
            colStr = ':'.join([str(n) for n in col])
            cols[colStr] = cols.get(colStr, 0) + 1

        for rowNum in range(len(grid)):
            rowStr = ':'.join([str(grid[n][rowNum]) for n in range(len(grid))])
            rows[rowStr] = rows.get(rowStr, 0) + 1

        for colStr in cols:
            pairs += cols[colStr] * rows.get(colStr, 0)

        return pairs
    
print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))