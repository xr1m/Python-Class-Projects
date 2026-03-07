# Tic Tac Toe Game:

'''We will make the board using dictionary in which keys will be the location and initially it's values will be empty space and then after every move we will change the value according to player's choice of move'''

board = {"7": " ", "8": " ", "9": " ",
         "4": " ", "5": " ", "6": " ",
         "1": " ", "2": " ", "3": " "}

board_key = []
for key in board:
    board_key.append(key)

''' We will have to print the updated board after every move in the game and thus we will make a function in which we'll define the printBoard function so that we can easily print the board everytime by calling this function. '''

def print_board(theboard):
    print(theboard["7"] + "|" + theboard["8"] + "|" + theboard["9"])
    print("-+-+-")
    print(theboard["4"] + "|" + theboard["5"] + "|" + theboard["6"])
    print("-+-+-")
    print(theboard["1"] + "|" + theboard["2"] + "|" + theboard["3"])

def game():
    turn = "X"
    count = 0
    for i in range(10):
        print_board(board)
        print("It's your turn", turn, "Which place to move?")
        move = input()
        if board[move] == " ":
            board[move] = turn
            count = count+1
        else:
            print("That slot is already taken.")
            continue
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                print_board(board)
                print("\nGame Over.\n")

                print(" **** " +turn + " won. ****")
                break

            elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                print_board(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        if count == 9:
            print("Game Over, It's a Tie!")
        if turn == 'X':
            turn = "0"
        else:
            turn = "X"
    newstart = input("Do you want to play another game? (Y/N)")
    if newstart == "Y" or newstart == "y":
        for e in board_key:
            board[key] = " "
        game()
if __name__ == "__main__":
    game()