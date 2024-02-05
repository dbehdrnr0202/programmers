import heapq

def solution(cap, n, deliveries, pickups):
    answer = 0
    del_que = []
    pick_que = []
    for index, value in enumerate(zip(deliveries, pickups)):
        deli, pick = value
        if deli:
            heapq.heappush(del_que, (-index-1, deli))
        if pick:
            heapq.heappush(pick_que, (-index-1, pick))
    
    while del_que or pick_que:
        left_cap = cap
        dist = 1
        while del_que:
            if left_cap:
                next_delivery, box = heapq.heappop(del_que)
                if box>left_cap:
                    box-=left_cap
                    left_cap=0
                    heapq.heappush(del_que, (next_delivery, box))
                else:
                    left_cap-=box
                next_delivery = -next_delivery
                dist = max(dist, next_delivery)
            else:
                break
        left_cap = cap
        while pick_que:
            if left_cap:
                next_delivery, pickup = heapq.heappop(pick_que)
                if pickup>left_cap:
                    pickup-=left_cap
                    left_cap=0
                    heapq.heappush(pick_que, (next_delivery, pickup))
                else:
                    left_cap-=pickup
                next_delivery = -next_delivery
                dist = max(dist, next_delivery)
            else:
                break
        answer+=2*dist
        #print(pick_que)

    return answer

cap = 4	
n=5	
deliveries=[1, 0, 3, 1, 2]	
pickups=[0, 3, 0, 4, 0]
print(solution(cap, n, deliveries, pickups))