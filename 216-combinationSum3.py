from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = {1,2,3,4,5,6,7,8,9}
        ans = set()

        def combSum(k1: int, n1: int, numsLeft: set, comb: List[int]) -> None:
            if k1 == 0 or n1 <= 0 or not numsLeft:
                return
            
            if k1 == 1 and n1 in numsLeft:
                ans.add(tuple(sorted(comb + [n1])))
                return
            else:
                for num in numsLeft:
                    combSum(k1 - 1, n1 - num, numsLeft-{num}, comb + [num])

        combSum(k, n, nums, [])

        return [list(x) for x in ans]
    
print(Solution().combinationSum3(k = 3, n = 7))
print(Solution().combinationSum3(k = 3, n = 9))
print(Solution().combinationSum3(k = 4, n = 1))