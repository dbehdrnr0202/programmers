def solution(order):
    answer = 0
    stack = []
    cur = 1
    for box in order:
        flag = False
        if stack:
            if stack[-1]==box:
                answer+=1
                stack.pop(-1)
                continue
            flag = True
        while cur<box:
            stack.append(cur)
            cur+=1
        if cur==box:
            answer+=1
            cur+=1
            continue
        if flag:
            return answer
    return answer