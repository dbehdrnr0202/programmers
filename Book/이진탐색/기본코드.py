def sequential_search(n, target, array):
    for i in range(n):
        if array[i]==target:
            return i+1
    return -1

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n, target = map(int, input().split())
array = list(map(int, input().split()))

ans = binary_search(array, target, 0, n-1)

if ans==None:
    print("None")
else:
    print(ans)


'''
10 7
1 3 5 7 9 11 13 15 17 19
3
'''