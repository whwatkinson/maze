from random import randint,getrandbits
from typing import Tuple, List
from collections import namedtuple
from datetime import datetime


WallMeta = namedtuple('WallMeta', [
    "vertical",
    "wall_length",
    "x",
    "y",
    "wall_coords",
    "is_door",
    "door_coords"
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

        # TODO add a check for min number of walls if wift/ height is too small

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
        :return: The coordinates of the wall
        """

        wall_coords = []

        for _ in range(length):
            wall_coords.append((x, y))
            if vertical:
                x += 1
            else:
                y += 1

        return wall_coords

    @staticmethod
    def narnia(x: int, y: int, temporal: int = None) -> bool:
        """
        Is there a door, deterministic with the illusion of randomness
        :param x:
        :param y:
        :param temporal:
        :return:
        """

        # Combine coords to get unique identifier
        if not temporal:
            temporal = datetime.now().second

        lucy = (x + y) % 4
        edmund = temporal % 8
        aslan = True if (lucy == 0 and edmund == 0) else False

        return aslan

    def get_walls_meta(
            self, height: int, width: int, max_wall_length: int
    ) -> List[WallMeta]:
        """
        Generates a list of WallMeta tuples
        :param height: The height of the maze
        :param width: The width of the maze
        :param max_wall_length: The length of the maze
        :return: A list of wall_metas
        """

        walls_meta = []

        # No list comp as need x and y vars
        for _ in range(self.number_of_walls):

            # Vertical
            vertical = bool(getrandbits(1))

            # Length of wall
            wall_length = randint(1, max_wall_length)

            # x coordinate
            x = randint(1, height - 1)

            # y coordinate
            y = randint(1, width - 1)

            # Get the wall coordinates
            wall_coords = self.get_wall_coords(vertical, wall_length, x, y)

            # Is there a door? If so unlinkely!
            is_door = self.narnia(x, y)

            # Door coords
            door_coords = None

            wm = WallMeta(
                vertical=vertical,
                wall_length=wall_length,
                x=x,
                y=y,
                wall_coords=wall_coords,
                is_door=is_door,
                door_coords=door_coords
            )
            walls_meta.append(wm)

        return walls_meta

    def __repr__(self):
        """The goal is to be unambiguous."""
        return f"|SIMPLE_WALL| (number_of_walls: {self.number_of_walls})"
