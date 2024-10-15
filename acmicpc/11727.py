arr = [-1] * 1001

def dp(n):
    if arr[n] != -1:
        return arr[n]
    arr[n] = ((dp(n-2)*2)+dp(n-1)*1)%10007
    
    return arr[n]

def solution():
    '''
    2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
    아래 그림은 2×17 직사각형을 채운 한가지 예이다.
    '''
    n = int(input())
    arr[0] = 0
    arr[1] = 1
    arr[2] = 3
    print(dp(n))


solution()