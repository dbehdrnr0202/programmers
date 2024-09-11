from heapq import heappush, heappop

class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    # union by size
    def find_size(self, a):
        parent = self.data[a]
        if parent < 0:
            return a
        return self.find_size(parent)
    def union_size(self, a, b):
        a, b = self.find_size(a), self.find_size(b)
        if a == b:
            return
        if self.data[a] < self.data[b]:
            self.data[a] += self.data[b]
            self.data[b] = a
        else:
            self.data[b] += self.data[a]
            self.data[a] = b
        self.size -= 1
    # union by rank
    def find_rank(self, idx):
        parent = self.data[idx]
        if parent < 0:
            return idx
        return self.find_rank(parent)
    def union_rank(self, x, y):
        x, y = self.find_rank(x), self.find_rank(y)
        if x == y:
            return
        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
        self.size -= 1
        
def check_disjoint(n, roads, destination):
    a = DisjointSet(n+1)
    for road in roads:
        a.union_rank(road[0], road[1])
    connected_dst = []
    dst_rank = a.find_rank(destination)
    for idx in range(1, n+1):
        finded_rank = a.find_rank(idx)
        if finded_rank==dst_rank:
            connected_dst.append(idx)
    return set(connected_dst)
    
def dijkstra(n, roads, sources, destination, connected_points):
    answer = []
    edges = [[] for _ in range(n+1)]
    nodes = [False for _ in range(n+1)]
    dists = [-1 for _ in range(n+1)]
    for road in roads:
        if road[0] in connected_points or road[1] in connected_points:
            edges[road[0]].append(road[1])
            edges[road[1]].append(road[0])
    queue = []
    heappush(queue, (0, destination))
    while queue:
        dist, cur_node = heappop(queue)
        if nodes[cur_node]==True:
            continue
        nodes[cur_node] = True
        dists[cur_node] = dist
        for next_node in edges[cur_node]:
            if not nodes[next_node]:
                heappush(queue, (dist+1, next_node))
    for source in sources:
        answer.append(dists[source])
    return answer

def solution(n, roads, sources, destination):
    answer = []
    dst_connected_point = check_disjoint(n, roads, destination)
    answer = dijkstra(n, roads, sources, destination, dst_connected_point)
    return answer