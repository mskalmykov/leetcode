from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        ans = 0

        def dfs(city: int):
            for nei, conn in enumerate(isConnected[city]):
                if conn == 1 and nei not in seen:
                    seen.add(nei)
                    dfs(nei)


        for i in range(len(isConnected)):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)

        return ans
    
print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))