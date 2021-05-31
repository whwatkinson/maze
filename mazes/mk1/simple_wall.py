from random import randint
from typing import Tuple, List

from mazes.mk1 import SimpleMaze


class SimpleWall:

    markers = {
        'wall': 'w'
    }

    def __init__(self, number_of_walls: int = 5):
        self.number_of_walls = number_of_walls

    @staticmethod
    def get_wall_coords(x: int, y: int, length: int, v: bool) -> List[Tuple[int, int]]:

        wall_coords = []

        for _ in range(length):
            wall_coords.append((x, y))
            if v:
                y += 1
            else:
                x += 1

        return wall_coords

    def get_walls(self, height: int, width: int, ) -> List[Tuple[int, int, int, bool, List[Tuple[int, int]]]]:

        wall_meta = []

        for _ in range(self.number_of_walls):

            # x coordinate
            x = randint(1, height-1)

            # y coordinate
            y = randint(1, width-1)

            # Length of wall
            length = randint(1, 3)

            # Vertical
            v = bool(randint(0, 1))

            wall_coor = self.get_wall_coords(x, y, length, v)

            wall_meta.append((x, y, length, v, wall_coor))

        return wall_meta





    def place_walls(self, height: int, width: int) -> SimpleMaze:

        simple_maze = SimpleMaze(height=height, width=width)

        wall_meta = self.get_walls(height=height, width=width)

        for x, y in wall_meta:

            pass





        return simple_maze

    def __repr__(self):
        return f"SIMPLE_WALL (number_of_walls: {self.number_of_walls})"
