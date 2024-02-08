from collections import Counter
WINDOW_SIZE = 10
def solution(want, number, discounts):
    answer = 0
    want_dict = dict(zip(want, number))
    for i in range(len(discounts)-9):
        count = Counter(discounts[i:i+WINDOW_SIZE])
        if count==want_dict:
            answer+=1
    return answer