from collections import deque

def solution(x, y, n):
    queue = deque()
    counter = [0 for _ in range(1000001)]
    queue.append(x)
    counter[x] = 1
    while queue:
        cur_num = queue.popleft()
        if counter[cur_num]==0 and cur_num==y:
            continue
        if 0<=cur_num+n<=y  and counter[cur_num+n]==0:
            queue.append(cur_num+n)
            counter[cur_num+n] = counter[cur_num]+1
        if 0<=cur_num*2<=y  and counter[cur_num*2]==0:
            queue.append(cur_num*2)
            counter[cur_num*2] = counter[cur_num]+1
        if 0<=cur_num*3<=y  and counter[cur_num*3]==0:
            queue.append(cur_num*3)
            counter[cur_num*3] = counter[cur_num]+1
    if counter[y]==0:
        return -1
    return counter[y]-1