def my_solution():
    hour = int(input())
    ans = 0
    for h in range(hour+1):
        for m in range(60):
            for s in range(60):
                h, m, s = str(h), str(m), str(s)
                if '3' in h+m+s:
                    ans+=1
    return ans

def solution():
    h = int(input())

    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    count+=1
    return count

print(my_solution())