class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ 1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[-1]
    
print(Solution().uniquePaths(m = 3, n = 7))
print(Solution().uniquePaths(m = 3, n = 2))
print(Solution().uniquePaths(m = 10, n = 20))