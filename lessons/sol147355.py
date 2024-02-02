def solution(t, p):
    answer = 0
    len_p = len(p)
    p = int(p)
    if len_p==1:
        for c_i, c in enumerate(t):
            if p>=int(c):
                answer+=1
        return answer
    for c_i, c in enumerate(t[:-len_p+1]):
        if p >= int(t[c_i:c_i+len_p]):
            answer+=1
    return answer