from itertools import combinations
from collections import defaultdict
def solution(orders, courses):
    answer = []
    orders = [sorted(list(order)) for order in orders]
    comb_dict = defaultdict(dict)
    for course in courses:
        max_value = 0
        max_list = []
        for order in orders:
            for comb in combinations(order, course):
                comb = "".join(comb)
                if comb_dict[course].get(comb)==None:
                    comb_dict[course][comb]=0
                comb_dict[course][comb]+=1
                if comb_dict[course][comb]>max_value:
                    max_value = comb_dict[course][comb]
                    max_list = [comb]
                elif comb_dict[course][comb]==max_value:
                    max_list.append(comb)
        if max_value>1:
            answer+=max_list
    return sorted(answer)
orders = 	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
print(solution(orders, course))