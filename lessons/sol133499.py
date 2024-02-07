def check(babbling):
    default_babblings = ["aya", "ye", "woo", "ma"]
    before=""
    while babbling:
        flag = False
        for default_babbling in default_babblings:
            if babbling.startswith(default_babbling):
                if default_babbling==before:
                    return False
                before=default_babbling
                babbling=babbling[len(before):]
                if babbling=="":
                    return True
                flag = True
                break
        if not flag:
            return False
    return True

def solution(babblings):
    answer = 0
    for babbling in babblings:
        if check(babbling):
            answer+=1
    return answer