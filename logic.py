class Cell:
    def __init__(self,x_coord,y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


class Color:
    white = 1
    black = -1


class Checker:
    def __init__(self,cell,color):
        self.cell = cell
        self.color = color
