from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        x, y = 0, -1
        l, r = -1, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r and t < b:
            for y in range(y+1, r):
                result.append(matrix[x][y])
            r -= 1
            if r == l: break
            for x in range(x+1, b):
                result.append(matrix[x][y])
            b -= 1
            if b == t: break
            for y in range(y-1, l, -1):
                result.append(matrix[x][y])
            l += 1
            if r == l: break
            for x in range(x-1, t, -1):
                result.append(matrix[x][y])
            t += 1

        return result

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[1]]))
print(Solution().spiralOrder([[2,5,8],[4,0,-1]]))

