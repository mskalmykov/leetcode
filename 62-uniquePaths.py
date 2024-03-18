class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ [ None for _ in range(n+1) ] for _ in range(m+1)]

        def f(i: int, j: int) -> int:
            if i == 1 or j == 1:
                return 1
            
            if dp[i-1][j] == None:
                s = f(i-1, j)
            else:
                s = dp[i-1][j]

            if dp[i][j-1] == None:
                s += f(i, j-1)
            else:
                s += dp[i][j-1]
            
            dp[i][j] = s
            return s

        return f(m, n)
    
print(Solution().uniquePaths(m = 3, n = 7))
print(Solution().uniquePaths(m = 3, n = 2))
print(Solution().uniquePaths(m = 10, n = 20))