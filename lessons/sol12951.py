def solution(sentence):
    answer = ''
    sentence = sentence.lower()
    answer+=sentence[0].upper()
    for index, chr in enumerate(sentence[1:]):
        if chr==" ":
            answer+=chr
        elif sentence[index]==" ":
            answer+=chr.upper()
        else:
            answer+=chr.lower()
    return answer