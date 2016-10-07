class Board():
    def __init__(self):
        self.board = []
        for row in range(11):
            self.board.append(["O"] * 11)
        self.letters_to_columns = {"a":1, "b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}
        self.board[0][1] = '1'
        self.board[0][2] = '2'
        self.board[0][3] = '3'
        self.board[0][4] = '4'
        self.board[0][5] = '5'
        self.board[0][6] = '6'
        self.board[0][7] = '7'
        self.board[0][8] = '8'
        self.board[0][9] = '9'
        self.board[0][10] = '10'
        self.board[1][0] = 'A'
        self.board[2][0] = 'B'
        self.board[3][0] = 'C'
        self.board[4][0] = 'D'
        self.board[5][0] = 'E'
        self.board[6][0] = 'F'
        self.board[7][0] = 'G'
        self.board[8][0] = 'H'
        self.board[9][0] = 'I'
        self.board[10][0] = 'J'

    """ This method passes the coordinates of a ship to the
        method and places the pieces on the board.
    """
    def place_pieces_on_board(self, coordinates, player):
        number_of_coordinates = len(coordinates)
        #print "coordinates" + str(coordinates)
        if(player == 'user'):
            for index in range(number_of_coordinates):
                item = coordinates[index]
                #print "item" + str(item)
                self.board[self.letters_to_columns.get(item[0])][item[1]] = "S"
        else:
            for index in range(number_of_coordinates):
                item = coordinates[index]
                self.board[self.letters_to_columns.get(item[0])][item[1]] = "C"

    """ Prints the board """
    def print_board(self):
        for x in range(11):
            print " ".join(self.board[x])
    """ This method will check to see if the user's guess hits a ship or if it was a miss """
    def isHit(self, coordinate):
        if(self.board[self.letters_to_columns.get(coordinate[0])][coordinate[1]] == "C"):
            return True
        return False
    def mark(self, coordinate, letter):
        if(self.board[self.letters_to_columns.get(coordinate[0])][coordinate[1]] == letter):
            return False
        else:
            self.board[self.letters_to_columns.get(coordinate[0])][coordinate[1]] = letter
            return True
