def my_solution():
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 1
    for val in arr:
        if ans < val:
            break
        ans+=val
    return ans

print(my_solution())

'''
5
3 2 1 1 9
8
'''