from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums) - 2):
            n1 = nums[i]
            if n1 > 0: break

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == -n1:
                    ans.add((n1, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    continue
                if s < -n1:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in ans]

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
print(Solution().threeSum(nums = [0,1,1]))
print(Solution().threeSum([0,0,0]))
