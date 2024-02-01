def solution(string, skips, index):
    answer = ''
    alphabet = [chr(alpha) for alpha in range(ord('a'), ord('z')+1)]
    for skip in skips:
        alphabet.remove(skip)
    for s in string:
        answer+=alphabet[(alphabet.index(s)+index)%len(alphabet)]
    return answer


s = "aukks"	
skip = "wbqd"	
index = 5
print(solution(s, skip, index))