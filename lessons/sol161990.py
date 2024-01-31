def solution(wallpaper):
    answer = []
    left_up_point = [len(wallpaper), len(wallpaper[0])]
    right_down_point = [0, 0]
    for row_index,row in enumerate(wallpaper):
        for col_index, icon in enumerate(row):
            if icon=='#':
                left_up_point[0] = min(left_up_point[0], row_index)
                left_up_point[1] = min(left_up_point[1], col_index)
                right_down_point[0] = max(right_down_point[0], row_index+1)
                right_down_point[1] = max(right_down_point[1], col_index+1)
    for i in left_up_point:
        answer.append(i)
    for i in right_down_point:
        answer.append(i)
    
    return answer