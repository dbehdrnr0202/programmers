def solution():
    '''
    ### 합분해
    https://www.acmicpc.net/problem/2225

    0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
    덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.
    '''
    n, k = map(int, input().split())
    dp = [[1]*(n+1) for _ in range(k+1)]
    dp[1] = [1]*(n+1)
    for k_idx in range(2, k+1):
        for n_idx in range(1, n+1):
            dp[k_idx][n_idx] = (dp[k_idx][n_idx-1]+dp[k_idx-1][n_idx])%1000000000
    print(dp[k][n])
solution()