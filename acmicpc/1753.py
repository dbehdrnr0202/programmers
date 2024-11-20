import sys
import heapq

INF = float('inf')

def dijkstra(start, V, adj):
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        current_distance, current = heapq.heappop(pq)
        if dist[current] < current_distance:
            continue

        for next, weight in adj[current]:
            next_distance = current_distance + weight
            if next_distance < dist[next]:
                dist[next] = next_distance
                heapq.heappush(pq, (next_distance, next))
    return dist


if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())

    adj = [[] for _ in range(V + 1)]

    for i in range(2, 2 + E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    dist = dijkstra(K, V, adj)

    for i in range(1, V + 1):
        print(dist[i] if dist[i] != INF else "INF")
