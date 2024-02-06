def solution(storey):
    answer = 0
    while storey:
        if (storey%10)<10-(storey%10):
            answer+=(storey%10)
        elif (storey%10)==10-(storey%10):
            answer+=(storey%10)
            digit10=storey%100//10
            if digit10>=5:
                storey+=10
        else:
            answer+=10-(storey%10)
            storey+=10
        storey=storey//10
    return answer