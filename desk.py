import logic


class Color:
    black = 0
    white = 1


class Condition(Color):
    attack = 2
    move = 3
    empty = 4


class Desk:
    vertical_cell_quantity = 8
    horizontal_cell_quantity = 8

    quantity_of_white = 12
    quantity_of_black = 12
    turn = Color.white

    def __init__(self, cells):
        for row in range(self.horizontal_cell_quantity):
            for col in range(self.vertical_cell_quantity):
                if (row + col) % 2 != 0 and row < 2:
                    cells[row, col] = Condition.white
                elif (row + col) % 2 == 0 and row > 4:
                    cells[row, col] = Condition.black
                else:
                    cells[row, col] = Condition.empty

    def _is_in_desk_bounds(self, cell):
        return 0 <= cell.x_coord < self.vertical_cell_quantity and 0 <= cell.y_coord < self.horizontal_cell_quantity

    def _get_opposite_color(self, color):
        return Color.black if color == Color.white else Color.white

    def _get_condition_of_cell(self, cell):
        return self.cells[cell.x_coord, cell.y_coord]

    def _swap_player_turn(self):
        self.turn = self._get_opposite_color(self.turn)

    def _is_here_checker(self, cell):
        return self.cells[cell.x_coord,cell.y_coord] == Condition.black or self.cells[cell.x_coord,cell.y_coord] == Condition.white

    def _remove_checker(self, cell):
        self.cells[cell.x_coord,cell.y_coord] = Condition.empty

    def _move_checker(self, cell_from, cell_to):
        self.cells[cell_to.x_coord, cell_to.y_coord] = self._get_condition_of_cell(cell_from)
        self._remove_checker(cell_from)
