def init_board():
    board = [[0 for _ in range(22)] for _ in range(22)]    
    return board

def solution(dirs):
    answer = 0
    dir_x, dir_y = [0, 0, -1, 1], [-1, 1, 0, 0]
    board = init_board()
    cur_x, cur_y = 10, 10
    
    board[cur_y][cur_x] = True
    
    for dir in dirs:
        dir_idx = 0
        if dir=='U':
            dir_idx = 0
        elif dir=='D':
            dir_idx = 1
        elif dir=='L':
            dir_idx = 2
        elif dir=='R':
            dir_idx = 3
        next_x, next_y = cur_x+2*dir_x[dir_idx], cur_y+2*dir_y[dir_idx]
        if 0<=next_x<22 and 0<=next_y<22:
            if board[cur_y+dir_y[dir_idx]][cur_x+dir_x[dir_idx]]==0:
                answer+=1
                board[cur_y+dir_y[dir_idx]][cur_x+dir_x[dir_idx]]=1
            cur_x, cur_y = next_x, next_y
    return answer