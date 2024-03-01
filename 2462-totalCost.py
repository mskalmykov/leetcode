from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0

        left = []
        right = []
        common = []

        if len(costs) < candidates * 2:
            common = sorted(costs, reverse=True)
        else:
            for i in range(candidates):
                heapq.heappush(left, costs[i])
                heapq.heappush(right, costs[-i-1])

        idx_left = candidates - 1
        idx_right = len(costs) - candidates

        for _ in range(k):
            if common:
                ans += common.pop()
                continue

            if right[0] < left[0]:
                ans += heapq.heappop(right)
                idx_right -= 1
                if idx_left < idx_right:
                    heapq.heappush(right, costs[idx_right])
                else:
                    common = sorted(left + right, reverse=True)
            else:
                ans += heapq.heappop(left)
                idx_left += 1
                if idx_left < idx_right:
                    heapq.heappush(left, costs[idx_left])
                else:
                    common = sorted(left + right, reverse=True)

        return ans
    
print(Solution().totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
print(Solution().totalCost(costs = [1,2,4,1], k = 3, candidates = 3))
print(Solution().totalCost(costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], k = 13, candidates = 23))
print(Solution().totalCost(costs = [618,884,484,524,898,648,360,58,452,695,351,886,114,828,899,119,161,321,132,25,845,587,290,477,589,419,160,847,584,676,420,755,850,338,951,800,364,579,772,720,218,283,622,837,810,791,112,481,577,42,507,392,329,352,409,782,210,710,7,905,573,322,459], k = 31, candidates = 28))