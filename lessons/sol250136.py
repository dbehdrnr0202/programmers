from collections import deque

def bfs(land, x, y, visited):
    q = deque()
    q.append((x, y))
    dir_x, dir_y = [1, -1, 0, 0], [0, 0, 1, -1]
    oil_count = 0
    while q:
        cur_x, cur_y = q.popleft()
        if not visited[cur_y][cur_y]:
            visited[cur_y][cur_y] = True
            oil_count+=1
            for dir in range(4):
                next_x, next_y = cur_x+dir_x[dir], cur_y+dir_y[dir]
                if 0<=next_x <len(land[0]) and 0<=next_y<len(land) and land[next_y][next_x]==1:
                    q.append((next_x, next_y))
    return oil_count
def solution(land):
    answer = 0
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    for y in range(len(land)):
        for x, value in enumerate(land[y]):
            if value==1:
                print(x, y, bfs(land, x, y, visited))
    return answer

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	
print(solution(land))