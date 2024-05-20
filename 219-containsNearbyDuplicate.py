from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if i - k > 0:
                seen.remove(nums[i - k - 1])

            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False

print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
