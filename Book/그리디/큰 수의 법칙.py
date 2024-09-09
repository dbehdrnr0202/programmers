def my_solution():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data = sorted(data, reverse=True)
    result = 0
    max1, max2 = data[0], data[1]
    cnt = m//(k+1)
    remain = m%(k+1)
    result =  cnt * (max1*k + max2)
    result += remain*max1
    return result

def solution():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[n-1]
    second = data[n-2]

    count = int(m / (k+1)) * k
    count+= m%(k+1)

    result = 0
    result += count* first
    result += (m - count) * second

    return result