from collections import deque

global visited, size_x, size_y

def is_in(cur_x, cur_y):
    global size_x, size_y
    if cur_x>=0 and cur_y>=0 and cur_x<size_x and cur_y<size_y:
        return True
    return False

def get_next(cur_x, cur_y, board)->list:
    global visited
    next_poses = []
    dir_x = [0, 0, -1, 1]
    dir_y = [-1, 1, 0, 0]
    # 상
    for index in range(4):
        next_x = cur_x+dir_x[index]
        next_y = cur_y+dir_y[index]
        if not is_in(next_x, next_y):
            continue
        while board[next_y][next_x]!='D':
            next_x = next_x+dir_x[index]
            next_y = next_y+dir_y[index]
            if not is_in(next_x, next_y):
                break
        next_x = next_x-dir_x[index]
        next_y = next_y-dir_y[index]
        if is_in(next_x, next_y) and (next_x, next_y) not in visited:
            next_poses.append((next_x, next_y))
    return next_poses

def bfs(start_x, start_y, end_x, end_y, board):
    global visited
    global size_x, size_y
    size_x = len(board[0])
    size_y = len(board)
    minimum_dist = -1
    q = deque()
    q.append((start_x, start_y, 0))
    while q:
        cur_x, cur_y, cur_count = q.popleft()
        if cur_x==end_x and cur_y==end_y:
            minimum_dist = cur_count
            break
        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))
        next_poses = get_next(cur_x, cur_y, board)
        for next_pos in next_poses:
            next_x, next_y = next_pos
            next_count = cur_count+1
            if (next_x, next_y) not in visited:
                q.append((next_x, next_y, next_count))
    return minimum_dist

def solution(board):
    global visited
    visited = set()
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    # enumerate 로 탐색하는 방법 생각하기
    for y, board_line in enumerate(board):
        for x, value in enumerate(board_line):
            if value=='R':
                start_x = x
                start_y = y
            if value=='G':
                end_x = x
                end_y = y
    answer = bfs(start_x, start_y, end_x, end_y , board)
    return answer