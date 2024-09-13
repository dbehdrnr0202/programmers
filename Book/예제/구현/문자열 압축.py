def my_solution():
    arr = input()
    ans = len(arr)
    for cur_length in range(1, len(arr)//2+1):
        compressed = ""
        prev = arr[0:cur_length]
        count = 1
        for idx in range(cur_length, len(arr), cur_length):
            if prev==arr[idx:idx+cur_length]:
                count+=1
            else:
                compressed+=str(count)+prev if count>=2 else prev
                prev = arr[idx:idx+cur_length]
                count = 1
        compressed+=str(count)+prev if count>=2 else prev
        ans = min(len(compressed), ans)
    return ans

print(my_solution())


'''
aabbaccc
'''