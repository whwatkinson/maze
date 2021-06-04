from typing import List, Tuple
from random import randint


from solver import solver_names

# TODO BRAIN CLASS after we are sentient beings

class SimpleSolver:

    def __init__(self, brain: dict = None, path_taken: list = None, position: Tuple[int, int] = None):

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
            new_brain = {
                'sight': {
                    'up': None,
                    'down': None,
                    'left': None,
                    'right': None,
                    'z_minus': None,
                    'z_plus': None
                },
                'last_known_position': {
                    'up': None,
                    'down': None,
                    'left': None,
                    'right': None,
                    'z_minus': None,
                    'z_plus': None
                },

                'memory': {
                    'steps': 0
                }
            }
        return new_brain

    @staticmethod
    def get_path_taken(path: List[Tuple[int, int]]) -> List:
        if path:
            return path

        else:
            # Somthing special here or not?
            new_path = []
        return new_path

    def add_path(self, coords: Tuple[int, int]) -> str:

        self.path_taken.append(coords)

        return 'added :P'

    def update_step_count(self):

        steps = self.brain['memory']['steps']

        steps += 1

        return f'steps remainig {10000 - steps}!'

    def update_location(self, up: str, down: str, left: str, right: str, z_minus: str = None, z_plus: str = None) -> str:

        # Replace current sight with last known position
        self.brain['last_known_position'] = self.brain['sight']

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
        self.brain['sight'] = current_position

        return 'Thinking complete!'

    def __repr__(self) -> str:
        return f"SIMPLE_SOLVER (name: {self.name})"
