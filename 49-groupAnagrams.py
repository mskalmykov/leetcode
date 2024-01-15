def groupAnagrams(strs: list) -> list[list]:
    result = {}
    startIdx = ord('a')

    for s in strs:
        chrCount = [0]*26
        for c in s:
            chrCount[ord(c) - startIdx] += 1
        
        strKey = tuple(chrCount)

        if strKey in result:
            result[strKey].append(s)
        else:
            result[strKey] = [s]

    return list(result.values())

for strs in [["eat","tea","tan","ate","nat","bat"], [""], ["a"]] :
    print(strs)
    print(groupAnagrams(strs))