def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    zeroCount = 1
    freePlaces = 0

    for c in flowerbed:
        if c == 1:
            zeroCount = 0
        else:
            zeroCount += 1
            if zeroCount > 2:
                zeroCount = 1
                freePlaces += 1
                if freePlaces >= n:
                    return True
                
    if zeroCount == 2:
        freePlaces += 1

    return freePlaces >= n

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1], 1))