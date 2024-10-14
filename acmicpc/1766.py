import heapq

def solution():
    '''
    민오는 1번부터 N번까지 총 N개의 문제로 되어 있는 문제집을 풀려고 한다. 문제는 난이도 순서로 출제되어 있다. 즉 1번 문제가 가장 쉬운 문제이고 N번 문제가 가장 어려운 문제가 된다.

    어떤 문제부터 풀까 고민하면서 문제를 훑어보던 민오는, 몇몇 문제들 사이에는 '먼저 푸는 것이 좋은 문제'가 있다는 것을 알게 되었다. 예를 들어 1번 문제를 풀고 나면 4번 문제가 쉽게 풀린다거나 하는 식이다. 민오는 다음의 세 가지 조건에 따라 문제를 풀 순서를 정하기로 하였다.

    N개의 문제는 모두 풀어야 한다.
    먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
    가능하면 쉬운 문제부터 풀어야 한다.
    예를 들어서 네 개의 문제가 있다고 하자. 4번 문제는 2번 문제보다 먼저 푸는 것이 좋고, 3번 문제는 1번 문제보다 먼저 푸는 것이 좋다고 하자. 만일 4-3-2-1의 순서로 문제를 풀게 되면 조건 1과 조건 2를 만족한다. 하지만 조건 3을 만족하지 않는다. 4보다 3을 충분히 먼저 풀 수 있기 때문이다. 따라서 조건 3을 만족하는 문제를 풀 순서는 3-1-4-2가 된다.

    문제의 개수와 먼저 푸는 것이 좋은 문제에 대한 정보가 주어졌을 때, 주어진 조건을 만족하면서 민오가 풀 문제의 순서를 결정해 주는 프로그램을 작성하시오.
    '''
    result = []
    n, m = map(int, input().split())
    indegree = [0] *(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b]+=1
        graph[a].append(b)
    
    q = []
    for node_idx in range(1, n+1):
        if indegree[node_idx]==0:
            heapq.heappush(q, (0, node_idx))
            continue
        graph[node_idx].sort()
    while q:
        _, cur_node = heapq.heappop(q)
        result.append(cur_node)
        for next_node in graph[cur_node]:
            indegree[next_node]-=1
            if indegree[next_node]==0:
                heapq.heappush(q, (0, next_node))
    for val in result:
        print(val, end=' ')

solution()

'''
6 7
5 6
5 2
2 4
4 3
2 1
6 1
1 3

5 2 4 6 1 3
'''