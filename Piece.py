################################################################################
# This is the Piece class. This holds information related to a piece including
# the coordinates, if it's sunk or not, it will update the size when it's been
# hit, etc

#Author: Raina
#Last Updated: 12/17/16
#Update: added an attribute that says whether the coordinates for the Piece
#        has been set.
################################################################################

class Piece():
    ###########################################
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []
        self.sunk = False
        self.isSet = False
    ###########################################
    def assign_coordinates(self,coordinates):
        self.coordinates = coordinates
        self.isSet = True
    ###########################################
    def get_coordinates(self):
        return self.coordinates
    ###########################################
    def hit(self):
        self.size -= 1
    ###########################################
    def isSunk(self):
        if self.size == 0:
            return True
        return False
    ###########################################
