from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 0
    min_value = r1**2
    max_value = r2**2
    for x in range(1, r2+1):
        min_count = 0
        max_count = 0
    
        min_y = min_value-x**2
        max_y = max_value-x**2
        if min_y>=0:
            min_count = ceil(sqrt(min_y))
        max_count = floor(sqrt(max_y))
        answer+=(max_count-min_count+1)
    return answer*4