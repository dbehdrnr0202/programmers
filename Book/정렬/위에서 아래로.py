def my_solution():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    return sorted(arr, reverse=True)

print(my_solution())