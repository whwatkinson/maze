from typing import List, Tuple


class LogicBase:

    @staticmethod
    def update_sight(maze: List[List[str]], position: Tuple[int, int]):

        x, y = position

        sight_coords_map = {
            'up': (x + 1, y),
            'down': (x - 1, y),
            'left': (x, y - 1),
            'right': (x, y + 1),
            'z_minus': (None, None),
            'z_plus': (None, None)
        }

        new_sight = {
            'up': None,
            'down': None,
            'left': None,
            'right': None,
            'z_minus': None,
            'z_plus': None
        }

        for line_of_sight, coords in sight_coords_map.items():

            x, y = coords

            new_sight[line_of_sight] = maze[x][y]

        return new_sight

