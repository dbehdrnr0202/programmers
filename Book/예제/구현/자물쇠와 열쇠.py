from copy import deepcopy

def rotate(matrix):
    n = len(matrix)
    m = len((matrix[0]))
    rotated_matrix = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n-i-1] = matrix[i][j]
    return rotated_matrix

def check(lock):
    lock_length = len(lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock[i][j]!=1:
                return False
    return True
    

def my_solution(key, lock):
    n = len(lock)
    m = len(key)
    expanded_lock = [[0] *(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            expanded_lock[i+n][j+n]=lock[i][j]
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                copyed_lock = deepcopy(expanded_lock)
                for i in range(m):
                    for j in range(m):
                        copyed_lock[x+i][y+j] += key[i][j]
                if check(copyed_lock):
                    return True
    return False

print(my_solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])==True)