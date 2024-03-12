from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[:2]

        for n in cost[2:]:
            a, b = b, min(a + n, b + n)
        
        return min(a, b)

print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
