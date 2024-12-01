import unittest
from game_of_life import GameOfLife

"""
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
"""


class TestGameOfLife(unittest.TestCase):

    def test_if_mid_cell_with_0_neighbors_dies(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],  # the one alive
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_if_mid_cell_with_1_neighbor_dies(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_if_mid_cell_with_2_neighbors_survives(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_if_mid_cell_with_3_neighbors_survives(self):
        expected = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_if_mid_cell_with_4_neighbors_dies(self):  # todo loop from 4 to 8 here ?
        expected = [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_if_dead_mid_cell_with_exactly_3_neighbors_becomes_alive(self):
        expected = [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run()
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_the_pattern_moves_diagonally_in_4_iterations(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run(4)
        actual = gol.grid

        self.assertEqual(actual, expected)

    def test_the_stable_pattern_in_many_iterations(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        gol = GameOfLife(grid)
        gol.run(3)
        actual = gol.grid

        self.assertEqual(actual, expected)