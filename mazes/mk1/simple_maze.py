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

        (
            blank_maze,
            self.coords_start,
            self.coords_finish
        ) = self.get_blank_maze(
            height=self.height,
            width=self.width,
        )
        self.walls = SimpleWall(
            height=self.height,
            width=self.width,
            number_of_walls=self.number_of_walls
        )
        self.simple_maze = self.place_walls(
            blank_maze=blank_maze,
            walls_meta=self.walls.walls_meta
        )

    @staticmethod
    def get_start_end_pos(width: int) -> Tuple[int, int]:
        """Get the postionion of the start and finish"""
        ub = width - 2
        start_pos = randint(1, ub)
        end_pos = randint(1, ub)

        return start_pos, end_pos

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
    ) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        """Get a new maze with walls"""
        # Get start and finish postions
        start_pos, finish_pos = self.get_start_end_pos(width=width)

        # Get top row
        top = [self.markers['top'] for _ in range(width)]
        top[start_pos] = self.markers['start']
        maze = [top]

        # Get n middle rows
        rows_n_needed = height - 2
        for _ in range(rows_n_needed):
            maze += self.get_n_row(width)

        # Get bottom row
        bottom = [self.markers['bottom'] for _ in range(width)]
        bottom[finish_pos] = self.markers['finish']
        maze += [bottom]

        coords_start = (0, start_pos)
        coords_finish = (height-1, finish_pos)

        return maze, coords_start, coords_finish

    def ok_to_place_wall(
            self, blank_maze: List[List[str]], a: int, b: int
    ) -> bool:
        """Check the placement of the wall"""
        if blank_maze[a][b] == self.markers['clear']:
            if blank_maze[a-1][b] != self.markers['start']:
                if blank_maze[a+1][b] != self.markers['finish']:
                    return True
        else:
            return False

    def place_walls(
            self, blank_maze: List[List[str]], walls_meta: dict
    ) -> List[List[str]]:
        """Ronseal"""
        # Each row
        for wall in walls_meta:
            # Over each pair of coordinates
            for a, b in wall['wall_coords']:

                # TODO BETTER PLEASE
                try:
                    if self.ok_to_place_wall(blank_maze, a, b):
                        blank_maze[a][b] = self.markers['wall']
                except IndexError:
                    # Got to love and except index error
                    continue

        return blank_maze

    def display_maze(self) -> None:
        """Displays the maze"""

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
