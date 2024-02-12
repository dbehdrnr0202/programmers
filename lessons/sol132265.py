from collections import Counter, defaultdict
def solution(toppings):
    answer = 0
    second = dict(Counter(toppings))
    print(second)
    first=defaultdict(int)
    for topping in toppings:
        first[topping]+=1
        second[topping]-=1
        if second[topping]==0:
            second.pop(topping)
        if len(first)==len(second):
            answer+=1
    return answer