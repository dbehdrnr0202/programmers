def get_area(start:int,end:int):
    return (start+end)/2
# 10.5 - 12 - 6 - 3 - 1.5
def solution(target, ranges):
    answer = []
    count = 0
    dots = [(count, target)]
    areas = []
    area_sum = [0]
    while target>1:
        start = target
        if target%2:
            target=target*3+1
        else:
            target/=2
        count+=1
        area_sum.append(area_sum[-1]+get_area(start, target))
        areas.append(get_area(start, target))

    print(areas, area_sum)
    for start, b in ranges:
        end = count+b
        answer.append(area_sum[end]-area_sum[start])
    print(answer)
    return answer

k = 5
# 5 ⇒ 16 ⇒ 8 ⇒ 4 ⇒2 ⇒ 1 
# [(0, 5), (1, 16), (2, 8.0), (3, 4.0), (4, 2.0), (5, 1.0)]
# 10.5, 
# 12, 
# 6, 
# 3, 
# 1.5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]	
# [a, -b] : x = a, x = n - b, y = 0
print(solution(k,ranges))