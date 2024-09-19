from collections import deque

N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
dists = [-1]*(N+1)
dists[X] = 0

queue = deque([X])
while queue:
    cur_point = queue.popleft()
    for next_point in edges[cur_point]:
        if dists[next_point]==-1:
            dists[next_point] = dists[cur_point]+1
            queue.append(next_point)
check = False
for i in range(1, N+1):
    if dists[i]==K:
        print(i)
        check = True
if check==False:
    print(-1)
'''
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1 
1 2
1 3
2 3
2 4

'''