class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        nums = []
        
        n = 1
        s = x
        while s != 0:
            n = s % 10
            s = s // 10
            nums.append(n)

        for i in range(len(nums) // 2 + 1):
            if nums[i] != nums[-1-i]:
                return False
        
        return True

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
