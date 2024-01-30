# 1. 시작점과 끝점이 arr[0]를 가리키도록 한다.
# 2. 현재 부분 합이 target과 같다면 카운트한다.
# 3. 현재 부분 합이 target보다 작다면 end를 1 증가시킨다.
# 4. 현재 부분 합이 target보다 크거나 같다면 start_point를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2-4번 과정을 반복한다

def get_two_pointer_set(arr:list[int], target:int, init_start_point:int=0, init_end_point:int=0):
    start_point, end_point = init_start_point, init_end_point
    cur_sum = sum(arr[init_start_point:init_end_point+1])
    answer = []
    while end_point<len(arr) and start_point<=end_point:
        if cur_sum==target:
            answer.append((start_point, end_point))
            end_point+=1
            if end_point>=len(arr):
                break
            cur_sum+=arr[end_point]
        elif cur_sum<target:
            end_point+=1
            if end_point>=len(arr):
                break
            cur_sum+=arr[end_point]
        elif cur_sum>=target:
            cur_sum-=arr[start_point]
            start_point+=1
    return answer

def get_init_two_pointer(arr:list[int], target:int, init_start_point:int=0, init_end_point:int=0):
    start_point, end_point = init_start_point, init_end_point
    cur_sum = sum(arr[init_start_point:init_end_point+1])
    while end_point<len(arr) and start_point<=end_point:
        if cur_sum==target:
            return (start_point, end_point)
        elif cur_sum<target:
            end_point+=1
            if end_point>=len(arr):
                break
            cur_sum+=arr[end_point]
        elif cur_sum>=target:
            cur_sum-=arr[start_point]
            start_point+=1
    return -1

arr = [1, 4, 20, 3, 10, 5, 18]
target = 33
index_set = get_init_two_pointer(arr, target)
for start_index, end_index in index_set:
    print(sum(arr[start_index:end_index+1]))