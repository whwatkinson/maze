from random import randint
from typing import List, Tuple


class SimpleMaze:

    markers = {
        'top': '_',
        'start':  's',
        'side':  '|',
        'clear':  ' ',
        'finish':  'f',
        'bottom':  '‾'
    }

    def __init__(self, height: int = 10, width: int = 10):

        if height < 3:
            raise ValueError('This maze is to short.')

        if width < 3:
            raise ValueError('This maze is to narrow.')
        self.height = height
        self.width = width
        self.maze = self.get_blank_maze(
            height=height,
            width=width
        )

    @staticmethod
    def get_start_end_pos(width: int) -> Tuple[int, int]:

        ub = width - 2
        start_pos = randint(1, ub)
        end_pos = randint(1, ub)

        return start_pos, end_pos

    def get_n_row(self, width: int) -> List[List[str]]:

        clear_markers_needed = width - 2
        row_n = [[self.markers['side']] + [self.markers['clear'] for _ in range(clear_markers_needed)] + [self.markers['side']]]

        return row_n

    def get_blank_maze(self, height: int, width: int) -> List[List[str]]:

        start_pos, finish_pos = self.get_start_end_pos(width=width)

        top = [self.markers['top'] for _ in range(width)]
        top[start_pos] = self.markers['start']
        maze = [top]

        rows_n_needed = height - 2

        for _ in range(rows_n_needed):
            maze += self.get_n_row(width)

        bottom = [self.markers['bottom'] for _ in range(width)]
        bottom[finish_pos] = self.markers['finish']
        maze += [bottom]

        return maze

    def display_maze(self) -> None:

        for row in self.maze:
            print(row)

        return None

    def __repr__(self):
        return f"SIMPLE_MAZE (height: {self.height}, width {self.width})"
