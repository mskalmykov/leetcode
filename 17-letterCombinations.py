from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ltrs = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        q = deque()

        for d in digits:
            if not q:
                for c in ltrs[int(d) - 2]:
                    q.appendleft(c)
                continue
            for i in range(len(q)):
                s = q.pop()
                for c in ltrs[int(d) - 2]:
                    q.appendleft(s + c)

        return list(q)
    
print(Solution().letterCombinations('23'))
print(Solution().letterCombinations(''))
print(Solution().letterCombinations('2'))