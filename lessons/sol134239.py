def get_area(start:int,end:int):
    return (start+end)/2
def solution(target, ranges):
    answer = []
    area_sum = [0]
    while target>1:
        start = target
        if target%2:
            target=target*3+1
        else:
            target/=2
        area_sum.append(area_sum[-1]+get_area(start, target))
    for start, b in ranges:
        if start>len(area_sum)+b-1:
            answer.append(-1)
        else:
            answer.append(area_sum[len(area_sum)+b-1]-area_sum[start])
    return answer