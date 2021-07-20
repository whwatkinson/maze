from typing import List, Tuple, Optional
from random import randint
from enum import Enum


from solver.mk1.simple_brain import SimpleBrain
from solver.mk1.simple_organs import Sight
from solver import SolverMeta
from mazes import SimpleMaze


simple_meta = SolverMeta()
simple_maze = SimpleMaze()
path_clean = []


class SimpleDirection(Enum):
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'
    z_minus = 'z_minus'
    z_plus = 'z_plus'


class SimpleSolver:

    def __init__(
            self,
            brain: SimpleBrain = None,
            path_taken: list = None,
            current_position: Tuple[int, int] = None,
    ):
        """
        Generate a Simple Solver object
        :param brain: The brains behind the madness
        :param path_taken: Where have I gone?
        :param current_position: WHere am I?
        """
        self.brain = self.brain_check(brain)

        if not path_taken:
            self.path_taken = self.get_new_path_taken(path_taken)

        self.current_position = current_position

        # Please let me, and why the hell not
        self.name = simple_meta.solver_names[
            randint(0, len(simple_meta.solver_names)-1)
        ]
        self.language = simple_meta.language[
            randint(0, len(simple_meta.language)-1)
        ]

    @staticmethod
    def brain_check(brain: Optional[SimpleBrain]) -> SimpleBrain:

        if type(brain) is SimpleBrain:
            return brain
        else:
            new_brain = SimpleBrain()
            return new_brain

    @staticmethod
    def get_new_path_taken(
            path: Optional[List[Tuple[int, int]]]
    ) -> List[Tuple[int, int]]:
        """
        Get a new path taken if memory is foggy
        :param path:
        """

        if path:
            return path

        else:
            # Somthing special here or not?
            new_path = path_clean.copy()

        return new_path

    def update_path_taken(self, coords: Tuple[int, int]) -> bool:
        """
        Add path to memory
        :param coords:
        :return ?:
        """

        self.path_taken.append(coords)

        return True

    def update_step_count(self) -> bool:
        """Updates the step count"""

        # Get bain dict
        steps = self.brain.memory.steps

        # GOALS
        if steps > 10000:
            print("STEP GOAL REACHED")

        # Update steps
        self.brain.memory.steps += 1

        return True

    def get_step_count(self):
        """Returns the current step count"""
        return self.brain.memory.steps

    def update_location(
            self,
            maze: List[List[str]],
            position: Tuple[int, int],
    ) -> bool:
        """
        Update the sight and last_known_position
        :param maze:
        :param position:
        :return ?:
        """

        # Replace current sight with last known position
        self.brain.last_known_position = self.brain.sight

        current_position = self.update_sight(maze=maze, position=position)

        # Update brain
        self.brain.sight = current_position

        # TODO add check you have not rambled to far

        return True

    def update_sight(
            self,
            maze: List[List[str]],
            position: Tuple[int, int]
    ) -> Sight:
        """
        Updates the current line of sight
        :param maze:
        :param position:
        :return:
        """

        # Current location
        x, y = position

        # Mapping of sight
        # TODO DICT comp

        # Get the keys from the enum
        sight_coords_map = {
            item: self.look_around_you(SimpleDirection[item], maze, x, y)
            for item in [field.value for field in SimpleDirection]
        }

        current_position = Sight(**sight_coords_map)
        return current_position

    @staticmethod
    def look_around_you(
            direction: SimpleDirection, maze: List[List[str]], x: int, y: int) -> str:
        """
        This is our good friend Calcium
        :param direction:
        :param maze:
        :param x:
        :param y:
        :return:
        """
        # WOW just WOW, better to ship and send
        # TODO MAP OF WHERE TF TO GO?

        direction_map = {
            SimpleDirection.up: (x - 1, y),
            SimpleDirection.down: (x + 1, y),
            SimpleDirection.left: (x, y - 1),
            SimpleDirection.right: (x, y + 1),
            SimpleDirection.z_minus: None,
            SimpleDirection.z_plus: None,
        }

        line_of_sight = direction_map[direction]
        if line_of_sight:

            try:
                x_new, y_new = line_of_sight
                marker = maze[x_new][y_new]

                # Not the best implementation
                if x_new < 0 or y_new < 0:
                    raise IndexError('LOOK AROUND YOU')

            except IndexError:
                marker = simple_maze.markers.out_of_bounds

        else:
            marker = None

        return marker


    def __repr__(self) -> str:
        """Ronseal"""
        return f"|SIMPLE_SOLVER| name: {self.name}"
