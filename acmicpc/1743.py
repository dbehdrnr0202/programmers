from collections import deque
import heapq

def solution():
    '''
    ### 음식물 피하기
    https://www.acmicpc.net/problem/1743

    코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 
    이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 
    통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 
    선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.
    '''
    result = []
    n, m, k = map(int, input().split())
    board = [[0]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        r, c = map(int, input().split())
        board[r][c] = 1
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[False]*(m+1) for _ in range(n+1)]
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
                if 0<next_x<=m and 0<next_y<=n and visited[next_y][next_x]==False and board[next_y][next_x]==1:
                    q.append((next_x, next_y))
        heapq.heappush(result, -size)
    for y in range(1, n+1):
        for x in range(1, m+1):
            if board[y][x] and visited[y][x]==False:
                dfs(board, x, y)
    print(-heapq.heappop(result))

solution()