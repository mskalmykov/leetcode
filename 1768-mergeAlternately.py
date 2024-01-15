def mergeAlternately(word1: str, word2: str) -> str:
    result = ''
    len1 = len(word1)
    len2 = len(word2)

    for i in range(min(len1, len2)):
        result += word1[i]
        result += word2[i]

    if len1 > len2:
        result += word1[len2:]
    elif len2 > len1:
        result += word2[len1:]
    
    return result

word1 = "abc"
word2 = "pqr"
print(word1)
print(word2)
print(mergeAlternately(word1, word2))
