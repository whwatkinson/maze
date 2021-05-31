from random import randint
from typing import Tuple, List

from mazes.mk1 import SimpleMaze


class SimpleWall:

    markers = {
        'wall': 'w'
    }

    def __init__(self, height: int, width: int, number_of_walls: int = 10):
        self.number_of_walls = number_of_walls
        self.wall_meta = self.get_walls(height=height, width=width)

    @staticmethod
    def get_wall_coords(v: bool, length: int, x: int, y: int) -> List[Tuple[int, int]]:

        wall_coords = []

        for _ in range(length):
            wall_coords.append((x, y))
            if v:
                y += 1
            else:
                x += 1

        return wall_coords

    def get_walls(self, height: int, width: int) -> List[dict]:

        wall_meta = []

        for _ in range(self.number_of_walls):

            # Vertical
            v = bool(randint(0, 1))

            # Length of wall
            length = randint(1, 4)

            # x coordinate
            x = randint(1, width - length)

            # y coordinate
            y = randint(1, height - length)

            wall_coors = self.get_wall_coords(v, length, x, y)

            wall_meta.append({"v": v, "length": length, "x": x, "y": y, "wall_coors": wall_coors})

        return wall_meta

    def place_walls(self, height: int, width: int) -> SimpleMaze:

        simple_maze = SimpleMaze(height=height, width=width)

        for wall in self.wall_meta:

            for a, b in wall['wall_coors']:

                simple_maze.maze[a if a != width else a - 1][b if b != height else b - 1] = self.markers['wall']

        return simple_maze

    def __repr__(self):
        return f"SIMPLE_WALL (number_of_walls: {self.number_of_walls})"
