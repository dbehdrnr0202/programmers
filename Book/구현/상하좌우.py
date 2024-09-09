def my_solution():
    n = int(input())
    data = input().split()

    dir = {"L":0, "R":1, "U":2, "D":3}
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    cur_x, cur_y = 1, 1
    for next_dir in data:
        next_dx, next_dy = dx[dir[next_dir]], dy[dir[next_dir]]
        next_x, next_y = cur_x+next_dx, cur_y+next_dy
        if 1<=next_x<=n and 1<=next_y<=n:
            cur_x, cur_y = next_x, next_y

    return cur_x, cur_y

def solution():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan==move_types[i]:
                nx = x+dx[i]
                ny = y+dy[i]
        if nx < 1 or ny < 1 or nx>n or ny>n:
            continue
        x, y = nx, ny
    return x, y

print(my_solution())