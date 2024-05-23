class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        result = []
        idx = 1
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for w in words:
            if w[0].lower() in vowels:
                result.append(w + 'ma' + 'a'*idx)
            else:
                result.append(w[1:] + w[0] + 'ma' + 'a'*idx)
            idx += 1
        
        return ' '.join(result)

print(Solution().toGoatLatin("I speak Goat Latin"))
print(Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))