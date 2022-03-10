# 올바른 괄호 : 스택
# 스택 구현 도중 계산 필요.

brack = input()
stack = []

def solution():
    for char in brack:
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ')':
            temp = 0
            while len(stack) > 0 and type(stack[-1]) is int:
                temp += stack[-1]
                stack.pop()
            if len(stack) > 0 and stack[-1] == '(':
                temp *= 2
                if temp == 0:
                    temp = 2
                stack.pop()
                stack.append(temp)
            else:
                return 0
        elif char == ']':
            temp = 0
            while len(stack) > 0 and type(stack[-1]) is int:
                temp += stack[-1]
                stack.pop()
            if len(stack) > 0 and stack[-1] == '[':
                temp *= 3
                if temp == 0:
                    temp = 3
                stack.pop()
                stack.append(temp)
            else:
                return 0
    res = 0
    for integer in stack:
        if type(integer) is not int:
            return 0
        res += integer
    return res

print(solution())
