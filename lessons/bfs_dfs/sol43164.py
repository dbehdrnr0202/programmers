from collections import deque

def solution(tickets):
    answer = []
    cities = {}
    for ticket in tickets:
        if cities.get(ticket[0])==None:
            cities[ticket[0]]=[]
        cities[ticket[0]]+=[ticket[1]]

    start = "ICN"
    q = deque
    q.append(start)
    while q:
        cur = q.popleft()
    return answer