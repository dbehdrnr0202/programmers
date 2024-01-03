global grid_origin
global size_x, size_y

def preprocess(grid):
    global grid_origin
    grid_origin = [[]]
    for y in range(len(grid)):
        grid_origin.append([])
        for x in range(len(grid[y])):
            grid_origin[y].append({
                'value':grid[y][x],
                'N':False,
                'S':False,
                'E':False,
                'W':False})
    
def progress(init_y:int, init_x:int, init_dir:str):
    global grid_origin
    length = 0
    queue = []
    queue.append((init_y, init_x, init_dir))
    while queue:
        in_y, in_x, in_dir = queue.pop()
        if grid_origin[in_y][in_x][in_dir]==True:
            return length
        length+=1
        grid_origin[in_y][in_x][in_dir]=True
        out_y, out_x, out_dir = move(in_y, in_x, in_dir)
        result_y, result_x, result_dir = hit_wall(out_y, out_x, out_dir)
        
        queue.append((result_y, result_x, result_dir))
    return length

def move(in_y:int, in_x:int, in_dir:str):
    out_y = in_y 
    out_x = in_x
    out_dir = in_dir
    cur_grid_value = grid_origin[in_y][in_x]['value']
    # straight
    if cur_grid_value=='S':
        if in_dir=='N':
            out_y+=1
        elif in_dir=='S':
            out_y-=1
        elif in_dir=='W':
            out_x+=1
        elif in_dir=='E':
            out_x-=1
    # turn right(direction changed)
    elif cur_grid_value=='R':
        if in_dir=='N':
            out_x-=1
            out_dir='E'
        elif in_dir=='S':
            out_x+=1
            out_dir='W'
        elif in_dir=='W':
            out_y+=1
            out_dir='N'
        elif in_dir=='E':
            out_y-=1
            out_dir='S'
        
    # turn left
    elif cur_grid_value=='L':
        if in_dir=='N':
            out_x+=1
            out_dir='W'
        elif in_dir=='S':
            out_x-=1
            out_dir='E'
        elif in_dir=='W':
            out_y-=1
            out_dir='S'
        elif in_dir=='E':
            out_y+=1
            out_dir='N'
        
    return out_y, out_x, out_dir


def hit_wall(in_y:int, in_x:int, in_dir:str):
    out_x=in_x
    out_y=in_y
    out_dir=in_dir
    if in_x==-1 and in_dir=='E':
        out_x=size_x-1
    elif in_x==size_x and in_dir=='W':
        out_x=0
    elif in_y==-1 and in_dir=='S':
        out_y=size_y-1
    elif in_y==size_y and in_dir=='N':
        out_y=0
    return out_y, out_x, out_dir


def solution(grid):
    answer = []
    direction = ['N', 'S', 'E', 'W']
    preprocess(grid)
    global size_x, size_y
    size_y = len(grid)
    size_x = len(grid[0])
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for dir in direction:
                if (grid_origin[y][x][dir]==False):
                    answer.append(progress(y, x, dir))
    answer.sort()
    return answer