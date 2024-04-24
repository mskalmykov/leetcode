class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = ''

        for j in range(numRows):
            i = j
            if j > 0 and j < numRows-1:
                k = 2 * (numRows - j - 1)
            else:
                k = 0
            while i < len(s):
                ans += s[i]
                if k > 0 and i + k < len(s):
                    ans += s[i + k]
                i += 2 * numRows - 2

        return ans

print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))
print(Solution().convert(s = "PAYPALISHIRING", numRows = 4))
print(Solution().convert(s = "A", numRows = 1))
