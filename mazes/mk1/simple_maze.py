from random import randint
from typing import List


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

    def __init__(self, height: int = 5):

        self.maze = self.get_new_maze(height=height)

    def get_n_row(self, row_n: list, height: int) -> List[str]:

        row_n += [[self.markers['side']] + [self.clear for _ in range(height - 2)] + [self.markers['side']]]

        return row_n

    def get_new_maze(self, height: int) -> List[List[str]]:

        maze = []
        maze += [[self.markers['top'], self.markers['top'],  self.markers['start'],  self.markers['top'], self.markers['top']]]

        for _ in range(height):
            self.get_n_row(maze, height)

        maze += [[self.markers['bottom'], self.markers['bottom'],  self.markers['finish'], self.markers['bottom'], self.markers['bottom']]]

        return maze

    @staticmethod
    def display_maze(maze):

        for row in maze:
            print(row)

        return None
