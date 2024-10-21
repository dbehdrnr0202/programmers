import math

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a != parent_b:
        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

def calculate_distance(star1, star2):
    return math.sqrt((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2)

def solution():
    '''
    ### 별자리 만들기
    https://www.acmicpc.net/problem/4386

    시간 제한	메모리 제한
    1 초	128 MB

    문제
    도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
    - 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
    - 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
    별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

    입력
    첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
    둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.
    '''
    result = 0
    n = int(input())
    coord = []
    parent = list(range(n))
    for _ in range(n):
        x, y = map(float, input().split())
        coord.append((x, y))
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(coord[i], coord[j])
            edges.append((distance, i, j))
    edges.sort()
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            result += cost
    print(f"{result:.2f}")
    
solution()

'''
input
3
1.0 1.0
2.0 2.0
2.0 4.0

output
3.41
'''