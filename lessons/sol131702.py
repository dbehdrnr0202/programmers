def add_matrix(origin_mat, origin_x, origin_y):
    adding_matrix = [[0,1,0],[1,1,1],[0,1,0]]
    # is in bound
    if 0<origin_x<len(origin_mat)-1 and 0<origin_y<len(origin_mat)-1:
        for i in range(3):
            for j in range(3):
                origin_mat[origin_y][origin_x]=(origin_mat[origin_y][origin_x]-adding_matrix[i][j])%4
    # is out bound
    else:
            dir_x, dir_y = [0,0,-1,1,0], [-1,1,0,0,0]
            CENTER = 1
            for i in range(4):
                next_x, next_y = origin_x+dir_x[i], origin_y+dir_y[i]
                if 0<=next_x<len(origin_mat) and 0<=next_y<len(origin_mat):
                    origin_mat[next_y][next_x]=(origin_mat[next_y][next_y]-1)%4
    return origin_mat
def solution(clockHands):
    answer = 0
    for row_index in range(len(clockHands)):
        for column_index in range(len(clockHands)):
            clockHands[row_index][column_index]=(4-clockHands[row_index][column_index])%4
    print(clockHands)
    return answer

clockHands = [[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]	
print(solution(clockHands=clockHands))