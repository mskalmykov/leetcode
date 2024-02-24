from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in range(k):
            heapq.heappush(h, nums[i])

        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i])

        return heapq.heappop(h)


print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
