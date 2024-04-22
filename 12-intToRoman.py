class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        romChar = [['I','V','X'], ['X','L','C'], ['C','D','M'], ['M']]
        numStr = str(num)

        for i in range(len(numStr)):
            n = int(numStr[-1-i])
            if n < 4:
                ans = romChar[i][0] * n + ans
            elif n == 4:
                ans = romChar[i][0] + romChar[i][1] + ans
            elif n < 9:
                ans = romChar[i][1] + romChar[i][0] * (n - 5) + ans
            elif n == 9:
                ans = romChar[i][0] + romChar[i][2] + ans

        return ans

print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))