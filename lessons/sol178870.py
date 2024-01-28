def solution(sequence, k):
    answer = []
    start_point, end_point, seq_sum = 0, 0, sequence[0]
    while True:
        if end_point==len(sequence):
            if seq_sum==k:
                answer.append((start_point, end_point))
            break
        if seq_sum<k:
            end_point+=1
            if end_point==len(sequence):
                break
            seq_sum+=sequence[end_point]
        elif seq_sum>k:
            seq_sum-=sequence[start_point]
            start_point+=1
        else:
            answer.append((start_point, end_point))
            seq_sum-=sequence[start_point]
            start_point+=1
            if seq_sum==k:
                answer.append((start_point, end_point))

    answer.sort(key=lambda x: x[1]-x[0])
    answer = [*answer[0]]
    return answer