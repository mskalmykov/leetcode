def productExceptSelf(nums: list[int]) -> list[int]:
    size = len(nums)
    result = [1] * size

    for i in range(1, size):
        result[i] = result[i-1] * nums[i-1]

    backProd = 1

    for i in range(size-1, -1, -1):
        result[i] = result[i] * backProd
        backProd = backProd * nums[i]

    return result

arr = [2, 0, 1]
print(arr)
print(productExceptSelf(arr))

arr = [1, 2, 3, 4]
print(arr)
print(productExceptSelf(arr))