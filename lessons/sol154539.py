def solution(numbers):
    answer = []
    indexed_numbers = [[number, index] for index, number in enumerate(numbers)]
    indexed_numbers.sort(key=lambda x:[-x[0], x[1]])
    print("indexed_numbers: ",indexed_numbers)
    
    before_number, before_index = indexed_numbers[0]
    answer.append([[-1, -1], before_index])
    
    for number, index in indexed_numbers[1:]:
        if before_number>number:
            if before_index>index:
                answer.append([[before_number, before_index], index])
            else:
                answer.append([[-1, -1], index])
        elif before_number==number:
            if answer[-1][0][1]>index:
                answer.append([answer[-1][0], index])
            else:
                answer.append([[-1, -1], index])
        if index<before_index:
            before_number= number
            before_index = index        
    answer.sort(key=lambda x:x[1])
    print("answer: ",answer)
    rtn = [ans[0] for ans in answer]
    return rtn
numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
numbers = [2, 3, 3, 5]
print(solution(numbers))