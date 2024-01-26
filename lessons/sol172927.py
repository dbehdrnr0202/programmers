from math import ceil

def get_picks(picks, minerals):
    max_pick = min(sum(picks), ceil(len(minerals)/5))
    left_picks = []
    for _ in range(picks[0]):
        if len(left_picks)==max_pick:
            return left_picks
        left_picks.append(25)
    for _ in range(picks[1]):
        if len(left_picks)==max_pick:
            return left_picks
        left_picks.append(5)
    for _ in range(picks[2]):
        if len(left_picks)==max_pick:
            return left_picks
        left_picks.append(1)
    return left_picks

def solution(picks, minerals):
    answer = 0
    left_picks = get_picks(picks, minerals)
    how_much_index = sum(picks)*5
    
    mineral_dict = {
        "diamond":25,
        "iron":5,
        "stone":1
    }
    minerals = [minerals[i:i+5] for i in range(0,how_much_index,5)]
    minerals_sum = []
    for mineral in minerals:
        minerals_sum.append([mineral_dict[mine] for mine in mineral])
    mineral_sum = []
        
    for index in range(len(minerals_sum)):
        if minerals_sum[index]==[]:
            break
        mineral_sum.append(minerals_sum[index]+[sum(minerals_sum[index])])
    #minerals_sum = [sum(mineral_sum) for mineral_sum in minerals_sum]
    mineral_sum = sorted(mineral_sum, key= lambda x:x[-1], reverse=True)
    index = 0
    for using_pick in left_picks:
        for mineral in mineral_sum[index][:-1]:
            tired=int(ceil(mineral/using_pick))
            answer+=tired
        index+=1
    return answer