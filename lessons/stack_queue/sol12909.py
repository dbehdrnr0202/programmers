def solution(braket_str):
    answer = True
    s = []

    for braket in braket_str:
        if len(s)==0:
            if braket==')':
                return False
        else:
            if s[-1]=='(' and braket==')':
                s.pop(-1)
        if braket=='(':
            s.append('(')
    if len(s)!=0:
        return False
    return True