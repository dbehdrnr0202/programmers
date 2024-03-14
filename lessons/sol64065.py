from collections import defaultdict

def solution(s:str):
    answer = []
    s=s[2:-2]
    strs=s.split("},{")
    num_dict = defaultdict(int)
    for s in strs:
        nums = s.split(",")
        for num in nums:
            num_dict[num]+=1
    sorted_lists = sorted(num_dict.items(), key=lambda x:(x[1]), reverse=True)
    for value in sorted_lists:
        answer.append(int(value[0]))
    return answer