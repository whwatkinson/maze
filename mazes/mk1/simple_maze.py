from random import randint
from typing import List, Tuple
from collections import namedtuple


from walls.mk1.simple_wall import SimpleWall

Markers = namedtuple('Markers', [
    'top',
    'start',
    'side',
    'clear',
    'wall',
    'finish',
    'bottom',
    'path_taken',
    'out_of_bounds',
    'solver'
])


class SimpleMaze:

    markers = Markers(
        top='_',
        start='S',
        side='|',
        clear=' ',
        wall='W',
        finish='F',
        bottom='‾',
        path_taken='·',
        out_of_bounds='A',
        solver='%'
    )

    def __init__(
            self,
            height: int = 10,
            width: int = 10,
            number_of_walls: int = 10,
            level: int = 0
    ):

        if height < 3 or width < 3:
            raise ValueError(
                f'This maze is too small height: {height}, width {width}'
            )

        # OOP
        self.height = height
        self.width = width
        self.number_of_walls = number_of_walls
        self.level = level
        self.coords_start, self.coords_finish = self.get_start_finish_pos()
        self.blank_maze = self.get_blank_maze()
        self.walls = SimpleWall(
            height=self.height,
            width=self.width,
            number_of_walls=self.number_of_walls
        )
        self.simple_maze = self.place_walls()

    # TODO @property for start and end coords?

    def get_start_finish_pos(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """Get the postionion of the start and finish"""
        upper_bound = self.width - 2
        start_position = randint(1, upper_bound)
        finish_position = randint(1, upper_bound)

        coords_start = (0, start_position)
        coords_finish = (self.height - 1, finish_position)

        return coords_start, coords_finish

    def get_n_row(self) -> List[List[str]]:
        """Get the middle rows of the maze"""
        clear_markers_needed = self.width - 2
        # TODO: ugly can do better
        row_n = [
            [
                self.markers.side
            ] + [
                self.markers.clear for _ in range(clear_markers_needed)
            ] + [
                self.markers.side
            ]
        ]

        return row_n

    def get_blank_maze(self) -> List[List[str]]:
        """Get a new maze with walls"""
        # Get start and finish postions
        _, y_s = self.coords_start
        _, y_f = self.coords_finish

        # Get top row
        top = [self.markers.top for _ in range(self.width)]
        top[y_s] = self.markers.start
        maze = [top]

        # Get n middle rows
        rows_n_needed = self.height - 2
        for _ in range(rows_n_needed):
            maze += self.get_n_row()

        # Get bottom row
        bottom = [self.markers.bottom for _ in range(self.width)]
        bottom[y_f] = self.markers.finish
        maze += [bottom]

        return maze

    def ok_to_place_wall(
            self, blank_maze: List[List[str]], x: int, y: int) -> bool:
        """
        Checks the placement of the wall
        :param blank_maze:
        :param x: The x coordinate
        :param y: The y coordinate
        :return bool: Its all good man or not
        """
        if blank_maze[x][y] == self.markers.clear:
            if blank_maze[x-1][y] != self.markers.start:
                if blank_maze[x+1][y] != self.markers.finish:
                    return True
        else:
            return False

    def place_walls(self) -> List[List[str]]:
        """Place the walls on the maze"""
        walls_meta = self.walls.walls_meta
        new_blank_maze = [x.copy() for x in self.blank_maze]
        # Each row
        for wall in walls_meta:
            # Over each pair of coordinates
            for x, y in wall.wall_coords:

                try:
                    # TODO BETTER PLEASE, really?!? also skips bad placements
                    # maybe this is preferred?
                    if self.ok_to_place_wall(new_blank_maze, x, y):
                        new_blank_maze[x][y] = self.markers.wall
                except IndexError:
                    # Got to love and except index error
                    continue

        return new_blank_maze

    def display_maze(self) -> None:
        """Displays the maze in real time"""

        for row in self.simple_maze:
            print(row)

        return None

    def __repr__(self) -> str:
        """The goal is to be unambiguous..."""
        return (
            f"|SIMPLE_MAZE| "
            f"(height: {self.height}, "
            f"width: {self.width}), "
            f"number_of_walls: {self.number_of_walls}"
                )
