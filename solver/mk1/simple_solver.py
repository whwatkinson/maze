from typing import List, Tuple
from random import randint


from solver.mk1.names import solver_names


class SimpleSolver:

    def __init__(self, brain: list = None, path_taken: list = None):

        if not brain:
            self.brain = self.get_brain(brain)

        if not path_taken:
            self.path_taken = self.get_path(path_taken)

        self.name = solver_names[randint(0, len(solver_names))]

    @staticmethod
    def get_brain(brain):

        if brain:
            return brain

        else:
            new_brain = []
        return new_brain

    @staticmethod
    def get_path(path):
        if path:
            return path

        else:
            new_path = []
        return new_path

    def add_path(self, coords: Tuple[int, int]):

        return self.path_taken.append(coords)

    def __repr__(self) -> str:
        return 'tbd'