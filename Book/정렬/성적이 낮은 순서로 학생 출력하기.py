def my_solution():
    n = int(input())
    score_dict = {}
    for _ in range(n):
        name, score = input().split()
        score_dict[name] = int(score)
    return sorted(score_dict, key=lambda x: score_dict[x])
print(my_solution())