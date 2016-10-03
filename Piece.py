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
