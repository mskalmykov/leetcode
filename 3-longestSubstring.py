class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        chars = set()

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1

        return longest

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
        