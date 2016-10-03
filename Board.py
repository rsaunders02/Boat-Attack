class Board():
    def __init__(self):
        self.board = []
        self.letters_to_columns = {"a":1, "b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}
        #set up board
        for row in range(11):
            for col in range(11):
                self.board.append("0")
        print self.board

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
