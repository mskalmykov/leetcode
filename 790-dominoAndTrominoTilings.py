class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        
        base = [0] * (n + 1)
        ext = [0] * (n + 1)

        base[1], base[2] = 1, 2
        ext[1],  ext[2]  = 1, 2

        for i in range(3, n+1):
            base[i] = (base[i-1] + base[i-2] + 2*ext[i-2]) % 1_000_000_007
            ext[i] = (base[i-1] + ext[i-1]) % 1_000_000_007

        return base[n]

for n in range(1, 10):
    print(Solution().numTilings(n))

