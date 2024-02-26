from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [ 0 for _ in range(len(temperatures))]
        stack = deque()

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[0]] < val:
                a_idx = stack.popleft()
                answer[a_idx] = idx - a_idx
            stack.appendleft(idx)

        return answer

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))
