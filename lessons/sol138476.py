from collections import Counter

def solution(k, tangerines):
    answer = 0
    tangerine_dict = Counter(tangerines)
    tangerines = sorted(tangerine_dict.items(), key=lambda x: x[1], reverse=True)
    for tangerine in tangerines:
        if k>0:
            answer+=1
            k-=tangerine[1]
    return answer