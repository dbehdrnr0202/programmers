def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for num in arr:
        if len(answer)!=0 and num==answer[-1]:
            continue
        answer.append(num)
    return answer