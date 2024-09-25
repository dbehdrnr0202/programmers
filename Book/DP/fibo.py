def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)
print(fibo(4))


# memoization
d = [0] * 100

def fibo_recursive(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x] = fibo_recursive(x-1)+fibo_recursive(x-2)
    return d[x]

# bottom-up
def fibo_bottom_up(x):
    for i in range(3, x+1):
        d[i] = d[i-1]+d[i-2]
    return d[x]