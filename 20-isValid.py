def isValid(s: str) -> bool:
    brackets = { '(': ')', '[': ']', '{': '}' }
    brStack = []

    for c in s:
        if c in brackets:
            brStack.append(c)
        else:
            if len(brStack) == 0:
                return False
            if c != brackets[brStack.pop()]:
                return False

    return len(brStack) == 0

s = '['
print(s)
print(isValid(s))
