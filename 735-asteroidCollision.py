from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for n in asteroids:
            if (n > 0) or (not ans):
                ans.append(n)
            else:
                while ans:
                    if ans[-1] < 0:
                        break
                    elif ans[-1] > -n:
                        n = 0
                        break
                    elif ans[-1] == -n:
                        ans.pop()
                        n = 0
                        break
                    else:
                        ans.pop()
                if n != 0:
                    ans.append(n)

        return ans
    
print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([-2,-2,1,-2]))
