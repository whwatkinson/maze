from random import randint, getrandbits, choice
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
            maze_height: int,
            maze_width: int,
            number_of_walls: int = 10,
            max_wall_length: int = 5
    ):
        self.maze_height = maze_height
        self.maze_width = maze_width
        self.number_of_walls = number_of_walls
        self.max_wall_length = max_wall_length
        self.walls_meta = self.get_walls_meta()

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
    def narnia(x: int, y: int, wall_length: int,  temporal: int) -> bool:
        """
        Is there a door, deterministic with the illusion of randomness
        :param x:
        :param y:
        :param wall_length:
        :param temporal:
        :return:
        """

        if wall_length < 3:
            return False

        # Combine coords to get unique identifier
        lucy = (x + y) % 4
        edmund = temporal % 8
        aslan = True if (lucy == 0 and edmund == 0) else False

        return aslan

    def determine_wall_upper_bound(
            self, vertical: bool, wall_length: int
    ) -> Tuple[int, int]:
        """
        Get the upper bound for the wall to be placed on the maze.
        :param vertical:
        :param wall_length:
        :return:
        """

        if vertical:

            try:
                x = randint(1, self.maze_height - wall_length - 1)
            except ValueError:
                x = 1
            y = randint(1, self.maze_width - 1)

        else:

            x = randint(1, self.maze_height - 1)
            try:
                y = randint(1, self.maze_width - wall_length - 1)
            except ValueError:
                y = 1

        return x, y

    def get_walls_meta(self) -> List[WallMeta]:
        """
        Generates a list of WallMeta tuples
        :return: A list of wall_metas
        """

        walls_meta = []

        # No list comp as need x and y vars
        for _ in range(self.number_of_walls):

            # Vertical
            vertical = bool(getrandbits(1))

            # Length of wall
            wall_length = randint(1, self.max_wall_length)

            # Wall starting coordinates
            x, y = self.determine_wall_upper_bound(vertical, wall_length)

            # Get the wall coordinates
            wall_coords = self.get_wall_coords(vertical, wall_length, x, y)

            # Is there a door? If so unlinkely!
            temporal = datetime.now().second
            is_door = self.narnia(x, y, wall_length, temporal)

            # Door coords
            door_coords = choice(wall_coords) if is_door else None

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
