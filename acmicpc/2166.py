def solution():
    '''
    ### 다각형의 면적
    https://www.acmicpc.net/problem/2166

    문제
    2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

    출력
    첫째 줄에 면적을 출력한다. 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.
    '''

    def shoelace_formula(points):
        n = len(points)
        area = 0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area += (x1 * y2) - (x2 * y1)
        return abs(area) / 2

    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    area = shoelace_formula(points)
    print(f"{area:.1f}")

solution()

'''
input
4
0 0
0 10
10 10
10 0

output
100.0
'''