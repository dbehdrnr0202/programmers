import heapq
INF = int(1e9)

def solution():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        board = [[] *(n) for _ in range(n)]
        dists = [[INF]*n for _ in range(n)]
        for i in range(n):
            board[i] = list(map(int, input().split()))
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        def shortest_path(board):
            result = 0
            q = []
            heapq.heappush(q, (0, 0, 0))
            while q:
                cur_dist, cur_x, cur_y = heapq.heappop(q)
                if cur_x==n-1 and cur_y==n-1:
                    return cur_dist+board[cur_y][cur_x]
                dists[cur_y][cur_x] = cur_dist
                for idx in range(4):
                    next_x, next_y = cur_x+dx[idx], cur_y+dy[idx]
                    next_dist = cur_dist+board[cur_y][cur_x]
                    if 0<=next_x<n and 0<=next_y<n and next_dist<dists[next_y][next_x]:
                        heapq.heappush(q, (next_dist, next_x, next_y))
        result = shortest_path(board)
        results.append(result)
    for result in results:
        print(result)

solution()

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 8 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

20
19
36
'''