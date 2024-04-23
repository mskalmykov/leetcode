class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        lH, lN = len(haystack), len(needle)

        for i in range(lH - lN + 1):
            if haystack[i:i+lN] == needle:
                return i
            
        return -1

print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
print(Solution().strStr(haystack = "leetcode", needle = "leeto"))