import numpy as np
global size_x
global size_y

def is_in(next_x, next_y):
    global size_x
    global size_y
    if next_x>=0 and next_y>=0 and next_x<size_x and next_y<size_y:
        return True
    return False

def progress(way):
    origin_way = way
    way_2 = []
    for i in range(len(origin_way)):
        for j in range(len(origin_way[i])):
            way_2.append(origin_way[i][j])
    if way_2==[]:
        return False
    for index in range(len(way_2)):
        if way_2[index]=='X':
            return False
        elif way_2[index]=='O':
            continue
    return True

def solution(park, routes):
    answer = []
    global size_x, size_y
    size_x = len(park[0])
    size_y = len(park)
    cur_x = 0
    cur_y = 0
    for line in park:
        if line.find("S")!=-1:
            cur_x = line.find("S")
            break
        else:
            cur_y+=1
    park = [list(line) for line in park]
    park_df = np.array(park)    
    for route in routes:
        next_x = cur_x
        next_y = cur_y
        direction, dist = route.split(" ")
        dist = int(dist)
        if direction == "E":
            next_x+=dist
        elif direction =='W':
            next_x-=dist
        elif direction =='N':
            next_y-=dist
        elif direction=='S':
            next_y+=dist
        if is_in(next_x, next_y):
            min_x = min(cur_x, next_x)
            max_x = max(cur_x, next_x)+1
            min_y = min(cur_y, next_y)
            max_y = max(cur_y, next_y)+1
            way = park_df[min_y:max_y,min_x:max_x].tolist()
            if progress(way):
                cur_x = next_x
                cur_y = next_y
    answer.append(cur_y)
    answer.append(cur_x)
    return answer