from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        seen = set()
        q = deque()
        count = 0

        q.appendleft(entrance)

        while q:
            count += 1
            for _ in range(len(q)):
                y, x = q.pop()
                seen.add((y, x))
                moves = ((y-1, x), (y+1, x), (y, x-1), (y, x+1))

                for y, x in moves:
                    if (y < 0) or (x < 0) or (y >= len(maze)) or (x >= len(maze[0])):
                        continue
                    elif maze[y][x] == '+':
                        continue
                    elif (y, x) in seen:
                        continue
                    elif (y == 0) or (x == 0) or (y == len(maze) - 1) or (x == len(maze[0]) - 1):
                        return count
                    else:
                        q.appendleft([y, x])
                        seen.add((y, x))

        return -1

print(Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print(Solution().nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
print(Solution().nearestExit(maze = [[".","+"]], entrance = [0,0]))
print(Solution().nearestExit(maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]], entrance = [0,1]))