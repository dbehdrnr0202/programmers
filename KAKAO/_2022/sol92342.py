import itertools

def cmp(a, b):
    return a[::-1] > b[::-1]

def get_max_score(left_arrow:int, apeach_info:list):
    win_plan = [-1]*12
    score_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for lion_record in itertools.combinations_with_replacement(score_index, left_arrow):
        # lion의 기록 : lion_record
        lion_info = [0 for i in range(12)]
        lion_score = 0
        for record in lion_record:
            lion_info[record]+=1
        if lion_info==[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]:
            print("here")
        for i in range(11):
            if lion_info[i] > apeach_info[i]:
                lion_score+=(10-i)
            elif apeach_info[i]!=0:
                lion_score-=(10-i)
        if lion_score<=0:
            continue
        lion_info[11]=lion_score
        if (cmp(lion_info, win_plan)):
            win_plan = lion_info[:]

    if win_plan[0]==-1:
        return [-1]
    return win_plan[:-1]

def solution(n, info):
    answer = get_max_score(n, info)
    return answer