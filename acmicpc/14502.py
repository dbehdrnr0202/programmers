from itertools import combinations
from collections import deque
import copy

def solution():
    '''
    ### 연구소
    https://www.acmicpc.net/problem/14502

    문제
    크기가 NxM인 연구소가 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 연구소의 일부 칸은 바이러스가 존재한다. 
    바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며 꼭 3개를 세워야 한다.
    바이러스가 퍼질 수 없는 곳을 안전 영역이라고 했을 때, 안전 영역의 최대 크기를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
    둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.

    출력
    첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
    '''
    # 입력 받기
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def spread_virus(temp_lab):
        queue = deque()
        for i in range(N):
            for j in range(M):
                if temp_lab[i][j] == 2:
                    queue.append((i, j))

        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and temp_lab[ny][nx] == 0:
                    temp_lab[ny][nx] = 2
                    queue.append((ny, nx))

    def calculate_safe_area(temp_lab):
        return sum(row.count(0) for row in temp_lab)

    def make_wall_and_simulate():
        global result
        empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
        max_safe_area = 0

        for walls in combinations(empty_spaces, 3):
            temp_lab = copy.deepcopy(lab)
            for y, x in walls:
                temp_lab[y][x] = 1

            spread_virus(temp_lab)
            max_safe_area = max(max_safe_area, calculate_safe_area(temp_lab))

        return max_safe_area

    result = make_wall_and_simulate()
    print(result)

solution()