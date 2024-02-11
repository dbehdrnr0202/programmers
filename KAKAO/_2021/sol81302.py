def check_block(place, x, y):
    size_x, size_y = 5, 5
    cur_x, cur_y = x, y
    blocked = [False for _ in range(8)]
    dir_y = [-1, 0, 1, 0]
    dir_x = [0, 1, 0, -1]
    #1차
    for i in range(4):
        next_y, next_x = cur_y+dir_y[i], cur_x+dir_x[i]
        if 0<=next_y<size_y and 0<=next_x<size_x:
            if place[next_y][next_x]=='P':
                return False
            elif place[next_y][next_x]=='X':
                blocked[i]=True
    for i in range(4):
        blocked[i+4] = (blocked[i] and blocked[(i+1)%4])
    #2차
    dir_y2 = [-2, 0, 2,  0, -1, 1, 1, -1]
    dir_x2 = [0, 2, 0, -2, 1, 1, -1, -1]
    
    for i in range(8):
        next_y, next_x = cur_y+dir_y2[i], cur_x+dir_x2[i]
        if 0<=next_y<size_y and 0<=next_x<size_x:
            if place[next_y][next_x]=='P':
                if not blocked[i]:
                    return False
                continue
    return True
    
def check(place, peoples):
    for x, y in peoples:
        if check_block(place, x, y):
            continue
        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        peoples = []
        for y, line in enumerate(place):
            for x, value in enumerate(line):
                if value=='P':
                    peoples.append((x, y))
        answer.append(check(place, peoples))
    return answer