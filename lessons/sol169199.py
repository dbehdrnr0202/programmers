from collections import deque

global visited


def is_in(cur_x, cur_y):
    global visited
    if cur_x>=0 and cur_y>=0 and cur_x<len(visited[0]) and cur_y<len(visited):
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
        if is_in(next_x, next_y) and not visited[next_y][next_x]:
            next_poses.append((next_x, next_y))
    return next_poses

def bfs(start_x, start_y, end_x, end_y, board):
    global visited
    minimum_dist = -1
    q = deque()
    q.append((start_x, start_y, 0))
    while q:
        cur_x, cur_y, cur_count = q.popleft()
        if cur_x==end_x and cur_y==end_y:
            minimum_dist = cur_count
            break
        if visited[cur_y][cur_x]:
            continue
        visited[cur_y][cur_x] = True
        next_poses = get_next(cur_x, cur_y, board)
        for next_pos in next_poses:
            next_x, next_y = next_pos
            next_count = cur_count+1
            if not visited[next_y][next_x]:
                q.append((next_x, next_y, next_count))
    return minimum_dist

def solution(board):
    global visited
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start_x = j
                start_y = i
            elif board[i][j]=='G':
                end_x = j
                end_y = i
            if start_x!=-1 and end_x!=-1:
                break
    answer = bfs(start_x, start_y, end_x, end_y , board)
    return answer