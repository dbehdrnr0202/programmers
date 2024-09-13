from heapq import heappush, heappop

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    hq = []
    for idx, val in enumerate(food_times):
        heappush(hq, (val, idx+1))
    cur_time = 0
    prev_min = 0
    one_round_length = len(food_times)
    while cur_time+(hq[0][0]-prev_min)*one_round_length <= k:
        min_val, idx = heappop(hq)
        cur_time+=(min_val-prev_min)*one_round_length
        one_round_length-=1
        prev_min = min_val
    hq = sorted(hq, key=lambda x:x[1])
    answer = hq[(k-cur_time)%one_round_length][1]
    return answer