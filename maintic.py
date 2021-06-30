#tic tac toe
board= ["-","-","-",   #board design
        "-","-","-",
        "-","-","-"]

#if game is going now
game_still_going = True

#who won or tie

winner = None

#whose turn

current_player = "X"



def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "   1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "   4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "   7 | 8 | 9")


def play_game():

    global current_player
    global winner

    display_board()  #display initial board

    while game_still_going:

        handle_turn(current_player)   #handle the turn when game is going

        check_if_game_over()

        flip_player()

         # game has ended
        if winner == "X" or winner == "O":
            print(winner, "is the winner")
        elif "-" not in board and winner == None:
            print("It's a Tie")




# Handle a turn for an arbitrary player
def handle_turn(player):
    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


def check_if_game_over():

    check_for_winner()
    check_for_tie()




def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going= False

        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        else:
            return None


def check_cols():

    global game_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going= False

        if col_1:
            return board[0]
        elif col_2:
            return board[1]
        elif col_3:
            return board[2]
        else:
            return None


def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_dia()
    diagonal_winner = check_dia()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_dia():

    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"

    if diag_1 or diag_2:
        game_still_going= False
        if diag_1:
            return board[0]
        elif diag_2:
            return board[6]
        else:
            return None


def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


def flip_player():    #dynamically changing the player.

    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


#to start the game

play_game()


