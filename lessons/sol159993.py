def bfs(start_point, end_point, maps):
    answer = 0
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    size_x = len(maps[0])
    size_y = len(maps)
    end_x, end_y = end_point
    visited = [[False for _ in range(size_x)] for _ in range(size_y)]
    queue = []
    start_point.append(0)
    queue.append(start_point)
    while queue:
        cur_x, cur_y, cur_count = queue.pop(0)
        if cur_x==end_x and cur_y==end_y:
            return cur_count
        if visited[cur_y][cur_x]:
            continue
        visited[cur_y][cur_x] = True
        if cur_count>=size_x*size_y:
            return False
        for dir_index in range(4):
            next_x = cur_x+dir_x[dir_index]
            next_y = cur_y+dir_y[dir_index]
            if 0<=next_x<size_x and 0<=next_y<size_y and not visited[next_y][next_x] and maps[next_y][next_x]!='X':
                queue.append([next_x, next_y, cur_count+1])
    return False

def solution(maps):
    answer = 0
    start_point = [0, 0]
    end_point = [0, 0]
    mid_point = [0, 0]
    # Find Pos of Start Point(start_point:"S"), Lever Point(mid_point:"L"), End Point(end_point:"E")
    for row_index, row in enumerate(maps):
        for col_index, item in enumerate(row):
            if item=="S":
                start_point = [col_index, row_index]
            if item=="L":
                mid_point = [col_index, row_index]
            if item=="E":
                end_point = [col_index, row_index]
    # Find Lever
    rtn = bfs(start_point, mid_point, maps)
    if rtn ==False:
        return -1
    answer+=rtn
    # Find End Point
    rtn = bfs(mid_point, end_point, maps)
    if rtn==False:
        return -1
    answer+=rtn
    return answer