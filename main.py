from Player import Player
from Player import User
from Player import Computer

player1 = User("Raina")
print player1
computer1 = Computer("Computer1")
print computer1

#print player1 ship coordinates
player1.place_ships()
print "pieces[0]: " + str(player1.pieces[0].coordinates)
print "pieces[1]: " + str(player1.pieces[1].coordinates)
print "pieces[3]: " + str(player1.pieces[2].coordinates)
print "pieces[4]: " + str(player1.pieces[3].coordinates)
print "pieces[5]: " + str(player1.pieces[4].coordinates)


#print computer ship coordinates
computer1.assign_pieces()
print "pieces[0]: " + str(computer1.pieces[0].coordinates)
print "pieces[1]: " + str(computer1.pieces[1].coordinates)
print "pieces[3]: " + str(computer1.pieces[2].coordinates)
print "pieces[4]: " + str(computer1.pieces[3].coordinates)
print "pieces[5]: " + str(computer1.pieces[4].coordinates)

for count in range(5):
    player1.fire()
    computer1.fire()
