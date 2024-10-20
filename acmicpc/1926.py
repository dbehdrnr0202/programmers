from collections import deque
import heapq

def solution():
    '''
    ### 그림
    https://www.acmicpc.net/problem/1926

    어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
    첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
    '''
    result = []
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[False]*(m) for _ in range(n)]
    def dfs(board, x, y):
        size = 0
        q = deque()
        q.append((x, y))
        while q:
            cur_x, cur_y = q.pop()
            if visited[cur_y][cur_x]:
                continue
            size+=1
            visited[cur_y][cur_x] = True
            for idx in range(4):
                next_x, next_y = cur_x+dx[idx], cur_y+dy[idx]
                if 0<=next_x<m and 0<=next_y<n and visited[next_y][next_x]==False and board[next_y][next_x]==1:
                    q.append((next_x, next_y))
        heapq.heappush(result, -size)
    for y in range(n):
        for x in range(m):
            if board[y][x] and visited[y][x]==False:
                dfs(board, x, y)
    print(len(result))
    print(-heapq.heappop(result)) if len(result) else print(0)
solution()