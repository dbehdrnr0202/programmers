def solution(elements):
    answer = 0
    fullelements = elements+elements
    subsums = [[] for _ in range(len(elements)+1)]
    subsums[1] = fullelements
    subanswer = elements[:]
    for length in range(2, 1+len(elements)):
        for idx in range(1+len(fullelements)-length):
            subsums[length].append(subsums[length-1][idx]+fullelements[idx+length-1])
        subanswer+=subsums[length]
    answer = set(subanswer)
    print(answer)
    return len(answer)