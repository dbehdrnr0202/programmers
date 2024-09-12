from collections import defaultdict

def my_solution():
    n, m = map(int, input().split())
    number_dict = defaultdict(int)
    lst = list(map(int, input().split()))
    for val in lst:
        number_dict[val]+=1
    total_sum = len(lst)
    ans = 0
    for key, val in number_dict.items():
        ans+=number_dict[key] * (total_sum - number_dict[key])
    return ans//2

print(my_solution())


'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''