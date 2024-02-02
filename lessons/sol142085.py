import heapq

def solution(n, k, enemys):
    answer = 0
    defenced_enermy = []
    for enemy in enemys:
        if not k:
            break
        heapq.heappush(defenced_enermy, -enemy)
        n -=enemy
        answer+=1
        if n<=0:
            k-=1
            n-=heapq.heappop(defenced_enermy)
    return answer

n = 2	
k=4	
enemys=[3, 3, 3, 3]	
print(solution(n, k, enemys))