def solution(n, moneys):
    dp = [0]*(n+1)
    for money in moneys:
        dp[money]+=1
        for y in range(money+1,n+1):
            dp[y]+=dp[y-money]
    return dp[n]