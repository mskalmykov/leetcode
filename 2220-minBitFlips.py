class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal

        return bin(x).count('1')

print(Solution().minBitFlips(10, 7))
print(Solution().minBitFlips(3, 4))
