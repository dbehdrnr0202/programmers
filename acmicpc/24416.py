def solution():
    '''
    ### 알고리즘 수업 - 피보나치 수 1
    https://www.acmicpc.net/problem/24416

    오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

    오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

    피보나치 수 재귀호출 의사 코드는 다음과 같다.

    fib(n) {
        if (n = 1 or n = 2)
        then return 1;  # 코드1
        else return (fib(n - 1) + fib(n - 2));
    }
    피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

    fibonacci(n) {
        f[1] <- f[2] <- 1;
        for i <- 3 to n
            f[i] <- f[i - 1] + f[i - 2];  # 코드2
        return f[n];
    }
    '''
    
    f = [0]*(41)
    f[1] = f[2] = 1
    code_result_1 = 0
    code_result_2 = 0

    def fib(n):
        nonlocal code_result_1
        if n == 1 or n == 2:
            code_result_1 += 1
            return 1
        else:
            return (fib(n - 1) + fib(n - 2))

    def fibonacci(n):
        nonlocal code_result_2
        for i in range(3, n + 1):
            code_result_2 += 1
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
    
    n = int(input())
    fib(n)
    fibonacci(n)
    print(code_result_1, code_result_2)
solution()