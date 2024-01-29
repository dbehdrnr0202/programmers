def solution(a, b):
    
    #        0, 1,  2,   3, 4,  5,  6,  7,  8
    days = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day = sum(days[:a])+b
    answer = week[day%7]
    
    #answer = ''
    return answer