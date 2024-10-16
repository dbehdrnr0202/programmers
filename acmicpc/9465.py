def solution():
    '''
    ### 스티커 
    https://www.acmicpc.net/problem/9465

    상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
    상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
    모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다. 먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.
    위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다. 가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.
    '''
    T = int(input())
    for _ in range(T):
        n = int(input())
        scores_1 = list(map(int, input().split()))
        scores_2 = list(map(int, input().split()))
        
        scores_1 = [0]+scores_1
        scores_2 = [0]+scores_2

        if n==1:
            print(max(scores_1[1], scores_2[1]))
            continue
        dp = [[0] * (n+1) for _ in range(3)]
        
        dp[1][1] = scores_1[1]
        dp[2][1] = scores_2[1]

        dp[1][2] = scores_1[2]+scores_2[1]
        dp[2][2] = scores_1[1]+scores_2[2]

        for idx in range(3, n+1):
            dp[1][idx] = scores_1[idx]+max(dp[2][idx-1], dp[2][idx-2])
            dp[2][idx] = scores_2[idx]+max(dp[1][idx-2], dp[1][idx-1])
        print(max(dp[1][n], dp[2][n]))
solution()