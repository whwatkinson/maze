from typing import List, Tuple
from random import randint

from solver.mk1.simple_brain import SimpleBrain
from solver import solver_names

# TODO BRAIN CLASS after all we are sentient beings


class SimpleSolver:

    def __init__(self, brain: SimpleBrain = None, path_taken: list = None, position: Tuple[int, int] = None):

        if not brain:
            self.brain = self.get_brain(brain)

        if not path_taken:
            self.path_taken = self.get_path_taken(path_taken)

        self.position = position

        # Please let me, and why the hell not
        self.name = solver_names[randint(0, len(solver_names))]

    @staticmethod
    def get_brain(brain):

        if brain:
            return brain

        else:
            # What consitutes a brain anway? Currently thinking a known state
            new_brain = SimpleBrain()

            return new_brain

    @staticmethod
    def get_path_taken(path: List[Tuple[int, int]]) -> List:
        if path:
            return path

        else:
            # Somthing special here or not?
            new_path = []
        return new_path

    def add_path(self, coords: Tuple[int, int]) -> bool:

        self.path_taken.append(coords)

        return True

    def update_step_count(self) -> bool:

        self.brain.brain['memory']['steps'] += 1

        return True

    def get_step_count(self):

        return self.brain.brain['memory']['steps']

    def update_location(self, up: str, down: str, left: str, right: str, z_minus: str = None, z_plus: str = None) -> bool:

        # Replace current sight with last known position
        self.brain.brain['last_known_position'] = self.brain.brain['sight']

        # Get new position from args
        current_position = {
            'up': up,
            'down': down,
            'left': left,
            'right': right,
            'z_minus': z_minus,
            'z_plus': z_plus
        }

        # Update brain
        self.brain.brain['sight'] = current_position

        return True

    def get_currecnt_postion(self):

        return self.brain.brain['sight']

    def __repr__(self) -> str:
        return f"SIMPLE_SOLVER (name: {self.name})"
