from itertools  import combinations

def solution(babblings):
    answer = 0
    for babbling in babblings:
        origin = babbling
        default_babblings = {"aya":False, 
                             "ye":False, 
                             "woo":False, 
                             "ma":False}
        while babbling:
            if babbling[:3]=='aya' and not default_babblings["aya"]:
                babbling=babbling[3:]
                default_babblings["aya"] = True
            elif babbling[:2]=='ye' and not default_babblings["ye"]:
                babbling=babbling[2:]
                default_babblings["ye"] = True
            elif babbling[:3]=='woo' and not default_babblings["woo"]:
                babbling=babbling[3:]
                default_babblings["woo"] = True
            elif babbling[:2]=='ma' and not default_babblings["ma"]:
                babbling=babbling[2:]
                default_babblings["ma"] = True
            else:
                break
        if babbling=="":
            answer+=1
    return answer