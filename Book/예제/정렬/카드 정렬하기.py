from heapq import heappop, heappush

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        heappush(arr, int(input()))
    answer = 0
    while len(arr)>1:
        card_1 = heappop(arr)
        card_2 = heappop(arr)
        new_card = card_1+card_2
        answer+=new_card
        heappush(arr, new_card)
    print(answer)
solution()

'''
3
10
20
40
'''