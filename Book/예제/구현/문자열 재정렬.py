def my_solution():
    arr = list(input())
    arr.sort()
    summation = 0
    for idx, val in enumerate(arr):
        if val.isnumeric()==False:
            arr = arr[idx:]
            break
        else:
            summation+=int(val)
    arr = "".join(arr)+str(summation)
    return arr

print(my_solution())


'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''