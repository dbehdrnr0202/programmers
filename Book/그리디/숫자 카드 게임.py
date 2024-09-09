def my_solution():
    n, m = map(int, input().split())
    result = 0

    for _ in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(min_value, result)
    return result