def solution():
    n = int(input())
    m = [0] * 1001
    m[1], m[2] = 1, 3
    for idx in range(3, n+1):
        m[idx] = (m[idx-1]+m[idx-2]*2)%796796
    return m[n]

print(solution())

'''
3
5
'''