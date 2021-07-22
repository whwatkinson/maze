from typing import Tuple, List

from mazes import SimpleMaze
from solver import SimpleOrgans, SimpleDirection


sm = SimpleMaze()
so = SimpleOrgans()


class SimpleLogic:

    @staticmethod
    def best_option_clear_path(
            current_position: Tuple[int, int],
            last_known_position: SimpleOrgans.sight_clean,
            maze: List[List[str]]
    ):
        new_coords = None
        x, y = current_position

        for direction in last_known_position:

            if direction == ' ':

                get_move = SimpleDirection[direction]

                x_m, y_m = SimpleDirection.movement[get_move]

                new_coords = x + x_m, y + y_m

        if new_coords:
            return new_coords
        else:
            return 'woods and trees'
