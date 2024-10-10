def solution():
    n, m = map(int, input().split())
    edges = []
    result = 0
    total = 0
    parent = list(range(n+1))
    
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

    for _ in range(m):
        x, y, z = map(int, input().split())
        total+=z
        edges.append((z,x,y))

    edges.sort()
    
    for edge in edges:
        cost, cur_node_1, cur_node_2 = edge
        if find_parent(cur_node_1)!=find_parent(cur_node_2):
            union(cur_node_1, cur_node_2)
            result+=cost
    return total-result
print(solution())

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

51

0,3,2,4,5,1,6

15 23 32 43 54

0 1 7
4 5 8
1 2 8
1 3 9
5 6 11
3 4 15


'''