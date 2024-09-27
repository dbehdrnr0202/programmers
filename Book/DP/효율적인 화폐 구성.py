INF = 10000001

def solution():
    n, m = map(int, input().split())
    lst = []
    arr = [INF] * 100001
    for _ in range(n):
        money = int(input())
        lst.append(money)
        arr[money] = 1
    for idx in range(1, m+1):
        for money in lst:
            arr[idx] = min(arr[idx-money]+1, arr[idx]) if (idx - money >= 0) and (arr[idx-money]!=INF) else arr[idx]
    
    return -1 if arr[m]==INF else arr[m]

print(solution())

'''
CASE#1
2 15
2
3

5
CASE#2
3 4
3
5
7

-1
'''