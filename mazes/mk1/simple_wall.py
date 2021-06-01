from random import randint
from typing import Tuple, List


class SimpleWall:

    markers = {
        'wall': 'w'
    }

    def __init__(self, height: int, width: int, number_of_walls: int = 10):
        self.number_of_walls = number_of_walls
        self.walls_meta = self.get_walls_meta(height=height, width=width)

    #  need check to not place on wall

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

    def get_walls_meta(self, height: int, width: int) -> List[dict]:

        walls_meta = []

        for _ in range(self.number_of_walls):

            # Vertical
            v = bool(randint(0, 1))

            # Length of wall
            length = randint(1, 4)

            # x coordinate
            x = randint(1, width - length)

            # y coordinate
            y = randint(1, height - length)

            wall_coords = self.get_wall_coords(v, length, x, y)

            walls_meta.append(
                {
                    "v": v,
                    "length": length,
                    "x": x,
                    "y": y,
                    "wall_coords": wall_coords
                }
            )

        return walls_meta

    def __repr__(self):
        return f"SIMPLE_WALL (number_of_walls: {self.number_of_walls})"
