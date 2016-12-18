################################################################################
# This is the player class. Two classes will inherit from this base class.
# User class and Computer class

#Author: Raina
#Last Updated: 12/17/16
#Update: changed a couple function functionality.
################################################################################


from Piece import Piece
from Board import Board

class Player():
    ###########################################
    def __init__(self, name):
        self.name = name                 #player name
        self.wins = 0                    #number of wins
        self.losses = 0                  #number of losses
        self.pieces = []                 #a list of Piece objects.
        self.opponent_board = Board()    #blank board for the player to see where it's hitting
        self.player_board = Board()      #the Player's board
        self.coordinate_dict= {}         #maps the coordinates to a ship

        #set up individual pieces in the Piece object array
        self.pieces.append(Piece("Aircraft Carrier", 5))
        self.pieces.append(Piece("Battleship", 4))
        self.pieces.append(Piece("Submarine", 3))
        self.pieces.append(Piece("Destroyer", 3))
        self.pieces.append(Piece("Patrol Boat", 2))
    ###########################################
    def __repr__(self):
        return 'Name: %s\nWins: %d\nLosses: %d\nNumber of Pieces: %d' % (
        self.name, self.wins, self.losses, len(self.pieces))
    ###########################################
    """ This method will make sure that the user inputted valid coordinates
        Column needs to be A-J
        Row needs to be 1-10
    """
    def check_coordinates(self, coordinate):
        valid_rows = ['a','b','c','d','e','f','g','h','i', 'j']
        if coordinate[0] not in valid_rows:
            print "Input a letter A-J"
            return False
        elif coordinate[1] < 1 or coordinate[1] >= 11:
            print "Enter a number between 1 and 10"
            return False
        else:
            return True
    ###########################################
    def getPiece(self, number):
        return self.pieces[number];
    ###########################################
    def setname(self, name):
        self.name = name;
    ###########################################
    def showOwnBoard(self):
        self.player_board.print_board()

################################################################################
class User(Player):
    ###########################################
    def __init__(self, name):
        Player.__init__(self, name)
    ###########################################
    def __repr__(self):
        return Player.__repr__(self)
    ###########################################
    def showOpponentBoard(self):
        self.opponent_board.print_board()

    ###########################################
    """ This method will ask the user what ship they'd like to place so it can assign the coordinates to the right ship
        It will show the board so the user will be able to see where their ships are placed
        uses the helper method getCoordinates
        Will loop 5 times to place the 5 ships
        Does not have error checking yet - still need to be implemented
    """
    def choose_coordinates(self, option):
        print "placing coordinates"
        #initial variables
        ship = ""
        times = 0
        if option == 1:
            ship = "Aircraft Carrier"
            times = 5
        elif option == 2:
            ship = "Battleship"
            times = 4
        elif option == 3:
            ship = "Submarine"
            times = 3
        elif option == 4:
            ship = "Destroyer"
            times = 3
        elif option == 5:
            ship = "Patrol Boat"
            times = 2
        #look for the correct piece to add the coordinates and get user's coordinates
        piece = self.pieces[option -1]
        list_of_coordinates = []
        for guess in xrange(times):
            list_of_coordinates.append(self.get_user_coordinate(option-1))
        piece.assign_coordinates(list_of_coordinates)   #assign the coordinates to the piece
        self.player_board.place_pieces_on_board(list_of_coordinates, "user")

    """ Gets the coordinates from the user for their ships.
        Expected format: A3 (need to add more flexibility for user input)
        separates the letter and number to check if they are valid placements on the board
        adds the coordinate and key to a dictionary <coordinate, piece>
    """
    ###########################################
    def get_user_coordinate(self, index):
        valid_input = False
        coordinates = []
        while(valid_input != True):
            user_input = raw_input("Enter a coordinate(ex. A8): ")
            coordinates.append(user_input[0].lower())
            coordinates.append(int(user_input[1:]))
            if(self.check_coordinates(coordinates) == True):
                self.coordinate_dict[user_input] = self.pieces[index]   #add to player's dictionary
                #print "dictionary: ", self.coordinate_dict[user_input].name
                valid_input = True
            else:
                print "try again...\n"
        return coordinates
    ###########################################
    def fire(self):
        print "Time to Attack!!!!"
        guess = raw_input("Enter a spot to attack (Ex: A8): ")
        coordinate = []
        coordinate.append(guess[0].lower())
        coordinate.append(int(guess[1:]))
        if self.check_coordinates(coordinate) == True:
            return guess, coordinate
        return None
################################################################################
# ******This class needs a lot of work. Focusing on User class right now*******#
class Computer(Player):
    ###########################################
    def __init__(self, name):
        Player.__init__(self, name)
    ###########################################
    def __repr__(self):
        return Player.__repr__(self)
    ###########################################
    """ Assigning hard code input for computer ships for now
    """
    def assign_pieces(self):
        self.pieces[0].assign_coordinates([['b', 1], ['b', 2],['b', 3],['b', 4],['b', 5]])
        self.player_board.place_pieces_on_board(self.pieces[0].get_coordinates(), 'computer')
        self.pieces[1].assign_coordinates([['a', 1], ['b', 1],['c', 1],['d', 1]])
        self.player_board.place_pieces_on_board(self.pieces[1].get_coordinates(), 'computer')
        self.pieces[2].assign_coordinates([['e', 10], ['f', 10],['g', 10]])
        self.player_board.place_pieces_on_board(self.pieces[2].get_coordinates(), 'computer')
        self.pieces[3].assign_coordinates([['j', 5], ['j', 6],['j', 7]])
        self.player_board.place_pieces_on_board(self.pieces[3].get_coordinates(), 'computer')
        self.pieces[4].assign_coordinates([['f', 5], ['g', 5]])
        self.player_board.place_pieces_on_board(self.pieces[4].get_coordinates(), 'computer')
        #assign ship_coordinate dictoinary
        self.coordinate_dict["F5"] = self.pieces[4]
        self.coordinate_dict["G5"] = self.pieces[4]
        #self.player_board.print_board()
    ###########################################
    def fire(self):
        print "Computer, it's time to Attack!!!!"
