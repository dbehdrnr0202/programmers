import bisect
from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer = []
    develops = defaultdict(list)
    for info in infos:
        infolist = info.split(" ")
        score = int(infolist[-1])
        keys = infolist[:-1]
        for select in range(5):
            for comb in combinations(keys, select):
                key_combation = "".join(comb)
                develops[key_combation].append(score)
    for key in develops.keys():
        develops[key].sort()

    for query in queries:
        qeury = query.replace(" and ", " ")
        qeury = qeury.replace("-", "")
        qeury = qeury.split(" ")
        key = "".join(qeury[:-1])
        score = int(qeury[-1])
        peoples = develops[key]
        if peoples==[]:
            answer.append(0)
            continue
        enter = bisect.bisect_left(peoples, score)
        answer.append(len(peoples)-enter)
    return answer