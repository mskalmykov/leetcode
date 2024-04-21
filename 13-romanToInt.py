class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        prev = ''

        for c in s:
            match c:
                case 'M':
                    if prev == 'C':
                        ans += 800
                    else:
                        ans += 1000
                case 'D':
                    if prev == 'C':
                        ans += 300
                    else:
                        ans += 500
                case 'C':
                    if prev == 'X':
                        ans += 80
                    else:
                        ans += 100
                case 'L':
                    if prev == 'X':
                        ans += 30
                    else:
                        ans += 50
                case 'X':
                    if prev == 'I':
                        ans += 8
                    else:
                        ans += 10
                case 'V':
                    if prev == 'I':
                        ans += 3
                    else:
                        ans += 5
                case 'I':
                    ans += 1
            prev = c

        return ans

print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
