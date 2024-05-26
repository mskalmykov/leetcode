class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)

        c = ''
        ov = 0

        for i in range(max(la,lb)):
            x = 0 if i >= la else int(a[-1 - i])
            y = 0 if i >= lb else int(b[-1 - i])
            digit = ov + x + y
            if digit < 2:
                c = str(digit) + c
                ov = 0
            else:
                c = str(digit - 2) + c
                ov = 1

        if ov == 1:
            c = '1' + c

        return c

print(Solution().addBinary(a = "11", b = "1"))
print(Solution().addBinary(a = "1010", b = "1011"))
