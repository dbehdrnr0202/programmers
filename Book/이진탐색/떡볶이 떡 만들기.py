def solution():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    start, end = 0, max(arr)
    ans = 0
    while start<=end:
        mid = (start+end)//2
        total_tteok = 0
        for val in arr:
            if val > mid:
                total_tteok+=(val-mid)
        if total_tteok<M:
            end = mid - 1
        else:
            ans = mid
            start = mid+1
    return ans

print(solution())

'''
4 6
19 15 10 17

15
'''