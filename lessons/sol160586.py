from collections import defaultdict
import math

def solution(keymaps, targets):
    answer = []
    key_dict = defaultdict(lambda : 900)
    for keymap in keymaps:
        keys = list(keymap)
        for index, key in enumerate(keys):
            key_dict[key] = min(key_dict[key], index+1)
    for target in targets:
        target_list = list(target)
        temp = 0
        flag = True
        for target_e in target_list:
            if key_dict[target_e]==900:
                flag = False
                break
            temp+=key_dict[target_e]
        if not flag:
            answer.append(-1)
            continue
        answer.append(temp)
        
    return answer