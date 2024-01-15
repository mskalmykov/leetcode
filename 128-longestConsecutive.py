def longestConsecutive(nums: list[int]) -> int:
    maxLen = 0

    numSet = set(nums)

    for n in nums:
        if n-1 in numSet:
            continue

        t = n
        while t in numSet:
            t += 1

        maxLen = max(maxLen, t - n)

    return maxLen


arr = [0,3,7,2,5,8,4,6,0,1]
print(arr)
print(longestConsecutive(arr))
