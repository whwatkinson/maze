# from typing import List, Tuple
#
#
# from solver.mk1 import Sight
#
#
# class SimpleLogic:
#
#     @staticmethod
#     def update_sight(maze: List[List[str]], position: Tuple[int, int]) -> dict:
#         """Updates the current line of sight"""
#
#         # Current location
#         x, y = position
#
#         # Mapping of sight
#         # TODO needs to be in "const" or somthing appropriate?
#         sight_coords_map = {
#             'up': (x + 1, y),
#             'down': (x - 1, y),
#             'left': (x, y - 1),
#             'right': (x, y + 1),
#             'z_minus': (None, None),
#             'z_plus': (None, None)
#         }
#         new_sight = Sight()
#
#         for direction, coords in sight_coords_map.items():
#
#             x, y = coords
#             try:
#                 new_sight.direction = maze[x][y]
#             except IndexError:
#                 new_sight.direction = 'OUT OF BOUNDS'
#
#         return new_sight
