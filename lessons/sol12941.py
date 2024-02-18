def solution(list1,list2):
    answer = 0
    list1 = sorted(list1, key=lambda x:x)
    list2 = sorted(list2, key=lambda x:-x)
    for x, y in zip(list1, list2):
        answer +=x*y
    return answer