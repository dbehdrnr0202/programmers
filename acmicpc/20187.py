def solution():
    '''
    ### 종이 접기
    https://www.acmicpc.net/problem/20187

    문제
    정사각형의 종이를 중앙선을 중심으로 접는 방법은 아래 그림에서 보인 것처럼 4가지가 있다.
    - D: 가로 중심선을 중심으로 반으로 접되 윗 면이 아랫 면을 덮도록 접음
    - U: 가로 중심선을 중심으로 반으로 접되 아랫 면이 윗 면을 덮도록 접음
    - R: 세로 중심선을 중심으로 반으로 접되 왼쪽 면이 오른쪽 면을 덮도록 접음
    - L: 세로 중심선을 중심으로 반으로 접되 오른쪽 면이 왼쪽 면을 덮도록 접음

    한 변의 길이가 2k인 정사각형 종이가 있을 때, 이를 세로로 k번, 가로로 k번 접으면 (접는 순서는 상관 없음) 각 변의 길이가 1인 정사각형이 된다. 아래 그림에서 보인 것처럼 각 변의 길이가 1인 정사각형의 네 귀퉁이 중 한 군데에 구멍을 낸다. 구멍의 위치는 그림에서 보인 것처럼 숫자로 표시한다.
    구멍을 낸 후 접은 순서의 역순으로 종이를 펼치면, 종이에 2^2k개의 구멍이 있게 된다. 예를 들어, 한 변의 길이가 4(= 22)인 정사각형을 <R, D, D, R>순서대로 접은 후, 3번 위치에 구멍을 낸 다음 종이를 펼치면 아래 그림처럼 구멍이 나게 된다.
    종이의 크기를 나타내는 정수 k, 종이를 접는 순서를 나타내는 정보, 구멍 뚫는 위치를 나타내는 정수가 주어질 때, 2k × 2k 격자에 뚫린 구멍의 위치를 출력하는 프로그램을 작성하시오.

    입력
    첫 번째 줄에 k가 주어진다.
    다음 줄에는 종이 접는 방법을 나타내는 문자가 2k개 주어지는데, 각 문자는 공백으로 구분된다. 종이를 접는 방법 D, U, R, L은 각각 해당하는 대문자 알파벳으로 주어진다.
    다음 줄에는 구멍 뚫는 위치를 나타내는 정수 h(0 ≤ h ≤ 3) 가 주어진다.

    출력
    접힌 종이를 접은 순서의 역순으로 펼친 후 정사각형에 뚫린 구멍의 위치를 번호로 출력한다. 출력은 총 2k줄로 이루어지며 i (1 ≤ i ≤ 2k)번째 줄에는 격자의 i번 행에 뚫린 구멍의 번호를 왼쪽에서 오른쪽 순서로, 공백을 사이에 두고 출력한다.
    '''
    k = int(input())
    foldings = list(input().split())
    h = int(input())
    paper = [[0]*(2**k) for _ in range(2**k)]
    
    df ={
        'D' : [2, 3, 0, 1],
        'U' : [2, 3, 0, 1],
        'R' : [1, 0, 3, 2],
        'L' : [1, 0, 3, 2]
    }

    def solve(i, j, sy, sx, ey, ex):
        if i == k and j == k:
            paper[sy][sx] = h
            return

        f = foldings[i + j]

        if f == 'U':
            ey = (sy + ey) // 2
            solve(i + 1, j, sy, sx, ey, ex)

            for y in range(2 ** (k - i - 1)):
                for x in range(sx, ex):
                    paper[ey + y][x] = df[f][paper[ey - y - 1][x]]

        elif f == 'D':
            sy = (sy + ey) // 2
            solve(i + 1, j, sy, sx, ey, ex)

            for y in range(2 ** (k - i - 1)):
                for x in range(sx, ex):
                    paper[sy - y - 1][x] = df[f][paper[sy + y][x]]

        elif f == 'L':
            ex = (sx + ex) // 2
            solve(i, j + 1, sy, sx, ey, ex)

            for y in range(sy, ey):
                for x in range(2 ** (k - j - 1)):
                    paper[y][ex + x] = df[f][paper[y][ex - x - 1]]
        else:
            sx = (sx + ex) // 2
            solve(i, j + 1, sy, sx, ey, ex)

            for y in range(sy, ey):
                for x in range(2 ** (k - j - 1)):
                    paper[y][sx - x - 1] = df[f][paper[y][sx + x]]

    solve(0, 0, 0, 0, 2**k, 2**k)

    for row in paper:
        print(*row)

solution()
'''
input 
2
R D D R
3

output
0 1 0 1
2 3 2 3
0 1 0 1
2 3 2 3
'''