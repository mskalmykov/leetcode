from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = 0
        after = len(intervals)
        
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                before += 1
                continue
            elif newInterval[1] < intervals[i][0]:
                after = i
                break
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        return intervals[:before] + [newInterval] + intervals[after:]

print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(Solution().insert(intervals = [[1,5]], newInterval = [2,3]))
