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

    for i in range(1, n+1):
        parent[i] = i
    results=[]
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op==0:
            union_parent(parent, a, b)
        else:
            check = find_parent(parent, a)==find_parent(parent, b)
            results.append('YES') if check else results.append("NO")
    for result in results:
        print(result)
solution()

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

NO
NO
YES
'''