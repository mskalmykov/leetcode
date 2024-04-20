from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prfx = ''
        i = 0

        while i < len(strs[0]):
            cur_letter = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != cur_letter:
                    return prfx
            prfx += cur_letter
            i += 1

        return prfx

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
