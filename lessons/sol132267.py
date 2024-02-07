def solution(cost, reward, having):
    answer = 0
    while having>=cost:
        answer+=(having//cost)*reward
        having=having%cost+having//cost*reward
    return answer