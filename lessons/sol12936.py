from math import factorial
def solution(n, k):
    answer = []
    k-=1
    left_numbers = list(range(n))
    while left_numbers:
        before_factoial = factorial(len(left_numbers)-1)
        target_index = k//before_factoial
        k-=before_factoial*target_index
        answer.append(left_numbers.pop(target_index)+1)
    return answer