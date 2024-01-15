def rotate(nums: list, k: int) -> None:
    l = len(nums)
    k = k % l
    
    if k == 0 or l == 1:
        return
    
    s = 0
    i = 0
    buf = nums[0]

    for _ in range(l):
        i = i + k
        if i >= l:
            i = i - l

        buf,nums[i] = nums[i],buf

        if i == s:
            i += 1
            s += 1
            buf = nums[i]


#arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
#k = 20
#arr = [0,1,2,3]
#k = 2
arr = [0,1,2,3,4,5]
k = 3
print(arr, k)
rotate(arr, k)
print(arr)