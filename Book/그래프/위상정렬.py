from collections import deque

v,e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = []
    q = deque()
    
    for node in range(1, v+1):
        if indegree[node]==0:
            q.append(node)
    
    while q:
        cur = q.popleft()
        result.append(cur)
        for next_node in graph[cur]:
            indegree[next_node]-=1
            if indegree[next_node]==0:
                q.append(next_node)
    
    for node in result:
        print(node, end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

1 2 5 3 6 4 7
'''