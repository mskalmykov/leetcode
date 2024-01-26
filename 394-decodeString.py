class Solution:
    def decodeString(self, s: str) -> str:
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        curNum = ''
        arr = ['']

        for c in s:
            if c in nums:
                curNum += c
            elif c == '[':
                arr.append(curNum)
                arr.append('')
                curNum = ''
            elif c == ']':
                tmp = arr.pop() * int(arr.pop())
                arr[-1] += tmp
            else:
                arr[-1] += c

        return ''.join(arr)

print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))