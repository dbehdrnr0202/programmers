global visited

def bfs(start_point, maps):
    global visited
    answer = 0
    size_x, size_y = len(maps[0]), len(maps)
    dir_x, dir_y = [0, 0, 1, -1], [1, -1, 0, 0]
    q = []
    q.append(start_point)
    while q:
        cur_x, cur_y = q.pop(0)
        if visited[cur_y][cur_x]:
            continue
        visited[cur_y][cur_x] = True
        answer+=int(maps[cur_y][cur_x])
        for dir_index in range(4):
            next_x = cur_x+dir_x[dir_index]
            next_y = cur_y+dir_y[dir_index]
            if 0<=next_x<size_x and 0<=next_y<size_y and maps[next_y][next_x]!='X' and not visited[next_y][next_x]:
                q.append([next_x, next_y])
    return answer

def solution(maps):
    answer = []
    global visited
    size_x, size_y = len(maps[0]), len(maps)
    visited = [[False for _ in range(size_x)] for _ in range(size_y)]
    for y, row in enumerate(maps):
        for x, item in enumerate(row):
            if item!='X' and not visited[y][x]:
                answer.append(bfs([x, y], maps))
    answer.sort()
    if answer==[]:
        answer.append(-1)
    return answer

maps = ["X591X","X1X5X","X231X", "1XXX1"]	
print(solution(maps))