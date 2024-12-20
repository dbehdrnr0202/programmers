def solution():
    '''
    ### 신나는 함수 실행
    https://www.acmicpc.net/problem/9184

    재귀 호출만 생각하면 신이 난다! 아닌가요?
    다음과 같은 재귀함수 w(a, b, c)가 있다.
    if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
        1
    if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
        w(20, 20, 20)
    if a < b and b < c, then w(a, b, c) returns:
        w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    otherwise it returns:
        w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
    a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
    '''
    while True:
        a, b, c = map(int, input().split())
        if a==b==c==-1:
            break
        result = 0
        dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
        def w(a, b, c):
            if a <= 0 or b <= 0 or c <= 0:
                return 1
            if a > 20 or b > 20 or c > 20:
                return w(20, 20, 20)
            if dp[a][b][c]:
                return dp[a][b][c]
            if a < b and b < c:
                dp[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
                return dp[a][b][c]
            else:
                dp[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
                return dp[a][b][c]
        result = w(a, b, c)
        print(f"w({a}, {b}, {c}) = {result}")

solution()