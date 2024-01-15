def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    maxCandies = candies[0]
    result = [False] * len(candies)

    for c in candies[1:]:
        if c > maxCandies:
            maxCandies = c

    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            result[i] = True

    return result

candies = [12,1,12]
extraCandies = 10

print(kidsWithCandies(candies, extraCandies))