def my_solution():
    n, k = map(int, input().split())
    result = 0
    while True:
        result += n % k
        if n < k:
            break
        n /= k
        result+=1
    return int(result + 1)

print(my_solution())