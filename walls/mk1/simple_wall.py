from random import randint
from typing import Tuple, List
from collections import namedtuple

WallMeta = namedtuple('WallMeta', [
    "vertical",
    "wall_length",
    "x",
    "y",
    "wall_coords"
])


class SimpleWall:

    def __init__(
            self,
            height: int,
            width: int,
            number_of_walls: int = 10,
            max_wall_length: int = 5
    ):
        self.number_of_walls = number_of_walls
        self.max_wall_length = max_wall_length
        self.walls_meta = self.get_walls_meta(
            height=height,
            width=width,
            max_wall_length=max_wall_length
        )

    @staticmethod
    def get_wall_coords(
            vertical: bool, length: int, x: int, y: int
    ) -> List[Tuple[int, int]]:
        """
        As it says on the tin
        :param vertical: Is the wall vertical
        :param length: The length of the wall
        :param x: The x coordinate
        :param y: The y coordinate
        :returns: The
        """

        wall_coords = []

        for _ in range(length):
            wall_coords.append((x, y))
            if vertical:
                x += 1
            else:
                y += 1

        return wall_coords

    def get_walls_meta(
            self, height: int, width: int, max_wall_length: int
    ) -> List[WallMeta]:
        """
        Generates a list of wall objects
        :param height: The height of the maze
        :param width: The width of the maze
        :param max_wall_length: The length of the maze
        :return: A list of wall_metas
        """

        walls_meta = []

        # TODO namedtuple?
        # No list comp as need x and y vars
        for _ in range(self.number_of_walls):

            # Vertical
            vertical = bool(randint(0, 1))

            # Length of wall
            wall_length = randint(1, max_wall_length)

            # x coordinate
            x = randint(1, height - 1)

            # y coordinate
            y = randint(1, width - 1)

            wall_coords = self.get_wall_coords(vertical, wall_length, x, y)

            wm = WallMeta(
                vertical=vertical,
                wall_length=wall_length,
                x=x,
                y=y,
                wall_coords=wall_coords
            )
            walls_meta.append(wm)

        return walls_meta

    def __repr__(self):
        return f"|SIMPLE_WALL| (number_of_walls: {self.number_of_walls})"
