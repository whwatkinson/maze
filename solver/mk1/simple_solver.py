from typing import List, Tuple
from random import randint


from solver.mk1.names import solver_names


class SimpleSolver:

    def __init__(self, brain: list = None, path_taken: list = None):

        if not brain:
            self.brain = self.get_brain(brain)

        if not path_taken:
            self.path_taken = self.get_path(path_taken)

        # Please let me, and why the hell not
        self.name = solver_names[randint(0, len(solver_names))]

    @staticmethod
    def get_brain(brain):

        if brain:
            return brain

        else:
            # What consitutes a brain anway?
            # Currently thinking a known state
            new_brain = {
                'sight': {
                    'up': None,
                    'down': None,
                    'left': None,
                    'right': None
                }

            }
        return new_brain

    @staticmethod
    def get_path(path: List[int]):
        if path:
            return path

        else:
            # Somthing special here
            new_path = []
        return new_path

    def add_path(self, coords: Tuple[int, int]) -> List[Tuple[int, int]]:

        return self.path_taken.append(coords)

    def __repr__(self) -> str:
        return 'tbd'
