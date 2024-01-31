from functools import reduce
def mul(a, b):
    return a*b

def solution(matrix_sizes):
    answer = 0
    for index, matrix_size in enumerate(matrix_sizes[:-1]):
        matrix_size.append(matrix_sizes[index+1][1])
    matrix_sizes = matrix_sizes[:-1]
    matrix_sizes.sort(key=lambda x:-x[1])
    for matrix_size in matrix_sizes:
        answer+=reduce(mul, matrix_size)
        print(reduce(mul, matrix_size))
    print(matrix_sizes)
    return answer