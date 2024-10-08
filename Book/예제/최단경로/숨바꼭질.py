import heapq

INF = int(1e9)

def solution():
    result = [0, 0, 0]
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dists = [INF] *(n+1)
    
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        dists[cur_node] = min(dists[cur_node], cur_dist)
        for next_node in graph[cur_node]:
            next_dist = cur_dist+1
            if dists[next_node]>next_dist:
                heapq.heappush(q, (next_dist, next_node))
    max_dist = 0
    cnt = 0
    for idx in range(n, 0, -1):
        if max_dist==dists[idx]:
            result = [idx, dists[idx]]
            cnt+=1
        elif max_dist<dists[idx]:
            max_dist = dists[idx]
            result = [idx, dists[idx]]
            cnt=1
    result.append(cnt)
    return result

solution()

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

4 2 3
'''