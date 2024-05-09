class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            s = 0
            digits = str(n)
            for c in digits:
                s += int(c) * int(c)
            if s in seen:
                break
            seen.add(s)
            n = s
        
        return n == 1

print(Solution().isHappy(19))
print(Solution().isHappy(2))
