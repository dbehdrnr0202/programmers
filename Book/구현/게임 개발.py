def my_solution():
    n, m = map(int, input().split())
    cur_x, cur_y, cur_dir = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    board = []
    
    dx, dy = [-1, 0,  1, 0], [0, 1, 0, -1]
    
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    def turn(cur_dir):
        cur_dir-=1
        if cur_dir== -1:
            cur_dir=3
        return cur_dir
    
    answer = 1
    turn_count = 0
    while True:
        cur_dir = turn(cur_dir)
        next_x, next_y = cur_x+dx[cur_dir], cur_y+dy[cur_dir]
        if not visited[next_x][next_y] and board[next_x][next_y]==0:
            board[next_x][next_y] = 1
            cur_x, cur_y = next_x, next_y
            answer +=1
            turn_count = 0
            continue
        else:
            turn_count+=1

        if turn_count==4:
            next_x, next_y = cur_x-dx[cur_dir], cur_y-dy[cur_dir]
            if board[next_x][next_y]==0:
                cur_x, cur_y = next_x, next_y
            else:
                break

            turn_count = 0

    return answer


print(my_solution())