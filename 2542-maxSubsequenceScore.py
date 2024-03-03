from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)
        ans = 0

        pq = [n[1] for n in nums[:k]]
        n1sum = sum(pq)
        heapq.heapify(pq)

        ans = n1sum * nums[k-1][0]

        for i in range(k, len(nums1)):
            n1sum += nums[i][1] - heapq.heapreplace(pq, nums[i][1])

            ans = max(ans, n1sum * nums[i][0])

        return ans
    
print(Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
print(Solution().maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))
print(Solution().maxScore(nums1 = [22,5,25,15,28,1], nums2 = [22,30,25,25,9,18], k = 3))
print(Solution().maxScore(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3))
