
import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print("----------------")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(""+ board[i][j]+"|",end="")
        print()
        print("----------------")
    pass

def welcome(board):
    print("Welcome to Noughts and Crosses!")
    draw_board(board)

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

def get_player_move(board):
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter column (0, 1, 2): "))
    while board[row][col] != ' ':
        print("Cell is already occupied. Choose another cell.")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
    return row, col

def choose_computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return i, j

def check_for_win(board, mark):
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return



def menu():
    choice = input("Enter 1 to play the game, 2 to save score, 3 to load and display scores or q to end the program: ")
    return choice

def load_scores():
    leaders = {}
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                leaders[name] = int(score)
    except FileNotFoundError:
        pass
    return leaders

def save_score(score):
    name = input("Enter your name: ")
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{score}\n")

def display_leaderboard(leaders):
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    print("\nLeaderboard:")
    for i, (name, score) in enumerate(sorted_leaders):
        print(f"{i + 1}. {name}: {score}")



def main():
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return
if __name__ == '__main__':
    main()