import random
board = [' ' for _ in range(9)]

def display_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('---------')

def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return 1
    if check_win(board, 'O'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
# AI makes moves
def ai_move():
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main 
while True:
    display_board()
    
    # Player's move
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
        board[player_move] = 'O'
    else:
        print("Invalid move. Try again.")
        continue
    
    if check_win(board, 'O'):
        display_board()
        print("You win!")
        break

    if is_full(board):
        display_board()
        print("It's a draw!")
        break
    # AI's move
    ai_move_index = ai_move()
    board[ai_move_index] = 'X'
    
    if check_win(board, 'X'):
        display_board()
        print("AI wins!")
        break
    if is_full(board):
        display_board()
        print("It's a draw!")
        break
