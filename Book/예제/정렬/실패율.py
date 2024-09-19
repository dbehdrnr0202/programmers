from collections import defaultdict

def solution(N, stages):
    answer = []
    stage_infos = defaultdict(int)
    for stage in stages:
        if stage>N:
            continue
        stage_infos[stage]+=1
    stage_infos = dict(sorted(stage_infos.items(), key=lambda x:x[0]))
    cur_stage_players = len(stages)
    
    for stage in range(1, N+1):
        players = stage_infos.get(stage, 0)
        fail_percent = players/cur_stage_players if cur_stage_players!=0 else 0
        answer.append((stage, fail_percent))
        cur_stage_players -= players
    answer = sorted(answer, key=lambda x:(-x[1], x[0]))
    answer = [stage for stage, rate in answer]
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
'''
5, [2, 1, 2, 6, 2, 4, 3, 3]
[3,4,2,1,5]

4, [4,4,4,4,4]
[4,1,2,3]
'''