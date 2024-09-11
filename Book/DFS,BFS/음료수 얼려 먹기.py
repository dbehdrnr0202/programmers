from collections import deque

def my_solution():
    '''
    ### using deque
    '''
    n, m = map(int, input().split())

    board = []
    for _ in range(n):
        board.append(list(map(int, input())))

    ans = 0

    def bfs(cur_x, cur_y):
        dq = deque()
        dq.appendleft((cur_x, cur_y))
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        while dq:
            cur_x, cur_y = dq.popleft()
            if board[cur_y][cur_x]==1:
                continue
            board[cur_y][cur_x] = 1
            for next_dir in range(4):
                next_x, next_y = cur_x+dx[next_dir], cur_y+dy[next_dir]
                if 0<=next_y<n and 0<=next_x<m and board[next_y][next_x]==0:
                    dq.append((next_x, next_y))

    for cur_y in range(n):
        for cur_x in range(m):
            if board[cur_y][cur_x]==0:
                bfs(cur_x, cur_y)
                ans+=1
    return ans

def my_solution():
    '''
    ### using recursive
    '''
    n, m = map(int, input().split())

    board = []
    for _ in range(n):
        board.append(list(map(int, input())))

    def dfs(cur_x, cur_y):
        if 0<=cur_x<m and 0<=cur_y<n:    
            if board[cur_y][cur_x] == 0:
                board[cur_y][cur_x] = 1
                dfs(cur_x-1, cur_y)
                dfs(cur_x, cur_y-1)
                dfs(cur_x+1, cur_y)
                dfs(cur_x, cur_y+1)
                return True
        return False
    ans = 0
    for y in range(n):
        for x in range(m):
            if dfs(x, y):
                ans+=1
    return ans


print(my_solution())