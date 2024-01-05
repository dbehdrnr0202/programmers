global is_prime

# n까지의 소수를 찾아서 is_prime list에 넣기
def prime_until_n(n:int):
    global is_prime
    is_prime=[-1]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

# n을 k진수로 translation
def base_notation(n:int, k:int):
    notation:str = ""
    while n!=0:
        appending_number = n%k
        notation+=str(appending_number)
        n = int(n/k)
    return notation[::-1]

import math

def check_rule(notation:str):
    global is_prime
    notation_list= notation.split("0")
    answer = 0
    for notation in notation_list:
        if not notation.isdigit():
            continue
        number = int(notation)
        sqrt_number = int(math.sqrt(number))
        if (number!=sqrt_number**2):
            prime_until_n(number)
            if (is_prime[number]==-1):
                answer+=1
    return answer
# 
def solution(n, k):
    answer = -1
    global is_prime    
    answer = check_rule(base_notation(n, k))
    return answer