from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        l = 0
        r = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[r] > 1:
                if l == r:
                    result.append(str(nums[l]))
                else:
                    result.append(f'{nums[l]}->{nums[r]}')
                l = i
                r = i
            else:
                r += 1
        if l == r:
            result.append(str(nums[l]))
        else:
            result.append(f'{nums[l]}->{nums[r]}')

        return result

print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))

