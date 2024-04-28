class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        letters = dict()

        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        for c in ransomNote:
            if c in letters:
                if letters[c] == 1:
                    del letters[c]
                else:
                    letters[c] -= 1
            else:
                return False
            
        return True

print(Solution().canConstruct(ransomNote = "a", magazine = "b"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))
