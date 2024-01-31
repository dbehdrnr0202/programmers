from collections import deque

def translate_time_to_int(time:str):
    hour, minute = time.split(":")
    return int(hour)*60+int(minute)

def solution(plans):
    answer = []
    scheduler = []
    for i in range(len(plans)):
        plans[i][1] = translate_time_to_int(plans[i][1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    for i in range(len(plans)-1):
        scheduler.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]
        while scheduler and gap:
            if scheduler[-1][1] <= gap:
                cn, ct = scheduler.pop()
                gap -= ct
                answer.append(cn)
            else:
                scheduler[-1][1] -= gap
                gap = 0
    answer.append(plans[-1][0])
    for i in range(len(scheduler)):
        answer.append(scheduler[~i][0])
    return answer