def solution(queue1, queue2):
    answer = float('INF')
    queue = queue1+queue2
    target = int((sum(queue1)+sum(queue2))/2)
    sum_of_queue = []
    range_of_queue_index = []
    target_min_index = 0
    target_max_index = 0
    exchange_answer = []

    for index in range(len(queue)):
        if index==0:
            appending_sum = queue[0]
        else:
            appending_sum = sum_of_queue[-1]+queue[index]
        sum_of_queue.append(appending_sum)

        if appending_sum==target:
            target_max_index=index
            target_min_index = 0
            exchange_count = (target_max_index+1)+(target_min_index-len(queue1))
            answer = min(answer, exchange_count)
            exchange_answer.append(abs(exchange_count))

            break
        if appending_sum<target:
            continue
        for small_index in range(index+1):
            if (appending_sum-sum_of_queue[small_index])==target:
                target_max_index = index
                target_min_index = small_index+1
                exchange_count = (target_max_index+1)+(target_min_index-len(queue1))
                answer = min(answer, exchange_count)
                exchange_answer.append(abs(exchange_count))

                break
            if (appending_sum-sum_of_queue[small_index])<target:
                break
    if answer == float('INF'):
        return -1
    answer = min(exchange_answer)
    return answer