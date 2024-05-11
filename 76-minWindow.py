from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen, tLen = len(s), len(t)
        if sLen < tLen:
            return ''
        
        result = ''
        tDict = Counter(t)
        sDict = Counter(s[0:tLen])

        if sDict == tDict:
            return s[0:tLen]
        
        l = 0
        minLen = sLen + 1

        for r in range(tLen, sLen):
            sDict[s[r]] += 1
            if tDict <= sDict:
                while True:
                    if r - l + 1 == tLen:
                        return s[l:r+1]
                    if r - l + 1 < minLen:
                        minLen = r - l + 1
                        result = s[l:r+1]
                    c = s[l]
                    sDict[c] -= 1
                    l += 1
                    if c in tDict and sDict[c] < tDict[c]:
                        break

        return result

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution().minWindow(s = "a", t = "a"))
print(Solution().minWindow(s = "a", t = "aa"))
print(Solution().minWindow(s = "bba", t = "ab"))
