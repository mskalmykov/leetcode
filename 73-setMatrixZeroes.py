from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        mark = 2**31
        zeroStr, zeroRow = False, False

        if matrix[0][0] == 0:
            zeroStr, zeroRow = True, True

        for i in range(1, m):
            if matrix[i][0] == 0:
                zeroRow = True
                matrix[i][0] = mark
        for j in range(1, n):
            if matrix[0][j] == 0:
                zeroStr = True
                matrix[0][j] = mark

        for i in range(1, m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = mark
                    matrix[i][0] = mark

        for i in range(1, m):
            if matrix[i][0] == mark:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == mark:
                for i in range(m):
                    matrix[i][j] = 0

        if zeroRow:
            for i in range(m):
                matrix[i][0] = 0

        if zeroStr:
            for j in range(n):
                matrix[0][j] = 0


m = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(m)
print(m)

m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(m)
print(m)