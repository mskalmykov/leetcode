def gcdOfStrings(str1: str, str2: str) -> str:
    prefix = ''
    l1 = len(str1)
    l2 = len(str2)
    
    for i in range(min(l1, l2)):
        if str1[i] == str2[i]:
            prefix += str1[i]

    prefixLen = len(prefix)

    while prefixLen > 0:
        if (l1 % prefixLen == 0) and (l2 % prefixLen == 0):
            if str1 == prefix[:prefixLen] * (l1 // prefixLen) and \
               str2 == prefix[:prefixLen] * (l2 // prefixLen):
                break
        prefixLen -= 1

    return prefix[:prefixLen]

str1 = 'ABCABC'
str2 = 'ABC'
print(str1, str2, gcdOfStrings(str1, str2))

str1 = 'ABABAB'
str2 = 'ABAB'
print(str1, str2, gcdOfStrings(str1, str2))

str1 = 'LEET'
str2 = 'CODE'
print(str1, str2, gcdOfStrings(str1, str2))