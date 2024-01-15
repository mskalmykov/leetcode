def reverseWords(s: str) -> str:
    # simple solution
    #return ' '.join(reversed(s.split()))

    # in-place modification
    def reverse(arr: list[str], start: int, end: int) -> None:
        i, j = start, end

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    chars = list(s)
    reverse(chars, 0, len(chars) - 1)

    i = 0
    wordStart = -1
    
    while i < len(chars):
        if chars[i] != ' ':
            if wordStart < 0:
                wordStart = i
        else:
            if wordStart >= 0:
                reverse(chars, wordStart, i - 1)
                wordStart = -1
        i += 1

    if wordStart >= 0:
        reverse(chars, wordStart, i - 1)


    j = 0
    spaceOK = False
    for i in range(len(chars)):
        if chars[i] == ' ':
            if spaceOK:
                chars[j] = ' '
                j += 1
                spaceOK = False
        else:
            if i != j:
                chars[j] = chars[i]
            j += 1
            spaceOK = True
        i += 1

    if chars[j-1] == ' ':
        j -= 1

    return ''.join(chars[:j])

print(reverseWords('the sky is blue'))
print(reverseWords('  hello world  '))
print(reverseWords('a good   example'))
