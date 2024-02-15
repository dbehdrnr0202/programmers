def bfs(x, y, maps):
    queue =[(x, y, 1)]
    target_x, target_y = len(maps[0])-1, len(maps)-1
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while queue:
        cur_x, cur_y, cur_count = queue.pop(0)
        if cur_x==target_x and cur_y==target_y:
            return cur_count
        if visited[cur_y][cur_x]:
            continue
        visited[cur_y][cur_x]= True
        for i in range(4):
            next_x, next_y = cur_x+dir_x[i], cur_y+dir_y[i]
            if 0<=next_x<len(maps[0]) and 0<=next_y<len(maps) and not visited[next_y][next_x] and maps[next_y][next_x]==1:
                queue.append((next_x, next_y, cur_count+1))
    return -1
def solution(maps):
    answer = 0
    answer = bfs(0, 0, maps)
    return answer
maps =[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
print(solution(maps))