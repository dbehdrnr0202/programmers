import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF]*(n+1)

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for (next, cost) in graph[start]:
        distance[next] = cost
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for (next, next_cost) in graph[now]:
            cost = distance[now] + next_cost
            if cost<distance[next]:
                distance[next] = cost

import heapq

def adjusted_dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if distance[cur_node] < cur_cost:
            continue
        for next_node, next_cost in graph[cur_node]:
            cost = cur_cost+next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

# dijkstra(start)

adjusted_dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])


'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

'''