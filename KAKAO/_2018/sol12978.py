import heapq
def dijkstra(start, adj, N, K):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    hp = []
    heapq.heappush(hp, [0, start])
    while hp:
        cur_cost, start_node = heapq.heappop(hp)
        for next_node, cost in adj[start_node]:
            if cur_cost+cost < dist[next_node]:
                dist[next_node] = cur_cost+cost
                heapq.heappush(hp,[cur_cost+cost, next_node])
    return len([i for i in dist if i<=K])
def solution(N, roads, K):
    adj = [[] for _ in range(N+1)]
    for a, b, cost in roads:
        adj[a].append((b, cost))
        adj[b].append((a, cost))
    return dijkstra(1, adj, N, K)