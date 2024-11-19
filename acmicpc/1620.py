def solution():
    '''
    ### 나는야 포켓몬 마스터 이다솜
    https://www.acmicpc.net/problem/1620
    '''
    n, m = map(int, input().split())
    name_dict = dict()
    number_dict = dict()
    for idx in range(1, n+1):
        name = input()
        name_dict[name] = str(idx)
        number_dict[str(idx)] = name
    for _ in range(m):
        query = input()
        if query.isnumeric():
            print(number_dict[query])
        else:
            print(name_dict[query])

solution()