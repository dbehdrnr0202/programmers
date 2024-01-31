def solution(n, m, sections):
    answer = 0
    last_painted = sections[0]-1
    for section in sections:
        if last_painted<section:
            answer+=1
            last_painted = section+m-1
    return answer