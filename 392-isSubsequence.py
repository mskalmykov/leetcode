class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idxT = idxS = 0

        while idxT < len(t) and idxS < len(s):
            if t[idxT] == s[idxS]:
                idxS += 1
            idxT += 1

        return idxS == len(s)
    
print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))
print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))