import heapq

INF = int(1e9)

def solution():
    n, m, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance= [INF] * (n+1)
    
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
    
    def dijkstra(start):
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

    dijkstra(1)

    total_city, total_time = 0, 0
    for i in range(2, n+1):
        if distance[i]==INF:
            continue
        total_city+=1
        total_time=max(distance[i], total_time)
    print(total_city, total_time)

solution()

'''
3 2 1
1 2 4
1 3 2

//2 4
'''