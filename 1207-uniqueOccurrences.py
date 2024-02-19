from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for n in arr:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        return len(counts) == len(set(counts.values()))
    
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
