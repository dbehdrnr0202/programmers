def find_parent(parent, x):
    if parent[x]!=x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    n, m = map(int, input().split())

    parent = [0]*(n+1)
    edges = []

    for i in range(1, n+1):
        parent[i] = i

    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    
    edges.sort()
    maximum_cost = 0
    result = 0
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a)!=find_parent(parent, b):
            union_parent(parent, a, b)
            maximum_cost = max(maximum_cost, cost)
            result+=cost
    result-=(maximum_cost)
    return result

print(solution())

'''


'''