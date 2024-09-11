def my_solution():
    n, k = map(int, input().split())

    lst1 = sorted(list(map(int, input().split())))
    lst2 = sorted(list(map(int, input().split())), reverse=True)

    for idx in range(k):
        lst1[idx] = max(lst1[idx], lst2[idx])

    return sum(lst1)

print(my_solution())

'''
5 3
1 2 5 4 3
5 5 6 6 5

26
'''