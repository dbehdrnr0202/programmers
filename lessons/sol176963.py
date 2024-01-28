from collections import defaultdict

def solution(names, yearnings, photos):
    answer = []
    name_dict = defaultdict(int, zip(names, yearnings))
    for photo in photos:
        answer.append(sum([name_dict[people] for people in photo]))
    return answer