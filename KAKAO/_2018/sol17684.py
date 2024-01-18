msg_dict = {}

def get_max_w(w, msg):
    global msg_dict
    if w==msg:
        return w, "", msg_dict[w], ""
    for c in msg[1:]:
        w+=c
        if w==msg and msg_dict.get(w)!=None:
            return w, "", msg_dict[w], ""
        elif msg_dict.get(w)==None:
            break

    adding_dict = w
    w = w[:-1]
    dict_value = msg_dict[w]
    msg = msg[len(w):]
    return w, adding_dict, dict_value, msg

def solution(msg):
    answer = []
    global msg_dict
    msg_dict = {chr(alpha).upper():(alpha + 1 - ord('a')) for alpha in range(ord('a'), ord('z')+1)}
    w = msg[0]
    while msg:
        #if msg==w and not msg_dict.get(w)==None:
        #    answer.append(msg_dict[w])
        #    break
        w, adding_dict, dict_value, msg = get_max_w(w, msg)
        if msg=="":
            answer.append(dict_value)
            break
        msg_dict[adding_dict] = len(msg_dict)+1
        answer.append(dict_value)
        w = msg[0]
    return answer
'''
20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34, 20
20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34
'''