from random import randint


class SimpleMaze:

    side = '|'
    top = '_'
    bottom = '‾'
    start = 's'
    finish = 'f'
    wall = 'x'
    clear = ' '

    def __init__(self):
        self.maze = self.get_maze()

    @staticmethod
    def get_maze():

        row0 = ['_', '_',  's',  '_',  '_']
        row1 = ['|', 'x',  'x',  'x',  '|']
        row2 = ['|', 'x',  'x',  'x',  '|']
        row3 = ['|', 'x',  'x',  'x',  '|']
        row4 = ['‾', '‾',  'f',  '‾',  '‾']

        maze = [row0, row1, row2, row3, row4]

        return maze
