from copy import deepcopy


class GameOfLife:
    GRID_SIZE = 5
    DEAD = 0
    ALIVE = 1
    NEIGHBORS_TO_BECOME_ALIVE = 3
    LEAST_NEIGHBOURS_TO_STAY_ALIVE = 2
    MAX_NEIGHBOURS_TO_STAY_ALIVE = 3

    def __init__(self, grid=None):
        # todo: _validate_externally_provided_grid first ?
        self.grid = grid or self._generate_grid()

    def run(self, iterations=1):
        """
        state of the grid cannot be calculated in O1 time based on number of
        iterations because not mathematically possible, that's why loop needed
        """
        for _ in range(iterations):
            old_grid = deepcopy(self.grid)

            for r in range(len(self.grid)):
                for c in range(len(self.grid[0])):
                    self._process_next_state_of_cell(
                        old_grid=old_grid, current_cell_coordinates=(r, c),
                    )

    def _process_next_state_of_cell(self, old_grid, current_cell_coordinates):
        r, c = current_cell_coordinates
        current_cell = old_grid[r][c]
        neighbours = self._get_alive_neighbours_count_of_cell(old_grid, current_cell_coordinates)
        if not self._is_cell_alive(current_cell) and neighbours == self.NEIGHBORS_TO_BECOME_ALIVE:
            self._born_cell(coordinates=(r, c))
        elif self._is_cell_alive(current_cell) and (
                neighbours < self.LEAST_NEIGHBOURS_TO_STAY_ALIVE or
                neighbours > self.MAX_NEIGHBOURS_TO_STAY_ALIVE
        ):
            self._kill_cell(coordinates=(r, c))

        return

    def _born_cell(self, coordinates):
        r, c = coordinates
        self.grid[r][c] = self.ALIVE

    def _kill_cell(self, coordinates):
        r, c = coordinates
        self.grid[r][c] = self.DEAD

    def _get_alive_neighbours_count_of_cell(self, grid, current_cell_coordinates):
        r, c = current_cell_coordinates
        alive = 0
        alive += self._get_a_neighbour_cell_val(grid, r - 1, c)
        alive += self._get_a_neighbour_cell_val(grid, r + 1, c)
        alive += self._get_a_neighbour_cell_val(grid, r, c - 1)
        alive += self._get_a_neighbour_cell_val(grid, r, c + 1)

        alive += self._get_a_neighbour_cell_val(grid, r - 1, c - 1)
        alive += self._get_a_neighbour_cell_val(grid, r + 1, c + 1)
        alive += self._get_a_neighbour_cell_val(grid, r - 1, c + 1)
        alive += self._get_a_neighbour_cell_val(grid, r + 1, c - 1)
        return alive

    @staticmethod
    def _get_a_neighbour_cell_val(grid, r, c):
        try:
            return grid[r][c]
        except IndexError:
            return 0

    def _is_cell_alive(self, cell_val):
        return cell_val == self.ALIVE

    def _generate_grid(self):
        return [[self.DEAD] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

    def __str__(self):
        rows = []
        for row in self.grid:
            rows.append("  ".join("1" if cell == self.ALIVE else "0" for cell in row))
        return "\n".join(rows)
