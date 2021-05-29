from random import randint
from typing import List, Tuple


class SimpleMaze:

    markers = {
        'top': '_',
        'start':  's',
        'side':  '|',
        'clear':  ' ',
        'wall': 'x',
        'finish':  'f',
        'bottom':  '‾'
    }

    def __init__(
            self,
            height: int = 5,
            width: int = 5,
    ):

        if height < 3:
            raise ValueError('This maze is to short.')

        if width < 3:
            raise ValueError('This maze is to narrow.')
        self.height = height
        self.width = width
        self.maze = self.get_new_maze(
            height=height,
            width=width
        )

    @staticmethod
    def get_start_end_pos(width: int) -> Tuple[int, int]:

        ub = width - 2

        start_pos = randint(1, ub)

        end_pos = randint(1, ub)

        return start_pos, end_pos

    def get_n_row(self, row_n: list, width: int = 5) -> List[str]:

        clear_needed = width - 2

        row_n += [[self.markers['side']] + [self.markers['clear'] for _ in range(clear_needed)] + [self.markers['side']]]

        return row_n

    def get_new_maze(self, height: int, width: int) -> List[List[str]]:

        maze = []
        start_pos, finish_pos = self.get_start_end_pos(width=width)
        top = [[self.markers['top'] for _ in range(width)]]

        top[0][start_pos] = self.markers['start']

        maze += top

        # maze += [[self.markers['top'], self.markers['top'],  self.markers['start'],  self.markers['top'], self.markers['top']]]

        height_needed = height - 2
        for _ in range(height_needed):
            self.get_n_row(maze, width)

        # maze += [[self.markers['bottom'], self.markers['bottom'],  self.markers['finish'], self.markers['bottom'], self.markers['bottom']]]
        bottom = [[self.markers['bottom'] for _ in range(width)]]

        bottom[0][finish_pos] = self.markers['finish']

        maze += bottom

        return maze

    @staticmethod
    def display_maze(maze):

        for row in maze:
            print(row)

        return None
