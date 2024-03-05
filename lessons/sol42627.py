from collections import deque
from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    q = []
    job_q = deque()
    jobs = [[job[0], job[1]] for job in jobs]
    job_q = deque(sorted(jobs, key=lambda x:(x[0],x[1])))
    can_job_start_time, can_job_doing_time = job_q.popleft()
    heappush(q, (can_job_doing_time, can_job_start_time))
    current_time = 0
    while q or job_q:
        while job_q and current_time>=job_q[0][0]:
            can_job_start_time, can_job_doing_time = job_q.popleft()
            heappush(q, (can_job_doing_time, can_job_start_time))
        if not q:
            can_job_start_time, can_job_doing_time = job_q.popleft()
            heappush(q, (can_job_doing_time, can_job_start_time))
            current_time = can_job_start_time
        current_time_doing_time, current_job_start_time = heappop(q)
        doing_time = 0
        if current_time<=current_job_start_time:
            doing_time = current_time_doing_time
            current_time = current_job_start_time+current_time_doing_time
        elif current_time>current_job_start_time:
            doing_time = (current_time-current_job_start_time)+current_time_doing_time
            current_time += current_time_doing_time
            
        answer+=doing_time
    answer/=len(jobs)
    return int(answer)