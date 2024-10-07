INF = int(1e9)

def solution():
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(c, graph[a][b])
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                graph[s][e] = min(graph[s][e], graph[s][m]+graph[m][e])
    for s in range(1, n+1):
        for e in range(1, n+1):
            print(graph[s][e], end=' ') if graph[s][e]<INF else print(0, end=' ')
        print()

solution()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''