INF = int(1e9)

def solution():
    n, m = map(int, input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for s in range(1, n+1):
        for e in range(1, n+1):
            if s==e:
                graph[s][e] = 0

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s][e] = 1
        graph[e][s] = 1
    x, k = map(int, input().split())

    for k in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                graph[s][e] = min(graph[s][e], graph[s][k]+graph[k][e])
    dist = graph[1][k]+graph[k][x]

    print("-1") if dist>=INF else print(dist)

solution()
'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

//3

4 2
1 3
2 4
3 4

//-1
'''