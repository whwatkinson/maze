from pytest import raises
from collections import namedtuple

from solver import SolverMeta
from solver.mk1 import SimpleSolver, Sight
from solver.mk1.tests.sample_mazes import maze0
from mazes.mk1.simple_maze import SimpleMaze

sm = SimpleMaze()


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

            assert ss.name in smeta.solver_names
            # assert type(ss.brain) is dict
            assert type(ss.path_taken) is list

    def test_brain_position(self):
        pass

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
            # Update steps
            ss.brain.memory['steps'] = case.steps

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

        test_cases = [
            TestCase('up', maze0, 1, 1, None),
            TestCase('UP', maze0, 1, 1, ValueError)
        ]

        for case in test_cases:
            ss = SimpleSolver()
            if case.exception:
                with raises(case.exception) as exec_info:
                    ss.look_around_you(
                        direction=case.direction,
                        maze=case.maze,
                        x=case.x,
                        y=case.y
                    )
                assert exec_info.type == case.exception

            else:

                calcium = ss.look_around_you(
                    direction=case.direction,
                    maze=case.maze,
                    x=case.x,
                    y=case.y
                )

                assert calcium in markers

    def test_update_sight(self):

        TestCase = namedtuple('TestCase', ['maze', 'position', 'expected'])

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
            for test, expected in zip(case.expected, sight):
                assert test == expected
