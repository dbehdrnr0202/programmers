def solution(queue1, queue2):
    answer = float('INF')
    queue = queue1+queue2+queue1+queue2
    target = int((sum(queue1)+sum(queue2))/2)
    start_point, end_point = 0, 0
    # 여기서 무엇을 해야할까
    # 그냥 two point를 사용해서 
    start_point, end_point = 0, len(queue1)-1
    init_start_point, init_end_point = start_point, end_point
    cur_sum = sum(queue1)
    answer = []
    while end_point<len(queue) and start_point<=end_point:
        if cur_sum==target:
            answer.append((start_point-init_start_point, end_point-init_end_point))
            end_point+=1
            if end_point>=len(queue):
                break
            cur_sum+=queue[end_point]
        elif cur_sum<target:
            end_point+=1
            if end_point>=len(queue):
                break
            cur_sum+=queue[end_point]
        elif cur_sum>=target:
            cur_sum-=queue[start_point]
            start_point+=1
    answer.sort(key=lambda x:(x[0]+x[1]))
    if answer==[]:
        return -1
    return sum(answer[0])