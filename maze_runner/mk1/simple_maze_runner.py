from random import randint


from mazes.mk1 import SimpleMaze
from solver.mk1 import SimpleSolver


simple_maze = SimpleMaze(height=25, width=25, number_of_walls=5)

simple_solver = SimpleSolver()


# random?
def random_walk(z: bool = False, stagger: int = 5) -> int:
    """CHAOS WILL REIGN"""

    if not z:
        stagger = 3

    return randint(0, stagger)


# with sight?
def spek_savers(current_position, maze: SimpleMaze):
    pass


# graph? with a spotter?
def node_builder():
    pass


def the_show():
    pass


if __name__ == "__main__":
    the_show()
