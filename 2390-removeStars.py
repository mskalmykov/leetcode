class Solution:
    def removeStars(self, s: str) -> str:
        resultChars = []

        for c in s:
            if c == '*':
                resultChars.pop()
            else:
                resultChars.append(c)

        return ''.join(resultChars)

print(Solution().removeStars('leet**cod*e'))
print(Solution().removeStars('erase*****'))
