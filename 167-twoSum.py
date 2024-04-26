from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
            
        while l < r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1

        return [l + 1, r + 1]

print(Solution().twoSum(numbers = [3,24,50,79,88,150,345], target = 200))
print(Solution().twoSum(numbers = [2,7,11,15], target = 9))
print(Solution().twoSum(numbers = [2,3,4], target = 6))
print(Solution().twoSum(numbers = [-1,0], target = -1))
