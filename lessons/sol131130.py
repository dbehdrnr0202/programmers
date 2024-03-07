from collections import deque
from heapq import heappop, heappush
global visited
def get_cycle(cards, index):
    global visited
    q = deque()
    q.append(index)
    cycle_length = 0
    while q:
        cur = q.popleft()
        if not visited[cur]:
            next = cards[cur]
            visited[cur]=True
            cycle_length+=1
            if not visited[next]:
                q.append(next)
            else:
                break            
    return cycle_length
def solution(cards):
    global visited
    visited = [False for _ in range(len(cards)+1)]
    cards = [0]+cards
    cycle_lengths = []
    for index,card in enumerate(cards):
        if index==0:
            continue
        if not visited[card]:
            heappush(cycle_lengths, -get_cycle(cards, index))
    if len(cycle_lengths)<2:
        return 0
    max_1, max_2 = heappop(cycle_lengths), heappop(cycle_lengths)
    return abs(max_1*max_2)