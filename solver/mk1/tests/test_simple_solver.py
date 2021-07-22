from pytest import raises
from collections import namedtuple

from solver import SolverMeta
from solver.mk1 import (
    SimpleSolver,
    Sight,
    SimpleBrain,
    SimpleDirection,
    SimpleOrgans
)
from mazes import SimpleMaze, SampleSimpleMazes

sm = SimpleMaze()
sample_simple_mazes = SampleSimpleMazes()


class TestSimpleSolver:

    test_cases = [
        {
            'brain': None,
            'path_taken': None
        }
    ]

    def test_get_solver(self):

        for case in self.test_cases:

            ss = SimpleSolver(**case)
            smeta = SolverMeta()
            s0 = SimpleOrgans()

            assert ss.name in smeta.solver_names
            assert ss.language in smeta.language
            assert type(ss.brain) is SimpleBrain
            assert ss.path_taken == []
            assert ss.current_position is None
            assert ss.brain.sight == s0.sight_clean
            assert ss.brain.last_known_position == s0.sight_clean
            assert ss.brain.memory.steps == 0

    def test_brain_step_count(self):
        TestCase = namedtuple('TestCase', ['steps', 'movement', 'total_steps'])

        test_cases = [
            TestCase(steps=0, movement=1, total_steps=1),
            TestCase(steps=420, movement=69, total_steps=489),
            TestCase(steps=10000, movement=1, total_steps=10001),

        ]
        for case in test_cases:

            # New SimpleSolver
            ss = SimpleSolver()

            # Replace steps taken
            ss.brain.memory.steps = case.steps

            # Update steps
            for steps in range(case.movement):
                ss.update_step_count()

            assert ss.get_step_count() == case.total_steps

    def test_look_around_you(self):

        TestCase = namedtuple('TestCase', [
            'direction',
            'maze',
            'x',
            'y',
            'exception'
        ]
                              )

        markers = set(sm.markers._asdict().values())
        as_of_yet_unsure = {'z_minus', 'z_plus'}
        maze0 = sample_simple_mazes.maze0

        test_cases = [
            TestCase('up', maze0, 1, 1, None),
            TestCase('Up', maze0, 5, 7, KeyError),
            TestCase('z_minus', maze0, 1, 2, None),
            TestCase('z_plus', maze0, 3, 2, None),
        ]

        for case in test_cases:
            ss = SimpleSolver()
            if case.exception:
                with raises(case.exception) as exec_info:
                    ss.look_around_you(
                        direction=SimpleDirection[case.direction],
                        maze=case.maze,
                        x=case.x,
                        y=case.y
                    )
                assert exec_info.type == case.exception

            else:
                calcium = ss.look_around_you(
                    direction=SimpleDirection[case.direction],
                    maze=case.maze,
                    x=case.x,
                    y=case.y
                )
                if case.direction in as_of_yet_unsure:
                    assert calcium is None
                else:
                    assert calcium in markers

    def test_update_sight(self):

        TestCase = namedtuple('TestCase', ['maze', 'position', 'expected'])
        maze0 = sample_simple_mazes.maze0
        test_cases = [
            # Top Left
            TestCase(maze0, (0, 0), Sight(
                up='A',
                down='|',
                left='A',
                right='_',
                z_minus=None,
                z_plus=None
            )),
            # Middle
            TestCase(maze0, (12, 17), Sight(
                up='W',
                down=' ',
                left='W',
                right='W',
                z_minus=None,
                z_plus=None
            )),
            # Bottom right
            TestCase(maze0, (24, 24), Sight(
                up='|',
                down='A',
                left='‾',
                right='A',
                z_minus=None,
                z_plus=None
            ))

        ]

        for case in test_cases:
            ss = SimpleSolver()
            sight = ss.update_sight(case.maze, case.position)
            for test, expected in zip(sight, case.expected):
                print()
                assert test == expected
