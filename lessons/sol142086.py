def solution(s):
    answer = []
    word_dict = {}
    for i, c in enumerate(s):
        if word_dict.get(c)==None:
            answer.append(-1)
            word_dict[c] = []
        else:
            answer.append(i - word_dict[c][-1])
        word_dict[c].append(i)
    return answer