def moveZeroes(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != j:
                nums[j] = nums[i]
                nums[i] = 0
            j += 1


nums = [0,1,0,3,12]
print(nums)
moveZeroes(nums)
print(nums)

nums = [0]
print(nums)
moveZeroes(nums)
print(nums)