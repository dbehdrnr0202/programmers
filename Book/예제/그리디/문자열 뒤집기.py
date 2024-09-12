def my_solution():
    arr = list(map(int, input()))
    
    zipped_arr = [arr[0]]
    count_0 = 1 if arr[0]==0 else 0
    count_1 = 1 if arr[0]==1 else 0
    for val in arr[1:]:
        if zipped_arr[-1]!=val:
            zipped_arr.append(val)
            if val==0:
                count_0+=1
            else:
                count_1+=1
    return min(count_0, count_1)

print(my_solution())