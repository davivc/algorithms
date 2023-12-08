# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    brackets = list(S)
    stack = []

    if len(brackets) == 0:
        return 1

    for b in brackets:
        if len(stack) > 0 and stack[-1] == "(" and b == ")":
            stack.pop()
        else:
            stack.append(b)

    if len(stack) == 0:
        return 1
    return 0