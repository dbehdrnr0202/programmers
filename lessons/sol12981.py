def solution(n, words):
    answer = []
    word_set = set()
    count = 1
    for index, word in enumerate(words):
        if index ==0:
            word_set.add(word)
            continue
        if word[0]!=words[index-1][-1]:
            answer.append(index%n+1)
            answer.append(index//n+1)
            return answer
        if word not in word_set:
            word_set.add(word)
        else:
            answer.append(index%n+1)
            answer.append(index//n+1)
            return answer
        if index%n==0:
            count+=1
    answer = [0, 0]
    return answer