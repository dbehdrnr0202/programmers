def solution(s:str):
    answer = ""
    temp=""
    num_dict = {"zero":0,
                "one":1,
                "two":2,
                "three":3,
                "four":4,
                "five":5,
                "six":6,
                "seven":7,
                "eight":8,
                "nine":9
                }
    for chr in s:
        if chr.isdigit():
            answer+=chr
        else:
            temp+=chr
            if temp in num_dict:
                answer+=str(num_dict[temp])
                temp=""
    return int(answer)