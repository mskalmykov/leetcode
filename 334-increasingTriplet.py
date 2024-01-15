def increasingTriplet(nums: list[int]) -> bool:
    numsLen = len(nums)
    i = 1
    l = nums[0]
    while i < numsLen and nums[i] <= l:
        l = nums[i]
        i += 1

    if i == numsLen:
        return False
    
    r = nums[i]
    i += 1

    while i < numsLen:
        if nums[i] > r:
            return True
        elif nums[i] < r and nums[i] > l:
            r = nums[i]
        elif nums[i] < l:
            l = nums[i]

        i += 1

    return False

nums = [1,2,3,4,5]
print(nums, increasingTriplet(nums))

nums = [5,4,3,2,1]
print(nums, increasingTriplet(nums))

nums = [2,1,5,0,4,6]
print(nums, increasingTriplet(nums))

nums = [1, 2, 0, 3, 2]
print(nums, increasingTriplet(nums))
