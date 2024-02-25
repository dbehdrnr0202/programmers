
def solution(n):
    answer = ''
    numbers = []
    n=int(n)
    while n:
        digit = n%3
        numbers.append(digit)
        n=n//3
    for index, number in enumerate(numbers):
        if number==0:
            if index==len(numbers)-1:
                break
            answer+="4"
            numbers[index+1]-=1
        else:
            answer+=str(number)
    return answer[::-1]
print(solution(3))