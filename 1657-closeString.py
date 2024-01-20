class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = {}
        freq2 = {}

        for c in word1:
            freq1[c] = freq1.get(c, 0) + 1
        for c in word2:
            freq2[c] = freq2.get(c, 0) + 1

        if sorted(freq1.keys()) != sorted(freq2.keys()):
            return False
        
        return sorted(freq1.values()) == sorted(freq2.values())
    
print(Solution().closeStrings("abc", "bca"))
print(Solution().closeStrings("a", "aa"))
print(Solution().closeStrings("cabbba", "abbccc"))
print(Solution().closeStrings("uau", "ssx"))
