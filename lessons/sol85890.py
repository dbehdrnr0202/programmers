def solution(my_string):
    answer = 0
    my_string.replace(" ", "")
    adds:list[str] = my_string.split("+")
    for add in adds:
        if add.isalnum():
            answer+=int(add)
        else:
            minus = add.split("-")
            answer+=int(minus[0])
            minus = minus[1:]
            for minu in minus:
                answer-=int(minu)
            
    return answer