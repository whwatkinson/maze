from random import randint
from typing import List, Tuple


from walls.mk1.simple_wall import SimpleWall


class SimpleMaze:

    markers = {
        'top': '_',
        'start':  'S',
        'side':  '|',
        'clear':  ' ',
        'wall': 'W',
        'finish':  'F',
        'bottom':  '‾'
    }

    def __init__(
            self,
            height: int = 10,
            width: int = 10,
            number_of_walls: int = 10,
            level: int = 0
    ):

        if height < 3:
            raise ValueError('This maze is to short.')
        if width < 3:
            raise ValueError('This maze is to narrow.')

        # OOP
        self.height = height
        self.width = width
        self.number_of_walls = number_of_walls
        self.level = level
        self.coords_start, self.coords_finish = self.get_start_finish_pos()
        self.blank_maze = self.get_blank_maze(
            height=self.height,
            width=self.width,
        )
        self.walls = SimpleWall(
            height=self.height,
            width=self.width,
            number_of_walls=self.number_of_walls
        )
        self.simple_maze = self.place_walls(
            walls_meta=self.walls.walls_meta
        )

    # TODO @property for start and end coords

    def get_start_finish_pos(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """Get the postionion of the start and finish"""
        ub = self.width - 2
        start_pos = randint(1, ub)
        finish_pos = randint(1, ub)

        coords_start = (0, start_pos)
        coords_finish = (self.height-1, finish_pos)

        return coords_start, coords_finish

    def get_n_row(self, width: int) -> List[List[str]]:
        """Get the middle rows of the maze"""
        clear_markers_needed = width - 2
        # TODO: ugly can do better
        row_n = [
            [
                self.markers['side']
            ] + [
                self.markers['clear'] for _ in range(clear_markers_needed)
            ] + [
                self.markers['side']
            ]
        ]

        return row_n

    def get_blank_maze(
            self, height: int, width: int
    ) -> List[List[str]]:
        """Get a new maze with walls"""
        # Get start and finish postions
        _, y_s = self.coords_start
        _, y_f = self.coords_start

        # Get top row
        top = [self.markers['top'] for _ in range(width)]
        top[y_s] = self.markers['start']
        maze = [top]

        # Get n middle rows
        rows_n_needed = height - 2
        for _ in range(rows_n_needed):
            maze += self.get_n_row(width)

        # Get bottom row
        bottom = [self.markers['bottom'] for _ in range(width)]
        bottom[y_f] = self.markers['finish']
        maze += [bottom]

        return maze

    def ok_to_place_wall(
            self, blank_maze: List[List[str]], a: int, b: int) -> bool:
        """Checks the placement of the wall"""
        if blank_maze[a][b] == self.markers['clear']:
            if blank_maze[a-1][b] != self.markers['start']:
                if blank_maze[a+1][b] != self.markers['finish']:
                    return True
        else:
            return False

    def place_walls(self, walls_meta: dict) -> List[List[str]]:
        """Place the walls on the maze"""
        # blank_maze = self.get_blank_maze(height=self.height, width=self.width)
        blank_maze = self.blank_maze.copy()
        # Each row
        for wall in walls_meta:
            # Over each pair of coordinates
            for a, b in wall['wall_coords']:

                try:
                    # TODO BETTER PLEASE, really?!? also skips bad placements
                    # maybe this is preferred?
                    if self.ok_to_place_wall(blank_maze, a, b):
                        blank_maze[a][b] = self.markers['wall']
                except IndexError:
                    # Got to love and except index error
                    continue

        return blank_maze

    def display_maze(self) -> None:
        """Displays the maze in real time"""

        for row in self.simple_maze:
            print(row)

        return None

    def __repr__(self) -> str:
        """goal is to be unambiguous..."""
        return (
            f"|SIMPLE_MAZE| "
            f"(height: {self.height}, "
            f"width: {self.width}), "
            f"number_of_walls: {self.number_of_walls}"
                )
