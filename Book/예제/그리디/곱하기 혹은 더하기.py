def my_solution():
    arr = list(map(int, input()))
    ans = arr[0]
    for val in arr[1:]:
        ans = max(ans*val, ans+val)
    return ans
print(my_solution())

'''
02984

576

567

210
'''