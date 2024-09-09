def my_solution():
    cur = input()
    cur_x, cur_y = ord(cur[0]) - ord('a') + 1, int(cur[1])
    ans = 0

    move_types = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]
    for next_move in move_types:
        next_x, next_y = cur_x + next_move[0], cur_y + next_move[1]
        if 1 <= next_x <= 8 and 1<=next_y <= 8:
            ans+=1
    return ans

def my_solution():
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0]) - ord('a')) + 1
    
    steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]

    result = 0
    for step in steps:
        next_row = row+step[0]
        next_column = column+step[1]
        if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <=8:
            result+=1
    return result

print(my_solution())