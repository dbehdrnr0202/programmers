def solution(arr1, arr2):
    answer = []
    for index in range(len(arr1)):
        temp = []
        for jndex in range(len(arr2[0])):
            c = sum([arr1[index][k]*arr2[k][jndex] for k in range(len(arr2))])
            temp.append(c)
        answer.append(temp)
    return answer