from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        wDict = Counter(words)
        wordsCount = len(words)
        wordLen = len(words[0])
        substrLen = wordLen * wordsCount
        sLen = len(s)

        for i in range(wordLen):
            if i + substrLen > sLen:
                break

            curDict = Counter()

            for j in range(wordsCount):
                word = s[i + j*wordLen : i + (j+1)*wordLen]
                curDict[word] += 1
            
            if curDict == wDict:
                result.append(i)
            
            for j in range(i + wordLen, sLen - substrLen + 1, wordLen):
                prevWord = s[j-wordLen:j]
                nextWord = s[j + substrLen - wordLen: j + substrLen]
                curDict[prevWord] -= 1
                curDict[nextWord] += 1
                if nextWord not in wDict:
                    continue
                if curDict == wDict:
                    result.append(j)

        return result

print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(Solution().findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
print(Solution().findSubstring(s = "lingmindraboofooowingdingbarrwingmonkeypoundcake", words = ["fooo","barr","wing","ding","wing"]))
