def solution():
    '''
    ### 부분합
    https://www.acmicpc.net/problem/1806

    문제
    10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 부분합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

    출력
    첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
    '''

    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    
    left = 0
    total = 0
    min_length = float('inf')
    
    for right in range(n):
        total += seq[right]
        
        while total >= s:
            min_length = min(min_length, right - left + 1)
            total -= seq[left]
            left += 1
    
    if min_length == float('inf'):
        print(0)
    else:
        print(min_length)

solution()

'''
input
10 15
5 1 3 5 10 7 4 9 2 8

output
2
'''