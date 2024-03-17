class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [ [0 for _ in range(n + 1)] for _ in range(m + 1) ]

        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
            
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])

        return dp[m][n]

print(Solution().minDistance(word1 = "horse", word2 = "ros"))
print(Solution().minDistance(word1 = "intention", word2 = "execution"))