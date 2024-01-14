GIFT_FROM = 1
GIFT_TO = 0

def compare_gift_score(friend1:str, friend2:str, gift_map:list[list[int]]):
    
    return True


def solution(friends, gifts):
    answer = 0
    friend_index_dict = {friend:index for index, friend in enumerate(friends)}
    gift_map = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_list = [[0 for _ in range(3)] for _ in range(len(friends))]

    for gift in gifts:
        gift_from, gift_to = gift.split(" ")
        gift_from = friend_index_dict[gift_from]
        gift_to =  friend_index_dict[gift_to]
        gift_map[gift_from][gift_to]+=1
        gift_list[gift_from][GIFT_TO]+=1
        gift_list[gift_to][GIFT_FROM]+=1

    for gift in range(len(gift_list)):
        gift_list[gift][2] = gift_list[gift][GIFT_TO]-gift_list[gift][GIFT_FROM]
    
    gift_score = [0 for _ in range(len(friends))]

    for gift_from in range(len(gift_map)):
        for gift_to in range(len(gift_map[gift_from])):
            # 같은 사람
            if gift_from == gift_to:
                continue
            # 기록 O
            if gift_map[gift_from][gift_to]>gift_map[gift_to][gift_from]:
                gift_score[gift_from]+=1
                continue
            # 기록 X
            if gift_map[gift_from][gift_to]==0 and gift_map[gift_to][gift_from]==0:
                if gift_list[gift_from][2]>gift_list[gift_to][2]:
                    gift_score[gift_from]+=1
                continue
            if gift_map[gift_from][gift_to]==gift_map[gift_to][gift_from]:
                if gift_list[gift_from][2]>gift_list[gift_to][2]:
                    gift_score[gift_from]+=1
    answer = max(gift_score)
    return answer