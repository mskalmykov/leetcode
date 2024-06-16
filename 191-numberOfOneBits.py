class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0

        while n != 0:
            ones += n & 1
            n = n >> 1
            
        return ones

print(Solution().hammingWeight(11))
print(Solution().hammingWeight(128))
print(Solution().hammingWeight(2147483645))