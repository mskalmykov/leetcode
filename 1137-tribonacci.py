class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return [0,1,1][n]

        a, b, c = 0, 1, 1

        for i in range(3, n + 1):
            t = a + b + c
            a, b, c = b, c, t
        
        return t


print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
