class Piece():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []
        self.sunk = False

    def assign_coordinates(self,coordinates):
        self.coordinates = coordinates
    def get_coordinates(self):
        return self.coordinates
    def hit(self):
        self.size -= 1
    def isSunk(self):
        if self.size == 0:
            return True
        return False
