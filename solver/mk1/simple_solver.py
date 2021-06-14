from typing import List, Tuple
from random import randint

from solver.mk1.simple_brain import SimpleBrain
from solver import SolverMeta

# TODO BRAIN CLASS after all we are sentient beings

sm = SolverMeta()


class SimpleSolver:

    def __init__(
            self,
            brain: SimpleBrain = None,
            path_taken: list = None,
            position: Tuple[int, int] = None
    ):

        if not brain:
            self.brain = SimpleBrain(brain)

        if not path_taken:
            self.path_taken = self.get_path_taken(path_taken)

        self.position = position

        # Please let me, and why the hell not
        self.name = sm.solver_names[randint(0, len(sm.solver_names))]
        self.language = sm.language[randint(0, len(sm.language))]

    @staticmethod
    def get_path_taken(path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Get a new path taken if memory is foggy"""

        if path:
            return path

        else:
            # Somthing special here or not?
            new_path = []
        return new_path

    def add_path(self, coords: Tuple[int, int]) -> bool:
        """Add path to memory"""

        self.path_taken.append(coords)

        return True

    def update_step_count(self) -> bool:
        """Updates the step count"""

        # Get bain dict
        steps = self.brain.brain['memory']

        # GOALS
        if steps['steps'] > 10000:
            print("STEP GOAL REACHED")

        # Update steps
        steps['steps'] += 1

        return True

    def get_step_count(self):
        """Returns the current step count"""
        return self.brain.brain['memory']['steps']

    def update_location(
            self, up: str, down: str, left: str, right: str,
            z_minus: str = None, z_plus: str = None
    ) -> bool:
        """Update the sight and last_known_position"""

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

        # TODO add check you have not rambled to far

        return True

    def get_current_postion(self):
        """Where am I?"""
        return self.brain.brain['sight']

    def __repr__(self) -> str:
        """Ronseal"""
        return f"|SIMPLE_SOLVER| name: {self.name}"
