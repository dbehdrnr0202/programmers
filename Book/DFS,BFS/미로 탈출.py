from collections import deque

def my_solution():
    n, m = map(int, input().split())
    board = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int, input())))

    def bfs(cur_x, cur_y):
        dq = deque()
        dq.appendleft((cur_x, cur_y, 1))
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        while dq:
            cur_x, cur_y, cur_dist = dq.popleft()
            if cur_y == n-1 and cur_x==m-1:
                return cur_dist
            if board[cur_y][cur_x]==0:
                continue
            board[cur_y][cur_x] = 1
            visited[cur_y][cur_x] = True
            for next_dir in range(4):
                next_x, next_y = cur_x+dx[next_dir], cur_y+dy[next_dir]
                if 0<=next_y<n and 0<=next_x<m and board[next_y][next_x]==1 and not visited[next_y][next_x]:
                    dq.append((next_x, next_y, cur_dist+1))
        return None
    ans = bfs(0, 0)
    return ans

print(my_solution())


'''
5 6
101010
111111
000001
111111
111111

'''