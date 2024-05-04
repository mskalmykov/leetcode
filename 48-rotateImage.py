from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2):
            l = len(matrix) - i - 1
            for j in range(i, l):
                matrix[i][j], matrix[j][l]   = matrix[j][l]  , matrix[i][j]
                matrix[i][j], matrix[l][l+i-j] = matrix[l][l+i-j], matrix[i][j]
                matrix[i][j], matrix[l+i-j][i] = matrix[l+i-j][i], matrix[i][j]
            
m = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(m)
print(m)

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(m)
print(m)
