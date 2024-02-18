def solution(s):
    answer = ''
    numbers = s.split(" ")
    max_n, min_n = -float("INF"), float("INF")
    for number in numbers:
        if number.isdigit()==False:
            number = -int(number[1:])
        else:
            number = int(number)
        max_n = max(max_n, number)
        min_n = min(min_n, number)
    answer = str(min_n)+" "+str(max_n)
    return answer