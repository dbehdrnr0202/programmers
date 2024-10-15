def solution():
    '''
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
    '''
    arr1 = list(input())
    arr2 = list(input())
    dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
    for i in range(1, len(arr1)+1):
        for j in range(1, len(arr2)+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])

solution()