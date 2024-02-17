from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
            
        return [list(n1-n2), list(n2-n1)]
    
print(Solution().findDifference([1,2,3], [2,4,6]))
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))