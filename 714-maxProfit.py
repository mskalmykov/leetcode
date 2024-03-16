from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        maximumProfit = 0
        sellDiff = - float('inf')
        
        for p in prices:
            nextProfit = p + sellDiff
            nextDiff = -p - fee + maximumProfit

            sellDiff = max(sellDiff, nextDiff)
            maximumProfit = max(maximumProfit, nextProfit)

        return maximumProfit

print(Solution().maxProfit(prices = [1,3,2,8,4,9], fee = 2))
print(Solution().maxProfit(prices = [1,3,7,5,10,3], fee = 3))
