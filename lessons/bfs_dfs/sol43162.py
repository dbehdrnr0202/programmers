from collections import deque

global visited

def bfs(start, edge):
    global visited
    cur_i = start
    q = deque()
    q.append(cur_i)
    while q:
        cur_i = q.popleft()
        visited[cur_i] = True
        for next_i in range(len(edge[cur_i])):
            if cur_i==next_i:
                continue
            if edge[cur_i][next_i]==1 and not visited[next_i]:
                q.append(next_i)
    return

def solution(n, computers):
    answer = 0
    global visited
    visited = [False for _ in range(n)]
    for start in range(n):
        if not visited[start]:
            bfs(start, computers)
            answer+=1
    return answer