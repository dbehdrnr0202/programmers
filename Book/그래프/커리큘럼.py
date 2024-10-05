from collections import deque
import copy

def solution():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    times = [0]*(n+1)
    for idx in range(1,n+1):
        temp_arr = list(map(int, input().split()))[:]
        times[idx] = temp_arr[0]
        precourses = temp_arr[1:-1]
        indegree[idx]+=len(precourses)
        for precourse in precourses:
            graph[precourse].append(idx)
    result = [0]*(n+1)
    q = deque()
    for idx in range(1, n+1):
        if indegree[idx]==0:
            q.append(idx)
    result = copy.deepcopy(times)
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            indegree[next_node]-=1
            result[next_node] = max(result[cur_node]+times[next_node], result[next_node])
            if indegree[next_node]==0:
                q.append(next_node)
    return result[1:]
print(solution())


'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

10
20
14
18
17
'''