INF = int(1e9)

def solution():
    result = 0
    n, m = map(int, input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                graph[s][e] = min(graph[s][e], graph[s][m]+graph[m][e])
    print()
    for s in range(1, n+1):
        cnt = 0
        for e in range(1, n+1):
            if graph[s][e]>=INF and graph[e][s]>=INF:
                break
            cnt+=1
        if cnt==n:
            result+=1
    print(result)
    return result
solution()

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4

1
'''