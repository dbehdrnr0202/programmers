global g_number
global g_target
global g_answer

def dfs(depth, cur_value):
    global g_number
    global g_target
    global g_answer
    if depth==len(g_number):
        if cur_value==g_target:
            g_answer+=1
            return
        return
    dfs(depth+1, cur_value-g_number[depth])
    dfs(depth+1, cur_value+g_number[depth])

def solution(numbers, target):
    answer = 0
    global g_number
    global g_target
    global g_answer
    g_answer = 0
    g_number = numbers
    g_target = target
    dfs(0, 0)
    answer = g_answer
    return answer