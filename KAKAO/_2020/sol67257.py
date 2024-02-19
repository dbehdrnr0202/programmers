import re
from itertools import permutations
def operate(op, a, b):
    if op=="+":
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
def solution(expression):
    answer = 0
    op_lists = list(permutations(['+','-','*'],3))
    expression = re.split("([^0-9])",expression)    
    for op_list in op_lists:
        exp = expression
        for op in op_list:
            s = []
            for term in exp:
                if s and s[-1]==op:
                    operation = s.pop()
                    s[-1] = operate(operation, int(s[-1]), int(term))
                else:
                    s.append(term)
            exp = s
        answer = max(answer, abs(exp[0]))
    return answer