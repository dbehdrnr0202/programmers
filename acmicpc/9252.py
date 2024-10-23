def solution():
    '''
    ### LCS 2
    https://www.acmicpc.net/problem/9252

    문제
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

    입력
    첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

    출력
    첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.
    LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
    '''
    arr1 = list(input())
    arr2 = list(input())
    dp = [[(0, "")] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
    for i in range(1, len(arr1)+1):
        for j in range(1, len(arr2)+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = (dp[i-1][j-1][0] + 1, dp[i-1][j-1][1]+arr1[i-1])
            else:
                if dp[i-1][j][0]>dp[i][j-1][0]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    print(dp[-1][-1][0])
    if dp[-1][-1][0]:
        print(dp[-1][-1][1])

solution()