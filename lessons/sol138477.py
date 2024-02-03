import heapq

def solution(k, scores):
    answer = []
    heap = []
    for score in scores:
        heapq.heappush(heap, score)
        if len(heap)>k:
            min_value = heapq.heappop(heap)
        min_value=heap[0]
        answer.append(min_value)
    return answer