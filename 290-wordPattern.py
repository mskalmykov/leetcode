class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = {}
        w = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in l and words[i] not in w:
                l[pattern[i]] = words[i]
                w[words[i]] = pattern[i]
            elif pattern[i] in l and words[i] in w:
                if l[pattern[i]] != words[i]:
                    return False
                if w[words[i]] != pattern[i]:
                    return False
            else:
                return False

        return True

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
