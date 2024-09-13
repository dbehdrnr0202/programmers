def my_solution():
    arr = list(map(int, input()))
    half_index = int(len(arr)/2)
    return "LUCKY" if sum(arr[:half_index])*2==sum(arr) else "READY"

print(my_solution())

'''
123402

7755
'''