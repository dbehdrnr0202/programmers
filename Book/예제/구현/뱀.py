from collections import deque
EMPTY = 0
SNAKE = 1
APPLE = 2

def my_solution():
    cur_time = 0
    n = int(input())
    board = [[0] * (n + 1) for _ in range(n+1)]
    k = int(input())
    for _ in range(k):
        apple_y, apple_x = map(int, input().split())
        board[apple_y][apple_x] = APPLE
    l = int(input())
    moves = deque()
    for _ in range(l):
        second, direction = input().split()
        moves.append((int(second), direction))
    dq = deque()
    dq.append((1, 1))
    board[1][1] = SNAKE
    cur_dir = 1
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    while moves:
        next_move_time, next_dir = moves.popleft()
        while cur_time<next_move_time:
            cur_head_x, cur_head_y = dq[0]
            next_head_x, next_head_y = cur_head_x+dx[cur_dir], cur_head_y+dy[cur_dir]
            cur_time+=1
            if next_head_x<=0 or next_head_x>n or next_head_y <= 0 or next_head_y>n or board[next_head_y][next_head_x]==SNAKE:
                return cur_time if not (0<next_head_x<=n and 0<next_head_y<=n) else cur_time
            if board[next_head_y][next_head_x]==APPLE:
                dq.appendleft((next_head_x, next_head_y))
            if board[next_head_y][next_head_x]==EMPTY:
                dq.appendleft((next_head_x, next_head_y))
                cur_tail_x, cur_tail_y = dq.pop()
                board[cur_tail_y][cur_tail_x] = EMPTY
            board[next_head_y][next_head_x] = SNAKE
        cur_dir = (cur_dir+1)%4 if next_dir=='D' else (cur_dir-1)%4
    while True:
        cur_head_x, cur_head_y = dq[0]
        next_head_x, next_head_y = cur_head_x+dx[cur_dir], cur_head_y+dy[cur_dir]
        cur_time+=1
        if next_head_x<=0 or next_head_x>n or next_head_y <= 0 or next_head_y>n or board[next_head_y][next_head_x]==SNAKE:
            return cur_time
        if board[next_head_y][next_head_x]==APPLE:
            dq.appendleft((next_head_x, next_head_y))
        if board[next_head_y][next_head_x]==EMPTY:
            dq.appendleft((next_head_x, next_head_y))
            cur_tail_x, cur_tail_y = dq.pop()
            board[cur_tail_y][cur_tail_x] = EMPTY
        board[next_head_y][next_head_x] = SNAKE
print(my_solution())

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

'''