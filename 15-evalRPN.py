def evalRPN(tokens: list[str]) -> int:
    opStack = []
    ops = {'+', '-', '*', '/'}

    for s in tokens:
        if s not in ops:
            opStack.append(int(s))
            continue
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()

        if s == '+':
            opStack.append(op1 + op2)
        elif s == '-':
            opStack.append(op1 - op2)
        elif s == '*':
            opStack.append(op1 * op2)
        elif s == '/':
            opStack.append(int(op1 / op2))

    return opStack.pop()


tokens = ["2","1","+","3","*"]
print(tokens, '->', evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(tokens, '->', evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(tokens, '->', evalRPN(tokens))
