def valid(quiz):
    quiz = quiz.replace('=', '==')
    return eval(quiz)

def solution(quizs):
    return ["O" if valid(quiz) else "X" for quiz in quizs]