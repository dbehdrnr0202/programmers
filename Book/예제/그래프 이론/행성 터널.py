def solution():
    n = int(input())
    parent = list(range(n+1))
    result = 0

    def find_parent(a):
        if parent[a]==a:
            return a
        return find_parent(parent[a])
    
    def union(a, b) :
        a = find_parent(a)
        b = find_parent(b)
        if a < b :
            parent[b] = a
        else :
            parent[a] = b

    x = []
    y = []
    z = []
    edges =[]

    for idx in range(n):
        coord = list(map(int, input().split()))
        x.append((coord[0], idx))
        y.append((coord[1], idx))
        z.append((coord[2], idx))
    
    x.sort()
    y.sort()
    z.sort()

    for idx in range(n-1):
        edges.append((x[idx+1][0]-x[idx][0], x[idx+1][1], x[idx][1]))
        edges.append((y[idx+1][0]-y[idx][0], y[idx+1][1], y[idx][1]))
        edges.append((z[idx+1][0]-z[idx][0], z[idx+1][1], z[idx][1]))
    edges.sort()
    for edge in edges:
        length, a, b = edge
        if find_parent(a)!=find_parent(b):
            union(a, b)
            result+=length
    print(result)

solution()