from random import randint


class SimpleMaze:

    top = '_'
    start = 's'
    side = '|'
    clear = ' '
    wall = 'x'
    finish = 'f'
    bottom = '‾'

    def __init__(self):
        self.maze = self.get_new_maze()

    def get_new_maze(self):

        row0 = [self.top, self.top,  self.start,  self.top, self.top]
        row1 = [self.side, self.clear, self.clear, self.clear, self.side]
        row2 = [self.side, self.clear, self.clear, self.clear, self.side]
        row3 = [self.side, self.clear, self.clear, self.clear, self.side]
        row4 = [self.bottom, self.bottom,  self.finish,  self.bottom, self.bottom]

        maze = [row0, row1, row2, row3, row4]

        return maze
