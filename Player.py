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

    """ This method will make sure that the user inputted valid coordinates
        Column needs to be A-J
        Row needs to be 1-10
    """
    def check_coordinates(self, coordinate):
        valid_rows = ['a','b','c','d','e','f','g','h','i', 'j']
        if coordinate[0] not in valid_rows:
            print "Input a letter A-J"
            return -1
        elif coordinate[1] < 1 or coordinate[1] >= 11:
            print "Enter a number between 1 and 10"
            return -1
        else:
            return 1

    """ This menu will only show which pieces you haven't put on the board yet
        Need to set it up so that the player can edit pieces already on the board
    """
    def display_menu(self):
        print"Enter the number of the ship you want to add to the board"
        if len(self.pieces[0].coordinates) == 0:
            print"1. Aircraft"
        if len(self.pieces[1].coordinates) == 0:
            print"2. Battleship"
        if len(self.pieces[2].coordinates) == 0:
            print"3. Submarine"
        if len(self.pieces[3].coordinates) == 0:
            print"4. Destroyer"
        if len(self.pieces[4].coordinates) == 0:
            print"5. Patrol Boat"
        option = raw_input("Number: ");
        return option


class User(Player):
    def __init__(self, name):
        Player.__init__(self, name)
    def __repr__(self):
        return Player.__repr__(self)

    def print_board(self):
        self.opponent_board.print_board()


    """ This method will ask the user what ship they'd like to place so it can assign the coordinates to the right ship
        It will show the board so the user will be able to see where their ships are placed
        uses the helper method getCoordinates
        Will loop 5 times to place the 5 ships
        Does not have error checking yet - still need to be implemented
    """
    def place_ships(self):
        num_of_ships = 0
        while(num_of_ships < 2):
            option = self.display_menu()
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
            #look for the correct piece to add the coordinates and get user's coordinates
            for piece in self.pieces:
                if piece.name == ship:
                    coordinate = self.get_user_coordinate(times)
                    #assign the coordinates to that Piece Object
                    piece.assign_coordinates(coordinate)
                    self.player_board.place_pieces_on_board(piece.coordinates, 'user')
            #end of for loop
            num_of_ships += 1
        #end of while loop
        #self.player_board.print_board()


    """ Gets the coordinates from the user for their ships.
        Asks for the coordinates in this format: A3
        Returns a list of coordinates for a particular piece
    """
    def get_user_coordinate(self, times):
        valid_input = False
        list_of_coordinates = []
        for number in range(times):
            valid_input = False
            while(valid_input != True):
                coordinates = []
                input = raw_input("Enter a coordinate(ex. A8): ")
                coordinates.append(input[0].lower())
                coordinates.append(int(input[1:]))
                if(self.check_coordinates(coordinates) == 1):
                    list_of_coordinates.append(coordinates)
                    valid_input = True
            #end while
        #end for
        return list_of_coordinates

    def fire(self):
        print "Time to Attack!!!!"
        guess = raw_input("Enter a spot to attack (Ex: A8): ")
        coordinate = []
        coordinate.append(guess[0].lower())
        coordinate.append(int(guess[1:]))
        if(self.check_coordinates(coordinate) == 1):
            return coordinate
        return None

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
        #self.player_board.print_board()
    def fire(self):
        print "Computer, it's time to Attack!!!!"
