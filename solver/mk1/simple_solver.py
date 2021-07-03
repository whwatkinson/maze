from typing import List, Tuple, Optional
from random import randint

from solver.mk1.simple_brain import SimpleBrain
from solver.mk1.simple_organs import Sight
from solver import SolverMeta
from mazes import SimpleMaze

# TODO BRAIN CLASS after all we are sentient beings

simple_meta = SolverMeta()
simple_maze = SimpleMaze()
path_clean = []


class SimpleSolver:

    def __init__(
            self,
            brain: SimpleBrain = None,
            path_taken: list = None,
            current_position: Tuple[int, int] = None
    ):
        self.brain = self.brain_check(brain)

        if not path_taken:
            self.path_taken = self.get_path_taken(path_taken)

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
    def get_path_taken(path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
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

    def add_path(self, coords: Tuple[int, int]) -> bool:
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
        steps = self.brain.memory['steps']

        # GOALS
        if steps > 10000:
            print("STEP GOAL REACHED")

        # Update steps
        self.brain.memory['steps'] = steps + 1

        return True

    def get_step_count(self):
        """Returns the current step count"""
        return self.brain.memory['steps']

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
        # TODO needs to be in "const" or somthing appropriate?
        sight_coords_map = {
            'up': self.look_around_you('up', maze, x, y),
            'down': self.look_around_you('down', maze, x, y),
            'left': self.look_around_you('left', maze, x, y),
            'right': self.look_around_you('right', maze, x, y),
            'z_minus': self.look_around_you('z_minus', maze, x, y),
            'z_plus': self.look_around_you('z_plus', maze, x, y),
        }
        current_position = Sight(**sight_coords_map)

        return current_position

    @staticmethod
    def look_around_you(
            direction: str, maze: List[List[str]], x: int, y: int) -> str:
        """
        This is our good friend Calcium
        :param direction:
        :param maze:
        :param x:
        :param y:
        :return:
        """
        # WOW just WOW, better to ship and send
        try:
            if direction == 'up':
                if x - 1 < 0:
                    raise IndexError
                marker = maze[x - 1][y]
            elif direction == 'down':
                marker = maze[x + 1][y]
            elif direction == 'left':
                if y - 1 < 0:
                    raise IndexError
                marker = maze[x][y - 1]
            elif direction == 'right':
                marker = maze[x][y + 1]
            elif direction == 'z_minus':
                marker = None
            elif direction == 'z_plus':
                marker = None
            else:
                raise ValueError('WHERE ARE YOU GOING?')

        except IndexError:
            marker = simple_maze.markers.out_of_bounds

        return marker

    def get_current_postion(self):
        """Where am I?"""
        return self.brain.memory['sight']

    def __repr__(self) -> str:
        """Ronseal"""
        return f"|SIMPLE_SOLVER| name: {self.name}"
