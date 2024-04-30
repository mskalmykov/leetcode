class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tr1, tr2 = {}, {}

        for i in range(len(s)):
            if s[i] not in tr1 and t[i] not in tr2:
                tr1[s[i]] = t[i]
                tr2[t[i]] = s[i]
            else:
                if tr1.get(s[i], 'XX') != t[i] or tr2.get(t[i], 'XX') != s[i]:
                    return False
                
        return True

print(Solution().isIsomorphic(s = "egg", t = "add"))
print(Solution().isIsomorphic(s = "foo", t = "bar"))
print(Solution().isIsomorphic(s = "paper", t = "title"))
print(Solution().isIsomorphic(s = "badc", t = "baba"))

