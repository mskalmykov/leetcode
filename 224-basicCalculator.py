class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        isNegative = False
        stack = []

        numStr = ''

        for c in s + ' ':
            if c.isdigit():
                numStr += c
            elif c in '+- ()':
                if numStr:
                    result = result - int(numStr) if isNegative else result + int(numStr)
                    numStr = ''
                    isNegative = (c == '-')
                elif c == '-':
                    isNegative = True
                if c == '(':
                    stack.append((result, isNegative))
                    result = 0
                    isNegative = False
                elif c == ')':
                    braceResult = result
                    result, isNegative = stack.pop()
                    result = result - braceResult if isNegative else result + braceResult
                    isNegative = False

        return result

print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 2-1 + 2 "))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("(7)-(0)+(4)"))