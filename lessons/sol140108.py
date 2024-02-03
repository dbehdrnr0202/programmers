def word_func(word):
    first_char = word[0]
    OTHER = "-1"
    word_dict = {first_char:0, OTHER:0} 
    for index, char in enumerate(word):
        if char== first_char:
            word_dict[first_char]+=1
        else:
            word_dict[OTHER]+=1
        if word_dict[first_char]==word_dict[OTHER]:
            rtn = word[index+1:]
            return rtn
    return ""

def solution(word):
    answer = 0
    while word:
        word = word_func(word)
        answer+=1
    return answer