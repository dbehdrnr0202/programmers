from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    start = ("ICN",["ICN"], [])
    q.append(start)
    while q:
        current, path, used_tickets =  q.popleft()
        
        if len(used_tickets) == len(tickets):
            answer.append(path)
        for idx, ticket in enumerate(tickets):
            if ticket[0] == current and not idx in used_tickets:
                q.append((ticket[1], path+[ticket[1]], used_tickets+[idx]))
    answer.sort()

    return answer[0]