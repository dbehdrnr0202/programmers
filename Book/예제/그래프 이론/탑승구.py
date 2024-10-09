def solution():
    G = int(input())
    P = int(input())
    parent = list(range(G+1))
    
    def find_parent(a):
        if parent[a]==a:
            return a
        return find_parent(parent[a])
    
    def union(a, b):
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        parent[a], parent[b] = min(parent_a, parent_b), min(parent_a, parent_b)

    result = 0
    planes = []
    for _ in range(P):
        planes.append(int(input()))
    for plane in planes:
        data = find_parent(plane)
        if data==0:
            break
        union(data, data-1)
        result+=1
    print(result)

solution()

'''
4
3
4
1
1

#2

4
6
2
2
3
3
4
4

#3
'''