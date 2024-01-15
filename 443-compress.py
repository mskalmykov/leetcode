def compress(chars: list[str]) -> int:
    if len(chars) == 1:
        return 1
    
    j = 1
    currChar = chars[0]
    charsCount = 1

    for i in range(1, len(chars)):
        if chars[i] == currChar:
            charsCount += 1
        else:
            if charsCount != 1:
                for c in str(charsCount):
                    chars[j] = c
                    j += 1
                charsCount = 1

            currChar = chars[i]
            chars[j] = currChar
            j += 1

    if charsCount != 1:
        for c in str(charsCount):
            chars[j] = c
            j += 1

    return j

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(chars)
print(compress(chars))
print(chars)