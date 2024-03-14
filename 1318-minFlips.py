class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        abxc = (a | b) ^ c
        ab = a & b

        return abxc.bit_count() + (ab & abxc).bit_count()


print(Solution().minFlips(a = 2, b = 6, c = 5))
print(Solution().minFlips(a = 4, b = 2, c = 7))
print(Solution().minFlips(a = 1, b = 2, c = 3))
