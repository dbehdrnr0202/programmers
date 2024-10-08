INF = int(1e9)
def solution():
    n, m = map(int, input().split())
    parent = list(range(n+1))
    def find_parent(a):
        if parent[a]==a:
            return a
        return find_parent(parent[a])
    
    def union(a, b):
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        parent[a], parent[b] = min(parent_a, parent_b), min(parent_a, parent_b)

    graph = [[0] for _ in range(n+1)]
    for idx in range(1, n+1):
        arr = list(map(int, input().split()))
        graph[idx]+=arr
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]==1:
                union(i, j)
    travels = list(map(int, input().split()))
    travel_set = set()
    for travel in travels:
        travel_set.add(find_parent(travel))
    print("YES") if len(travel_set) else print("NO")
solution()

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

YES
'''