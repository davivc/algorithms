def solution(S):
    my_stack = []

    for i in S:
        if (len(my_stack) > 0 and
            ((i == ")" and my_stack[-1] == "(") or
            (i == "]" and my_stack[-1] == "[") or
            (i == "}" and my_stack[-1] == "{"))):
            my_stack.pop()
        else:
            my_stack.append(i)

    if len(my_stack) == 0:
        return 1
    else:
        return 0