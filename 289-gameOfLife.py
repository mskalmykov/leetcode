from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                nbrs = 0
                for ii in range(i-1, i+2):
                    if ii < 0 or ii >= m:
                        continue
                    for jj in range(j-1, j+2):
                        if jj < 0 or jj >= n:
                            continue
                        if ii == i and jj == j:
                            continue
                        if board[ii][jj] == 1 or board[ii][jj] == 11:
                            nbrs += 1
                if board[i][j] == 0:
                    if nbrs == 3:
                        board[i][j] = 10
                else:
                    if nbrs < 2 or nbrs > 3:
                        board[i][j] = 11
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 10:
                    board[i][j] = 1
                elif board[i][j] == 11:
                    board[i][j] = 0

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)

board = [[1,1],[1,0]]
Solution().gameOfLife(board)
print(board)
