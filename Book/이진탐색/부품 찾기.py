N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
to_find = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>=target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
    
for target in to_find:
    if binary_search(arr, target, 0, N-1)==None:
        print("no")
    else:
        print("yes")

'''
5
8 3 7 9 2
3
5 7 9
'''