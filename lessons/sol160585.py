def finished(board, player):
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[0][2]==board[1][1]==board[2][0]==player:
        return True
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]==player:
            return True
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True
    return False

def solution(board):
    O_count, X_count = 0, 0
    for line in board:
        for blank in line:
            if blank=='O':
                O_count+=1
            elif blank=='X':
                X_count+=1
    board_value = [i for li in board for i in li]
    if (set(board_value) == {"X"}) or (set(board_value)=={".", "X"}):
        return 0
    diff = O_count - X_count
    if diff not in [0, 1]:
        return 0    
    if finished(board, 'O'):
        if diff!=1:
            return 0
        else:
            if finished(board, 'X'):
                return 0
    if finished(board, 'X'):
        if diff!=0:
            return 0
    return 1