from Player import Player
from Board import Board
from Player import User
from Player import Computer

player1 = User("Raina")
print player1
computer1 = Computer("Computer1")
print computer1

#both players place their ships on their respective board
player1.place_ships()
computer1.assign_pieces()

"""print the board to double check
print "Program's board of player 1"
user_board.print_board()
print "Program's board of computer's board"
computer_board.print_board()"""
print "Player 1's own board"
player1.player_board.print_board()
print "Player 1's oppoenent's board"
player1.opponent_board.print_board()


"""print player1 ship coordinates
print "pieces[0]: " + str(player1.pieces[0].coordinates)
print "pieces[1]: " + str(player1.pieces[1].coordinates)
print "pieces[3]: " + str(player1.pieces[2].coordinates)
print "pieces[4]: " + str(player1.pieces[3].coordinates)
print "pieces[5]: " + str(player1.pieces[4].coordinates)
#print computer ship coordinates
print "pieces[0]: " + str(computer1.pieces[0].coordinates)
print "pieces[1]: " + str(computer1.pieces[1].coordinates)
print "pieces[3]: " + str(computer1.pieces[2].coordinates)
print "pieces[4]: " + str(computer1.pieces[3].coordinates)
print "pieces[5]: " + str(computer1.pieces[4].coordinates)"""

count = 0
while count < 5:
    print "Here. Take a look at your progress"
    print player1.opponent_board.print_board()
    coordinate = []
    guess, coordinate = player1.fire()
    print "guess: ", guess
    if guess in computer1.coordinate_dict:
        if player1.opponent_board.mark(coordinate, "H") == False:
            print "You already guessed there!"
        else:
            count += 1
            print "Hit!"
            piece = computer1.coordinate_dict[guess]    #grab piece Object that corresponds to that guess
            piece.hit()
            player1.opponent_board.mark(coordinate, "H")
            if piece.isSunk() == True:
                print "You sunk my battleship!"
    else:
        if player1.opponent_board.mark(coordinate, "M") == False:
            print "You already guessed there!"
        else:
            count += 1
            print "Aww nice try"
