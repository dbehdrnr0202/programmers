def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    def search(arr, left, right):
        if left>right:
            return None
        mid = (left+right)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid]<mid:
            return search(arr, mid+1, right)
        else:
            return search(arr, left, mid-1)
    index = search(arr, 0, n-1)
    print(-1 if index==None else index)

solution()

'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''