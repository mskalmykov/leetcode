from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if r == l:
            return 0

        while True:
            if r == l + 1:
                break
            
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid

        return r if nums[r] > nums[l] else l

print(Solution().findPeakElement([1,6,5,4,3,2,1]))
print(Solution().findPeakElement([2,1]))
print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
