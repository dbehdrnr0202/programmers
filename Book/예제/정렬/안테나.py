def my_solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mid = arr[(n-1)//2]
    print(mid)

my_solution()

'''
4
5 1 7 9
'''