def maxProfit(prices: list[int]) -> int:
    profit = 0

    prev = prices[0]
    bought = False

    for p in prices[1:]:
        if p < prev:
            if bought:
                profit += prev - buy
                bought = False
        elif p > prev:
            if not bought:
                buy = prev
                bought = True
        prev = p
    
    if bought:
        profit += prev - buy

    return profit


arr = [7,1,5,3,6,4]
print(arr, '->', maxProfit(arr))
arr = [1,2,3,4,5]
print(arr, '->', maxProfit(arr))
arr = [7,6,4,3,1]
print(arr, '->', maxProfit(arr))

