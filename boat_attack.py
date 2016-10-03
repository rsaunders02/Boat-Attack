from random import randint

""""this function sets up the board size.
    depending on the number of ships, the grid size
    is big or small

    returnns an int, grid_size
"""
def set_up_board(board, ships):
    grid_size = 0
    if ships > 0 and ships < 2:
        grid_size = 5
    elif ships >= 2 and ships < 5:
        grid_size = 10
    elif ships >= 5 and ships < 8:
        grid_size = 15
    for x in range(grid_size):
        board.append(["O"] * grid_size)
    return grid_size

def set_up_game(player, computer, board):
    name = raw_input("Enter your name: ")
    player['name'] = name
    player['wins'] = 0
    computer['wins'] = 0
    player['losses'] = 0
    computer['loses'] = 0
    player['safe_ships'] = number_of_ships
    computer['safe_ships'] = number_of_ships
    place_ships(board, number_of_ships, grid_size, "user", player)
    place_ships(board, number_of_ships, grid_size, "computer", computer)

def place_ships(board, ships, grid_size, player, info):
    turns = 0
    player_ships = []
    computer_ships = []
    while turns < ships:
        print "turns: " + str(turns)
        #place ships on the board
        if (player == "user"):
            row = int(raw_input("Enter a row number (0 - %d): " % (grid_size-1)))
            col = int(raw_input("Enter a column number (0 - %d): " % (grid_size-1)))
        elif (player == "computer"):
            row = randint(0, grid_size - 1)
            col = randint(0, grid_size - 1)
        #see if there is an item there
        if (board[row][col] == "S" or board[row][col] == "C"):
            print "you already put something there!"
        else:
            if (player == "user"):
                placement = [row, col]
                player_ships.append(placement)
                board[row][col] = "S"
            else:
                print "-------------------------------------"
                board[row][col] = "C"
                placement = [row, col]
                computer_ships.append(placement)
            turns+=1
            print_board(board)
    if (player == "user"):
        info['ships'] = player_ships
    else:
        info['ships'] = computer_ships

def player_guess(player, computer, board):
    #get user input
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    guess = [guess_row, guess_col]
    #winning guess
    if guess in computer['ships']:
        print "Congratulations! You sunk a battleship!"
        computer['safe_ships'] -= 1
        if (computer['safe_ships'] == 0):
            return True
    #wrong guess
    else:
        if (guess_row < 0 or guess_row >= len(board)) or (guess_col < 0 or guess_col >= len(board)):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Missed"
            board[guess_row][guess_col] = "X"
    return False

def computer_guess(player, computer, board):
    #get user input
    guess_row = randint(0, grid_size - 1)
    guess_col = randint(0, grid_size - 1)
    guess = [guess_row, guess_col]
    #winning guess
    if guess in player['ships']:
        print "The computer sunk one of your ships!"
        player['safe_ships'] -= 1
        if (computer['safe_ships'] == 0):
            return True
    #wrong guess
    else:
        if (board[guess_row][guess_col] == "M"):
            return False
        else:
            print "Missed"
            board[guess_row][guess_col] = "M"
        return False

def print_board(board):
    for row in board:
        print " ".join(row)

#----------------Main function--------------------#
#player dictionary
player = {}
computer = {}
board = []
print "Let's play Battleship!"
number_of_ships = int(raw_input("Enter # of ships: "))
grid_size = set_up_board(board, number_of_ships)
print_board(board)
option = int(raw_input("Enter how you would like to play\n1: Me vs Computer\n2: Me vs my friend\nOption: "))
set_up_game(player, computer, board)
print computer

#Give the player 4 turns to guess
print "You have 4 turns"
turns = 4
for turn in range(4):
    if(player_guess(player, computer, board)):
        print "You win!!"
        player['wins'] += 1
        break
    elif(player_guess == False):
        print "Computer wins!!"
        computer['wins'] += 1
        break
    turns -= 1
    print "You have %d more moves" % (turns)
    print_board(board)
