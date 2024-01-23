from heapq import heappush, heappop

def solution(targets):
    answer = 1
    targets = sorted(targets, key=lambda target:target[1])
    heap = []
    for target in targets:
        if not heap:
            heappush(heap, target[1])
        else:
            if target[0]<heap[0]:
                continue
            else:
                heappop(heap)
                answer+=1
            heappush(heap, target[1])
    return answer