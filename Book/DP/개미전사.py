def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    m = [0] * 1001
    for idx in range(len(arr)):
        if idx==0 or idx==1:
            m[idx] = arr[idx]
        else:
            m[idx] = max(m[idx-2]+arr[idx], m[idx-1])
    return m[n-1]

print(solution())

'''
4
1 3 1 5
'''