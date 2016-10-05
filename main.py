from Player import Player
from Board import Board
from Player import User
from Player import Computer

player1 = User("Raina")
print player1
computer1 = Computer("Computer1")
print computer1

#user board and computer board
user_board = Board()
computer_board = Board()

player1.place_ships()
computer1.assign_pieces()

user_board = player1.player_board
computer_board = computer1.player_board

user_board.print_board()
computer_board.print_board()

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



for count in range(2):
    coordinate = []
    coordinate = player1.fire()
    if computer_board.board[2][1] == "C":
        print "Yay!"
