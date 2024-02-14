from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unseen = set([x for x in range(1, len(rooms))])

        def dfs(room: int):
            for k in rooms[room]:
                if k in unseen:
                    unseen.remove(k)
                    dfs(k)
        
        dfs(0)

        return not unseen
    
print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
