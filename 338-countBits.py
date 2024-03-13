from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        bits = [0] * 17
        bitCount = 0

        for i in range(n):
            overflow = 1
            j = 0
            while overflow == 1 and j < 17:
                if bits[j] == 0:
                    bits[j] = 1
                    overflow = 0
                    bitCount += 1
                else:
                    bits[j] = 0
                    bitCount -= 1
                j += 1
            result.append(bitCount)

        return result

print(Solution().countBits(2))
print(Solution().countBits(5))
