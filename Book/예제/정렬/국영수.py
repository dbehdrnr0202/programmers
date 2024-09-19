def my_solution():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input().split()))

    sorted_infos = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    # sorted_infos = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for info in sorted_infos:
        print(info[0])
my_solution()