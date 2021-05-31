from random import randint
from typing import Tuple, List

from mazes.mk1 import SimpleMaze

s = SimpleMaze()


class SimpleWall:

    markers = {
        'wall': 'w'
    }

    def __init__(self, number_of_walls: int = 5):
        self.number_of_walls = number_of_walls

    def get_walls(self) -> List[Tuple[int, int, int, bool]]:

        wall_coords = []

        for _ in range(self.number_of_walls):

            a = randint(0, 3)

            b = randint(0, 3)

            c = randint(0, 3)

            d = bool(randint(0, 1))

            wall_coords.append((a, b, c, d))

            return wall_coords

    def __repr__(self):
        return f"SIMPLE_WALL (number_of_walls: {self.number_of_walls})"
