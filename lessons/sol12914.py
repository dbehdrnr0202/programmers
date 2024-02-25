def solution(n):
    dp = [0 for _ in range(1, n+4)]
    for number in range(n+1):
        if number==0:
            dp[number]=1
        dp[number+1]+=dp[number]
        dp[number+2]+=dp[number]
    return dp[n]%1234567