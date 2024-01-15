from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        extraCandies = 0
        upDown = 0
        seriesLen = 0
        prevSeriesLen = 0

        for i in range(1, len(ratings)):
            if ratings[i] == ratings[i-1]:
                if upDown == -1 and prevSeriesLen != 0:
                    extraCandies -= min(seriesLen, prevSeriesLen)
                upDown = 0
                seriesLen = 0
                prevSeriesLen = 0
            elif ratings[i] > ratings[i-1]:
                if upDown == 1:
                    seriesLen += 1
                elif upDown == -1:
                    if prevSeriesLen != 0:
                        extraCandies -= min(seriesLen, prevSeriesLen)
                        prevSeriesLen = 0
                    seriesLen = 1
                    upDown = 1
                else:
                    seriesLen = 1
                    upDown = 1
                extraCandies += seriesLen
            else:
                if upDown == -1:
                    seriesLen += 1
                elif upDown == 1:
                    prevSeriesLen = seriesLen
                    seriesLen = 1
                    upDown = -1
                else:
                    seriesLen = 1
                    upDown = -1
                extraCandies += seriesLen

        if prevSeriesLen != 0:
            extraCandies -= min(seriesLen, prevSeriesLen)

        return len(ratings) + extraCandies
    
ratings = [1,0,2]
print(ratings, Solution().candy(ratings))
ratings = [1,2,2]
print(ratings, Solution().candy(ratings))
ratings = [1,6,10,8,7,3,2]
print(ratings, Solution().candy(ratings))
ratings = [1,2,3,5,4,3,2,1,4,3,2,1]
print(ratings, Solution().candy(ratings))
