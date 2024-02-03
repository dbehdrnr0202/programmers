from math import sqrt
def solution(k, d):
    answer = 0
    for y in range(0, d+1, k):
        max_x = int(sqrt(d**2-y**2))
        answer+=max_x//k+1
    return answer