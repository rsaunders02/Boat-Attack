from Piece import Piece
from Board import Board

class Player():
    def __init__(self, name):
        self.name = name                 #player name
        self.wins = 0                    #number of wins
        self.losses = 0                  #number of losses
        self.pieces = []                 #a list of Piece objects.
        self.opponent_board = Board()    #blank board for the player to see where it's hitting
        self.player_board = Board()      #the Player's board

        #set up individual pieces in the Piece object array
        self.pieces.append(Piece("Aircraft Carrier", 5))
        self.pieces.append(Piece("Battleship", 4))
        self.pieces.append(Piece("Submarine", 3))
        self.pieces.append(Piece("Destroyer", 3))
        self.pieces.append(Piece("Patrol Boat", 2))

    def __repr__(self):
        return 'Name: %s\nWins: %d\nLosses: %d\nNumber of Pieces: %d' % (
        self.name, self.wins, self.losses, len(self.pieces))

    """ This will double check the computer or user's guess
    """
    def check_guess(self, player):
        pass

    """ This method will ask the user to enter coordinates. It will make sure
        that the letter is between A-J and the number is between
        1-10.
        returns: a list of coordinate ['a', 1]
    """
    def check_coordinates(self, coordinates):
        valid_rows = ['a','b','c','d','e','f','g','h','i', 'j']
        if letter in valid_rows:
            print "correct"
        else:
            print "Input a letter A-J"
            return -1
        if number > 0 and number < 11:
            print "correct"
        else:
            print "Enter a number 1-10"
            return -1
        return 1


class User(Player):
    def __init__(self, name):
        Player.__init__(self, name)
    def __repr__(self):
        return Player.__repr__(self)


    """ This method will ask the user what ship they'd like to place so it can assign the coordinates to the right ship
        It will show the board so the user will be able to see where their ships are placed
        uses the helper method getCoordinates
        Will loop 5 times to place the 5 ships
        Does not have error checking yet - still need to be implemented
    """
    def place_ships(self):
        num_of_ships = 0
        ship = ""
        while(num_of_ships < 2):
            option = raw_input("Enter a number for the ship you'd like to place:\n1: Aircraft Carrer\t*****\n2: BattleShip\t****\n3: Submarine\t***\n4: Destoyer\t***\n5: Patrol Boat\t**\nNumber: ")
            if option == "1":
                ship = "Aircraft Carrier"
                times = 5
            elif option == "2":
                ship = "Battleship"
                times = 4
            elif option == "3":
                ship = "Submarine"
                times = 3
            elif option == "4":
                ship = "Destroyer"
                times = 3
            elif option == "5":
                ship = "Patrol Boat"
                times = 2
            else:
                print "Input a number 1-5"
                continue
            #look for the correct piece to add the coordinates
            for piece in self.pieces:
                if piece.name == ship:
                    #get coordinates from player
                    coordinate = self.getUserCoordinates(times)
                    #assign the coordinates to the piece
                    piece.assign_coordinates(coordinate)
                    self.player_board.place_pieces_on_board(piece.coordinates, 'user')
            #end of for loop
            valid_input = 0
            num_of_ships += 1
        #end of while loop
        self.player_board.print_board()


    """ Gets the coordinates from the user for their ships.
        Asks for the coordinates in this format: A3
        Makes sure
    """
    def getUserCoordinates(self, times):
        valid_input = False
        list_of_coordinates = []
        for x in range(times):
            while(valid_input != True):
                coordinates = []
                coordinates = raw_input("Enter a coordinate(ex. A8): ")
                letter = coordinates[0].lower()
                number = int(coordinates[1:])
                if(self.check_coordinates(coordinates) == 1):
                    list_of_coordinates.append(coordinates)
                    valid_input = True
            #end while
        #end for
        return list_of_coordinates

    def fire(self):
        print "Time to Attack!!!!"
        #coordinates = self.validate_coordinates()
        #self.check_guess(coordinates, 'user')

class Computer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
    def __repr__(self):
        return Player.__repr__(self)

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
        self.player_board.print_board()
    def fire(self):
        print "Computer, it's time to Attack!!!!"
