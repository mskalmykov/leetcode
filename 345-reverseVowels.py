def reverseVowels(s: str) -> str:
    vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
    arr = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] not in vowels:
            i += 1
            continue
        if s[j] not in vowels:
            j -= 1
            continue
        if i != j:
            arr[i] = s[j]
            arr[j] = s[i]
            i += 1
            j -= 1

    return ''.join(arr)

s = 'hello'
print(s, '->', reverseVowels(s))
s = 'leetcode'
print(s, '->', reverseVowels(s))