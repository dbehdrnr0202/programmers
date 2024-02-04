from collections import defaultdict
from itertools import combinations

def solution(weights):
    answer = 0
    # counter를 써도된다
    weight_dict = defaultdict(int)
    for weight in weights:
        weight_dict[weight]+=1
    muls = [(2,3),(1,2),
            (3,2),(3,4),
            (2,1),(4,3)]
    weight_values = weight_dict.keys()
    for weight_key in weight_values:
        if weight_dict[weight_key]>1:
            answer+=(weight_dict[weight_key]-1)*weight_dict[weight_key]//2
    for weight_value1, weight_value2 in combinations(weight_values, 2):
        for mul in muls:
            if mul[0]*weight_value1==mul[1]*weight_value2:
                answer+=weight_dict[weight_value1]*weight_dict[weight_value2]
    return answer