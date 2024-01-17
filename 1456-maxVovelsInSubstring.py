class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        curVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        left = right = 0
        while right < k:
            if s[right] in vowels:
                curVowels += 1
            right += 1
        
        result = curVowels

        while right < len(s):
            if s[right] in vowels:
                curVowels += 1
            if s[left] in vowels:
                curVowels -= 1
            
            result = max(result, curVowels)
            
            right += 1
            left += 1

        return result
    
s = "abciiidef"
k = 3
print(f'"{s}", {k} -> {Solution().maxVowels(s, k)}')
s = "aeiou"
k = 2
print(f'"{s}", {k} -> {Solution().maxVowels(s, k)}')
s = "leetcode"
k = 3
print(f'"{s}", {k} -> {Solution().maxVowels(s, k)}')
