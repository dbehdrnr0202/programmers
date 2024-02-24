def solution(str):
    stack = []
    for chr in str:
        if stack and stack[-1]==chr:
            stack.pop(-1)
        else:
            stack.append(chr)
    if stack:
        return 0
    return 1