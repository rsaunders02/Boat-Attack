class Board():
    def __init__(self):
        self.letters_to_columns = {"a":1, "b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}
        #set up board
        self.board = [["0" for 11 in range(11)] for 11 in range(11)]
        self.board[0][1] = "1"
        self.board[0][2] = "2"
        self.board[0][3] = "3"
        self.board[0][4] = "4"
        self.board[0][5] = "5"
        self.board[0][6] = "6"
        self.board[0][7] = "7"
        self.board[0][8] = "8"
        self.board[0][9] = "9"
        self.board[0][10] = "10"
        self.board[1][0] = "A"
        self.board[2][0] = "B"
        self.board[3][0] = "C"
        self.board[4][0] = "D"
        self.board[5][0] = "E"
        self.board[6][0] = "F"
        self.board[7][0] = "G"
        self.board[8][0] = "H"
        self.board[9][0] = "I"
        self.board[10][0] = "J"

    """ This method passes the coordinates of a ship to the
        method and places the pieces on the board.
    """
    def place_pieces_on_board(self, coordinates, player):
        number_of_coordinates = len(coordinates)
        index = 0
        if(player == 'user'):
            for coordinate in range(number_of_coordinates):
                item = coordinates[coordinate]
                self.player_board[self.letters_to_columns.get(item[0])][item[1]] = "S"
                index += 1
        else:
            for coordinate in range(number_of_coordinates):
                item = coordinates[coordinate]
                self.player_board[self.letters_to_columns.get(item[0])][item[1]] = "C"
                index += 1


    """ Prints the board """
    def print_board(self):
        for row in self.player_board:
            print " ".join(row)
