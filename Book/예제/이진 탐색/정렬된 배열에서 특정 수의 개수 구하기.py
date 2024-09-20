def solution():
    ans = 0
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    def left_search(arr, target, left, right):
        if left>right:
            return None
        mid = (left+right)//2
        if (mid==0 or target>arr[mid-1]) and arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return left_search(arr, target, mid+1, right)
        else:
            return left_search(arr, target, left, mid-1)
            
    def right_search(arr, target, left, right):
        if left>right:
            return None
        mid = (left+right)//2
        if (mid==(n-1) or target<arr[mid+1]) and arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return right_search(arr, target, left, mid-1)
        else:
            return right_search(arr, target, mid+1, right)

    left_index = left_search(arr, x, 0, n-1)
    if left_index==None:
        return -1
    right_index = right_search(arr, x, 0, n-1)
    return right_index - left_index + 1

print(solution())

'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''