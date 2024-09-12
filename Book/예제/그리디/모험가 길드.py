def my_solution():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    ans = 0
    group_sum = 0
    for value in arr:
        if group_sum+1>=value:
            ans+=1
            group_sum = 0
        else:
            group_sum+=1

    return ans

print(my_solution())