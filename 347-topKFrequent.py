def topKFrequent(nums: list[int], k: int) -> list[int]:
    freqs = {}

    for n in nums:
        freqs[n] = freqs.get(n,1) + 1

    invFreqs = {}

    for n, f in freqs.items():
        if f in invFreqs:
            invFreqs[f].append(n)
        else:
            invFreqs[f] = [n]
    
    result = []
    for f in sorted(invFreqs.keys(), reverse=True):
        if len(result) >= k:
            break
        result += invFreqs[f]

    return result

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1,2], 2))
